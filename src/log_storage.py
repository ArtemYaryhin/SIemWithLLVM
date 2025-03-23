import sqlite3

DB_NAME = "logs.db"

def init_db(db_name=DB_NAME):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            device_id TEXT,
            event_type TEXT,
            message TEXT,
            llm_result TEXT
        )
    ''')
    conn.commit()
    conn.close()

def store_log(log_entry, db_name=DB_NAME):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO logs (timestamp, device_id, event_type, message, llm_result) VALUES (?, ?, ?, ?, ?)",
        (
            log_entry["timestamp"],
            log_entry["device_id"],
            log_entry["event_type"],
            log_entry["message"],
            log_entry.get("llm_result")
        )
    )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    sample_log = {
        "timestamp": "2025-03-24T01:05:00",
        "device_id": "PLC-1",
        "event_type": "INFO",
        "message": "Test log entry for storage",
        "llm_result": None
    }
    store_log(sample_log)
    print("Log stored successfully.")
