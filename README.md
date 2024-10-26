# fulcrum API
A python wrapper for fulcrum api

# Instalation
python required >=3.9.0

```sh
pip install -U git+https://github.com/br4nch/fulcrum_api
```

# Example
```py
import discord
from discord.ext import commands
from fulcrum_api import FulcrumAPI

bot = commands.Bot(command_prefix="," intents=discord.Intents.all())
fulcrumapi = FulcrumAPI()

@bot.command()
async def tiktok(ctx, username: str):
  data = await fulcrumapi.tiktok_user(username)
  embed = discord.Embed(color=0xffffff, title=data["nickname"])
  embed.add_field(name="followers", value=data["followers"])
  embed.add_field(name="following", value=data["following"])
  embed.add_field(name="videos", value=data["videos"])
  await ctx.send(embed=embed)
```
