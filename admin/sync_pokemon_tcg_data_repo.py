import os
import git

# Set the path to the cloned repository
repo_path = "M:\DEV_Projects\PokeMentor\data\pokemon-tcg-data"

# Initialize the Git repository object
repo = git.Repo(repo_path)

# Pull updates from the remote repository
try:
    origin = repo.remote("origin")
    origin.pull()
    print("Repository updated successfully.")
except git.GitCommandError as e:
    print("Error:", e)
except git.NoSuchPathError as e:
    print("Error:", e)
