from flask import Flask, render_template, g
import sqlite3
from log_storage import init_db

app = Flask(__name__, template_folder="../templates")
DB_NAME = "logs.db"

init_db()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_NAME)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT timestamp, device_id, event_type, message, llm_result FROM logs ORDER BY id DESC")
    logs = cursor.fetchall()
    return render_template("index.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
