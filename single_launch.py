from discord.ext import commands
from collections import Counter
import discord, datetime, os
import aiohttp, aiomysql
import json, logging

log = logging.getLogger()
log.setLevel(logging.INFO)
logFormat = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
fileHandler = logging.FileHandler(filename=f"logs/{datetime.datetime.utcnow()}.log", encoding="utf-8", mode="w")
fileHandler.setFormatter(logFormat)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormat)
log.addHandler(fileHandler)
log.addHandler(consoleHandler)

def _prefix_callable(bot, msg):
    prefixes = ['h!', 'H!']
    return commands.when_mentioned_or(*prefixes)(bot, msg)

class HentaiBoi(commands.AutoShardedBot):

    def __init__(self):
        super().__init__(command_prefix=_prefix_callable,
                         description="Hentai Boat UwU",
                         pm_help=None,
                         shard_id=0,
                         status=discord.Status.dnd,
                         help_attrs={'hidden': True})
        self.command_usage = Counter()
        self.session = aiohttp.ClientSession(loop=self.loop)
        self.counter = Counter()
        self.config = json.load(open("config.json"))
        self.webhook = self.config["webhook"]

        self.load_extension("events.error_handler")
        self.load_extension("events.ready")
        self.load_extension("events.misc")

        async def _init_sql():
            self.sql_conn = await aiomysql.create_pool(host='localhost', port=3306,
                                              user='root', password=self.config["dbpass"],
                                              db='hentaiboi', loop=self.loop, autocommit=True)

        self.loop.create_task(_init_sql())

        for file in os.listdir("modules"):
            if file.endswith(".py"):
                name = file[:-3]
                try:
                    self.load_extension(f"modules.{name}")
                    print(f"[INFO] Loaded {name.title()}")
                except Exception as e:
                    print(f"[ERROR] Failed to load {name}\n{e}")

    async def send_cmd_help(self, ctx):
        if ctx.invoked_subcommand:
            pages = await self.formatter.format_help_for(ctx, ctx.invoked_subcommand)
            for page in pages:
                await ctx.send(page)
        else:
            pages = await self.formatter.format_help_for(ctx, ctx.command)
            for page in pages:
                await ctx.send(page)

    async def on_message(self, message):
        self.counter["messages_read"] += 1
        if message.author.bot:
            return
        await self.process_commands(message)

    async def close(self):
        await super().close()
        await self.close()

    async def on_ready(self):
        if not hasattr(self, 'uptime'):
            self.uptime = datetime.datetime.utcnow()

    def run(self):
        super().run(self.config["token"])

def run_bot():
    bot = HentaiBoi()
    bot.run()

if __name__ == '__main__':
    run_bot()
