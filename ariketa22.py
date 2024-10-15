import os
import hashlib
import subprocess

def calculate_md5(file_path):
    # Calculate the MD5 hash of the file
    hash_md5 = hashlib.md5()
    # Read the file in chunks to avoid loading it all into memory
    with open(file_path, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def find_file_with_hash(folder_path, target_hash):
    # Walk through the folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Calculate the hash of the file   
            file_path = os.path.join(root, file)
            file_hash = calculate_md5(file_path)
            if file_hash == target_hash:
                return file_path
    print("No file with the specified hash found.")
    return None

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Command failed: {command}")
        print(result.stderr)
    return result.stdout

# Specify the folder path and target hash
folder_path = "/home/mikel/Descargas/imagen/" #Depende de donde se encuentre la imagen
target_hash = "e5ed313192776744b9b93b1320b5e268"

# Find the file
matching_file = find_file_with_hash(folder_path, target_hash)
print(f"Mezu sekretua duen argazkia: {matching_file} da.")
