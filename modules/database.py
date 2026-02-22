import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("dfir_cases.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_id TEXT,
            risk_level TEXT,
            failed_attempts INTEGER,
            suspicious_files INTEGER,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_case(case_id, risk_level, failed_attempts, suspicious_files):
    conn = sqlite3.connect("dfir_cases.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO cases (case_id, risk_level, failed_attempts, suspicious_files, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (
        case_id,
        risk_level,
        failed_attempts,
        suspicious_files,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()