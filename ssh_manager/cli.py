# ssh_manager/cli.py
import questionary
import sys
import argparse
from ssh_manager.core import SSHManager

def main():
    parser = argparse.ArgumentParser(
        prog="ssh-manager",
        description="Manage SSH configuration files by group and subgroup.",
        epilog="""
Examples:
  ssh-manager -a
  ssh-manager -d hostname
  ssh-manager -r old new
  ssh-manager -m host from_group/sub to_group/sub
  ssh-manager -l customerA --subgroup server
""",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    action_group = parser.add_argument_group("Host actions")
    action_group.add_argument("-a", "--add", action="store_true", help="Add a new host")
    action_group.add_argument("-d", "--delete", metavar="HOSTNAME", help="Delete a host")
    action_group.add_argument("-r", "--rename", nargs=2, metavar=("OLD", "NEW"), help="Rename a host")
    action_group.add_argument("-m", "--move", nargs=3, metavar=("HOST", "FROM", "TO"), help="Move host between groups/subgroups")

    list_group = parser.add_argument_group("Listing")
    list_group.add_argument("-l", "--list", nargs="?", const="default", metavar="GROUP", help="List hosts in a group")
    list_group.add_argument("--subgroup", metavar="SUBGROUP", help="Filter hosts by subgroup")

    export_group = parser.add_argument_group("Export & Git")
    export_group.add_argument("-e", "--export", action="store_true", help="Export SSH config files to a .zip archive")
    export_group.add_argument("-p", "--push", action="store_true", help="Commit and push configs to Git")

    meta_group = parser.add_argument_group("General")
    meta_group.add_argument("-v", "--version", action="version", version="ssh-manager v0.1.5")

    args = parser.parse_args()
    manager = SSHManager()

    try:
        if args.add:
            manager.add_host()
        elif args.delete:
            manager.delete_host(args.delete)
        elif args.rename:
            manager.rename_host(args.rename[0], args.rename[1])
        elif args.move:
            manager.move_host(args.move[0], args.move[1], args.move[2])
        elif args.export:
            manager.export_configs()
        elif args.push:
            manager.push_configs()
        elif args.list is not None:
            manager.list_hosts(args.list, filter_subgroup=args.subgroup)
        else:
            parser.print_help()
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user.")
        sys.exit(1)
