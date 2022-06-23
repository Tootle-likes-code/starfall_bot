from discord.ext import commands
from discord.ext.commands import Cog, Context


class SuggestionCog(Cog):
    @commands.command()
    async def suggestion(self, ctx: Context, *, suggestion: str):
        pass