from dotenv import load_dotenv
import os
import sqlite3
import random
from apscheduler.schedulers.background import BackgroundScheduler
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import asyncio

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Bot token is missing! Please set it in the .env file.")

# Initialize the bot application
application = Application.builder().token(BOT_TOKEN).build()

conn = sqlite3.connect("subscribers.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS subscribers (
    chat_id INTEGER PRIMARY KEY
)
""")
conn.commit()

def add_subscriber(chat_id):
    cursor.execute("INSERT OR IGNORE INTO subscribers (chat_id) VALUES(?)", (chat_id,))
    conn.commit()

def remove_subscriber(chat_id):
    cursor.execute("DELETE FROM subscribers WHERE chat_id = ?", (chat_id,))
    conn.commit()

def get_all_subscriber():
    cursor.execute("SELECT chat_id FROM subscribers")
    return [row[0] for row in cursor.fetchall()]

# Command handlers
async def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    subscribers = get_all_subscriber()
    if chat_id in subscribers:
        await update.message.reply_text(
            "You're already a subscriber, wait and you'll recieve your morning message everyday at 7am"
        )
    else:
        add_subscriber(chat_id)
        await update.message.reply_text(
            "You've now been subscribed, love! You will receive your morning message at 7 AM every day. 😘"
        )

async def stop(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    remove_subscriber(chat_id)
    await update.message.reply_text("Why are you leaving, hunn? 🤧🤧, \n You've been unsubscribed")

# Where the list of quotes goes
quotes = [
    "Mma Goodmorning, every time I think of you, my heart whispers, 'She's the one.' You make my world perfect.",
    "Heyy babyy, Goodmorning. You're the melody that plays in my heart every moment, and I can’t wait to love you more today.",
    "Goodmorning baby, your smile is my sunshine, your love is my fuel, and your presence is my greatest blessing.",
    "Mma Goodmorning, waking up is magical because I get to spend another day loving you.",
    "Heyy babyy, Goodmorning. If I could, I’d wrap the warmth of my love around you every second of the day.",
    "Goodmorning baby, you’re not just the love of my life—you’re my entire universe wrapped in one amazing soul.",
    "Mma Goodmorning, with every sunrise, I’m reminded that you’re my greatest gift and my happiest thought.",
    "Heyy babyy, Goodmorning. I hope you know you’re my dream come true, every single day.",
    "Goodmorning baby, life feels like a fairytale because you’re my forever happy ending.",
    "Mma Goodmorning, your love is the sweetest thing I’ve ever known, and I can’t imagine my world without you.",
    "Heyy babyy, Goodmorning. Loving you feels like discovering a new kind of happiness every day.",
    "Goodmorning baby, my love for you is endless, like the sky, and every moment with you is a blessing.",
    "Mma Goodmorning, you’re the reason my heart beats a little faster and my world feels a little brighter.",
    "Heyy babyy, Goodmorning. You have a way of making my heart feel at home, no matter where I am.",
    "Goodmorning baby, you’re my sunrise, my calm, and my most beautiful dream all in one.",
    "Mma Goodmorning, I wish I could hold your hand and remind you how deeply and endlessly I love you.",
    "Heyy babyy, Goodmorning. Every moment I spend loving you feels like a treasure I’ll cherish forever.",
    "Goodmorning baby, your laughter is my favorite sound, and your happiness is my favorite goal.",
    "Mma Goodmorning, with you in my life, even the ordinary feels extraordinary.",
    "Heyy babyy, Goodmorning. You’re the reason I believe in miracles—you’re mine.",
    "Goodmorning baby, no words can describe how grateful I am to have someone as beautiful as you in my life.",
    "Mma Goodmorning, every little thing about you makes me fall in love with you all over again.",
    "Heyy babyy, Goodmorning. You’re not just my love—you’re the peace and joy my heart has always longed for.",
    "Goodmorning baby, waking up is easier when I know I have the sweetest soul loving me every day.",
    "Mma Goodmorning, you’re the softest part of my heart, the gentlest part of my soul, and the best part of my life.",
    "Heyy babyy, Goodmorning. Every morning, I thank the universe for giving me someone as amazing as you.",
    "Goodmorning baby, you light up my world in ways I never thought possible. I’m so lucky to call you mine.",
    "Mma Goodmorning, being loved by you feels like a beautiful dream I never want to wake up from.",
    "Heyy babyy, Goodmorning. You’re my first thought in the morning and my last wish at night.",
    "Goodmorning baby, you’re my heart’s safest place and my soul’s happiest home.",
]

async def daily_quote():
    subscribers = get_all_subscriber()
    if not subscribers:
        print("No one to send quotes to.")
        return

    quote = random.choice(quotes)
    for chat_id in subscribers:
        try:
            await application.bot.send_message(chat_id=chat_id, text=quote)
        except Exception as e:
            print(f"Failed to send message to {chat_id}: {e}")

# Wrapper function to run the coroutine in a new event loop
def run_daily_quote():
    loop = asyncio.new_event_loop()  # Create a new event loop
    asyncio.set_event_loop(loop)    # Set it as the current event loop for this thread
    loop.run_until_complete(daily_quote())  # Run the coroutine in this new loop
    loop.close()  # 

# Scheduler setup
scheduler = BackgroundScheduler()
scheduler.add_job(run_daily_quote, 'cron', hour=22, minute=43)  # Adjust time as needed for testing
scheduler.start()

# Add command handlers to the application
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('stop', stop))

# Run the bot
if __name__ == "__main__":
    print("Bot is running...")
    application.run_polling()

