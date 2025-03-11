import os
from ssh_manager.config_handler import ConfigHandler
from ssh_manager.git_handler import GitHandler
from ssh_manager.utils import prompt_host_data, load_env

class SSHManager:
    def __init__(self):
        self.env = load_env()
        self.config_handler = ConfigHandler(self.env)
        self.git_handler = GitHandler(self.env)

    def add_host(self):
        try:
            data = prompt_host_data(self.env)
            self.config_handler.add_host(data)
        except KeyboardInterrupt:
            print("\n❌ Host creation cancelled by user.")

    def delete_host(self, hostname):
        if not hostname:
            print("Please provide a hostname to delete.")
            return
        self.config_handler.delete_host(hostname)

    def rename_host(self, old, new):
        self.config_handler.rename_host(old, new)

    def move_host(self, hostname, from_path, to_path):
        self.config_handler.move_host(hostname, from_path, to_path)

    def export_configs(self):
        self.config_handler.export_all()

    def push_configs(self):
        self.git_handler.push()

    def list_hosts(self, group):
        group = group or "default"
        self.config_handler.list_hosts(group)
