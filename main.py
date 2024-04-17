import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio
import requests
import random
from keep_alive import keep_alive
import os

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@client.event
async def on_ready():
  print("Diana is on")


async def get_joke():
  url = "https://v2.jokeapi.dev/joke/Any"
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()
    if data["error"]:
      return "Sorry, I couldn't fetch a joke at the moment. Please try again later."
    if data["type"] == "twopart":
      return f"{data['setup']}\n{data['delivery']}"
    else:
      return data['joke']
  except requests.exceptions.RequestException as e:
    return f"Sorry, an error occurred while fetching the joke: {e}"


@client.command(pass_context=True)
@client.event
async def on_member_join(member: discord.Member):
  channel = discord.get_channel("1213485772192088104")
  embed = discord.Embed(title=f"Welcome {member}",
                        description="Hope you will enjoy here.",
                        color=0x1ddb82)
  if member.avatar.url == None:
    embed.set_thumbnail(
        url=
        "https://imgs.search.brave.com/vwimYLUDcAbT_ZWKjz9DlBVRoovzdUlB7dl-L8ZFB78/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/ZnJlZS1waG90by91/c2VyLXByb2ZpbGUt/ZnJvbnQtc2lkZV8x/ODcyOTktMzk1OTUu/anBnP3NpemU9NjI2/JmV4dD1qcGc"
    )
  else:
    embed.set_thumbnail(url=member.avatar.url)
  await client.channel.send(embed=embed)


@client.command(pass_context=True)
@client.event
async def on_member_remove(member: discord.Member):
  channel = discord.get_channel("1213453499027689494")
  embed = discord.Embed(title=f"Goodbye {member}",
                        description="You will be missed.",
                        color=0xdb231d)
  if member.avatar.url == None:
    embed.set_thumbnail(
        url=
        "https://imgs.search.brave.com/vwimYLUDcAbT_ZWKjz9DlBVRoovzdUlB7dl-L8ZFB78/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/ZnJlZS1waG90by91/c2VyLXByb2ZpbGUt/ZnJvbnQtc2lkZV8x/ODcyOTktMzk1OTUu/anBnP3NpemU9NjI2/JmV4dD1qcGc"
    )
  else:
    embed.set_thumbnail(url=member.avatar.url)
  await client.channel.send(embed=embed)


@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f"{member} has been kicked.")


@kick.error
async def kick_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("You dont have permission to kick anyone in this server.")


@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f"{member} has been banned.")


@ban.error
async def ban_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("You dont have permission to ban anyone in this server.")


@client.command()
async def cal(ctx, arg):
  newarg = arg.replace('X', '*').replace('x', '*')
  embed = discord.Embed(title=f"{str(arg)} = {eval(str(newarg))}",
                        color=0x00a2ff)
  await ctx.send(embed=embed)


#Owo function - start


#Slap
@client.command()
async def slap(ctx, member: discord.Member):
  await ctx.send(f"{ctx.author} slaps {member}")
  await ctx.send("https://tenor.com/view/yuuri-gif-17416729081201359957")


#Knock
@client.command()
async def knock(ctx, member: discord.Member):
  await ctx.send(f"{ctx.author} knocks {member}")
  await ctx.send(
      "https://tenor.com/view/mocha-drop-kick-dropkick-ninja-gif-16099688")


#Kiss
@client.command()
async def kiss(ctx, member: discord.Member):
  await ctx.send(f"{ctx.author} kisses {member}")
  await ctx.send(
      "https://tenor.com/view/%ED%8C%A1%EB%B0%8D-gif-15244761720736387823")


#Bully
@client.command()
async def bully(ctx, member: discord.Member):
  await ctx.send(f"{ctx.author} bullies {member}")
  await ctx.send("https://tenor.com/view/k%C5%AFkr-bully-gif-19223636")


#Hug
@client.command()
async def hug(ctx, member: discord.Member):
  await ctx.send(f"{ctx.author} hugs {member}")
  await ctx.send(
      "https://tenor.com/view/hug-warm-hug-depressed-hug-gif-4585064738068342394"
  )


@client.command()
async def pat(ctx, member: discord.Member):
  await ctx.send(f"{ctx.author} pats {member}")
  await ctx.send(
      "https://tenor.com/view/tsumiki-anime-waifu-miia-neko-gif-27055340")


@client.command()
async def tease(ctx, member: discord.Member):
  await ctx.send(f"{ctx.author} teases {member}")
  await ctx.send(
      "https://tenor.com/view/minions-tongue-out-bleh-teasing-annoying-gif-15645196"
  )


@client.command()
async def oops(ctx):
  await ctx.send(f"{ctx.author} says oops...")
  await ctx.send(
      "https://tenor.com/view/the-simpsons-homer-simpson-good-gif-126191627745920871"
  )


@client.command()
async def embarrass(ctx):
  await ctx.send(f"{ctx.author} is embarrassed...")
  await ctx.send(
      "https://tenor.com/view/embarrassed-panda-gif-17198172971511780380")


#Owo function - end


@client.command()
async def ping(ctx):
  # Calculate the bot's latency (response time)
  latency = round(client.latency * 1000)  # in milliseconds

  # Send the latency as a message
  await ctx.send(f'**Pong! {latency}ms**')


@client.command()
async def timer(ctx, arg: int):
  i = arg
  while i != 0:
    await ctx.send(i)
    i -= 1
    asyncio.sleep(1)

  await ctx.send("Times up")


@client.command()
async def joke(ctx):
  joke = await get_joke()
  await ctx.send(joke)


@client.command()
async def toss(ctx):
  coins = ["Heads", "Tails"]
  await ctx.send(f"Its a {random.choice(coins)}")


@client.command()
async def createchannel(ctx, channel_name):
  # Check if the bot has permissions to manage channels
  if not ctx.guild.me.guild_permissions.manage_channels:
    return await ctx.send("I don't have permission to manage channels.")

  # Create the channel
  try:
    new_channel = await ctx.guild.create_text_channel(channel_name)
    await ctx.send(
        f"Channel {new_channel.mention} has been created successfully.")
  except discord.Forbidden:
    await ctx.send("I don't have permission to create channels.")
  except discord.HTTPException:
    await ctx.send("An error occurred while creating the channel.")

keep_alive()
client.run(os.environ.get("token"))
