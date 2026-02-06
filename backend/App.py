from fastapi import FastAPI
from .Scheduler import start_scheduler
import mysql.connector

app = FastAPI(title="EchoTrace-AutoShield")

@app.on_event("startup")
def startup_event():
    start_scheduler()

@app.get("/")
def root():
    return {"status": "EchoTrace running in background"}

@app.get("/logs")
def get_logs():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_mysql_password",
        database="echotrace"
    )

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM logs ORDER BY id DESC")
    logs = cursor.fetchall()

    cursor.close()
    conn.close()
    return logs
