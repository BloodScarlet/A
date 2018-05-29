from discord.ext import commands

class Misc:

    def __init__(self, bot):
        self.bot = bot

    async def on_command(self, ctx):
        self.bot.command_usage[str(ctx.command)] += 1

def setup(bot):
    bot.add_cog(Misc(bot))