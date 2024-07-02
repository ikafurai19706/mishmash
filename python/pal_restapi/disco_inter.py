import discord
from discord.ext import tasks, commands
from interactions import SlashCommand, SlashContext
import req

TOKEN = "MTI1NzAyOTg1NTEzMjkwOTYwOQ.Gxg2PM.9s0rJXoHRUzZu_xeyLPH9sQoZifR3UM2LHimbU"
intents = discord.Intents.all() 
bot = commands.Bot(command_prefix="/", intents=intents) 
slash_client = SlashCommand(bot)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")

@slash_client.slash(name='palinfo', description='サーバーの状態を取得します。')
async def info_cmd(interaction: discord.Interaction): 
  await interaction.response.defer()
  info = req.get_info().json()
  metrics = req.get_metrics().json()
  desc = f"Version: {info["version"]}\nCurrent players: {metrics["currentplayernum"]}/{metrics["maxplayernum"]}\nServer FPS: {metrics["serverfps"]}"
  embed = discord.Embed(title=info["servername"], description=desc, color=0xFFFF00)
  await interaction.followup.send(embed=embed)

bot.run(TOKEN)