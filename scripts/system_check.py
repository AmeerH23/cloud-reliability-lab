import subprocess


def run_command(command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print(f"Command failed: {result.stderr.strip()}")
            return None

    except FileNotFoundError as error:
        print(f"Could not execute command: {error}")
        return None


system_info = run_command(["uname", "-a"])
current_directory = run_command(["pwd"])
git_status = run_command(["git", "status"])

print(f"System: {system_info}")
print(f"Directory: {current_directory}")
print(f"\nGit status:\n{git_status}")

if git_status is None:
    print("Unable to determine repository status.")
elif "working tree clean" in git_status:
    print("Repository is clean.")
else:
    print("Repository has changes.")
