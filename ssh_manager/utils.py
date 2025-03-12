# ssh_manager/utils.py
import os
import ipaddress
from dotenv import load_dotenv
import questionary
import re
import shutil

def load_env():
    if not os.path.exists(".env") and os.path.exists(".env.example"):
        shutil.copy(".env.example", ".env")
        print("📄 .env not found. Copied from .env.example")

    load_dotenv()
    return {
        "base_group_dir": os.path.expanduser(os.getenv("base_group_dir", "~/.ssh")),
        "default_user": os.getenv("default_user", "root"),
        "default_port": os.getenv("default_port", "22"),
        "default_identity_file": os.path.expanduser(os.getenv("default_identity_file", "~/.ssh/id_rsa")),
        "known_groups": os.getenv("known_groups", "default").split(","),
        "known_subgroups": os.getenv("known_subgroups", "default,backbone").split(","),
        "git_provider": os.getenv("git_provider", "github"),
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

def ask_or_exit(question):
    answer = question.ask()
    if answer is None:
        print("\n❌ Operation cancelled by user.")
        raise SystemExit
    return answer

def prompt_host_data(env):
    try:
        hostname = ask_or_exit(
        questionary.text("Hostname:", validate=lambda val: True if val.strip() else "This field is required.")
        )
        ip = ask_or_exit(questionary.text("IP address or FQDN:", validate=validate_ip_or_fqdn))
        port = ask_or_exit(questionary.text("SSH Port:", default=env["default_port"]))
        identity = ask_or_exit(questionary.text("SSH key path:", default=env["default_identity_file"]))
        group = ask_or_exit(questionary.select("Select group:", choices=env["known_groups"]))
        subgroup = ask_or_exit(questionary.select("Select subgroup:", choices=env["known_subgroups"]))

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