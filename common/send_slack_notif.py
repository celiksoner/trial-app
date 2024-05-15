import requests

def send_notification(webhook_url,message):
    data = {
        "text": message
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code != 200:
        return f"Failed send message to Slack: {response.text}", 500
    else:
        return "Message sended.", 200