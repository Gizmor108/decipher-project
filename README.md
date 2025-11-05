# 🧠 Decipher  
### A Secure File Encryption & Decryption Tool  
*Built with Python — by Gizmo and Blessed*

██████╗ ███████╗ ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
██╔══██╗██╔════╝██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
██║  ██║█████╗  ██║     ██║██████╔╝███████║█████╗  ██████╔╝
██║  ██║██╔══╝  ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
██████╔╝███████╗╚██████╗██║██║     ██║  ██║███████╗██║  ██║
╚═════╝ ╚══════╝ ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝



---

## 🔐 Overview

**Decipher** is a Python-based CLI tool for **secure file encryption and decryption**.  
It allows users to generate AES keys, protect those keys with RSA public/private pairs, and safely share encrypted files.  
Everything happens locally — **no data ever leaves your system.**

---

## ⚙️ Features

✅ Generate and store AES-256 secret keys  
✅ Encrypt and decrypt files with OpenSSL  
✅ Generate RSA key pairs for secure key sharing  
✅ Encrypt/decrypt secret keys with RSA public/private keys  
✅ Fully interactive CLI with command hints  
✅ Works on **Windows**, **Linux**, and **macOS**

---

## Installation

### 1️⃣ Clone the repository:
```bash
git clone https://github.com/<Gizmor108/Decipher.git
cd Decipher

Make sure Python 3.x and OpenSSL are installed:
python --version
openssl version

🚀 Usage

python decipher.py
