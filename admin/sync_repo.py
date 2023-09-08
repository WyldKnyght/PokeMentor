import os
import subprocess

# Define the path to your local repository and the GitHub URL
local_repo_path = r"M:\DEV_Projects\PokeMentor"
github_repo_url = "https://github.com/WyldKnyght/PokeMentor"

# Change to the repository directory
os.chdir(local_repo_path)

# Pull changes from the remote repository and push local changes
subprocess.run(
    "git pull && git add . && git commit -m 'Automated commit' && git push origin main",
    shell=True,
    check=True,
)

print("Sync completed successfully!")