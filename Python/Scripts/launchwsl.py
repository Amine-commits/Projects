## script to launch wsl

import subprocess

def launch_wsl_as_root():
    try:
        # Command to launch WSL with root
        command = "wsl -u root"
        
        # Execute the command
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to launch WSL as root. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    launch_wsl_as_root()