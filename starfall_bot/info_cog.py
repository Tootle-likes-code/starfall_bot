from discord.ext import commands
from discord.ext.commands import Cog, Context

from starfall_bot.info_service import InfoService


class InfoCog(Cog):
    def __init__(self, info_service: InfoService):
        self._info_service = info_service

    @commands.command()
    async def define(self, ctx: Context, *, word: str):
        definition = self._info_service.define(word)

        await ctx.send(f"> {word}: {definition}")

    