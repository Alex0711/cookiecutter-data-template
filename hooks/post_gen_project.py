import os
import subprocess
ERROR_COLOR = "\x1b[31m"
WARNING_COLOR = "\x1b[33m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

project_slug = "{{ cookiecutter.project_slug }}"
environment = "{{ cookiecutter.environment }}"

def run_command(command, error_message):
    """Ejecuta un comando y muestra errores si falla."""
    print(f"{MESSAGE_COLOR}{command}{RESET_ALL}")
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        print(f"{ERROR_COLOR}[ERROR] {error_message}: {result.stderr}{RESET_ALL}")
        exit(1)

# os.chdir(project_slug)

print(f"{MESSAGE_COLOR}Setting up the environment...{RESET_ALL}")

if environment == "conda":
    run_command(f"conda env create -f environment.yml", "Failed to create Conda environment")
    run_command(f"rm -rf requirements.txt", "Failed to remove requirements.txt")
    print(f"{MESSAGE_COLOR}Conda environment created!{RESET_ALL}")

else:
    
    run_command("python3 -m venv venv", "Failed to create venv")    
    run_command("venv/bin/python -m pip install --upgrade pip", "Failed to upgrade pip")
    run_command("venv/bin/python -m pip install -r requirements.txt", "Failed to install dependencies")
    run_command("rm -rf environment.yml", "Failed to remove environment.yml")
    print(f"{MESSAGE_COLOR}Virtual environment created!{RESET_ALL}")

print(f"{MESSAGE_COLOR}Initializing Git repository...{RESET_ALL}")
run_command("git init", "Failed to initialize Git repository")
run_command("git add .", "Failed to add files to Git")
run_command('git commit -m "Initial commit"', "Failed to create initial commit")

print(f"{MESSAGE_COLOR}Project setup complete!{RESET_ALL}")