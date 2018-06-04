from discord.ext import commands
import discord, datetime

class General:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["ping"])
    async def latency(self, ctx):
        """Get Bot Latency"""
        data = '\n'.join(f'**Shard {shard}:** ' +
                         str(round(self.bot.latencies[shard][1] * 1000)) + 'ms' for shard in self.bot.shards)
        em = discord.Embed(color=0xDEADBF,
                           title="Latency",
                           description=data)
        await ctx.send(embed=em)

    @commands.command()
    async def invite(self, ctx):
        """Get the bots invite."""
        await ctx.send("**Invite the bot:** <https://awau.moe/42a434>\n"
                       "**Support Server:** <https://discord.gg/q98qeYN>")

    def get_bot_uptime(self, *, brief=False):
        now = datetime.datetime.utcnow()
        delta = now - self.bot.uptime
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        if not brief:
            if days:
                fmt = '{d} days, {h} hours, {m} minutes, and {s} seconds'
            else:
                fmt = '{h} hours, {m} minutes, and {s} seconds'
        else:
            fmt = '{h}h {m}m {s}s'
            if days:
                fmt = '{d}d ' + fmt

        return fmt.format(d=days, h=hours, m=minutes, s=seconds)

    @commands.command()
    async def info(self, ctx):
        """Get bot info"""
        server = len(self.bot.guilds)
        members = len(set(self.bot.get_all_members()))
        shards = self.bot.shard_count
        commands = len(self.bot.commands)
        em = discord.Embed(color=0xDEADBF,
                           title="Info~!",
                           description=f"Servers: **{server}**\n"
                                       f"Members: **{members}**\n"
                                       f"Shards: **{shards}**\n"
                                       f"Commands: **{commands}**\n"
                                       f"Uptime: **{self.get_bot_uptime(brief=False)}**")
        await ctx.send(embed=em)

    @commands.command()
    async def neko(self, ctx):
        """Get cute nekos :3"""
        r = await self.bot.session.get("https://nekobot.xyz/api/image?type=neko")
        res = await r.json()
        em = discord.Embed(color=0xDEADBF)
        await ctx.send(embed=em.set_image(url=res["message"]))

    @commands.command()
    async def kanna(self, ctx):
        """Get Kanna Pics"""
        r = await self.bot.session.get("https://nekobot.xyz/api/image?type=kanna")
        res = await r.json()
        em = discord.Embed(color=0xDEADBF)
        await ctx.send(embed=em.set_image(url=res["message"]))

    @commands.command()
    async def help(self, ctx):
        """HentaiBoi Help"""
        try:
            em = discord.Embed(color=0xDEADBF)
            em.add_field(name="General", value="`help`, `latency`, `invite`, `info`, `neko`, `kanna`",
                         inline=False)
            em.add_field(name="Fun", value="`weebify`, `bodypillow`, `ship`, `awooify`, `jpeg`, `deepfry`, `bigletter`",
                         inline=False)
            em.add_field(name="Economy", value="`balance`, `daily`, `transfer`, `bet`",
                         inline=False)
            em.add_field(name="Hentai", value="`hentai`, `lewdneko`, `anal`, `holo`, `lewdkitsune`, `trap`",
                         inline=False)
            em.add_field(name="IRL NSFW", value="`pgif`, `4k`, `gonewild`, `thighs`, `ass`, `pussy`",
                         inline=False)
            em.add_field(name="Weeb", value="`animepic`, `kiss`, `hug`, `pat`, `cuddle`",
                         inline=False)
            await ctx.send(embed=em)
        except:
            await ctx.send("I can't send embeds.")
        try:
            emoji = self.bot.get_emoji(450703860999258134)
            await ctx.message.add_reaction(emoji)
        except:
            pass

def setup(bot):
    bot.remove_command('help')
    bot.add_cog(General(bot))