from dotenv import load_dotenv
from os import getenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")

WEBHOOK_HOST = getenv("WEBHOOK_HOST", "")  # example: https://my.domain.com
WEBHOOK_PATH = getenv("WEBHOOK_PATH", "/{{cookiecutter.project_name}}_webhook")  # example: /mybot_webhook
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"


POSTGRES_USER = getenv("POSTGRES_USER")
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD")
POSTGRES_DB = getenv("POSTGRES_DB")
POSTGRES_HOST = getenv("POSTGRES_HOST")


TORTOISE_ORM = {
    "connections": {"default": f'postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}'
                               f'@{POSTGRES_HOST}/{POSTGRES_DB}'},
    "apps": {
        "models": {
            "models": ["{{cookiecutter.project_name}}.models.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
