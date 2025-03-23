import time
import json
import logging
from logging_config import setup_logger
from synthetic_ot_log_generator import generate_ot_log
from rule_based_detection import detect_threat
from real_llm_analysis import analyze_with_real_llm
from log_storage import init_db, store_log

logger = setup_logger("siem", "siem.log", level=logging.DEBUG)

def main():
    init_db()
    logger.info("Starting SIEM demo. Press Ctrl+C to stop.")
    try:
        while True:
            log_entry = generate_ot_log()
            if detect_threat(log_entry):
                logger.warning("ALERT: Threat detected in log: %s", json.dumps(log_entry, indent=2))
                llm_result = analyze_with_real_llm(log_entry)
                log_entry["llm_result"] = llm_result
                logger.info("LLM analysis result: %s", llm_result)
            else:
                log_entry["llm_result"] = None
            logger.debug("Generated log: %s", json.dumps(log_entry, indent=2))
            store_log(log_entry)
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("SIEM demo terminated by user.")
    except Exception as e:
        logger.exception("An error occurred: %s", e)

if __name__ == "__main__":
    main()
