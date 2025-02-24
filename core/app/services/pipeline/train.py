import app.services.pipeline.recommentation
import time
from app.services.pipeline.pre_processing import pre_processing
from app.services.pipeline.build import build
from app.services.pipeline.evaluate import evaluate
from apscheduler.schedulers.background import BackgroundScheduler
from app.services.pipeline.recommentation import RecommendationSystem

class Train:
    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def start(self):
        print("Training initializing...")
        pre_processing()
        build()
        recommendationSystem = RecommendationSystem()
        recommendationSystem.generate()
        evaluate()
        print("Model training completed!")

    def schedule(self):
        self.scheduler.add_job(self.start, "interval", seconds=60)
        self.scheduler.start()