from discord.ext import commands
import discord, random

class Fun:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def weebify(self, ctx, *, text: str):
        """Weebify Text"""
        try:
            key = self.bot.config["idiotic_api"]
            header = {"Authorization": key}
            r = await self.bot.session.get(f'https://dev.anidiots.guide/text/owoify?text={text}', headers=header)
            res = await r.json()
            em = discord.Embed(color=0xDEADBF, description=res['text'])
            await ctx.send(embed=em)
        except:
            await ctx.send("Failed to connect.")

    @commands.command(aliases=['pillow'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def bodypillow(self, ctx, user: discord.Member):
        """Bodypillow someone"""
        await ctx.trigger_typing()
        userurl = user.avatar_url_as(format='png')
        r = await self.bot.session.get(f"https://nekobot.xyz/api/imagegen?type=bodypillow&url={userurl}")
        res = await r.json()
        if res['success'] != True:
            return await ctx.send(
                embed=discord.Embed(color=0xDEADBF, description="Failed to successfully get the image."))
        em = discord.Embed(color=0xDEADBF, title=f"{user.name}'s body pillow.")
        await ctx.send(embed=em.set_image(url=res['message']))

    @commands.command()
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def ship(self, ctx, user1: discord.Member, user2: discord.Member = None):
        """Ship OwO"""
        if user2 is None:
            user2 = ctx.message.author
        await ctx.trigger_typing()
        user2url = user2.avatar_url
        user1url = user1.avatar_url

        self_length = len(user1.name)
        first_length = round(self_length / 2)
        first_half = user1.name[0:first_length]
        usr_length = len(user2.name)
        second_length = round(usr_length / 2)
        second_half = user2.name[second_length:]
        finalName = first_half + second_half

        score = random.randint(0, 100)
        filled_progbar = round(score / 100 * 10)
        counter_ = '█' * filled_progbar + '‍ ‍' * (10 - filled_progbar)
        r = await self.bot.session.get(f"https://nekobot.xyz/api/imagegen?type=ship&user1={user1url}&user2={user2url}")
        res = await r.json()
        e = discord.Embed(color=0xDEADBF, title=f'{user1.name} ❤ {user2.name}', description=f"**Love %**\n"
                                                                                            f"`{counter_}` **{score}%**\n\n"
                                                                                            f"{finalName}")
        if res['success'] != True:
            return await ctx.send(
                embed=discord.Embed(color=0xDEADBF, description="Failed to successfully get the image."))
        await ctx.send(content="{}".format(finalName),
                       embed=e.set_image(url=res['message']))

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def awooify(self, ctx:commands.Context, user1: discord.Member):
        """AwWOOOOO"""
        await ctx.trigger_typing()
        user1url = user1.avatar_url_as(format='png')
        r = await self.bot.session.get(f"https://nekobot.xyz/api/imagegen?type=awooify&url={user1url}")
        res = await r.json()
        if res['success'] != True:
            return await ctx.send(embed=discord.Embed(color=0xDEADBF, description="Failed to successfully get the image."))
        await ctx.send(embed=discord.Embed(color=0xDEADBF).set_image(url=res['message']))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def jpeg(self, ctx, user:discord.Member):
        """JPEGify Someone"""
        await ctx.trigger_typing()
        avatar = user.avatar_url_as(format='png')
        r = await self.bot.session.get(f"https://nekobot.xyz/api/imagegen?type=jpeg&url={avatar}")
        res = await r.json()
        if res['success'] != True:
            return await ctx.send(embed=discord.Embed(color=0xDEADBF, description="Failed to successfully get the image."))
        await ctx.send(embed=discord.Embed(color=0xDEADBF).set_image(url=res['message']))

    @commands.command()
    @commands.cooldown(1, 7, commands.BucketType.user)
    async def deepfry(self, ctx, user:discord.Member):
        """Deepfry Someones Avatar"""
        await ctx.trigger_typing()
        avatar = user.avatar_url_as(format='png')
        r = await self.bot.session.get(f"https://nekobot.xyz/api/imagegen?type=deepfry&image={avatar}")
        res = await r.json()
        if res['success'] != True:
            return await ctx.send(embed=discord.Embed(color=0xDEADBF, description="Failed to successfully get the image."))
        await ctx.send(embed=discord.Embed(color=0xDEADBF).set_image(url=res['message']))

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def bigletter(self, ctx, *, text: str):
        """Big Letter Generator"""
        await ctx.trigger_typing()
        r = await self.bot.session.get("http://nekobot.xyz/api/text?type=bigletter&text=" + text)
        res = await r.json()
        return await ctx.send(res["message"])

def setup(bot):
    bot.add_cog(Fun(bot))