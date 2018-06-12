import discord, asyncio, logging

log = logging.getLogger()

class Ready:

    def __init__(self, bot):
        self.bot = bot
        self.dbl_auth = { "Authorization": self.bot.config["dbl"] }

    async def on_shard_ready(self, shard_id):
        log.info(f"[INFO] Shard {shard_id} ready.")
        payload = {
            "embeds": [
                {
                    "title": "Shard Connect.",
                    "description": f"Shard {shard_id} has connected.",
                    "color": 14593471
                }
            ]
        }
        await self.bot.session.post(self.bot.webhook, json=payload)

    def getgame(self):
        members = len(set(self.bot.get_all_members()))
        guilds = len(self.bot.guilds)
        game = discord.Streaming(name=f"{guilds} | {members}", url="https://twitch.tv/rektdevlol")
        return game

    async def on_ready(self):
        log.info("-----------------")
        log.info(f"[INFO] Ready!")
        members = len(set(self.bot.get_all_members()))
        guilds = len(self.bot.guilds)
        log.info(f"Shards: {self.bot.shard_count}")
        log.info(f"Servers {guilds}")
        log.info(f"Users {members}")
        if not hasattr(self.bot, "wewloop"):
            self.bot.wewloop = True
            while True:
                await self.bot.change_presence(activity=self.getgame())
                await self.bot.session.post(f"https://discordbots.org/api/bots/{self.bot.user.id}/stats",
                                           headers=self.dbl_auth,
                                           json={
                                               "server_count": len(self.bot.guilds),
                                               "shard_count": self.bot.shard_count
                                           })
                await asyncio.sleep(1800)

def setup(bot):
    bot.add_cog(Ready(bot))