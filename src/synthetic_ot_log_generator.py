import time
import random
import json

def generate_ot_log():
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%S")
    device_id = random.choice(["PLC-1", "PLC-2", "SCADA-1", "Sensor-1"])
    event_type = random.choice(["START", "STOP", "ERROR", "WARNING", "INFO"])
    message = f"Simulated log event from {device_id} with event {event_type}"
    log_entry = {
        "timestamp": timestamp,
        "device_id": device_id,
        "event_type": event_type,
        "message": message
    }
    return log_entry

if __name__ == "__main__":
    for _ in range(5):
        log = generate_ot_log()
        print(json.dumps(log, indent=2))
        time.sleep(1)