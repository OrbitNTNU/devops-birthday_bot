from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import random
import os 

SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

birthday_wishes = [
    "Happy Birthday! Wishing you a productive day! 🎉🎂",
    "Hooray, it's your day! May it be filled with success and joy! 🎈🎁",
    "Happy Birthday! Hope the coming year is successful for you! 🌟🎂",
    "Heartfelt congratulations on your birthday! May your day be efficient and positive! 🎉🎈",
    "Congratulations on another year of growth and experiences! 🎁📈",
    "A big birthday hug to you! Hope your day is productive and efficient! 🤖🎂",
    "Congratulations on becoming a year older and wiser! Wishing you success in upcoming challenges! 📚🎂",
    "Hope you have a day filled with positive moments! Happy Birthday! 🎈🎂",
    "Hip hip hooray! A big birthday hug and wishes for a productive year ahead! 🎉🎂",
    "Happy Birthday! May it be as brilliant as your achievements! 🌟🎈",
    "Happy Birthday! 🎉 May your day be filled with joy, laughter, and good memories. 🎂🎈",
    "Happy Birthday! 🎊 Hope your day is as fantastic as you deserve. 🥳🎁",
    "Hip hip hooray! 🥳 Wishing you a day full of positive surprises and smiles. 🎂🎉",
    "Happy Birthday! 🎈 May this year bring you success and fulfillment. 🌟🚀",
    "🎂 Happy Birthday! May your day be as special as you are. 🎁🎊",
    "Hooray for you! 🎉 Wishing you a year filled with joy, love, and adventure. 🥳🌈",
    "Happy Birthday! 🎈 Hope you have a day full of positive vibes and good times. 🎂🎁",
    "Happy Birthday! 🎊 May this year bring you success and new exciting experiences. 🚀🌟",
    "Hip hip hooray! 🎉 Wishing you a splendid day and a fantastic year. 🥳🎂",
    "Happy Birthday! 🎈 May your life be filled with happiness, love, and exciting adventures. 🎁🌈",
    "Cheers to you on your birthday! May it be filled with laughter, fun, and unforgettable moments! 🎉🍾",
    "Wishing you all the happiness your heart can hold on your birthday. Have a truly wonderful day! 🎂🎈",
    "May your birthday be the start of a year filled with good luck, good health, and much happiness. 🎉🌟",
    "On your special day, I wish you all the very best, all the joy you can ever have and may you be blessed abundantly today, tomorrow, and the days to come! 🎁🎈",
    "May your birthday mark the beginning of a wonderful period of time in your life! 🎂🌟",
    "Here’s to a bright, healthy and exciting future, Happy birthday! 🥳🚀",
    "Happy Birthday! May you have a fabulous day and many more to come! 🎉🎊",
    "I hope your special day will bring you lots of happiness, love, and fun. You deserve them a lot. Enjoy! 🎂🎉",
    "May your birthday be filled with the warmth of sunshine, the happiness of smiles, and the feeling of love. 🌞🎈",
    "Let’s light the candles and celebrate this special day of your life. Happy birthday. 🎂🎉"
]


# WebClient instantiates a client that can call API methods
client = WebClient(SLACK_APP_TOKEN)
logger = logging.getLogger(__name__)

# ID of channel you want to post message to
channel_id = "C06KGNYGS64"

def slack_send_message(name_list, response, id):
   try: 
        if id:
             result = client.chat_postMessage(
                channel=channel_id,
                text=f"It's <@{id}>'s birthday! {birthday_wishes[random.randint(0, len(birthday_wishes)-1)]}"
            )
                
        else:
            result = client.chat_postMessage(
            channel=channel_id,
            text=f"It's {" ".join(name_list)}'s birthday! {birthday_wishes[random.randint(0, len(birthday_wishes)-1)]}"
            )
                  
   except SlackApiError as e:
            print(f"Error: {e}")
