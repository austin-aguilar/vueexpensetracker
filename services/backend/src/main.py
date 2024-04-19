from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 

from src.db.register import register_tortoise
from src.db.config import Tortoise_ORM

Tortoise.init_models(['src.db.models'], 'models')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_tortoise(app, config=Tortoise_ORM, generate_schemas = False)

@app.get("/")
def home():
    return "Hello World!"