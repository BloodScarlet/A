from discord.ext import commands
import discord, time

class Economy:

    def __init__(self, bot):
        self.bot = bot

    async def usercheck(self, user:int):
        async with self.bot.sql_conn.acquire() as conn:
            async with conn.cursor() as db:
                if not await db.execute("SELECT 1 FROM economy WHERE userid = %s", (user,)):
                    return False
                else:
                    return True

    async def create_user(self, user:int):
        async with self.bot.sql_conn.acquire() as conn:
            async with conn.cursor() as db:
                await db.execute("INSERT INTO economy VALUES (%s, 0, 0)", (user,))

    async def get_balance(self, user:int):
        async with self.bot.sql_conn.acquire() as conn:
            async with conn.cursor() as db:
                try:
                    await db.execute("SELECT balance FROM economy WHERE userid = %s", (user,))
                    balance = await db.fetchone()
                    return int(balance[0])
                except:
                    return 0

    async def get_time(self, user:int):
        async with self.bot.sql_conn.acquire() as conn:
            async with conn.cursor() as db:
                try:
                    await db.execute("SELECT lastdaily FROM economy WHERE userid = %s", (user,))
                    balance = await db.fetchone()
                    return int(balance[0])
                except:
                    return 0

    async def update_time(self, user:int):
        async with self.bot.sql_conn.acquire() as conn:
            async with conn.cursor() as db:
                await db.execute("UPDATE economy SET lastdaily = %s WHERE userid = %s", (int(time.time()), user,))

    async def update_credits(self, user:int, amount:int):
        async with self.bot.sql_conn.acquire() as conn:
            async with conn.cursor() as db:
                await db.execute("UPDATE economy SET balance = %s WHERE userid = %s", (amount, user,))

    @commands.command()
    async def balance(self, ctx, member:discord.Member = None):
        """View yours or someone elses balance."""
        if not await self.usercheck(ctx.message.author.id):
            await self.create_user(ctx.message.author.id)
        if member is None:
            member = ctx.message.author
            balance = await self.get_balance(member.id)
            msg = f"{member.mention}, you have **{balance}** HentaiCoin <:Gaasm:450703860999258134>"
        else:
            balance = await self.get_balance(member.id)
            msg = f"{member.name} has **{balance}** HentaiCoin <:Gaasm:450703860999258134>"
        await ctx.send(msg)

    @commands.command()
    async def daily(self, ctx):
        """Get your daily credits!"""
        if not await self.usercheck(ctx.message.author.id):
            await self.create_user(ctx.message.author.id)
        author = ctx.message.author
        balance = await self.get_balance(author.id)
        lastdaily = await self.get_time(author.id)
        curr_time = int(time.time())
        time_since = int(curr_time - lastdaily)
        if time_since >= 86400:
            await self.update_credits(author.id, int(balance + 500))
            await self.update_time(author.id)
            return await ctx.send("You have recieved **500** credits!")
        else:
            return await ctx.send("Come back tomorrow for your next daily!")

    @commands.command()
    async def transfer(self, ctx, user:discord.Member, amount:int):
        """Transfer HentaiCoin to Users"""
        if not await self.usercheck(ctx.message.author.id):
            await self.create_user(ctx.message.author.id)
        if user.bot:
            return await ctx.send("You can't send money to bots.")
        if user == ctx.message.author:
            return await ctx.send("You can't send yourself money")
        if amount <= 0:
            return await ctx.send("The amount must be higher than 0")
        author = ctx.message.author
        balance = await self.get_balance(author.id)
        if amount > balance:
            return await ctx.send("You don't have that much to transfer.")

        if not await self.usercheck(user.id):
            await self.create_user(user.id)

        user_balance = await self.get_balance(user.id)
        new_author_balance = int(balance - amount)
        new_user_balance = int(user_balance + amount)

        await self.update_credits(author.id, new_author_balance)
        await self.update_credits(user.id, new_user_balance)

        await ctx.send(f"📬 Sent **{user.name} {amount}** HentaiCoin.")

def setup(bot):
    bot.add_cog(Economy(bot))