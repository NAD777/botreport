#!pip3 install PyTelegramBotAPI
#!pip3 install gtts
import telebot
import random
from gtts import gTTS
import os

CHAT_ID = -1001209168677
TOKEN = "916274685:AAG-ZWgt8Cm_tehotyM4om10dWn2lJAOGJM"
bot = telebot.TeleBot(TOKEN)


def send_message_to_channel(type_event, text, chat_id=CHAT_ID):
    bot.send_message(chat_id, text)
    new_text=''
    for char in text:
        try:
            if(new_text[-1]!=char):
                new_text=new_text+char
        except:
            new_text=new_text+char
    new_text.replace('!','')
    new_text.replace(',','')
    new_text.replace('.','')
    speech = gTTS(text=new_text, lang='en', slow=False)
    speech.save("voice.mp3")
    bot.send_audio(chat_id, open("voice.mp3", 'rb'))
    rnd = random.randint(1, 100)
    if rnd >= 5 and rnd <= 9:
        if type_event == 'GOAL':
            bot.send_sticker(CHAT_ID, 'CAACAgIAAxkBAAEBrwxf2J9rjKdERUaj9SVf_mafW9wPJQACCwEAAladvQpOseemCPvtSR4E')
        if type_event == 'PENALTI':
            bot.send_sticker(CHAT_ID, 'CAACAgIAAxkBAAEBrxFf2KKkfzHy5iLRY_XCTiSttfxYzAAC_wADVp29Ctqt-n3kvEAkHgQ')

#send_message_to_channel('GOAL', 'GOAAAAAAAAAAAAAAAAAAL', CHAT_ID)