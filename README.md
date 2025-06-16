# Discord NewsAPI Bot

A small Python-based Discord bot that fetches and sends the latest news headlines using the NewsAPI service.

## Features

- Fetches top news headlines from various sources via NewsAPI
- Sends news summaries with titles, URLs, and sources
- Configurable via `.env` file (NewsAPI key, Discord token, command prefix)
- Simple and lightweight for personal use

## Usage

Run the bot:
   python main.py

Use the defined prefix followed by the news command to fetch the latest headlines:
   !news

Make sure the bot has permission to send messages in your channel.

## Notes

- Requires a free API key from [https://newsapi.org](https://newsapi.org)
- NewsAPI may have rate limits depending on the plan
- Headlines are retrieved in English by default

## License

This project is licensed under the MIT License.

## Disclaimer

This is a personal project created solely for learning and experimentation purposes.  
I do not take any responsibility for any misuse or damage caused by others using this code.  
Use it at your own risk.
