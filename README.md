# ssh-manager

`ssh-manager` is a command-line tool to manage SSH host configurations organized by group and subgroup. Ideal for IT professionals, sysadmins, and MSPs who work with many environments and clients.

---

## 🚀 Features
- Add, delete, rename, and move SSH host entries
- Organize hosts by group and subgroup (e.g., `customerA/server`)
- Optionally filter by subgroup with `--subgroup`
- Automatically writes `Include` directives to `~/.ssh/config`
- Uses separate SSH config files per group (including `default`)
- Export all configurations as a `.zip`
- Push configuration files to a Git repository
- Fully configurable via `.env`

---

## 📦 Installation
```bash
pip install -e .
```

Make sure Python ≥3.8 is installed. Dependencies: `questionary`, `python-dotenv`, `gitpython`.

---

## 🛠️ Usage
```bash
ssh-manager -a                          # Add a new host
ssh-manager -d hostname                # Delete a host
ssh-manager -r old new                 # Rename a host
ssh-manager -m host from to            # Move host from one group/subgroup to another
ssh-manager -l [group] [--subgroup sg] # List hosts (filter by group and optional subgroup)
ssh-manager -e                          # Export all SSH config files as .zip
ssh-manager -p                          # Push configuration to Git
ssh-manager -h                          # Show help
ssh-manager -v                          # Show version
```

Example structure:
```bash
~/.ssh/
├── config                              # contains Include lines
├── default/.ssh/config
├── customerA/.ssh/config
└── customerB/.ssh/config
```

Example line in `~/.ssh/config`:
```ssh
Include ~/.ssh/customerA/.ssh/config  # added by ssh-manager
```

---

## 📁 Environment Configuration (`.env`)
```dotenv
base_group_dir=~/.ssh
default_user=root
default_port=22
default_identity_file=~/.ssh/id_rsa
known_groups=default,customerA,customerB
known_subgroups=default,backbone,server,virtualization,network,vpn
git_provider=gitlab
git_repo_url=https://gitlab.com/youruser/ssh-manager.git
```

---

## ℹ️ Notes
- The `default` group uses `~/.ssh/default/.ssh/config` to avoid polluting the base file
- You can cancel input with `Ctrl+C`
- `IdentityFile` is omitted if it matches the default
- Subgroups are created and separated with `## subgroup_name`

---

## 📜 License
GPLv3