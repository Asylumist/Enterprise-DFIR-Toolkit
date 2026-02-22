import os

SUSPICIOUS_EXTENSIONS = [".exe", ".bat", ".ps1", ".dll"]

def scan_directory(folder_path):
    suspicious_files = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in SUSPICIOUS_EXTENSIONS):
                suspicious_files.append(os.path.join(root, file))

    return suspicious_files
