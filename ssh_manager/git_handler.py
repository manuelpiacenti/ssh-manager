from pathlib import Path
from git import Repo, GitCommandError

class GitHandler:
    def __init__(self, env):
        self.repo_url = env["git_repo_url"]
        self.repo_path = Path(env["base_group_dir"]).expanduser()
        try:
            self.repo = Repo(self.repo_path)
        except:
            self.repo = Repo.init(self.repo_path)

    def push(self):
        try:
            if self.repo.is_dirty(untracked_files=True):
                self.repo.git.add(all=True)
                self.repo.index.commit("Update SSH config")
                origin = self._get_or_create_remote()
                origin.push()
                print("✅ Configurations successfully pushed..")
            else:
                print("No changes to push..")
        except GitCommandError as e:
            print(f"Git error: {e}")

    def _get_or_create_remote(self):
        if "origin" in self.repo.remotes:
            return self.repo.remotes.origin
        return self.repo.create_remote("origin", self.repo_url)
