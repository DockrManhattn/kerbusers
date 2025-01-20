import argparse
import os
import subprocess

YELLOW = "\033[33m"
DARK_WHITE = "\033[2;37m"
BLUE = "\033[34m"
RESET = "\033[0m"

def print_informational(message):
    informational_msg = f"{YELLOW}{{🌀🌵[+]🌵🌀}}{RESET}"
    print(f"{informational_msg}{DARK_WHITE}{message}{RESET}")

def print_error(message):
    error_msg = f"{YELLOW}{{🔥💀💥[+]💥💀🔥}}{RESET}"
    print(f"{error_msg} {DARK_WHITE}{message}{RESET}")


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Kerbrute Helper Script')

    # Add domain argument
    parser.add_argument('-d', '--domain', required=True, help='Specify the domain')

    # Add DC IP argument
    parser.add_argument('-dc-ip', '--dc_ip', required=True, help='Specify the Domain Controller IP address')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values
    domain = args.domain
    dc_ip = args.dc_ip

    # Get the current working directory
    script_directory = os.getcwd()

    # List of source files
    user_home = os.path.expanduser("~")
    source_files = [
        f'{user_home}/.local/bin/wordlists/test-accounts.txt',
        f'{user_home}/.local/bin/wordlists/service-accounts.txt',
        f'{user_home}/.local/bin/wordlists/services-list.txt',
        f'{user_home}/.local/bin/wordlists/custom_services.txt',
        f'{user_home}/.local/bin/wordlists/cirt-default-usernames.txt',
        f'{user_home}/.local/bin/wordlists/top-usernames-shortlist.txt',
        f'{user_home}/.local/bin/wordlists/top-formats.txt',
    ]

    # Destination file
    destination_file = 'kerb-helper-temp.txt'

    try:
        # Open the destination file in append mode to avoid overwriting
        with open(destination_file, 'a') as dest_file:
            for source_file in source_files:
                try:
                    # Copy the file content directly to the destination file
                    with open(source_file, 'r') as src_file:
                        for line in src_file:
                            # Avoid blank lines
                            if line.strip():
                                dest_file.write(line)

                except FileNotFoundError:
                    print_error(f"Warning: Source file not found - {source_file}")

    except Exception as e:
        print_error(f"Error: {e}")

    #print_informational(f"Domain: {domain}")
    #print_informational(f"DC IP: {dc_ip}")

    # Add your Kerbrute related logic here
    kerbrute_command = f"kerbrute userenum -d {domain} --dc {dc_ip} {destination_file} -t 100"

    try:
        # Create a file to save the Kerbrute output
        kerbrute_output_file = os.path.join(script_directory, 'kerb-users-01.txt')

        # Run sed command on the destination file and capture the output to a temporary file
        temp_sed_output_file = 'temp_sed_output.txt'
        sed_command = f"sed 's/$/@{domain}/' {destination_file} > {temp_sed_output_file}"
        subprocess.run(sed_command, shell=True, check=True)

        try:
            # Remove duplicates using awk and write the sed output back to the destination file
            with open(destination_file, 'w') as dest_file:
                subprocess.run(f"awk '!x[$0]++' {temp_sed_output_file}", shell=True, check=True, stdout=dest_file)

        finally:
            # Remove the temporary sed output file
            os.remove(temp_sed_output_file)

        # Run kerbrute command and tee the output to both terminal and file
        with open(kerbrute_output_file, 'w') as kerb_output_file:
            subprocess.run(f"{kerbrute_command} < {destination_file} | tee {kerb_output_file.name}", shell=True, check=True)

        # Remove the kerb-helper-temp.txt file
        os.remove(destination_file)
    
        # Debugging output
        #print(f"Temporary kerb-helper file removed: {destination_file}")

    except subprocess.CalledProcessError as e:
        print_error(f"Error running Kerbrute: {e}")

if __name__ == "__main__":
    main()
