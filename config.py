from os import getenv
import logging
from logging.handlers import RotatingFileHandler


# ---------------------- ᴄᴏɴғɪɢ ---------------------- #

API_ID = int(getenv("API_ID", "25426270"))
API_HASH = getenv("API_HASH", "2f4948dc659e5af3f87bfc8baba6b921")
BOT_TOKEN = getenv("BOT_TOKEN", "6086645204:AAHe3eyFhCwNjGGso3b1tCBHpW0iWCdgXxw")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001914497289"))
OWNER_ID = list(map(int, getenv("SUDO_USERS", "6109551937 5416887843 6018550523").split()))
DB_URI = getenv("DATABASE_URL", "mongodb+srv://gareebk06:BYkppVuBAFg3qvb1@cluster0.3hsto05.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
FORCE_SUB_CHANNEL = int(getenv("FORCE_SUB_CHANNEL", "-1001831916389"))
BOT_WORKERS = int(getenv("BOT_WORKERS", "5"))

# --------- ʟɪɴᴋ sʜᴏʀᴛɴᴇʀ ᴄᴏɴᴠᴇʀᴛᴇʀ ---------
URL_SHORTNER_API = getenv("URL_SHORTNER_API", "https://api.urlshortex.com/api?api")
URL_SHORTNER_API_KEY = getenv("URL_SHORTNER_API_KEY", "c460f2f1a0f68b2c56cda7f12121c210ed10b08b")


default_custom_caption = """
📁 {file_caption}
━━━━━━━━━━━━━━━━━━━━━━━━━━━   
ɪғ ʏᴏᴜ ʟɪᴋᴇ ᴠɪᴅᴇᴏ ᴛʜᴀɴ ᴘʟᴇᴀsᴇ 
ᴀᴅᴅ sᴏᴍᴇ ᴍᴇᴍʙᴇʀ ᴀɴᴅ sʜᴀʀᴇ ᴛʜᴇ ʟɪɴᴋ
━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
CUSTOM_CAPTION = getenv("CUSTOM_CAPTION", default_custom_caption)

# --» sᴇᴛ ᴛʀᴜᴇ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴘʀᴇᴠᴇɴᴛ ᴜsᴇʀs ғʀᴏᴍ ғᴏʀᴡᴀʀᴅɪɴɢ ғɪʟᴇs ғʀᴏᴍ ʙᴏᴛ
if getenv("PROTECT_CONTENT", None) == 'True':
    PROTECT_CONTENT = True
else:
    PROTECT_CONTENT = False


# --> sᴇᴛ ᴛʀᴜᴇ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪsᴀʙʟᴇ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴘᴏsᴛs sʜᴀʀᴇ ʙᴜᴛᴛᴏɴ
if getenv("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False




LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
    
