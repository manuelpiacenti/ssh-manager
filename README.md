> **Latest version:** v0.2.1 – Released on 2025-03-12  
> See [CHANGELOG.md](./CHANGELOG.md) for full details.

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

### 🔧 Standard Installation
```bash
pip install -e .
```
Make sure Python ≥3.8 is installed. Dependencies: `questionary`, `python-dotenv`, `gitpython`.

---

## 🐧 Debian/Ubuntu Installation Notes
If you get the error:
```
This environment is externally managed
```
Your system restricts pip from installing globally due to PEP 668. Use one of these methods:

### ✅ Option 1: Use a virtual environment (recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

### ✅ Option 2: Use pipx (ideal for CLI tools)
```bash
sudo apt install pipx
pipx install .
```

If `ssh-manager` is not found after pipx install, add the following to your `~/.bashrc` or shell config:
```bash
export PATH="$HOME/.local/bin:$PATH"
```
Then reload:
```bash
source ~/.bashrc
```

### ⚠️ Option 3: Force install (not recommended)
```bash
pip install -e . --break-system-packages
```

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
You can customize the tool’s behavior via a `.env` file located in the root of the project.

### Default `.env.example` file
This file is already included in the repository:
```dotenv
base_group_dir=~/.ssh
default_user=root
default_port=22
default_identity_file=~/.ssh/id_rsa
known_groups=default
known_subgroups=default,backbone,server,virtualization,network,vpn
git_provider=github
git_repo_url=https://github.com/YOUR_USERNAME/ssh-manager.git
```

If `.env` is not found, it will automatically be created by copying `.env.example`.

---

## ℹ️ Notes
- The `default` group uses `~/.ssh/default/.ssh/config` to avoid polluting the base file
- You can cancel input with `Ctrl+C`
- `IdentityFile` is omitted if it matches the default
- Subgroups are created and separated with `## subgroup_name`

---

## 📜 License
GPLv3
