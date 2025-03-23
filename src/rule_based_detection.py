def detect_threat(log_entry):
    if log_entry["event_type"] == "ERROR":
        return True
    if log_entry["event_type"] == "WARNING" and log_entry["device_id"] == "SCADA-1":
        return True
    return False

if __name__ == "__main__":
    sample_log1 = {
        "timestamp": "2025-03-21T01:10:00",
        "device_id": "SCADA-1",
        "event_type": "WARNING",
        "message": "Test warning from SCADA-1"
    }
    sample_log2 = {
        "timestamp": "2025-03-24T01:10:01",
        "device_id": "PLC-1",
        "event_type": "WARNING",
        "message": "Test warning from PLC-1"
    }
    print("Threat Detected:" if detect_threat_enhanced(sample_log1) else "No Threat Detected.")
    print("Threat Detected:" if detect_threat_enhanced(sample_log2) else "No Threat Detected.")
