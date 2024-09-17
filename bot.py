import telebot
from telebot import types
from shazamio import Shazam
import asyncio
import os

TELEGRAM_TOKEN = 'your_bot_token'

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Path to save audio files
AUDIO_FILE_PATH = 'audio.ogg'

async def identify_song(file_path):
    shazam = Shazam()
    response = await shazam.recognize_song(file_path)
    song = response['track']['title']
    artist = response['track']['subtitle']
    # Assuming Shazam provides a link to the song
    song_url = response['track'].get('url', 'No URL available')
    return f'The song is "{song}" by {artist}. Listen here: {song_url}'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Send me a voice message and I will try to identify the song.')

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    file_id = message.voice.file_id
    file_info = bot.get_file(file_id)
    file_download_url = f'https://api.telegram.org/file/bot{TELEGRAM_TOKEN}/{file_info.file_path}'

    # Download the audio file
    downloaded_file = bot.download_file(file_info.file_path)
    with open(AUDIO_FILE_PATH, 'wb') as new_file:
        new_file.write(downloaded_file)

    # Identify the song
    async def process_voice():
        song_info = await identify_song(AUDIO_FILE_PATH)
        bot.reply_to(message, song_info)
        os.remove(AUDIO_FILE_PATH)

    # Run the identification function asynchronously
    asyncio.run(process_voice())

bot.polling()
