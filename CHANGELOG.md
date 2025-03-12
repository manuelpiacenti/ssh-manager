# Changelog

All notable changes to this project will be documented in this file.

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