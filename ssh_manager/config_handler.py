import os
from pathlib import Path
from collections import defaultdict

class ConfigHandler:
    def __init__(self, env):
        self.env = env

    def _get_config_path(self, group):
        base = Path(self.env['base_group_dir']).expanduser()
        return base / group / ".ssh" / "config"

    def _ensure_group_structure(self, group):
        base = Path(self.env['base_group_dir']).expanduser()
        group_path = base / group / ".ssh"
        group_path.mkdir(parents=True, exist_ok=True)
        main_config = base / "config"
        include_line = f'Include "{group_path}/config"  # added by ssh-manager'
        if not main_config.exists():
            main_config.write_text(f"{include_line}\n")
        else:
            content = main_config.read_text()
            if include_line not in content:
                with main_config.open("a") as f:
                    f.write(f"{include_line}\n")

    def _load_hosts(self, config_path):
        if not config_path.exists():
            return {}

        blocks = defaultdict(list)
        current_block = []
        current_subgroup = "default"

        with config_path.open() as f:
            for line in f:
                stripped = line.strip()

                if stripped.startswith("##"):
                    if current_block:
                        blocks[current_subgroup].append("".join(current_block))
                        current_block = []
                    current_subgroup = stripped.lstrip("# ").strip()

                elif stripped.startswith("Host "):
                    if current_block:
                        blocks[current_subgroup].append("".join(current_block))
                        current_block = []
                    current_block = [line]

                elif current_block:
                    current_block.append(line)

            if current_block:
                blocks[current_subgroup].append("".join(current_block))

        return blocks

    def _write_hosts(self, config_path, blocks):
        with config_path.open("w") as f:
            for subgroup in sorted(blocks):
                if blocks[subgroup]:
                    f.write(f"## {subgroup}\n")
                    for entry in blocks[subgroup]:
                        f.write(entry.strip() + "\n")
                    f.write("\n")

    def add_host(self, data):
        self._ensure_group_structure(data['group'])
        config_path = self._get_config_path(data['group'])
        config_path.parent.mkdir(parents=True, exist_ok=True)

        loaded_blocks = self._load_hosts(config_path)
        blocks = defaultdict(list, loaded_blocks)

        identity_line = (
            f"IdentityFile {data['identity_file']}\n"
            if data['identity_file'] != self.env['default_identity_file'] else ""
        )

        host_entry = (
            f"Host {data['host']}\n"
            f"HostName {data['ip']}\n"
            f"User {data['user']}\n"
            f"Port {data['port']}\n"
            f"{identity_line}"
        )

        blocks[data['subgroup']].append(host_entry)
        self._write_hosts(config_path, blocks)

        print(f"✅ Host '{data['host']}' added to group '{data['group']}' / subgroup '{data['subgroup']}'")

    def delete_host(self, hostname):
        base = Path(self.env['base_group_dir']).expanduser()
        found = False
        for path in base.rglob("config"):
            blocks = self._load_hosts(path)
            changed = False
            for k in list(blocks.keys()):
                new_entries = []
                for entry in blocks[k]:
                    if not entry.strip().startswith(f"Host {hostname}"):
                        new_entries.append(entry)
                    else:
                        changed = True
                        found = True
                blocks[k] = new_entries
            if changed:
                self._write_hosts(path, blocks)
        if found:
            print(f"🗑️  Host '{hostname}' deleted")
        else:
            print(f"⚠️  Host '{hostname}' not found")

    def rename_host(self, old, new):
        base = Path(self.env['base_group_dir']).expanduser()
        for path in base.rglob("config"):
            blocks = self._load_hosts(path)
            for k in blocks:
                for i, entry in enumerate(blocks[k]):
                    if entry.strip().startswith(f"Host {old}"):
                        blocks[k][i] = entry.replace(f"Host {old}", f"Host {new}")
            self._write_hosts(path, blocks)

    def move_host(self, hostname, from_path, to_path):
        from_group, from_sub = from_path.split("/")
        to_group, to_sub = to_path.split("/")
        from_config = self._get_config_path(from_group)
        to_config = self._get_config_path(to_group)
        blocks_from = self._load_hosts(from_config)
        blocks_to = self._load_hosts(to_config)
        moved = False
        for k in blocks_from:
            for entry in blocks_from[k]:
                if entry.strip().startswith(f"Host {hostname}"):
                    blocks_to[to_sub].append(entry)
                    blocks_from[k].remove(entry)
                    moved = True
                    break
            if moved:
                break
        self._write_hosts(from_config, blocks_from)
        self._write_hosts(to_config, blocks_to)

    def export_all(self):
        from zipfile import ZipFile
        export_path = Path("export")
        export_path.mkdir(exist_ok=True)
        zip_name = export_path / "ssh-configs.zip"
        with ZipFile(zip_name, 'w') as zipf:
            base = Path(self.env['base_group_dir']).expanduser()
            for path in base.rglob("config"):
                zipf.write(path, arcname=path.relative_to(base))

    def list_hosts(self, group, filter_subgroup=None):
        config_path = self._get_config_path(group)
        blocks = self._load_hosts(config_path)

        print(f"Host list for group: {group}\n")

        if not blocks:
            print("No hosts found.")
            return

        for subgroup in sorted(blocks):
            if filter_subgroup and subgroup != filter_subgroup:
                continue
            print(f"[{subgroup}]")
            for entry in blocks[subgroup]:
                lines = entry.strip().splitlines()
                host = hostname = user = port = ""

                for line in lines:
                    line = line.strip()
                    if line.startswith("Host "):
                        host = line.split(maxsplit=1)[1]
                    elif line.startswith("HostName "):
                        hostname = line.split(maxsplit=1)[1]
                    elif line.startswith("User "):
                        user = line.split(maxsplit=1)[1]
                    elif line.startswith("Port "):
                        port = line.split(maxsplit=1)[1]

                print(f"- {host:<20} {user}@{hostname}:{port}")
            print("")