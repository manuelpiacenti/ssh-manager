# ssh-manager

> ⚠️ **Note**: *At 3pm I had a coffee thinking it was decaf and instead... at 2am I was still programming this... I'm not a programmer but the idea seemed good to me and so I got some AI to help me ☕🤖*


![GitHub release](https://img.shields.io/github/v/release/manuelpiacenti/ssh-manager?include_prereleases&label=Latest%20Version)
[![License: GPLv3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

> 🔧 Developer tools like `setup.py` and release scripts are available in the [`tools/`](./tools) folder.  
> These are not required for regular users of `ssh-manager`.

![GitHub release](https://img.shields.io/github/v/release/manuelpiacenti/ssh-manager?include_prereleases&label=Latest%20Version)
[![License: GPLv3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

`ssh-manager` is a command-line tool to manage SSH host configurations organized by group and subgroup. Ideal for IT professionals, sysadmins, and MSPs who work with many environments and clients.

📦 GitHub Repository: [github.com/manuelpiacenti/ssh-manager](https://github.com/manuelpiacenti/ssh-manager)

💬 I am available for:
- 🐛 Bug reports and fixes
- ✨ New feature implementations
- 🤝 Collaborations and contributions

Feel free to open issues or pull requests on the repository!

---

## 📁 Environment Configuration (`.env`)
You can customize the tool’s behavior via a `.env` file located in the root of the project.

### Default `.env.example` file
This file is already included in the repository:
```dotenv
base_group_dir=~/.ssh
default_user=root
default_port=22
default_identity_file=~/.ssh/id_rsa.pub
known_groups=default
known_subgroups=default,backbone,server,virtualization,network,vpn
git_provider=github
git_repo_url=https://github.com/YOUR_USERNAME/ssh-manager.git
```

If `.env` is not found, it will automatically be created by copying `.env.example`.

> ℹ️ Modify `.env.example` before running the tool for the first time to ensure your defaults are correctly applied.

---

## 📦 Installation

### 🔧 Standard Installation
```bash
pip install -e .
```
Make sure Python ≥3.8 is installed. Dependencies: `questionary`, `python-dotenv`, `gitpython`.

> 💡 **Tip:** Before installing, it's recommended to review and modify the `.env.example` file with your preferred defaults. This will be automatically copied to `.env` on first use.

---

## 🔄 Update to a new version
If you’ve previously installed `ssh-manager` and want to upgrade to the latest version:

### If installed with pip:
```bash
cd ~/ssh-manager   # or the correct repo path
git pull origin main
pip install -e . --upgrade
```

### If installed with pipx:
```bash
cd ~/ssh-manager   # or the correct repo path
git pull origin main
pipx reinstall .
```

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
ssh-manager -a                                  # Add a new host
ssh-manager -d hostname group                  # Delete a host from a specific group
ssh-manager -r old new group                   # Rename a host in a specific group
ssh-manager -m host from to                    # Move host from one group/subgroup to another
ssh-manager -l [group] [--subgroup sg]         # List hosts (filter by group and optional subgroup)
ssh-manager -e                                  # Export all SSH config files as .zip
ssh-manager -p                                  # Push configuration to Git
ssh-manager -h                                  # Show help
ssh-manager -v                                  # Show version
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

## 🔄 Uninstallation

### If installed with pip:
```bash
pip uninstall ssh-manager
```

### If installed with pipx:
```bash
pipx uninstall ssh-manager
```

---

## ℹ️ Notes
- The `default` group uses `~/.ssh/default/.ssh/config` to avoid polluting the base file
- You can cancel input with `Ctrl+C`
- `IdentityFile` is omitted if it matches the default
- Subgroups are created and separated with `## subgroup_name`
- Host deletion and renaming require the `group` to avoid conflicts across groups

---

## 📜 License
GPLv3
