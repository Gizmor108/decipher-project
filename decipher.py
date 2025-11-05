#!/usr/bin/env python3
import os
import subprocess
import sys



# ────────────────────────────────────────────────
# Banner / Branding (the "rizz")
# ────────────────────────────────────────────────
BANNER = """
    ██████╗ ███████╗ ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
    ██╔══██╗██╔════╝██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
    ██║  ██║█████╗  ██║     ██║██████╔╝███████║█████╗  ██████╔╝
    ██║  ██║██╔══╝  ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
    ██████╔╝███████╗╚██████╗██║██║     ██║  ██║███████╗██║  ██║
    ╚═════╝ ╚══════╝ ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                               A Secure File Encryption & Decryption Tool
           by Gizmo and Blessed
"""
# ────────────────────────────────────────────────
# Utility functions
# ────────────────────────────────────────────────

def generate_secret_key():
    subprocess.run(["openssl", "rand", "-base64", "32"], stdout=open("secret.key", "w"))
    print("✅ Secret key generated and saved as secret.key")

def encrypt_file(file_path, key_path):
    if not os.path.exists(file_path):
        print("❌ File not found:", file_path)
        return
    subprocess.run([
        "openssl", "enc", "-aes-256-cbc", "-salt",
        "-in", file_path,
        "-out", file_path + ".enc",
        "-pass", f"file:{key_path}"
    ])
    print(f"✅ Encrypted {file_path} → {file_path}.enc")

def decrypt_file(encrypted_file, key_path):
    try:
        out_file = encrypted_file.replace(".enc", "")
        subprocess.run([
            "openssl", "enc", "-aes-256-cbc", "-d",
            "-in", encrypted_file,
            "-out", out_file,
            "-pass", f"file:{key_path}"
        ], check=True)
        print(f"✅ Decrypted {encrypted_file} → {out_file}")
    except subprocess.CalledProcessError:
        print("❌ Failed to decrypt file. Check your paths or key.")

def generate_rsa_keys():
    user_name = input("Enter your name (for public key naming): ").strip()
    private_key = "private-key.pem"
    public_key = f"{user_name}_public_key.pem"

    print("🔑 Generating RSA keys... You'll be prompted for a passphrase.")
    try:
        subprocess.run([
            "openssl", "genpkey", "-algorithm", "RSA",
            "-aes-256-cbc", "-out", private_key
        ], check=True)
        subprocess.run([
            "openssl", "rsa", "-in", private_key,
            "-pubout", "-out", public_key
        ], check=True)
        print(f"✅ RSA keys generated!\nPrivate: {private_key}\nPublic: {public_key}")
    except subprocess.CalledProcessError:
        print("❌ Failed to generate RSA keys.")


def encrypt_secret_key(public_key_path):
    if not os.path.exists("secret.key"):
        print("❌ secret.key not found. Run 'generate secret key' first.")
        return
    subprocess.run([
        "openssl", "pkeyutl", "-encrypt",
        "-inkey", public_key_path,
        "-pubin",
        "-in", "secret.key",
        "-out", "encrypted_secret.key"
    ])
    print("✅ Secret key encrypted → encrypted_secret.key")

def decrypt_secret_key(encrypted_key_path, private_key_path):
    try:
        subprocess.run([
            "openssl", "pkeyutl", "-decrypt",
            "-inkey", private_key_path,
            "-in", encrypted_key_path,
            "-out", "decrypted_secret.key"
        ], check=True)
        print("✅ Secret key decrypted → decrypted_secret.key")
    except subprocess.CalledProcessError:
        print("❌ Failed to decrypt secret key. Check your files and paths.")

# ────────────────────────────────────────────────
# Main interactive CLI
# ────────────────────────────────────────────────

def main():
    # Print the rizz banner once on startup
    print(BANNER)
    print("Commands:")
    print("  - generate secret key")
    print("  - encrypt file <path/to/file>")
    print("  - generate rsa keys")
    print("  - encrypt secret key with <path/to/public_key>")
    print("  - decrypt secret key <encrypted_secret_key_path> with <private_key_path>")
    print("  - decrypt file <encrypted_file_path> with <decrypted_key_path>")
    print("  - exit\n")

    while True:
        user_input = input("decipher> ").strip()
        if user_input.lower() == "exit":
            print("👋 Goodbye.")
            break
        elif user_input.lower() == "generate secret key":
            generate_secret_key()

        elif user_input.lower().startswith("encrypt file "):
            parts = user_input.split(" ", 2)
            if len(parts) < 3:
                print("❌ Usage: encrypt file <path/to/file>")
            else:
                encrypt_file(parts[2].strip('"'), "secret.key")
        elif user_input.lower() == "generate rsa keys":
            generate_rsa_keys()
            
        elif user_input.lower().startswith("encrypt secret key with "):
            pubkey = user_input.lower().replace("encrypt secret key with ", "").strip('" ')
            encrypt_secret_key(pubkey)
            
        elif user_input.lower().startswith("decrypt secret key "):
            # Cleanly split on ' with '
            try:
                before, after = user_input[19:].split(" with ")
                decrypt_secret_key(before.strip('" '), after.strip('" '))
            except ValueError:
                print("❌ Usage: decrypt secret key <encrypted_secret_key_path> with <private_key_path>")

        elif user_input.lower().startswith("decrypt file "):
            try:
                # Split once on " with " to handle spaces or quotes in paths
                before, after = user_input[13:].split(" with ")
                decrypt_file(before.strip('" '), after.strip('" '))
            except ValueError:
                print("❌ Usage: decrypt file <encrypted_file_path> with <decrypted_key_path>")
            
        else:
            print("❌ Unknown command. Try one of the listed options.")
if __name__ == "__main__":
    main()

