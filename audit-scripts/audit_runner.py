import subprocess
import sys

def run_slither(target_path):
    try:
        subprocess.run(["slither", target_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Slither scan failed: {e}")

def run_foundry_tests(target_path):
    try:
        subprocess.run(["forge", "test", "--root", target_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Foundry test failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python audit_runner.py [slither|foundry] [target_path]")
        sys.exit(1)

    tool = sys.argv[1]
    target = sys.argv[2]

    if tool == "slither":
        run_slither(target)
    elif tool == "foundry":
        run_foundry_tests(target)
    else:
        print("Unknown tool. Use 'slither' or 'foundry'.")
