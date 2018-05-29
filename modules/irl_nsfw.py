from discord.ext import commands

class IRL_NSFW:

    def __init__(self, bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(IRL_NSFW(bot))