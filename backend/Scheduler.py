from apscheduler.schedulers.background import BackgroundScheduler
from .Predictor import run_prediction

scheduler = BackgroundScheduler()

def start_scheduler():
    scheduler.add_job(run_prediction, 'interval', minutes=2)
    scheduler.start()
