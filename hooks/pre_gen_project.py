import sys
ERROR_COLOR = "\x1b[31m"
WARNING_COLOR = "\x1b[33m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

environment = "{{ cookiecutter.environment }}"
python_version = "{{ cookiecutter.python_version }}"
default_python_version = "3.12"

if environment not in ["venv", "conda"]:
    print(f"{ERROR_COLOR}[ERROR] Invalid environment choice. Choose 'venv' or 'conda'.{RESET_ALL}")
    sys.exit(1)

if environment == "conda":
    valid_versions = ["3.8", "3.9", "3.10", "3.11", "3.12"]
    if python_version not in valid_versions:
        print(f"{ERROR_COLOR}[ERROR] Python {python_version} is not common. Choices are: {valid_versions}.{RESET_ALL}")
        sys.exit(1)
elif environment == "venv":
    if python_version != default_python_version:
        print(f"{ERROR_COLOR}[ERROR] Python {python_version} is not available. Use {default_python_version} or select conda.{RESET_ALL}")
        sys.exit(1)
        