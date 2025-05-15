import os
import subprocess
from datetime import datetime, timedelta

# --- Configuration ---
repo_name = "jubayerhossain625"
author_name = "Jubayer Hossain"
author_email = "jubayer.engr.soft@email.com"
github_url = "https://github.com/jubayerhossain625/jubayerhossain625.git"

start_date = datetime(2024, 6, 1)
end_date = datetime(2024, 6, 7)  # exclusive
commits_per_day = 5

# --- Setup repo folder ---
if not os.path.exists(repo_name):
    os.makedirs(repo_name)
os.chdir(repo_name)
subprocess.run(["git", "init"])

# --- Set Git config ---
subprocess.run(["git", "config", "user.name", author_name])
subprocess.run(["git", "config", "user.email", author_email])

# --- Create commits ---
current_date = start_date
while current_date < end_date:
    for i in range(commits_per_day):
        commit_time = f"{current_date.strftime('%Y-%m-%d')} 12:{i:02d}:00"
        with open("activity.txt", "a") as f:
            f.write(f"Commit {i+1} on {current_date.date()}\n")

        subprocess.run(["git", "add", "activity.txt"])
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = commit_time
        env["GIT_COMMITTER_DATE"] = commit_time
        subprocess.run(["git", "commit", "-m", f"Commit {i+1} on {current_date.date()}"], env=env)

    current_date += timedelta(days=1)

# --- Connect and push to GitHub ---
subprocess.run(["git", "branch", "-M", "main"])
subprocess.run(["git", "remote", "add", "origin", github_url])
subprocess.run(["git", "push", "-u", "origin", "main"])