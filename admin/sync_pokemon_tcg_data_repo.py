import git

# Set the path to the cloned repository
repo_path = "M:/DEV_Projects/PokeMentor/data/pokemon-tcg-data"

# Initialize the Git repository object and pull updates from the remote repository
try:
    repo = git.Repo(repo_path)
    origin = repo.remote("origin")
    origin.pull()
    print("Repository updated successfully.")
except (git.GitCommandError, git.NoSuchPathError) as e:
    print("Error:", e)