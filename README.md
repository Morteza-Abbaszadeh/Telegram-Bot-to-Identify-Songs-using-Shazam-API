# Telegram Bot to Identify Songs using Shazam API

## Overview

This project features a Telegram bot that identifies songs from voice messages using the Shazam API. When a user sends a voice message, the bot processes it to determine the song's title and artist, and provides a link to listen to the song.

## Features

- Identifies songs from voice messages
- Returns song title, artist, and a listening URL
- Built with Python, Telebot, and ShazamIO

## Requirements

- Python 3.x
- A Telegram bot token (acquired from BotFather)
- Python packages: `pyTelegramBotAPI`, `shazamio`, `asyncio`

## Installation

1. **Clone the repository:**
    
```shell
git clone https://github.com/your-username/Telegram-Bot-to-Identify-Songs-using-Shazam-API.git
```

    
2. **Navigate to the project directory:**
    
```shell
cd Telegram-Bot-to-Identify-Songs-using-Shazam-API
```
    
3. **Install the required Python packages:**
    
```shell
pip install pyTelegramBotAPI shazamio
```
    
4. **Set up your bot token:**
    
    Open the `bot.py` file and replace `'your_bot_token'` with your actual Telegram bot token.
    
```python
TELEGRAM_TOKEN = 'your_bot_token'
```
    

## Usage

1. **Run the bot:**
    
```shell
python bot.py
```
    
2. **Start interacting with the bot:**
    
    - Send a voice message to the bot on Telegram.
    - The bot will process the message, identify the song, and reply with the song details and a listening URL.

## Example

1. Send a voice message to the bot.
2. Receive a response with the song title, artist, and a link to listen to the song.

## Contributing

If you want to contribute to this project, please fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License.
