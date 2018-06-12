# Modified version of https://github.com/KawaiiBot/AIO_Launcher
# License https://github.com/KawaiiBot/AIO_Launcher/blob/master/LICENSE

import json, os
from datetime import datetime
from collections import Counter
import aiohttp, aiomysql

import discord, logging
from discord.ext import commands

log = logging.getLogger()
log.setLevel(logging.INFO)
logFormat = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
fileHandler = logging.FileHandler(filename=f"logs/{datetime.utcnow()}.log", encoding="utf-8", mode="w")
fileHandler.setFormatter(logFormat)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormat)
log.addHandler(fileHandler)
log.addHandler(consoleHandler)

def _prefix_callable(bot, msg):
    prefixes = ['h!', 'H!']
    return commands.when_mentioned_or(*prefixes)(bot, msg)

class Instance:

    def __init__(self, instance, shard_count, ids, pipe):
        self.pipe = pipe

        self.bot = commands.AutoShardedBot(command_prefix=_prefix_callable,
                                           shard_count=shard_count,
                                           shard_ids=ids,
                                           help_attrs=dict(Hidden=True),
                                           pm_help=None,
                                           fetch_offline_members=False)
        self.bot.prefix = "n!"
        self.bot.instance = instance
        self.bot.config = json.load(open("config.json"))
        self.bot.command_usage = Counter()
        self.bot.session = aiohttp.ClientSession(loop=self.bot.loop)
        self.bot.counter = Counter()
        self.bot.webhook = self.bot.config["webhook"]

        if not hasattr(self, "uptime"):
            self.bot.uptime = datetime.utcnow()

        self.bot.add_listener(self.on_ready)
        self.bot.add_listener(self.on_message)
        self.bot.run(self.bot.config["token"])

        async def _init_sql():
            self.sql_conn = await aiomysql.create_pool(host='localhost', port=3306,
                                              user='root', password=self.bot.config["dbpass"],
                                              db='hentaiboi', loop=self.bot.loop, autocommit=True)

        self.bot.loop.create_task(_init_sql())

    async def on_ready(self):
        log.info(f"Instance {self.bot.instance} Ready..")
        self.bot.load_extension("events.error_handler")
        self.bot.load_extension("events.ready")
        self.bot.load_extension("events.misc")

        for file in os.listdir("modules"):
            if file.endswith(".py"):
                name = file[:-3]
                try:
                    self.bot.load_extension(f"modules.{name}")
                    log.info(f"Loaded {name}")
                except Exception as e:
                    log.error(f"Failed to load {name}, {e}")

        self.pipe.send(1)
        self.pipe.close()

    async def on_message(self, msg):
        self.bot.counter["messages_read"] += 1
        if msg.author.bot:
            return
        await self.bot.process_commands(msg)