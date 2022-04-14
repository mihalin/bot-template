from dotenv import load_dotenv
from os import getenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")

WEBHOOK_HOST = getenv("WEBHOOK_HOST", "")  # example: https://my.domain.com
WEBHOOK_PATH = getenv("WEBHOOK_PATH", "/{{cookiecutter.project_name}}_webhook")  # example: /mybot_webhook
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
