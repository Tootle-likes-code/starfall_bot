from discord.ext import commands

from starfall_bot.definition_sheets_collector import DefinitionSheetsCollector
from starfall_bot.info_cog import InfoCog
from starfall_bot.info_service import InfoService


def run_bot(token, command_prefix="!"):
    bot = commands.Bot(command_prefix=command_prefix)

    info_cog = InfoCog(InfoService(DefinitionSheetsCollector("1fys6qXWVRWVXLECZBRRycffQo9VW3X6WnLUxNSV5jmE")))

    bot.add_cog(info_cog)

    bot.run(token)
