import hashlib  # Hash banane ke liye library

# Function to calculate SHA256 hash of a file
def get_file_hash(filename):
    with open(filename, 'rb') as f:  # 'rb' means read in binary
        file_data = f.read()         # File ka data read
        return hashlib.sha256(file_data).hexdigest()  # Hash generate

# Input le rahe user se
file1 = input("Enter first file path: ")
file2 = input("Enter second file path: ")

# Hash generate
hash1 = get_file_hash(file1)
hash2 = get_file_hash(file2)

# Compare karke result de rahe
if hash1 == hash2:
    print("✅ Files are same (No change detected)")
else:
    print("⚠️ Files are different (Change detected)")
