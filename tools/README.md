# Developer Tools

This folder contains developer tools and scripts not required for end users.

## Contents

- `release.sh`: used for tagging, committing, and pushing releases.
- `setup.py`: used for editable installation and local development setup.

These files are not necessary for general users of `ssh-manager`.

---

## 🔁 What `release.sh` does

When executed, the script:
1. Asks which version component to increment (major/minor/patch)
2. Updates the version inside `setup.py`
3. Commits all changes to the `main` branch
4. Creates a Git tag (e.g., `v0.5.0`)
5. Pushes both the branch and tag to GitHub

✅ After running `release.sh`, your new version is immediately:
- Available on the `main` branch
- Published as a tagged release (visible on GitHub)

You can now draft a new GitHub release using that tag and optionally attach a .zip file.