# 🛡️ Enterprise Digital Forensics & Incident Response Toolkit

## 📌 Overview

The **Enterprise DFIR Toolkit** is a modular Python-based digital forensics platform designed to simulate real-world forensic investigation workflows.

This system integrates:

- Evidence Integrity Verification (MD5, SHA256)
- Suspicious File Detection
- Log Analysis & Brute-Force Detection
- Suspicious IP Extraction
- Risk Scoring Engine
- Timeline Reconstruction
- Automated PDF Report Generation
- SQLite-based Case Management
- Enterprise GUI (CustomTkinter)
- Standalone Executable Deployment

---

## 🎯 Objectives

This project demonstrates:

- Practical implementation of DFIR concepts
- Modular software architecture
- Incident risk assessment modeling
- Persistent forensic case tracking
- Automated forensic reporting

---

## 🧠 Core Features

### 🔐 Evidence Integrity Module
Generates MD5 and SHA256 hashes to ensure evidence authenticity and integrity verification.

### 📂 Suspicious File Detection
Scans directories for potentially malicious file extensions (.exe, .dll, .ps1, etc.)

### 📜 Log Analysis Engine
- Detects failed authentication attempts  
- Extracts IP addresses  
- Identifies repeated brute-force sources  

### 🌐 Suspicious IP Analysis
Performs frequency analysis of IP addresses to identify potential attack origins.

### 📊 Risk Scoring System
Classifies investigations as:
- 🟢 LOW
- 🟡 MEDIUM
- 🔴 HIGH

Based on suspicious indicators and log activity.

### 🕒 Timeline Reconstruction
Records investigative workflow events with timestamps.

### 🗃 Case Management System
Uses SQLite to store investigation history persistently.

### 📄 Automated PDF Report
Generates structured forensic reports including:
- Hash values
- Log findings
- Suspicious IP analysis
- Suspicious files
- Timeline reconstruction
- Risk assessment

---

## 🖥 Technology Stack

- Python 3.x
- CustomTkinter
- SQLite3
- ReportLab
- PyInstaller

---

## 🚀 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Asylumist/Enterprise-DFIR-Toolkit.git
cd Enterprise-DFIR-Toolkit
