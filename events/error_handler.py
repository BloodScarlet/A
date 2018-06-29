from discord.ext import commands
import discord
import traceback, sys, logging

log = logging.getLogger()

class error_handler:

    def __init__(self, bot):
        self.bot = bot

    async def send_cmd_help(self, ctx):
        if ctx.invoked_subcommand:
            pages = await self.bot.formatter.format_help_for(ctx, ctx.invoked_subcommand)
            for page in pages:
                await ctx.send(page)
        else:
            pages = await self.bot.formatter.format_help_for(ctx, ctx.command)
            for page in pages:
                await ctx.send(page)

    async def on_command_error(self, ctx, e):
        if isinstance(e, commands.NoPrivateMessage):
            return
        elif isinstance(e, commands.DisabledCommand):
            return
        elif isinstance(e, discord.Forbidden):
            return
        elif isinstance(e, discord.NotFound):
            return
        elif isinstance(e, commands.CommandInvokeError):
            em = discord.Embed(color=0xff6928,
                               title="Error",
                               description=f"Error in {ctx.command.qualified_name}\n"
                                           f"Support sevrer: https://discord.gg/q98qeYN")
            log.info('In {}:'.format(ctx.command.qualified_name))
            log.info('{}: {}'.format(e.original.__class__.__name__, e.original))
            await ctx.send(embed=em)
            payload = {
                "embeds": [
                    {
                        "title": f"Command: {ctx.command.qualified_name}",
                        "description": f"```py\n{e}\n```",
                        "color": 16740159
                    }
                ]
            }
            await self.bot.session.post(self.bot.webhook, json=payload)
        elif isinstance(e, commands.BadArgument):
            await self.send_cmd_help(ctx)
        elif isinstance(e, commands.MissingRequiredArgument):
            await self.send_cmd_help(ctx)
        elif isinstance(e, commands.CheckFailure):
            await ctx.send('You are not allowed to use that command.', delete_after=5)
        elif isinstance(e, commands.CommandOnCooldown):
            await ctx.send('Command is on cooldown... {:.2f}s left'.format(e.retry_after), delete_after=5)
        elif isinstance(e, commands.CommandNotFound):
            return
        else:
            return

def setup(bot):
    bot.add_cog(error_handler(bot))