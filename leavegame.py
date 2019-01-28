import discord
async def leavegame1(message, client, game1, Game):
  await client.remove_roles(message.author, discord.utils.get(message.author.server.roles, name="game1"))

async def leavegame2(message, client, game2, Game):
  await client.remove_roles(message.author, discord.utils.get(message.author.server.roles, name="game2"))

async def leavegame3(message, client, game3, Game):
  await client.remove_roles(message.author, discord.utils.get(message.author.server.roles, name="game3"))

async def leavegame4(message, client, game4, Game):
  await client.remove_roles(message.author, discord.utils.get(message.author.server.roles, name="game4"))