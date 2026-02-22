import re
from collections import Counter

def analyze_log(log_file_path):
    failed_attempts = 0
    ip_list = []

    with open(log_file_path, "r", errors="ignore") as f:
        for line in f:
            if "Failed password" in line or "failed login" in line.lower():
                failed_attempts += 1

                # Extract IP address
                ip_match = re.search(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", line)
                if ip_match:
                    ip_list.append(ip_match.group())

    ip_counter = Counter(ip_list)

    return failed_attempts, ip_counter