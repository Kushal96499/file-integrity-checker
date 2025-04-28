# 🔐 Advanced File Integrity Checker (Colorful Terminal Version)

This is a **File Integrity Checker** tool with a **colorful, user-friendly interface** built using **Python 3**.  
It is specially developed during the **Cyber Security Internship at CODTECH** by **Kushal**.

---

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: KUSHAL KUMAWAT

*INTERN ID*: CT04DK768

*DOMAIN*: Cyber Security & Ethical Hacking

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

---

## ✨ Features

- 🎨 Color-coded terminal output for better readability
- 🔒 Calculates **SHA-256** secure hashes
- 💾 **Saves** file hashes in a local JSON database
- 🔍 **Verifies** file integrity anytime
- 🛡️ Helps detect unauthorized file modifications
- 🧠 Fully **user-friendly menu** and messages
- 📜 **Internship credit** included (CODTECH Cyber Security)

---

## 📦 Requirements

- Python 3.x
- No external libraries needed (uses only built-in modules)

---

## 🚀 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/Kushal96499/file-integrity-checker.git
cd file-integrity-checker
```

2. Run the Script
```bash
python3 file_integrity_checker.py
```
---

## 🖥️ Menu Options
### Option | Action
 #### 1      | Save hash of a file.
 #### 2      | Verify integrity of a file.
 #### 3      | Exit the tool.

---

## 📂 Folder Structure
### file-integrity-checker/
#### │
#### ├── file_integrity_checker.py   # Main Python Script
#### ├── hashes.json                 # (Auto-created) Database of saved hashes
#### ├── README.md                   # Project Guide

---

# ⚡ Example Usage
Save File Hash
```bash
python3 file_integrity_checker.py
```
Enter your choice (1/2/3): 1
Enter the full path of the file: /home/kushal/Documents/test.txt
[+] Hash saved successfully for file: /home/kushal/Documents/test.txt

Verify File Integrity
```bash
python3 file_integrity_checker.py
```
Enter your choice (1/2/3): 2
Enter the full path of the file: /home/kushal/Documents/test.txt
[✔] File is intact. No changes detected.

OR (if file changed)
[⚠] WARNING: File has been modified!

---

## 📢 Important Notes
Always save the hash first before trying to verify file integrity.

Deleting or modifying hashes.json will remove saved data.

The tool uses SHA-256 encryption for strong security.

Works on Linux (Kali, Ubuntu) and Windows both.

---

# 📸 Screenshots 

![Image](https://github.com/user-attachments/assets/ac98ae55-bdb3-4413-a4e6-59a99f237ac8)

---
## 🤝 Credits
Developed with ❤️ by Kushal Kumawat
for the CODTECH Cyber Security Internship Program.
