import asyncio
import os
from telegram import Bot
from datetime import datetime


current_date = datetime.now().strftime("%Y-%m-%d")
async def envoyer_message_telegram(message, chat_id, token):
    bot = Bot(token=token)
    await bot.send_message(chat_id=chat_id, text=message)

if __name__ == "__main__":
    # Remplacez YOUR_BOT_TOKEN par le token de votre bot Telegram
    token = "YOUR_BOT_TOKEN"

    # Remplacez CHAT_ID par l'identifiant du chat où vous souhaitez envoyer le message
    chat_id = "CHAT_ID"

    message2 = f" The 🔗FIREFOX🔗 shortcut is launched 🤖✅"
  
    

    # Utilisez asyncio pour exécuter la coroutine
    asyncio.run(envoyer_message_telegram(message2, chat_id, token))
  

