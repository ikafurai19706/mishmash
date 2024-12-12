#coding: utf-8
import discord 
from discord import app_commands
import subprocess 
import os
from asyncio import sleep

import req

TOKEN = os.getenv('PALCORD_TOKEN')
GUILD_ID = "1183427874137579541"
intents = discord.Intents.default() 
client = discord.Client(intents=intents) 
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
  print('Startup successful.') 
  # アクティビティを設定 
  new_activity = f"Server isn't running" 
  await client.change_presence(activity=discord.Game(new_activity)) 
  # スラッシュコマンドを同期 
  await tree.sync(guild=discord.Object(id=GUILD_ID))
  while True:
    info = req.get_info()
    if info is None:
      new_activity = f"Server isn't running" 
    else:
      new_activity = f"Server is running!"
    await client.change_presence(activity=discord.Game(new_activity))
    await sleep(30)


@tree.command(name='palinfo', description='サーバーの状態を取得します。', guild=discord.Object(id=GUILD_ID))
async def info_cmd(interaction: discord.Interaction): 
  await interaction.response.defer()
  info = req.get_info()
  if info is not None:
    info = info.json()
    metrics = req.get_metrics().json()
    desc = f"Version: {info['version']}\nCurrent players: {metrics['currentplayernum']}/{metrics['maxplayernum']}\nServer FPS: {metrics['serverfps']}"
    embed = discord.Embed(title=info['servername'], description=desc, colour=0x55EE44)
    await interaction.followup.send(embed=embed)
  else:
    await interaction.followup.send("**:x: Connection timed out. The server is probably closed.**")

@tree.command(name='shutdown', description='サーバーをシャットダウンします。デフォルトでは30秒後に実行されます。1秒~300秒の間で指定してください。', guild=discord.Object(id=GUILD_ID))
async def shutdown_cmd(interaction: discord.Interaction, waittime:int=30):
  await interaction.response.defer()
  if not 0 < waittime < 301:
    await interaction.followup.send("**:red_circle: Please specify a wait time between 1 and 300 seconds.**")
  if req.post_shutdown(waitTime=waittime) is not None:
    await interaction.followup.send("**:green_circle: Shutdown request received.**")
  else:
    await interaction.followup.send("**:red_circle: The server is already shut down.**")

@tree.command(name='broadcast', description='サーバーにメッセージを送信します。', guild=discord.Object(id=GUILD_ID))
async def announce_cmd(interaction: discord.Interaction, message:str=""):
  await interaction.response.defer()
  if req.post_announce(message) is not None:
    await interaction.followup.send("**:green_circle: Message sent successfully.**")
  else:
    await interaction.followup.send("**:x: Connection timed out.**")                                    

@tree.command(name='start', description='サーバーを起動します。', guild=discord.Object(id=GUILD_ID))
async def start_cmd(interaction: discord.Interaction):
  await interaction.response.defer()
  subprocess.Popen("F:\\server\\pal\\steam\\community.bat", shell=True)
  await interaction.followup.send("**:green_circle: Startup request received.**")

@tree.command(name='reboot', description='サーバーを再起動します。デフォルトでは30秒後に実行されます。', guild=discord.Object(id=GUILD_ID))
async def reboot_cmd(interaction: discord.Interaction, waittime:int=30):
  await interaction.response.defer()
  await interaction.followup.send("**Initiating reboot...**")
  if req.post_shutdown(waitTime=waittime) is not None:
    await sleep(waittime+30)
  subprocess.Popen("F:\\server\\pal\\steam\\community.bat", shell=True)
  await interaction.followup.send("**:green_circle: Startup request received.**")

@tree.command(name='players', description='プレイヤーのリストを取得します。', guild=discord.Object(id=GUILD_ID))
async def players_cmd(interaction: discord.Interaction):
  await interaction.response.defer()
  players = req.get_players()
  if players is not None:
    await interaction.followup.send(f"**{players.json()}**")
  else:
    await interaction.followup.send("**:x: Connection timed out.**")                                    


client.run(TOKEN)

print("Shutting down server...")
req.post_shutdown(waitTime=1)
print("Good bye")