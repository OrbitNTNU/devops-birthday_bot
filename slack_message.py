from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import random
import os 

SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

birthday_wishes = [
    "Gratulerer med dagen! Ønsker deg en produktiv dag! 🎉🎂",
    "Hurra, det er din dag! Må den være fylt med suksess og glede! 🎈🎁",
    "Stort grattis på dagen din! Håper det kommende året blir vellykket for deg! 🌟🎂",
    "Hjertelig til lykke på bursdagen din! Må dagen være effektiv og positiv! 🎉🎈",
    "Gratulerer med nok et år med vekst og erfaringer! 🎁📈",
    "En stor bursdagsklem til deg! Håper dagen din er produktiv og effektiv! 🤖🎂",
    "Gratulerer med å bli et år eldre og klokere! Ønsker deg suksess i kommende utfordringer! 📚🎂",
    "Håper du har en dag fylt med positive øyeblikk! Gratulerer med dagen! 🎈🎂",
    "Hipp hurra! En stor bursdagsklem og ønsker om et produktivt år foran! 🎉🎂",
    "Gratulerer med dagen! Må den være like strålende som dine prestasjoner! 🌟🎈",
    "Gratulerer med dagen! 🎉 Må dagen være fylt med glede, latter og gode minner. 🎂🎈",
    "Happy Birthday! 🎊 Håper dagen din er like fantastisk som du fortjener. 🥳🎁",
    "Hipp hipp hurra! 🥳 Ønsker deg en dag full av positive overraskelser og smil. 🎂🎉",
    "Gratulerer med dagen! 🎈 Må dette året bringe deg suksess og oppfyllelse. 🌟🚀",
    "🎂 Happy Birthday! Må dagen være like spesiell som du er. 🎁🎊",
    "Hurra for deg! 🎉 Ønsker deg et år fylt med glede, kjærlighet og eventyr. 🥳🌈",
    "Gratulerer med dagen! 🎈 Håper du får en dag full av positive vibber og gode tider. 🎂🎁",
    "Happy Birthday! 🎊 Må dette året bringe deg suksess og nye spennende opplevelser. 🚀🌟",
    "Hipp hipp hurra! 🎉 Ønsker deg en strålende dag og et fantastisk år. 🥳🎂",
    "Gratulerer med dagen! 🎈 Må livet ditt være fylt med lykke, kjærlighet og spennende eventyr. 🎁🌈"]

# WebClient instantiates a client that can call API methods
client = WebClient(SLACK_APP_TOKEN)
logger = logging.getLogger(__name__)

# ID of channel you want to post message to
channel_id = "C06KGNYGS64"

def slack_send_message(name):
    try:
        # Call the conversations.list method using the WebClient
            result = client.chat_postMessage(
                channel=channel_id,
                text=f"{name} har bursdag! {birthday_wishes[random.randint(0, len(birthday_wishes)-1)]}"
            )

    except SlackApiError as e:
            print(f"Error: {e}")
        
