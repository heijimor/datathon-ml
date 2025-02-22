from fastapi import FastAPI
from app.services.train_scheduler import train_scheduler
import routes
from fastapi.middleware.cors import CORSMiddleware

def enableCors(app):
    origins = [
        "http://localhost:5173",
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app = FastAPI()
enableCors(app)
train_scheduler()
routes.handle(app)

@app.get("/")
async def root():
    return {"message": "Welcome to ML FIAP Datathon"}