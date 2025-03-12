# Changelog
## [0.2.1] - 2025-03-12
### Added
- Support for dynamic version display via `importlib.metadata`
- Required `group` parameter for `--delete` and `--rename` to handle host conflicts across groups
- Updated CLI help and README to reflect new parameters

## [0.2.0] - 2025-03-11
### Added
- --subgroup filter for `--list`
- Feedback after add/delete actions
- Auto-copy of `.env.example` to `.env` on first run
- Improved CLI help and README
- Debian/Ubuntu install compatibility

y
## [0.1.6] - 2025-03-11
### Added
- --subgroup filter for host listing
- Host feedback after add/delete operations
- Improved CLI help and argument grouping

## [0.1.5] - 2025-03-11
### Changed
- Do not write `IdentityFile` if it matches the default value
- Compact output for `--list`, shell-friendly
- Unified group structure (default included as subdir)

## [0.1.4]
- Improved output formatting
- CLI migrated to argparse
