from apscheduler.schedulers.background import BackgroundScheduler
from app.services.train import train_model

scheduler = BackgroundScheduler()

def train_scheduler():
  scheduler.add_job(train_model, "interval", seconds=30)
  scheduler.start()