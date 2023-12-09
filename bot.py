import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6836997893:AAFQ-ukSIQSQUNTAoeQpERfV_BuiEsxBOqM")

API_ID = int(os.environ.get("API_ID", "25145421"))

API_HASH = os.environ.get("API_HASH", "faa6f8032ee368c78522a9fded1c18c6")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
