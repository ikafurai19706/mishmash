#coding: utf-8
import discord 
from discord import app_commands
import subprocess 
import req
TOKEN = "MTI1NzAyOTg1NTEzMjkwOTYwOQ.Gxg2PM.9s0rJXoHRUzZu_xeyLPH9sQoZifR3UM2LHimbU"
GUILD_ID = "1183427874137579541"
intents = discord.Intents.default() 
client = discord.Client(intents=intents) 
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
  print('Startup successful.') 
  # アクティビティを設定 
  new_activity = f"During the experiment" 
  await client.change_presence(activity=discord.Game(new_activity)) 
  # スラッシュコマンドを同期 
  await tree.sync(guild=discord.Object(id=GUILD_ID))

@tree.command(name='palinfo', description='サーバーの状態を取得します。', guild=discord.Object(id=GUILD_ID))
async def info_cmd(interaction: discord.Interaction): 
  await interaction.response.defer()
  info = req.get_info().json()
  metrics = req.get_metrics().json()
  desc = f"Version: {info["version"]}\nCurrent players: {metrics["currentplayernum"]}/{metrics["maxplayernum"]}\nServer FPS: {metrics["serverfps"]}"
  embed = discord.Embed(title=info["servername"], description=desc)
  await interaction.followup.send(embed=embed)

@tree.command(name='shutdown', description='サーバーをシャットダウンします。', guild=discord.Object(id=GUILD_ID))
async def shutdown_cmd(interaction: discord.Interaction, waittime:int=30):
  await interaction.response.defer()
  req.post_shutdown(waitTime=waittime)
  await interaction.followup.send("**Shutdown request received.**")

@tree.command(name='broadcast', description='サーバーにメッセージを送信', guild=discord.Object(id=GUILD_ID))
async def announce_cmd(interaction: discord.Interaction, message:str=""):
  await interaction.response.defer()
  req.post_announce("Hello Palworld!")
  await interaction.followup.send("**Message sent successfully.**")

@tree.command(name='start', description='サーバーを起動します。', guild=discord.Object(id=GUILD_ID))
async def announce_cmd(interaction: discord.Interaction):
  await interaction.response.defer()
  subprocess.Popen("F:\\server\\pal\\steam\\community.bat", shell=True)
  await interaction.followup.send("**Startup request received.**")

@tree.command(name='players', description='プレイヤーのリストを取得します。', guild=discord.Object(id=GUILD_ID))
async def announce_cmd(interaction: discord.Interaction):
  await interaction.response.defer()
  players = req.get_players()
  await interaction.followup.send(f"**{players.json()}**")

client.run(TOKEN)
