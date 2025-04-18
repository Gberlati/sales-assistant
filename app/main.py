from fastapi import FastAPI, Request
from app.telegram_bot import setup_telegram_webhook, bot_app
from app.database import init_db
import telegram

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    init_db()
    await setup_telegram_webhook()

@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = telegram.Update.de_json(data, bot_app.bot)
    await bot_app.process_update(update)
    return {"ok": True}
