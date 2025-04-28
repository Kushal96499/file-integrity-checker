import hashlib
import json
import os
import sys

HASH_DATABASE = 'hashes.json'

# Color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'

def calculate_hash(filename):
    """
    Calculates the SHA-256 hash of a file.
    """
    h = hashlib.sha256()
    with open(filename, 'rb') as file:
        chunk = file.read(1024)
        while chunk:
            h.update(chunk)
            chunk = file.read(1024)
    return h.hexdigest()

def load_hashes():
    """
    Loads the saved hashes from the JSON database.
    """
    if not os.path.exists(HASH_DATABASE):
        return {}
    with open(HASH_DATABASE, 'r') as f:
        return json.load(f)

def save_hashes(hashes):
    """
    Saves the hashes dictionary into the JSON database.
    """
    with open(HASH_DATABASE, 'w') as f:
        json.dump(hashes, f, indent=4)

def save_file_hash(filename):
    """
    Saves the SHA-256 hash of a given file into the database.
    """
    hashes = load_hashes()
    file_hash = calculate_hash(filename)
    hashes[filename] = file_hash
    save_hashes(hashes)
    print(f"{GREEN}[+] Hash saved successfully for file:{RESET} {filename}")

def verify_file_integrity(filename):
    """
    Verifies if the file has been modified by comparing current hash with saved hash.
    """
    hashes = load_hashes()
    if filename not in hashes:
        print(f"{RED}[-] No saved hash found for {filename}.{RESET} Please save the hash first.")
        return
    current_hash = calculate_hash(filename)
    saved_hash = hashes[filename]

    if current_hash == saved_hash:
        print(f"{GREEN}[✔] File '{filename}' is intact. No changes detected.{RESET}")
    else:
        print(f"{RED}[⚠] WARNING: File '{filename}' has been modified!{RESET}")

def banner():
    """
    Displays the project banner and internship info.
    """
    print(f"""
{CYAN}{BOLD}
===============================================
   FILE INTEGRITY CHECKER - ADVANCED VERSION
===============================================
{RESET}
{YELLOW}Developed by: KUSHAL KUMAWAT
Internship: Cyber Security Internship at CODTECH
{RESET}
""")

def main():
    """
    Main function to interact with the user.
    """
    banner()

    while True:
        print(f"""
{BLUE}Please select an option:{RESET}
{GREEN}1.{RESET} Save hash of a file
{GREEN}2.{RESET} Verify file integrity
{GREEN}3.{RESET} Exit
""")
        choice = input(f"{BOLD}Enter your choice (1/2/3): {RESET}")

        if choice == '1':
            filename = input(f"{CYAN}Enter the full path of the file to save hash:{RESET} ").strip()
            if os.path.isfile(filename):
                save_file_hash(filename)
            else:
                print(f"{RED}[-] File not found. Please enter a valid path.{RESET}")
        elif choice == '2':
            filename = input(f"{CYAN}Enter the full path of the file to verify:{RESET} ").strip()
            if os.path.isfile(filename):
                verify_file_integrity(filename)
            else:
                print(f"{RED}[-] File not found. Please enter a valid path.{RESET}")
        elif choice == '3':
            print(f"{YELLOW}Exiting... Thank you for using the File Integrity Checker!{RESET}")
            sys.exit()
        else:
            print(f"{RED}[-] Invalid choice. Please select 1, 2, or 3.{RESET}")

if __name__ == "__main__":
    main()
