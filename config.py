# config.py

# --- Bot Setup ---
BOT_TOKEN = "8446263135:AAHUDtkgfF6ECZAWZRWwb5hXz9P6NR2i6S8"
BOT_USERNAME = "@earnmoneywathchads_bot"
ADMIN_TELEGRAM_ID = 6832776945
ANNOUNCEMENT_GROUP = "https://t.me/+OMPv3xudyOk0OTBl"

# --- Ad Integration ---
ADSTERRA_DIRECT_LINK = "https://plugfundsbadger.com/j6itaewfnb?key=fb3c50708dcecc4b5f531b8e3c8363ab"
# It's highly recommended to add a secret key for postback validation
POSTBACK_SECRET_KEY = "YOUR_UNIQUE_AND_SECRET_KEY"

# --- Coin Economy ---
COINS_PER_AD_VIEW = 10
COIN_TO_TAKA_RATE = {"coins": 4500, "taka": 100}
DAILY_EARNING_LIMIT = 1000
MINIMUM_WITHDRAW_LIMIT = 9000
REFERRAL_BONUS_PERCENTAGE = 0.20  # 20%

# --- Withdraw System ---
PROCESSING_FEE = 5  # in Taka
WITHDRAW_HOLD_PERIOD_HOURS = 24

# --- Server & Database (for Render) ---
DB_HOST = "your_render_mysql_host"
DB_USER = "your_render_mysql_user"
DB_PASSWORD = "your_render_mysql_password"
DB_NAME = "your_render_mysql_database_name"
