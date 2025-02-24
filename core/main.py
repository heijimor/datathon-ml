from fastapi import FastAPI
from app.services.pipeline.train import Train
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
Train().schedule()
routes.handle(app)

@app.get("/")
async def root():
    return {"message": "Welcome to ML FIAP Datathon"}