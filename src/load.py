import os
import subprocess

def run_git_command(args):
    """Run a git command and handle errors gracefully."""
    try:
        subprocess.run(["git"] + args, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {' '.join(args)}")
        print(e)

def load_data(repo_url, branch="main", commit_message="Publish processed data", user_name="auto-user", user_email="auto@example.com"):
    # Initialize Git repo if it doesn't exist
    if not os.path.exists(".git"):
        run_git_command(["init"])
        run_git_command(["branch", "-M", branch])
        run_git_command(["remote", "add", "origin", repo_url])
    else:
        # Update remote URL in case it changed
        run_git_command(["remote", "set-url", "origin", repo_url])

    # Stage all changes
    run_git_command(["add", "."])

    # Configure Git user info
    run_git_command(["config", "user.name", user_name])
    run_git_command(["config", "user.email", user_email])

    # Commit changes (allow empty commit)
    run_git_command(["commit", "--allow-empty", "-m", commit_message])

    # Safer push: use --force-with-lease instead of --force
    run_git_command(["push", "-u", "origin", branch, "--force-with-lease"])

    print(f"Published updates to GitHub repo: {repo_url} on branch {branch}")

def main():
    # CHANGE THESE to your GitHub repo details
    repo_url = "https://github.com/jessicabpa9-hub/test5.git"
    branch = "main"
    commit_message = "Publish processed data safely"
    load_data(repo_url, branch, commit_message)

if __name__ == "__main__":
    main()
