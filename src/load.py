import os
import subprocess

def load_data(repo_url):
    git_cmd = "git"

    # Ensure .git exists
    if not os.path.exists(".git"):
        subprocess.run([git_cmd, "init"])
        subprocess.run([git_cmd, "branch", "-M", "main"])
        subprocess.run([git_cmd, "remote", "add", "origin", repo_url])
    else:
        # Always update the remote to the provided repo URL
        subprocess.run([git_cmd, "remote", "set-url", "origin", repo_url])

    # Add everything
    subprocess.run([git_cmd, "add", "."])

    # Basic Git identity (user can change if needed)
    subprocess.run([git_cmd, "config", "user.name", "auto-user"])
    subprocess.run([git_cmd, "config", "user.email", "auto@example.com"])

    # Commit
    subprocess.run([git_cmd, "commit", "--allow-empty", "-m", "Publish processed data"])

    # Force push so remote always matches local
    subprocess.run([git_cmd, "push", "-u", "origin", "main", "--force"])

    print(f"Published updates to GitHub repo: {repo_url}")


if __name__ == "__main__":
    # USER CAN CHANGE THIS
    load_data("https://github.com/jessicabpa9-hub/test2.git")
