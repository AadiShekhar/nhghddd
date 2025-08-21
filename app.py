
from flask import Flask
import os
import threading
import time
from bot import Bot

app = Flask(__name__)

@app.route('/')
def hello_world():
    return {
        'status': 'Bot is running',
        'message': 'VJ Save Restricted Bot is active',
        'health': 'OK'
    }

@app.route('/health')
def health_check():
    return {'status': 'healthy'}, 200

@app.route('/status')
def bot_status():
    return {
        'bot': 'VJ Save Restricted Bot',
        'status': 'active',
        'timestamp': time.time()
    }

def run_bot():
    """Function to run the Telegram bot"""
    try:
        bot = Bot()
        bot.run()
    except Exception as e:
        print(f"Bot error: {e}")
        # Restart bot after 5 seconds if it crashes
        time.sleep(5)
        run_bot()

if __name__ == "__main__":
    # Start the bot in a separate thread
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    
    # Start Flask app
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
