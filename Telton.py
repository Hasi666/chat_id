from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio
from heroku3 import from_key
import os
API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", None)
STRING_SESSION = os.environ.get("STRING_SESSION", None)
admin = int(os.environ.get("admin", 0))
APP_NAME = os.environ.get("APP_NAME", None)
API_KEY = os.environ.get("API_KEY", None)
HU_APP = from_key(API_KEY).apps()[APP_NAME]

client=TelegramClient(StringSession(STRING_SESSION),API_ID,API_HASH)
print('Bot Run')
	

async def chat_id(event):
	text = event.message.message
	chat_id = event.chat_id
	if text == "chat_id":
		await client.send_message(chat_id , f"{chat_id}")
		
client.add_event_handler(chat_id , events.NewMessage)










client.start()
client.run_until_disconnected()
