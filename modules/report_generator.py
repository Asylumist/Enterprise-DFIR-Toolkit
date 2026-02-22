from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, case_id, md5, sha256, failed_attempts, suspicious_files, risk, timeline, ip_data):

    doc = SimpleDocTemplate(filename)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph("Digital Forensics Investigation Report", styles["Title"]))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph(f"Case ID: {case_id}", styles["Normal"]))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph("Evidence Hashes:", styles["Heading2"]))
    elements.append(Paragraph(f"MD5: {md5}", styles["Normal"]))
    elements.append(Paragraph(f"SHA256: {sha256}", styles["Normal"]))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph("Log Analysis:", styles["Heading2"]))
    elements.append(Paragraph(f"Failed Login Attempts: {failed_attempts}", styles["Normal"]))
    elements.append(Spacer(1, 20))

    # IP Section
    elements.append(Paragraph("Suspicious IP Analysis:", styles["Heading2"]))
    elements.append(Spacer(1, 10))

    if ip_data:
        for ip, count in ip_data.items():
            elements.append(Paragraph(f"{ip} - Attempts: {count}", styles["Normal"]))
    else:
        elements.append(Paragraph("No suspicious IPs detected.", styles["Normal"]))

    elements.append(Spacer(1, 20))

    # Suspicious Files
    elements.append(Paragraph("Suspicious Files Detected:", styles["Heading2"]))
    elements.append(Spacer(1, 10))

    if suspicious_files:
        for file in suspicious_files:
            elements.append(Paragraph(file, styles["Normal"]))
    else:
        elements.append(Paragraph("No suspicious files detected.", styles["Normal"]))

    elements.append(Spacer(1, 20))

    # Timeline
    elements.append(Paragraph("Investigation Timeline:", styles["Heading2"]))
    elements.append(Spacer(1, 10))

    if timeline:
        for event in timeline:
            elements.append(Paragraph(event, styles["Normal"]))
    else:
        elements.append(Paragraph("No timeline events recorded.", styles["Normal"]))

    elements.append(Spacer(1, 20))

    elements.append(Paragraph(f"Overall Risk Level: {risk}", styles["Heading2"]))

    doc.build(elements)