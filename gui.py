from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import datetime

def generate_report(filename, case_id, md5, sha256, failed_attempts, suspicious_files, risk, timeline, ip_data):

    doc = SimpleDocTemplate(filename)
    elements = []
    styles = getSampleStyleSheet()

    # ---------------- Title ----------------
    elements.append(Paragraph("Digital Forensics Investigation Report", styles["Title"]))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph(f"Case ID: {case_id}", styles["Normal"]))
    elements.append(Paragraph(f"Generated On: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles["Normal"]))
    elements.append(Spacer(1, 30))

    # ---------------- Evidence Section ----------------
    elements.append(Paragraph("1. Evidence Integrity Verification", styles["Heading2"]))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(f"MD5 Hash: {md5}", styles["Normal"]))
    elements.append(Paragraph(f"SHA256 Hash: {sha256}", styles["Normal"]))
    elements.append(Spacer(1, 25))

    # ---------------- Log Analysis ----------------
    elements.append(Paragraph("2. Log Analysis Summary", styles["Heading2"]))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(f"Failed Login Attempts: {failed_attempts}", styles["Normal"]))
    elements.append(Spacer(1, 20))

    # ---------------- Suspicious IP Section ----------------
    elements.append(Paragraph("3. Suspicious IP Analysis", styles["Heading2"]))
    elements.append(Spacer(1, 10))

    if ip_data:
        for ip, count in ip_data.items():
            elements.append(Paragraph(f"IP Address: {ip} | Attempts: {count}", styles["Normal"]))
    else:
        elements.append(Paragraph("No suspicious IPs detected.", styles["Normal"]))

    elements.append(Spacer(1, 25))

    # ---------------- Suspicious Files ----------------
    elements.append(Paragraph("4. Suspicious Files Detected", styles["Heading2"]))
    elements.append(Spacer(1, 10))

    if suspicious_files:
        for file in suspicious_files:
            elements.append(Paragraph(file, styles["Normal"]))
    else:
        elements.append(Paragraph("No suspicious files detected.", styles["Normal"]))

    elements.append(Spacer(1, 25))

    # ---------------- Timeline ----------------
    elements.append(Paragraph("5. Investigation Timeline", styles["Heading2"]))
    elements.append(Spacer(1, 10))

    if timeline:
        for event in timeline:
            elements.append(Paragraph(event, styles["Normal"]))
    else:
        elements.append(Paragraph("No timeline events recorded.", styles["Normal"]))

    elements.append(Spacer(1, 30))

    # ---------------- Risk Section ----------------
    elements.append(Paragraph("6. Overall Risk Assessment", styles["Heading2"]))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(f"Final Risk Level: {risk}", styles["Normal"]))

    doc.build(elements)