from datetime import datetime as dt
from pytz import timezone as tz
from discord import Embed, Colour
from discord.ext import commands, tasks
from utils import MongoHandler


class EMailer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Mango = MongoHandler.MongoHandler()
        self.autoFetchEMails.start()

    def cog_unload(self):
        self.autoFetchEMails.stop()

    @commands.command(name='fetch')
    async def email_cmd(self, ctx):
        berlin_tz = tz('Europe/Berlin')  # <-- change this as well to your timezone if needed!
        idx = 1
        userId = str(123456789)  # <-- change this to your discord-id !
        mails = await self.Mango.fetchNewEMails()
        mails_num = len(mails)
        em = Embed(title="New Mails Summary", colour=Colour.blurple(), timestamp=dt.now(tz=berlin_tz))
        em.description = f"You have {mails_num} new Mails."
        await ctx.send(f"<@{userId}>")
        await ctx.send(embed=em)
        if mails_num == 0:
            return
        for mail_ in mails:
            mailEmbed = Embed(title=f"Mail {idx} of {mails_num}", colour=Colour.dark_teal(),
                              timestamp=dt.now(tz=berlin_tz))
            mailEmbed.add_field(name='Sender', value=f'{mail_.mail}', inline=False)
            mailEmbed.add_field(name='Subject', value=f'{mail_.subject}', inline=False)
            mailEmbed.add_field(name='Message', value=f'{mail_.message}', inline=False)
            mailEmbed.add_field(name='Date', value=f'{berlin_tz.fromutc(mail_.date)}', inline=False)
            await ctx.send(embed=mailEmbed)
            idx = idx + 1
        await self.run_purger()
        return

    async def run_purger(self):
        await self.Mango.deleteMails()

    @tasks.loop(minutes=59)  # <-- change this for faster refresh, although an hour is alright.
    async def autoFetchEMails(self):
        channelId = 123456789  # <-- change this to your target channel-id
        _channel = self.bot.get_channel(channelId)
        await self.email_cmd(_channel)

    @autoFetchEMails.before_loop
    async def before_autoFetchEMails(self):
        print("[EMailer][*]: Waiting...")
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(EMailer(bot))
