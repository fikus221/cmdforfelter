import nextcord
from nextcord.ext import commands
from code import *
from asyncio.tasks import sleep

bot = commands.Bot(command_prefix="you prefix bot")
bot.remove_command('help')
token = "you token bot"


@commands.has_permissions(administrator=True)
@bot.command(aliases=["cod", "CODE", "cmd"])
@commands.cooldown(rate=1, per=5, type=commands.BucketType.guild)
async def code(ctx, text, code):

  if text == send:
    await ctx.send(code)
  elif text == delete:
    await ctx.channel.purge(limit=2)
  elif text == mention:
    await ctx.send(f"<@{code}>")
  elif text == sendemb:
    await ctx.send(embed=nextcord.Embed(description=code))
  elif text == change_name_server:
        send1 = await ctx.reply(f"Server name change: {code}")
        server = bot.get_guild(ctx.guild.id)
        await server.edit(name = code)
        await sleep(5)
        await send1.delete()
  elif text == 'help':
    message = await ctx.send(" \\ ")
    await sleep(0.1)
    await message.edit(content="|")
    await sleep(0.1)
    await message.edit(content="/")
    await sleep(0.3)
    await message.delete()
    await ctx.reply("ℹ️\n`f+code send <you text>` send message \n `f+code delete 1` delete 1 message\n `f+code mention <id member>` mention for id member\n `f+code sendemb <you text>` send text in embed\n`f+code change_name_server <New name server> Change guild name!` `\nℹ️ By felter bot CMD")
  else:
    await ctx.reply("Команда не найдена\nComand not found")


bot.run(token)