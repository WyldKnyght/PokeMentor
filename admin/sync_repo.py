import os
import subprocess
from pathlib import Path

# Define the path to your local repository and the GitHub URL
local_repo_path = Path(r"M:\DEV_Projects\PokeMentor")
github_repo_url = "https://github.com/WyldKnyght/PokeMentor"

# Change to the repository directory
os.chdir(local_repo_path)

cmd = ["git", "rm", "-r", "--cached", ".vs"]
subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=local_repo_path).communicate()
# Pull changes from the remote repository and push local changes
cmd = ["git", "pull"]
subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=local_repo_path).communicate()

cmd = ["git", "add", "."]
subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=local_repo_path).communicate()

cmd = ["git", "commit", "-m", "Automated commit"]
subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=local_repo_path).communicate()

cmd = ["git", "push", "origin", "main"]
subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=local_repo_path).communicate()

print("Sync completed successfully!")
