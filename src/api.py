import json
import boto3
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

SQS_QUEUE_URL = os.getenv('SQS_QUEUE_URL')

sqs = boto3.resource('sqs')
queue = sqs.Queue(SQS_QUEUE_URL)

def lambda_handler(event, context):
    logger.info("event: {}".format(json.dumps(event)))
    try:
        # I`m getting rid of all the unnecessary data from telegram and sending only the message and chat_id
        message_body = json.loads(event["body"])
        message_to_queue = json.dumps({"message": message_body['message']['text'],
                                       "chat_id": message_body['message']['chat']['id']})
        queue.send_message(MessageBody=message_to_queue)
        return {
            'statusCode': 200,
            'body': 'Success'
        }

    except Exception as exc:
        return {
            'statusCode': 500,
            'body': 'Failure'
        }
