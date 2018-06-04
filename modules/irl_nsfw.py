from discord.ext import commands
import discord

class IRL_NSFW:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def pgif(self, ctx):
        """Pron Gifs"""
        if not ctx.message.channel.is_nsfw():
            em = discord.Embed(color=0xff6928, description="This isnt an NSFW Channel <:vanillaStare:441126443842404352>")
            return await ctx.send(embed=em, delete_after=3)
        r = await self.bot.session.get("https://nekobot.xyz/api/image?type=pgif")
        res = await r.json()
        em = discord.Embed(color=0xDEADBF).set_image(url=res["message"])
        await ctx.send(embed=em)

    @commands.command(name="4k")
    @commands.guild_only()
    async def fourk(self, ctx):
        """4K Girls"""
        if not ctx.message.channel.is_nsfw():
            em = discord.Embed(color=0xff6928, description="This isnt an NSFW Channel <:vanillaStare:441126443842404352>")
            return await ctx.send(embed=em, delete_after=3)
        r = await self.bot.session.get("https://nekobot.xyz/api/image?type=4k")
        res = await r.json()
        em = discord.Embed(color=0xDEADBF).set_image(url=res["message"])
        await ctx.send(embed=em)

    @commands.command()
    @commands.guild_only()
    async def gonewild(self, ctx):
        """r/gonewild images"""
        if not ctx.message.channel.is_nsfw():
            em = discord.Embed(color=0xff6928, description="This isnt an NSFW Channel <:vanillaStare:441126443842404352>")
            return await ctx.send(embed=em, delete_after=3)
        r = await self.bot.session.get("https://nekobot.xyz/api/image?type=gonewild")
        res = await r.json()
        em = discord.Embed(color=0xDEADBF).set_image(url=res["message"])
        await ctx.send(embed=em)

    @commands.command(aliases=["thigh"])
    @commands.guild_only()
    async def thighs(self, ctx):
        """r/gonewild images"""
        if not ctx.message.channel.is_nsfw():
            em = discord.Embed(color=0xff6928, description="This isnt an NSFW Channel <:vanillaStare:441126443842404352>")
            return await ctx.send(embed=em, delete_after=3)
        r = await self.bot.session.get("https://nekobot.xyz/api/image?type=thigh")
        res = await r.json()
        em = discord.Embed(color=0xDEADBF).set_image(url=res["message"])
        await ctx.send(embed=em)

    @commands.command()
    @commands.guild_only()
    async def ass(self, ctx):
        """Ass images owo"""
        if not ctx.message.channel.is_nsfw():
            em = discord.Embed(color=0xff6928, description="This isnt an NSFW Channel <:vanillaStare:441126443842404352>")
            return await ctx.send(embed=em, delete_after=3)
        r = await self.bot.session.get("https://nekobot.xyz/api/image?type=ass")
        res = await r.json()
        em = discord.Embed(color=0xDEADBF).set_image(url=res["message"])
        await ctx.send(embed=em)

    @commands.command()
    @commands.guild_only()
    async def pussy(self, ctx):
        """Not cats 😩"""
        if not ctx.message.channel.is_nsfw():
            em = discord.Embed(color=0xff6928, description="This isnt an NSFW Channel <:vanillaStare:441126443842404352>")
            return await ctx.send(embed=em, delete_after=3)
        r = await self.bot.session.get("https://nekobot.xyz/api/image?type=pussy")
        res = await r.json()
        em = discord.Embed(color=0xDEADBF).set_image(url=res["message"])
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(IRL_NSFW(bot))