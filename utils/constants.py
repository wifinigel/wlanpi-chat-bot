"""
Central store of all constants used across the chatbot code
"""

TELEGRAM_URL = "https://api.telegram.org"
TELEGRAM_HOST = "api.telegram.org"
TELEGRAM_PORT = 443

CONFIG_FILE = "/opt/wlanpi-chat-bot/etc/config.json"

SPOOL_DIR = "/var/spool/wlanpi-chatbot"
SPOOL_DIR_MSGS = SPOOL_DIR + "/messages"
SPOOL_DIR_FILES = SPOOL_DIR + "/files"
MAX_SPOOL_SIZE = 5

SUPPORTED_VERBS = [ 'show', 'exec', 'set']
HIDDEN_COMMANDS = [ 'exec_cmd' ]