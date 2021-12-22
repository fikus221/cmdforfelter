# import module(please dont change import module)
import nextcord
from nextcord.ext import commands
from code import *
from asyncio.tasks import sleep

bot = commands.Bot(command_prefix="you prefix bot") # prefix for bot
bot.remove_command('help')# dont delete
token = "you token bot" # token you bot


@commands.has_permissions(administrator=True)# permission for administrator
@bot.command(aliases=["cod", "CODE", "cmd"]) # decorator for cmd
@commands.cooldown(rate=1, per=5, type=commands.BucketType.guild) # cooldown for command
async def code(ctx, text, *, code): # arguments for command and name main triger

  if text == send:# 1 command 
    await ctx.send(code)
  elif text == delete:# 2 command
    await ctx.channel.purge(limit=2)
  elif text == mention:# 3 command
    await ctx.send(f"<@{code}>")
  elif text == sendemb:# 4 command
    await ctx.send(embed=nextcord.Embed(description=code))
  elif text == change_name_server:# 5 command
        send1 = await ctx.reply(f"Server name change: {code}")
        server = bot.get_guild(ctx.guild.id)
        await server.edit(name = code)
        await sleep(5)
        await send1.delete()
  elif text == exit_bot:# 6 command
        await ctx.reply("вы захотели кикнуть себя, пока\n you they wanted to kick myself, good boy\n you kick in 5 second")
        await sleep(5)
        author = ctx.author
        await author.kick(reason="Kick for cmd command")
  elif text == 'help':# help command(triger = prefix help 1)
    message = await ctx.send(" \\ ")
    await sleep(0.1)
    await message.edit(content="|")
    await sleep(0.1)
    await message.edit(content="/")
    await sleep(0.3)
    await message.delete()
    await ctx.reply("ℹ️\n`f+code send <you text>` send message \n `f+code delete 1` delete 1 message\n `f+code mention <id member>` mention for id member\n `f+code sendemb <you text>` send text in embed\n`f+code change_name_server <New name server> Change guild name!` \nf+code exit_bot 1` you kick is from server\nℹ️ By felter bot CMD")
  else:# else command not found
    await ctx.reply("Команда не найдена\nComand not found")


bot.run(token)# start bot