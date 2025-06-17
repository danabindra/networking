import requests
from config import SLACK_WEBHOOK_URL

def send_slack_notification(message, channel=None):
    """
    Send a notification to Slack using webhook
    """
    if not SLACK_WEBHOOK_URL:
        print("Warning: SLACK_WEBHOOK_URL not configured")
        return False

    payload = {
        "text": message
    }
    
    if channel:
        payload["channel"] = channel

    try:
        response = requests.post(
            SLACK_WEBHOOK_URL,
            json=payload
        )
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error sending Slack notification: {e}")
        return False 