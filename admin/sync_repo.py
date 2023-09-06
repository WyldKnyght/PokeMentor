import os
import subprocess

# Define the path to your local repository and the GitHub URL
local_repo_path = r"M:\DEV_Projects\PokeMentor"
github_repo_url = "https://github.com/WyldKnyght/PokeMentor"

# Change to the repository directory
os.chdir(local_repo_path)

try:
    # Pull changes from the remote repository
    subprocess.run(["git", "pull"])

    # Add all changes, commit, and push to GitHub
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Automated commit"])
    subprocess.run(["git", "push", "origin", "master"])

    print("Sync completed successfully!")
except Exception as e:
    print("Error:", e)
