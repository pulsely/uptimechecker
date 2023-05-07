



from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from django.conf import settings

def postMessage( channel, text ):
    client = WebClient(token=settings.SLACK_TOKEN)
    try:
        response = client.chat_postMessage(channel=channel, text=text)
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")

        return None
    return response
