import os

from dotenv import load_dotenv

from starfall_bot import bot


def run():
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")

    bot.run_bot(token)


if __name__ == "__main__":
    run()
