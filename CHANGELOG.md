# Changelog

All notable changes to this project will be documented in this file.

## [0.3.2] - 2025-03-12
### Added
- Section in README explaining how to upgrade to a newer version via pip or pipx
- GitHub badges: latest version, license
- GitHub repo link and contribution note in README

## [0.3.1] - 2025-03-12
### Fixed
- Host field is now required, preventing empty or invalid host entries
- Ctrl+C or ESC during prompts cleanly cancels the host creation
- Better error handling in list view for malformed config blocks

## [0.3.0] - 2025-03-12
### Added
- `-p` command to push all SSH configs to Git (GitHub/GitLab)
- Reads repo URL from `.env` (git_repo_url)
- Auto-inits the repo and handles first-time remote setup

## [0.2.2] - 2025-03-12
### Changed
- Introduced full semantic versioning (major.minor.patch)
- Interactive release script: choose to bump major, minor or patch
- Improved help and version reporting

## [0.2.1] - 2025-03-12
### Added
- Dynamic version display using importlib.metadata
- Required `group` parameter for `--delete` and `--rename`
- CLI help updated accordingly
- README improved with version usage and pipx instructions

## [0.2.0] - 2025-03-11
### Added
- `--subgroup` filter support in `--list` command
- Auto-copy `.env.example` to `.env` on first load
- Feedback output on `add` and `delete` actions
- Debian/Ubuntu install guidance and pipx support
- Improved output formatting for list command

## [0.1.8] - 2025-03-10
### Added
- Initial public release with group/subgroup structure
- Add, delete, rename, move, export, and push commands
- Environment-driven configuration
- Git integration support