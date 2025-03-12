from ssh_manager.config_handler import ConfigHandler
from ssh_manager.utils import load_env, prompt_host_data
from ssh_manager.git_handler import GitHandler

class SSHManager:
    def __init__(self):
        self.env = load_env()
        self.config_handler = ConfigHandler(self.env)
        self.git_handler = GitHandler(self.env)

    def add_host(self):
        data = prompt_host_data(self.env)
        self.config_handler.add_host(data)

    def delete_host(self, hostname, group):
        self.config_handler.delete_host(hostname, group)

    def rename_host(self, old, new, group):
        self.config_handler.rename_host(old, new, group)

    def move_host(self, hostname, from_path, to_path):
        self.config_handler.move_host(hostname, from_path, to_path)

    def list_hosts(self, group, filter_subgroup=None):
        self.config_handler.list_hosts(group, filter_subgroup=filter_subgroup)

    def export_configs(self):
        self.config_handler.export_all()

    def push_configs(self):
        self.git_handler.push()