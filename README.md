# 🛡️ File Integrity Checker - Python

This is a simple and powerful *File Integrity Checker* built using Python. It helps verify whether two files are exactly the same or have been tampered with, by comparing their *SHA-256 hash values*.

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: KUSHAL KUMAWAT

*INTERN ID*: CT04DK768

*DOMAIN*: Cyber Security & Ethical Hacking

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

---

## 📌 Features

- ✅ Compares two files securely using SHA-256
- 🔐 Detects even the smallest changes in file content
- 🧠 Simple and beginner-friendly Python script
- 📂 CLI-based tool — works on Linux, Windows, MacOS

---

## 🚀 How It Works

1. You provide two file paths.
2. The script calculates the *SHA-256 hash* for both files.
3. If hashes match → files are same.
4. If hashes differ → files have been modified.

---

## 🧪 Example Usage

### 🔹 Step 1: Create test files

echo "This is a test file" > file1.txt
cp file1.txt file2.txt

🔹 Step 2: Run the script

python3 file_integrity_checker.py

🔹 Step 3: Enter file paths when prompted

Enter first file path: file1.txt
Enter second file path: file2.txt

🔹 Output

✅ Files are same (No change detected)

🧰 Requirements
Python 3.x

No extra libraries required (uses built-in hashlib)

🧠 Concepts Used
SHA-256 Hashing

File handling in binary mode

Hash comparison for file integrity check

## 📁 File Structure

### file_integrity_task/
### ├── file1.txt
### ├── file2.txt
### └── file_integrity_checker.py

👨‍💻 Author
Kushal Kumawat
Cyber Security & Ethical Hacking Intern @ CodTech
Kali Linux User 💻 | Python Learner 🐍

📜 License
This project is open-source and free to use for educational purposes.
