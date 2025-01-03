import slacky
from celery import shared_task
from . import ai, utils

@shared_task
def slack_message_task(message, channel_id=None, user_id=None, thread_ts=None):
    # openai_msg = utils.chat_with_openai(message, raw=False)
    # print(message, openai_msg)
    # res = slacky.send_message(openai_msg, channel_id=channel_id, user_id=user_id, thread_ts=thread_ts)
    # pdf_ai_msg = ai.query(message, raw=False)
    res = slacky.send_message(message, channel_id=channel_id, user_id=user_id, thread_ts=thread_ts)
    return res.status_code