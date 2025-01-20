import os
import zipfile
from shutil import copyfile
import urllib.request

# Define paths
home_dir = os.path.expanduser("~")
local_bin_dir = os.path.join(home_dir, ".local", "bin")
kerbusers_script = "kerbusers.py"
kerbrute_url = "https://github.com/ropnop/kerbrute/releases/download/v1.0.3/kerbrute_linux_amd64"
kerbrute_dest = os.path.join(local_bin_dir, "kerbrute")
wordlists_zip = "wordlists.zip"
wordlists_dest = os.path.join(local_bin_dir, "wordlists")

# Create local bin directory if it doesn't exist
if not os.path.exists(local_bin_dir):
    os.makedirs(local_bin_dir)

# Copy kerbusers script to local bin and set executable permissions
kerbusers_dest = os.path.join(local_bin_dir, "kerbusers.py")
copyfile(kerbusers_script, kerbusers_dest)
os.chmod(kerbusers_dest, 0o755)

# Download kerbrute binary and set executable permissions
print(f"Downloading kerbrute from {kerbrute_url}...")
urllib.request.urlretrieve(kerbrute_url, kerbrute_dest)
os.chmod(kerbrute_dest, 0o755)

# Extract wordlists.zip to the local bin directory
if os.path.exists(wordlists_zip):
    with zipfile.ZipFile(wordlists_zip, 'r') as zip_ref:
        zip_ref.extractall(local_bin_dir)
    print(f"Wordlists extracted to {wordlists_dest}.")
else:
    print(f"{wordlists_zip} not found. Please ensure it is in the current directory.")

# Add shell alias for kerbusers
shell = os.environ.get("SHELL", "").lower()
alias_command = f'alias kerbusers="python3 {kerbusers_dest}"'

config_file = None
if "zsh" in shell:
    config_file = os.path.join(home_dir, ".zshrc")
elif "bash" in shell:
    config_file = os.path.join(home_dir, ".bashrc")

if config_file:
    with open(config_file, "a") as shell_rc:
        shell_rc.write(alias_command)
    print(f"Alias for kerbusers added to {config_file}.")
    print(f"To use the alias immediately, run:\n  source {config_file}")
else:
    print("Unknown shell. Please add the following alias manually:")
    print(alias_command)

# Completion messages
print(f"kerbusers has been installed to {kerbusers_dest}. You can run 'kerbusers' after sourcing your shell configuration.")
print(f"kerbrute has been downloaded and installed to {kerbrute_dest}.")
