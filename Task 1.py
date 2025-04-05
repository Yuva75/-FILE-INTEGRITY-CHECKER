import os
import hashlib
import time
import logging

# Setup logging
logging.basicConfig(filename='file_monitor.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to calculate the hash of a file
def calculate_hash(file_path):
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

# Function to monitor file changes
def monitor_files(file_paths, interval=5):
    file_hashes = {file: calculate_hash(file) for file in file_paths}

    while True:
        time.sleep(interval)
        for file in file_paths[:]:  # Use a copy to avoid modifying the list during iteration
            new_hash = calculate_hash(file)
           if new_hash is None:
                 logging.warning(f"File removed: {file}")
                  print(f"File removed: {file}")
                file_paths.remove(file)  # Remove from list only if it exists
           elif new_hash != file_hashes[file]:
                logging.warning(f"File changed: {file}")
                print(f"File changed: {file}")
                file_hashes[file] = new_hash  # Update stored hash

if __name__ == "__main__":
    # Use raw strings (r"") for Windows paths or double backslashes
    files_to_monitor = [r"M:\CS\ss1.txt", r"M:\CS\testing2.log"]  
    monitor_files(files_to_monitor)
