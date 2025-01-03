import helpers
import requests

SLACK_BOT_TOKEN = helpers.config('SLACK_BOT_TOKEN', default=None, cast=str)

# https://api.slack.com/messaging/sending#composing
def send_message(message, channel_id=None, user_id=None, thread_ts=None):
    url = 'https://slack.com/api/chat.postMessage'
    headers = {
        'Content-type': 'application/json; charset=utf-8',
        'Authorization': f"Bearer {SLACK_BOT_TOKEN}",
        'Accept': 'application/json'
    }
    if user_id is not None:
        message = f"<@{user_id}> {message}"
    data = {
        "channel": f"{channel_id}",
        "text": f"{message}".strip()
    }
    if thread_ts is not None:
        data['thread_ts'] = thread_ts
    return requests.post(url, json=data, headers=headers)