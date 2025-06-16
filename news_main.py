import discord
from discord.ext import tasks, commands
import requests
import json
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Your bot token and news API key
TOKEN = '[Tama token]'
NEWS_API_KEY = '[News API Key' # Your newsapi.org API key

ANNOUNCEMENT_CHANNEL_ID = ['Tama discord channel ID']  # Your Discord channel ID
sent_articles = set()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

def fetch_news():
    url = f'https://newsapi.org/v2/everything?q=anime OR manga&apiKey={NEWS_API_KEY}&pageSize=10'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        logging.error(f"Error: Unable to fetch news (status code: {response.status_code})")
        return []

# Update Checker
@tasks.loop(minutes=1)  # Check every 1 minute
async def check_news_updates():
    logging.info("Attempting to fetch news updates...")
    articles = fetch_news()
    
    if articles:
        channel = bot.get_channel(ANNOUNCEMENT_CHANNEL_ID)
        new_articles = []

        for article in articles:
            title = article['title']
            name = article['source']['name']
            article_id = article['url']

            if article_id not in sent_articles:
                new_articles.append(article_id)
                logging.info(f"Update: {name}, {title}")

                embed = discord.Embed(title=title, url=article['url'], description=article.get('description', 'No description'), color=0x00ff00)
                embed.set_footer(text=f"Source: {name}")
                await channel.send(embed=embed)

        sent_articles.update(new_articles)

@bot.event
async def on_ready():
    logging.info(f"{bot.user} has connected to Discord!")
    check_news_updates.start()

bot.run(TOKEN)
