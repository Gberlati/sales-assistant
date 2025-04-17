from fastapi import FastAPI
from app.telegram_bot import setup_telegram_webhook
from app.database import init_db

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    init_db()
    await setup_telegram_webhook()

