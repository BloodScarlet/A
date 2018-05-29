from discord.ext import commands
import discord

LOWERCASE, UPPERCASE = 'x', 'X'
def triplet(rgb, lettercase=LOWERCASE):
    return format(rgb[0]<<16 | rgb[1]<<8 | rgb[2], '06'+lettercase)

base = "https://api.weeb.sh/images/random?type="

class Weeb:

    def __init__(self, bot):
        self.bot = bot
        self.auth = {"Authorization": "Wolke " + self.bot.config["weeb"]}

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def animepic(self, ctx):
        """Get an anime pic owowowo"""
        url = "https://api.computerfreaker.cf/v1/anime"
        await ctx.channel.trigger_typing()
        r = await self.bot.session.get(url)
        res = await r.json()
        em = discord.Embed(color=0xDEADBF)
        await ctx.send(embed=em.set_image(url=res['url']))

    @commands.command()
    async def kiss(self, ctx, user:discord.Member):
        """Kiss someone >~<"""
        if user == self.bot.user:
            return await ctx.send(embed=discord.Embed(color=0xDEADBF,
                                                      title=f"Kisses {ctx.message.author.name} back :3"))
        r = await self.bot.session.get(base + "kiss", headers=self.auth)
        res = await r.json()
        em = discord.Embed(color=0xDEADBF,
                           title=f"{ctx.message.author.name} kisses {user.name} ❤")
        await ctx.send(embed=em.set_image(url=res["url"]))

    @commands.command()
    async def hug(self, ctx, user:discord.Member):
        """Hug :3"""
        if user == self.bot.user:
            return await ctx.send(embed=discord.Embed(color=0xDEADBF,
                                                      title=f"Hugs {ctx.message.author.name} back :3"))
        r = await self.bot.session.get(base + "hug", headers=self.auth)
        res = await r.json()
        em = discord.Embed(color=0xDEADBF,
                           title=f"{ctx.message.author.name} hugged {user.name} ❤")
        await ctx.send(embed=em.set_image(url=res["url"]))

    @commands.command()
    async def pat(self, ctx, user:discord.Member):
        """Headpats!"""
        if user == self.bot.user:
            return await ctx.send(embed=discord.Embed(color=0xDEADBF,
                                                      title=f"Pats {ctx.message.author.name} back :3"))
        r = await self.bot.session.get(base + "pat", headers=self.auth)
        res = await r.json()
        em = discord.Embed(color=0xDEADBF,
                           title=f"{ctx.message.author.name} patted {user.name} owo")
        await ctx.send(embed=em.set_image(url=res["url"]))

    @commands.command()
    async def cuddle(self, ctx, user:discord.Member):
        """Cudddlee uwu!"""
        if user == self.bot.user:
            return await ctx.send(embed=discord.Embed(color=0xDEADBF,
                                                      title=f"Cuddles {ctx.message.author.name} back 😊"))
        r = await self.bot.session.get(base + "cuddle", headers=self.auth)
        res = await r.json()
        em = discord.Embed(color=0xDEADBF,
                           title=f"{ctx.message.author.name} cuddled with {user.name} 😊")
        await ctx.send(embed=em.set_image(url=res["url"]))

def setup(bot):
    bot.add_cog(Weeb(bot))