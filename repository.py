import os
import configparser

class GitRepository():
    def __init__(self, path, force = False):
        self.worktree = path
        self.gitdir = os.path.join(path, '.git')

        if not (force or os.path.isdir(self.gitdir)):
            raise Exception("Not a Git repository %s" % path)

        # Read configuration file in .git/config
        self.conf = configparser.ConfigParser()
        cf = repo_file(self, "config")

        if cf and os.path.exists(cf):
            self.conf.read([cf])

        elif not force:
            raise Exception("Configuration file is missing")

        if not force:
            vers = int(self.conf.get("core", "repositoryformatversion"))

            if vers != 0:
                raise Exception("Unsupported repositoryformatversion %s", % vers)
