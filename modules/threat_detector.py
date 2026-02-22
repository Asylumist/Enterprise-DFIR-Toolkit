def calculate_risk(failed_attempts, suspicious_files):

    score = 0

    if failed_attempts >= 5:
        score += 2

    if len(suspicious_files) > 0:
        score += 2

    if failed_attempts >= 10:
        score += 1  # extra severity

    if score == 0:
        return "LOW"
    elif score <= 2:
        return "MEDIUM"
    else:
        return "HIGH"