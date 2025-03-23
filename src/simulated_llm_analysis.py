def analyze_with_llm(log_entry):
    if log_entry['event_type'] == 'WARNING':
        return "LLM Analysis: Warning event detected. Please verify system status."
    return "LLM Analysis: No further action required."

if __name__ == "__main__":
    sample_log = {
        "timestamp": "2023-03-21T12:00:00",
        "device_id": "PLC-2",
        "event_type": "WARNING",
        "message": "Simulated log event from PLC-2 with event WARNING"
    }
    result = analyze_with_llm(sample_log)
    print(result)
