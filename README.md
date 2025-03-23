# SIEM Demo

This repository contains a demo prototype of a SIEM (Security Information and Event Management) system for OT security in an automotive environment. The demo includes synthetic log generation, rule-based and enhanced threat detection, log storage in SQLite, real-time visualization via a Flask dashboard, and integration with a real LLM (Large Language Model) for log analysis.

## Features

- **Synthetic Log Generation**  
  Simulates OT logs from various devices (e.g., PLC, SCADA, Sensors).

- **Threat Detection**  
  Implements both basic and enhanced rule-based threat detection. Alerts are triggered for specific event types (e.g., `ERROR` events and `WARNING` events from `SCADA-1`).

- **Log Storage**  
  Persists logs, along with LLM analysis results, in an SQLite database for later analysis.

- **LLM Analysis**  
  Integrates with a real LLM API (e.g., OpenAI GPT-3/4) to analyze log entries and provide recommendations.

- **Dashboard Visualization**  
  A Flask-based web dashboard displays stored logs with LLM analysis results and supports client-side filtering.

- **Logging and Error Handling**  
  Uses Python's `logging` module to record key events, API call performance, and errors.

## Prerequisites

- **Python 3.x**
- **Virtual Environment:** Recommended for package management.
- **SQLite:** No extra installation is required since Python includes the `sqlite3` module.
- **Flask:** Used for the web dashboard.
- **OpenAI API Key:** Required for real LLM integration (set as an environment variable).

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/siem-demo.git
   cd siem-demo
   ```
Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```
Set your OpenAI API key:
Export your API key as an environment variable:

```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```
Usage
Run the SIEM Demo
To generate logs, perform threat detection, analyze with the LLM, and store logs in the database, run:

```bash
python3 src/main.py
```
Run the Dashboard
To view stored logs and LLM analysis results, run the Flask dashboard:

```bash
python3 src/dashboard.py
```
Then open your browser and navigate to http://127.0.0.1:5000/.

Testing
Tests are located in the tests/ directory. You can run the tests with your preferred testing tool (e.g., pytest):

```bash
pytest tests/
```
Future Enhancements
Advanced Threat Detection:
Integrate more advanced machine learning models and anomaly detection techniques.

Dashboard Enhancements:
Expand the dashboard with additional filtering, sorting, and graphical visualizations.

Performance Monitoring:
Improve error handling, implement API call retries, and add performance monitoring.

Integration:
Extend integration with additional external systems and further enrich log data.



