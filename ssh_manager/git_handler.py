# ssh_manager/git_handler.py
import os
import subprocess
from datetime import datetime
from pathlib import Path
from git import Repo, GitCommandError

class GitHandler:
    def __init__(self, env):
        self.env = env
        self.repo_path = Path(env["base_group_dir"]).expanduser()
        self.remote_url = env.get("git_repo_url", "")

    def push(self):
        if not self.remote_url:
            print("❌ git_repo_url not set in .env")
            return

        if not (self.repo_path / ".git").exists():
            print("📂 Initializing Git repository...")
            Repo.init(self.repo_path)

        repo = Repo(self.repo_path)

        try:
            repo.git.add(all=True)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            repo.index.commit(f"Update SSH configs: {timestamp}")
        except GitCommandError as e:
            if "nothing to commit" in str(e):
                print("ℹ️  Nothing new to commit.")
            else:
                raise

        if "origin" not in [remote.name for remote in repo.remotes]:
            print(f"🔗 Setting remote to {self.remote_url}")
            repo.create_remote("origin", self.remote_url)

        try:
            print("🚀 Pushing to remote...")
            repo.remotes.origin.push()
            print(f"✅ Pushed to {self.remote_url}")
        except GitCommandError as e:
            print(f"❌ Push failed: {e}")
