import os
import openai
import json
import logging
import time

logger = logging.getLogger("siem")
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_with_real_llm(log_entry):
    prompt = (
        f"Analyze the following log entry from an OT system and provide a brief summary "
        f"of potential issues or recommendations for further investigation:\n\n{json.dumps(log_entry, indent=2)}"
    )
    max_retries = 3
    for attempt in range(max_retries):
        try:
            start_time = time.time()
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=100,
                temperature=0.5
            )
            duration = time.time() - start_time
            logger.info("LLM API call succeeded in %.2f seconds", duration)
            return response.choices[0].text.strip()
        except Exception as e:
            logger.exception("LLM API call failed on attempt %d: %s", attempt + 1, e)
            if attempt < max_retries - 1:
                time.sleep(1)
            else:
                return f"Error during LLM analysis after {max_retries} attempts: {e}"

if __name__ == "__main__":
    sample_log = {
        "timestamp": "2025-03-24T01:15:00",
        "device_id": "PLC-1",
        "event_type": "ERROR",
        "message": "Test error log from PLC-1"
    }
    analysis = analyze_with_real_llm(sample_log)
    print("LLM Analysis Result:")
    print(analysis)
