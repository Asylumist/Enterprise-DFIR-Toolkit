import hashlib

def generate_hashes(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        md5_hash = hashlib.md5(data).hexdigest()
        sha256_hash = hashlib.sha256(data).hexdigest()
    return md5_hash, sha256_hash
