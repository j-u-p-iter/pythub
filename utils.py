import os

def repo_path(repo, *path):
    return os.path.join(repo["gitdir"], *path)

