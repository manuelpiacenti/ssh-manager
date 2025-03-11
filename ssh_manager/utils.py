import os
import ipaddress
from dotenv import load_dotenv
import questionary
import re

def load_env():
    load_dotenv()
    return {
        "base_group_dir": os.path.expanduser(os.getenv("base_group_dir", "~/.ssh")),
        "default_user": os.getenv("default_user", "root"),
        "default_port": os.getenv("default_port", "22"),
        "default_identity_file": os.path.expanduser(os.getenv("default_identity_file", "~/.ssh/id_rsa")),
        "known_groups": os.getenv("known_groups", "default").split(","),
        "known_subgroups": os.getenv("known_subgroups", "default,backbone").split(","),
        "git_provider": os.getenv("git_provider", "gitlab"),
        "git_repo_url": os.getenv("git_repo_url", "")
    }

def validate_ip_or_fqdn(value):
    if not value:
        return "This field is required."
    fqdn_pattern = re.compile(r'^(?=.{1,255}$)([a-zA-Z0-9]+(-?[a-zA-Z0-9])*\.)+[a-zA-Z]{2,}$')
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        if fqdn_pattern.match(value):
            return True
    return "Please enter a valid IP address or FQDN."

def prompt_host_data(env):
    try:
        hostname = questionary.text("Host alias name?").ask()
        ip = questionary.text("IP address or FQDN?", validate=validate_ip_or_fqdn).ask()
        port = questionary.text("SSH Port?", default=env["default_port"]).ask()
        identity = questionary.text("SSH key path?", default=env["default_identity_file"]).ask()
        group = questionary.select("Select group:", choices=env["known_groups"]).ask()
        subgroup = questionary.select("Select subgroup:", choices=env["known_subgroups"]).ask()

        return {
            "host": hostname,
            "ip": ip,
            "port": port,
            "identity_file": identity,
            "group": group,
            "subgroup": subgroup,
            "user": env["default_user"]
        }
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user.")
        raise SystemExit
