from pytrun.description import description 
from pytrun.assertion import expect 

from pythub.utils import *

tests_name = "Utils"

@description("\"repo_path\" creates path to artifacts in .git")
def test_path_to_git_artifacts():
    fake_repo = { "gitdir": ".git" } 

    result_path = repo_path(fake_repo, 'some_folder', 'some_file')

    expect(result_path).to_equal('.git/some_folder/some_file')
