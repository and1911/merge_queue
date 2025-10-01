import subprocess

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running: {cmd}\n{result.stderr}")
        raise Exception("Git command failed")
    return result.stdout.strip()

def main():
    for i in range(1, 101):
        commit_msg = f"Automated commit #{i}"
        filename = "auto_commit_file.txt"

        with open(filename, "a") as f:
            f.write(f"Commit number {i}\n")

        run_cmd(f"git add {filename}")
        run_cmd(f'git commit -m "{commit_msg}"')
        run_cmd("git push origin main")

        print(f"Pushed commit #{i}")

if __name__ == "__main__":
    main()
