from datetime import datetime
import os


def sample_responces(input_text):
    user_message = str(input_text).lower()

    if user_message in ('hello', 'hi', 'sup'):
        return "Hey, Hows It going"
    
    if user_message in ('who are you', 'who are you?'):
        return "I am a Bot"

    if user_message in ('time', 'time?'):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M;%S")

        return str(datetime)
    if user_message in ('op', 'op!'):
        return "Yeahhhhhhhhhhh Over Powwwweeeeerrrrrr!!!!"
    
    return "I didnt understand what you said"