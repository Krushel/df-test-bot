import json
import asyncio
from telegram.ext import ApplicationBuilder, ContextTypes
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
SQS_QUEUE_URL = os.getenv('SQS_QUEUE_URL')

application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

async def hello(message, context: ContextTypes.DEFAULT_TYPE):
    # I`m using lower() method to make the bot case-insensitive
    if 'hello' in message['message'].lower():
        await application.bot.send_message(chat_id=message['chat_id'], text="Hello, world!")

def lambda_handler(event, context):
    logger.info("event: {}".format(json.dumps(event)))
    asyncio.get_event_loop().run_until_complete(main(event, context))

async def main(event, context):
    # The event is a dictionary that contains the message body and chat id
    for record in event['Records']:
        try:
            await application.initialize()
            await hello(json.loads(record['body']), application.bot)
        except Exception as exc:
            logger.error(f"Error processing message: {record['body']}")
            logger.error(exc)
    return None
