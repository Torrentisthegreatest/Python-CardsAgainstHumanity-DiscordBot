# Boards Against the Human Race Discord Bot
# by: Simon W. (incomplete)

from leavegame import leavegame1, leavegame2, leavegame3, leavegame4
from game1 import startGame1, playcard1, choose_card1
from game2 import startGame2, playcard2, choose_card2
from game3 import startGame3, playcard3, choose_card3
from game4 import startGame4, playcard4, choose_card4
from keep_alive import keep_alive
from newgame import newgame
import discord
import os

client = discord.Client()

class Game:
  is_started = False
  is_closed = False
  has_owner = False
  Players = ["","",""]
  Playercount = 0
  dealer = ""
  max_score = 0
  cardsPlayed_inround = {}

  def info(self):
    print(str(self.is_started))
    print(str(self.is_closed))
    print(str(self.has_owner))
    print(str(self.Players))
    print(str(self.Playercount))
    
def helpmenu():
  global helpmenu
  helpmenu = '''\
!newgame will make a new game
!helpmenu will open the menu
!join game1/game2/game3/game4 will add you to that game, if it is open.
!cleargames will reset all games.
!leavegame will remove you from a game.\
'''.format(length='multi-line', ordinal='second')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Torrent scream in frustration.", type=2))
    print("I'm in")
    print(client.user)
    Init()

def Init():
  global game1, game2, game3, game4
  game1 = Game()
  game2 = Game()
  game3 = Game()
  game4 = Game()

@client.event
async def on_message(message):
    if message.content == "!newgame" and str(message.channel.name) == "game-lobby":
        await newgame(message, game1, game2, game3, game4, client)
        await client.send_message(destination=message.channel, content="Yeehaw, I'm not done yet!")

    elif message.content == "!cleargames" and str(message.channel.name) == "game-lobby":
        Init()
        await client.purge_from(channel=discord.utils.get(message.author.server.channels, id="518500991235260458"), limit=1000)
        await client.purge_from(channel=discord.utils.get(message.author.server.channels, id="518501045425537024"), limit=1000)
        await client.purge_from(channel=discord.utils.get(message.author.server.channels, id="518501089784627215"), limit=1000)
        await client.purge_from(channel=discord.utils.get(message.author.server.channels, id="518501127247888421"), limit=1000)

    elif message.content == "!helpmenu" and str(message.channel.name) == "game-lobby":
      helpmenu()
      em = discord.Embed(title = "Help Menu", type = "rich", description = helpmenu)
      await client.send_message(destination=message.channel, embed=em)

    elif message.content[4:] == "!join" and str(message.channel.name) == "game-lobby":
      
      if message.content == "!join game1" and game1.Playercount < 4:
        if game1.has_owner == True:
          game1.Playercount += 1
          game1.Players.append(message.author)
          await client.add_roles(message.author, discord.utils.get(message.author.server.roles, name="game1"))

      elif message.content == "!join game2" and game2.Playercount < 4:
        if game2.has_owner == True: 
          game2.Playercount += 1
          game2.Players.append(message.author)
          await client.add_roles(message.author, discord.utils.get(message.author.server.roles, name="game2"))

      elif message.content == "!join game3" and game3.Playercount < 4:
        if game3.has_owner == True:
          game3.Playercount += 1
          game3.Players.append(message.author)
          await client.add_roles(message.author, discord.utils.get(message.author.server.roles, name="game3"))

      elif message.content == "!join game4" and game4.Playercount < 4:
        if game4.has_owner == True:
          game4.Playercount += 1
          game4.Players.append(message.author)
          await client.add_roles(message.author, discord.utils.get(message.author.server.roles, name="game4"))

    elif message.content == "!leavegame":

      if str(message.channel.name) == "game1":
        await leavegame1(message, client, game1, Game)

      elif str(message.channel.name) == "game2":
        await leavegame2(message, client, game2, Game)

      elif str(message.channel.name) == "game3":
        await leavegame3(message, client, game3, Game)

      elif str(message.channel.name) == "game4":
        await leavegame4(message, client, game4, Game)

    elif message.content == "!clearlobby" and str(message.channel.name) == "game-lobby":
        client.purge_from(client.get_channel("518500017494032385"), limit=1000)

    elif message.content == "!startgame":

      if str(message.channel.name) == "game1":
        game1.is_started = True
        game1.is_closed = True
        await startGame1(game1, client)

      elif str(message.channel.name) == "game2":
        game2.is_started = True
        game2.is_closed = True
        await startGame2(game2, client)

      elif str(message.channel.name) == "game3":
        game3.is_started = True
        game3.is_closed = True
        await startGame3(game3, client)

      elif str(message.channel.name) == "game4":
        game4.is_started = True
        game4.is_closed = True
        await startGame4(game4, client)

    elif message.content[4:] == "!card":

      if message.content[:6] == "1":
        card = 1
        if str(message.channel) in str(game1.Players) and str(message.author) != str(game1.dealer):
          await playcard1(message, client, game1, card)
        elif str(message.channel) in str(game2.Players) and str(message.author) != str(game2.dealer):
          await playcard2(message, client, game1, card)
        elif str(message.channnel) in str(game3.Players) and str(message.author) != str(game3.dealer):
          await playcard3(message, client, game1, card)
        elif str(message.channel) in str(game4.Players) and str(message.author) != str(game4.dealer):
          await playcard4(message, client, game1, card)
        elif str(message.channel.name) ==  "game1" and str(message.author) == str(game1.dealer):
          await choose_card1(message, client, game1, card)
        elif str(message.channel.name) ==  "game2"and str(message.author) == str(game2.dealer):
          await choose_card2(message, client, game2, card)
        elif str(message.channel.name) ==  "game3" and str(message.author) == str(game3.dealer):
          await choose_card3(message, client, game3, card)
        elif str(message.channel.name) ==  "game4" and str(message.author) == str(game4.dealer):
          await choose_card4(message, client, game4, card)
      elif message.content[:6] == "2":
        card = 2
        if str(message.channel) in str(game1.Players):
          await playcard1(message, client, game1, card)
        elif str(message.channel) in str(game2.Players):
          await playcard2(message, client, game1, card)
        elif str(message.channnel) in str(game3.Players):
          await playcard3(message, client, game1, card)
        elif str(message.channel) in str(game4.Players):
          await playcard4(message, client, game1, card)
        elif str(message.channel.name) ==  "game1":
          await choose_card1(message, client, game1, card)
        elif str(message.channel.name) ==  "game2":
          await choose_card2(message, client, game2, card)
        elif str(message.channel.name) ==  "game3":
          await choose_card3(message, client, game3, card)
        elif str(message.channel.name) ==  "game4":
          await choose_card4(message, client, game4, card)
      elif message.content[:6] == "3":
        card = 3
        if str(message.channel) in str(game1.Players):
          await playcard1(message, client, game1, card)
        elif str(message.channel) in str(game2.Players):
          await playcard2(message, client, game1, card)
        elif str(message.channnel) in str(game3.Players):
          await playcard3(message, client, game1, card)
        elif str(message.channel) in str(game4.Players):
          await playcard4(message, client, game1, card)
        elif str(message.channel.name) ==  "game1":
          await choose_card1(message, client, game1, card)
        elif str(message.channel.name) ==  "game2":
          await choose_card2(message, client, game2, card)
        elif str(message.channel.name) ==  "game3":
          await choose_card3(message, client, game3, card)
        elif str(message.channel.name) ==  "game4":
          await choose_card4(message, client, game4, card)
      elif message.content[:6] == "4":
        card = 4
        if str(message.channel) in str(game1.Players):
          await playcard1(message, client, game1, card)
        elif str(message.channel) in str(game2.Players):
          await playcard2(message, client, game2, card)
        elif str(message.channnel) in str(game3.Players):
          await playcard3(message, client, game3, card)
        elif str(message.channel) in str(game4.Players):
          await playcard4(message, client, game4, card)
        elif str(message.channel.name) ==  "game1":
          await choose_card1(message, client, game1, card)
        elif str(message.channel.name) ==  "game2":
          await choose_card2(message, client, game2, card)
        elif str(message.channel.name) ==  "game3":
          await choose_card3(message, client, game3, card)
        elif str(message.channel.name) ==  "game4":
          await choose_card4(message, client, game4, card)
      elif message.content[:6] == "5":
        card = 5
        if str(message.channel) in str(game1.Players):
          await playcard1(message, client, game1, card)
        elif str(message.channel) in str(game2.Players):
          await playcard2(message, client, game2, card)
        elif str(message.channnel) in str(game3.Players):
          await playcard3(message, client, game3, card)
        elif str(message.channel) in str(game4.Players):
          await playcard4(message, client, game4, card)
      elif message.content[:6] == "6":
        card = 6
        if str(message.channel) in str(game1.Players):
          await playcard1(message, client, game1, card)
        elif str(message.channel) in str(game2.Players):
          await playcard2(message, client, game2, card)
        elif str(message.channnel) in str(game3.Player):
          await playcard3(message, client, game3, card)
        elif str(message.channel) in str(game4.Players):
          await playcard4(message, client, game4, card)
      elif message.content[:6] == "7":
        card = 7
        if str(message.channel) in str(game1.Player):
          await playcard1(message, client, game1, card)
        elif str(message.channel) in str(game2.Players):
          await playcard2(message, client, game2, card)
        elif str(message.channnel) in str(game3.Players):
          await playcard3(message, client, game3, card)
        elif str(message.channel) in str(game4.Players):
          await playcard4(message, client, game4, card)

        

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)