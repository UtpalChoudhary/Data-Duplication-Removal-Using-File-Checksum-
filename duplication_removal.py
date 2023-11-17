import os
import hashlib

# Function to calculate the checksum of a file
def calculate_checksum(file_path, block_size=65536, algorithm='md5'):
    hash_algorithm = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            hash_algorithm.update(data)
    return hash_algorithm.hexdigest()

# Function to find and remove duplicate files
def remove_duplicate_files(directory):
    # Dictionary to store checksums and their corresponding file paths
    checksums = {}

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            checksum = calculate_checksum(file_path)

            if checksum in checksums:
                # This file is a duplicate; remove it
                print(f"Removing duplicate file: {file_path}")
                os.remove(file_path)
            else:
                # This is a new file; add its checksum to the dictionary
                checksums[checksum] = file_path

if __name__ == "__main__":
    directory_to_scan = "Duplicate"
    remove_duplicate_files(directory_to_scan)


