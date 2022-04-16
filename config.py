from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
ARQ_API_KEY = "ZWFCNH-CUCNLI-YNOZZL-CPYUNU-ARQ"
ARQ_API_URL = "https://arq.hamker.in/"
BOT_TOKEN = getenv("BOT_TOKEN","")
BOT_NAME = getenv("BOT_NAME","𝗛𝗲𝗿𝗼𝘅 𝗠𝘂𝘀𝗶𝗰")
BOT_USERNAME = getenv("BOT_USERNAME", "Herox_Music_RoBot")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/21de9fccf241461391963.jpg")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Herox_xd")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Techno_Trickop")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "TrickyAbhii_Op")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "80"))
SESSION_NAME = getenv("SESSION_NAME", "")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "• / ! ^ . + ~").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5124507794").split()))
