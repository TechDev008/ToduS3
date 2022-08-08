from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from todus3.client import ToDusClient
import os

bot = Client(
    "appbots3_techdev_bot",
    api_hash="131b576240be107210aace99a5f5c5b0",
    api_id=int(9024532), # aqui va el api id
    bot_token="5598005294:AAEPgR6Erjju1Kxi6eCRoHaTxMk2d-0nA_k",
)

Conversation_state = {}
token = open("token.txt", "r").read()

from pathlib import Path
@bot.on_message()
async def dl_file(client, message: Message):
    who = message.from_user.id
    state = Conversation_state.get(who)
    
    owner = 1593891519


    async def progress(current, total, client, info):
        prog = f"{current * 100 / total}%"
        await info.edit(f"Descargado OwO\n\n{prog}")
        print(prog)

    
    if message.document:
        if message.from_user.id == owner:

            info = await message.reply("Descargando puto, espera", quote=True)
            f = await message.download(file_name=f"./TodusDownload/", progress=progress, progress_args=(client, info))
            try:
                t = ToDusClient()
                print(f)
                spl = f.split("\\")[-1]
                print(spl)
                url = t.upload_file(token, Path(f))
                all = await message.reply(f"{url}" + "  " + f"{spl}")
                os.remove(f)
                with open(spl + ".txt", "w") as f:
                    f.write(all.text)
                await message.reply_document(document=spl + ".txt")
                os.remove(spl + ".txt")
            except Exception as e:
                print(e)
                await message.reply(f"Error: {e}")
        else:
            await message.reply("No tienes permisos para usar este bot")

    elif message.video:
        if message.from_user.id == owner:
            info = await message.reply("Descargando puto, espera", quote=True)
            f = await message.download(file_name=f"./TodusDownload/", progress=progress, progress_args=(client, info))
            try:
                t = ToDusClient()
                print(f)
                spl = f.split("\\")[-1]
                print(spl)
                url = t.upload_file(token, Path(f))
                all = await message.reply(f"{url}" + "  " + f"{spl}")
                os.remove(f)
                with open(spl + ".txt", "w") as f:
                    f.write(all.text)
                await message.reply_document(document=spl + ".txt")
                os.remove(spl + ".txt")
            except Exception as e:
                print(e)
                await message.reply(f"Error: {e}")
        else:
            await message.reply("No tienes permisos para usar este bot")

    elif message.audio:
        if message.from_user.id == owner:
            info = await message.reply("Descargando puto, espera", quote=True)
            f = await message.download(file_name=f"./TodusDownload/", progress=progress, progress_args=(client, info))
            try:
                t = ToDusClient()
                print(f)
                spl = f.split("\\")[-1]
                print(spl)
                url = t.upload_file(token, Path(f))
                all = await message.reply(f"{url}" + "  " + f"{spl}")
                os.remove(f)
                with open(spl + ".txt", "w") as f:
                    f.write(all.text)
                await message.reply_document(document=spl + ".txt")
                os.remove(spl + ".txt")
            except Exception as e:
                print(e)
                await message.reply(f"Error: {e}")
        else:
            await message.reply("No tienes permisos para usar este bot")

    elif message.photo:
        if message.from_user.id == owner:

            info = await message.reply("Descargando puto, espera", quote=True)
            f = await message.download(file_name=f"./TodusDownload/", progress=progress, progress_args=(client, info))
            try:
                t = ToDusClient()
                # print(filee)
                print(f)
                spl = f.split("\\")[-1]
                print(spl)
                url = t.upload_file(token, Path(f))
                all = await message.reply(f"{url}" + "  " + f"{spl}")
                os.remove(f)
                with open(spl + ".txt", "w") as f:
                    f.write(all.text)
                await message.reply_document(document=spl + ".txt")
                os.remove(spl + ".txt")
            except Exception as e:
                print(e)
                await message.reply(f"Error: {e}")
        else:
            await message.reply("No tienes permisos para usar este bot")

    elif message.sticker:
        if message.from_user.id == owner:
            info = await message.reply("Descargando puto, espera", quote=True)
            f = await message.download(file_name=f"./TodusDownload/", progress=progress, progress_args=(client, info))
            try:
                t = ToDusClient()
                # print(filee)
                print(f)
                spl = f.split("\\")[-1]
                print(spl)
                url = t.upload_file(token, Path(f))
                all = await message.reply(f"{url}" + "  " + f"{spl}")
                os.remove(f)
                with open(spl + ".txt", "w") as f:
                    f.write(all.text)
                await message.reply_document(document=spl + ".txt")
                os.remove(spl + ".txt")
            except Exception as e:
                print(e)
                await message.reply(f"Error: {e}")
        else:
            await message.reply("No tienes permisos para usar este bot")
    
        
    if message.text == '/start':
        username = message.from_user.username
        name = message.from_user.first_name
        if message.from_user.id == owner:
            await message.reply(f"Hola [{name}](https://t.me/{username}), Bienvenido al bot de Todus", disable_web_page_preview=True)
        else:
            await message.reply("No tienes permiso para usar este bot")
            return
    if message.text == '/help':
        if message.from_user.id == owner:
            await message.reply("""
/start - Inicia el bot
/help - Muestra este mensaje
/token - Reemplaza el actual token del bot por el que pongas

Solo envie el archivo que desea subir al bot
y automaticamente se subira a Todus
            """)
        else:
            await message.reply("No tienes permiso para usar este bot")
            return

    REPLACE = 0
    if state is None and message.text == '/token':
        if message.from_user.id == owner:
            await message.reply("Envie el token de Todus")
            Conversation_state[who] = REPLACE
            return
    if state == REPLACE and message.text != '/token':
        if message.from_user.id == owner:
            del Conversation_state[who]
            with open("token.txt", "w") as t:
                t.write(message.text)
                t.close()
            await message.reply("Nuevo Token guardado")
            return

            
        else:
            await message.reply("No tienes permiso para usar este bot")
            return

##########################
##########################
##########################
#### CREATED BY Titi #####
#### IN TELEGRAM:    #####
#### @TitiLM30        ####
##########################
##########################
##########################
        
if __name__ == "__main__":
    print("Bot is running...")
    bot.run()
