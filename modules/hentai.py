from discord.ext import commands
from .utils.images import boobbot
import discord

class NSFW:

    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.command()
    @commands.guild_only()
    async def yaoi(self, ctx):
        if not ctx.message.channel.is_nsfw():
            em = discord.Embed(color=0xff6928, description="This isnt an NSFW Channel <:vanillaStare:441126443842404352>")
            return await ctx.send(embed=em, delete_after=3)
        em = discord.Embed(color=0xDEADBF).set_image(url=(await boobbot("yaoi")))
        await ctx.send(embed=em)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def hentai(self, ctx):
        """Send hentai owo"""
        if not ctx.message.channel.is_nsfw():
            em = discord.Embed(color=0xff6928, description="This isnt an NSFW Channel <:vanillaStare:441126443842404352>")
            return await ctx.send(embed=em, delete_after=3)
        r = await self.bot.session.get("https://nekobot.xyz/api/image?type=hentai")
        res = await r.json()
        em = discord.Embed(color=0xDEADBF).set_image(url=res["message"])
        await ctx.send(embed=em)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def lewdneko(self, ctx):
        """Get a loood neko ~w~"""
        if not ctx.message.channel.is_nsfw():
            em = discord.Embed(color=0xff6928,
                               description="This isnt an NSFW Channel <:vanillaStare:441126443842404352>")
            return await ctx.send(embed=em, delete_after=3)
        r = await self.bot.session.get("https://nekobot.xyz/api/image?type=lewdneko")
        res = await r.json()
        em = discord.Embed(color=0xDEADBF).set_image(url=res["message"])
        await ctx.send(embed=em)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def anal(self, ctx):
        """Anal hentai 👀"""
        if not ctx.message.channel.is_nsfw():
            em = discord.Embed(color=0xff6928,
                               description="This isnt an NSFW Channel <:vanillaStare:441126443842404352>")
            return await ctx.send(embed=em, delete_after=3)
        r = await self.bot.session.get("https://nekobot.xyz/api/image?type=hentai_anal")
        res = await r.json()
        em = discord.Embed(color=0xDEADBF).set_image(url=res["message"])
        await ctx.send(embed=em)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def holo(self, ctx):
        """Lewd Holo from Spice and Wolf"""
        if not ctx.message.channel.is_nsfw():
            em = discord.Embed(color=0xff6928,
                               description="This isnt an NSFW Channel <:vanillaStare:441126443842404352>")
            return await ctx.send(embed=em, delete_after=3)
        r = await self.bot.session.get("https://nekos.life/api/v2/img/hololewd")
        res = await r.json()
        em = discord.Embed(color=0xDEADBF).set_image(url=res["url"])
        await ctx.send(embed=em)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def gasm(self, ctx):
        """Get gasm images."""
        if not ctx.message.channel.is_nsfw():
            em = discord.Embed(color=0xff6928,
                               description="This isnt an NSFW Channel <:vanillaStare:441126443842404352>")
            return await ctx.send(embed=em, delete_after=3)
        r = await self.bot.session.get("https://nekos.life/api/v2/img/gasm")
        res = await r.json()
        em = discord.Embed(color=0xDEADBF).set_image(url=res["url"])
        await ctx.send(embed=em)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def lewdkitsune(self, ctx):
        """Get a looooood kitsune (foxgirl's)"""
        if not ctx.message.channel.is_nsfw():
            em = discord.Embed(color=0xff6928,
                               description="This isnt an NSFW Channel <:vanillaStare:441126443842404352>")
            return await ctx.send(embed=em, delete_after=3)
        r = await self.bot.session.get("https://nekobot.xyz/api/image?type=lewdkitsune")
        res = await r.json()
        em = discord.Embed(color=0xDEADBF).set_image(url=res["message"])
        await ctx.send(embed=em)

    @commands.command(aliases=["futa"])
    @commands.guild_only()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def trap(self, ctx):
        """Get trap loods (futa)"""
        if not ctx.message.channel.is_nsfw():
            em = discord.Embed(color=0xff6928,
                               description="This isnt an NSFW Channel <:vanillaStare:441126443842404352>")
            return await ctx.send(embed=em, delete_after=3)
        r = await self.bot.session.get("https://api.computerfreaker.cf/v1/trap")
        res = await r.json()
        em = discord.Embed(color=0xDEADBF).set_image(url=res["url"])
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(NSFW(bot))