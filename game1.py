import discord
from random import randint

usedcards_w = [] #All of the white cards that were taken from the deck.
usedcards_b = [] #All of the black cards that were taken from the deck.
cards_played = [] #All cards played in the current round.
channelid = "518500991235260458"

async def startGame1(game1, client):
  global player1, player2, player3, player4

  #creating all the player's hands and sending them.
  if game1.Playercount == 4:

    player1 = hand()
    player1.owner = game1.Players[0]
    await player1.send_hand()

    player2 = hand()
    player2.owner = game1.Players[1]
    await player2.send_hand()

    player3 = hand()
    player3.owner = game1.Players[2]
    await player3.send_hand()

    player4 = hand()
    player4.owner = game1.Players[3]
    await player4.send_hand()

    await startRound(game1, client)

  else:
    await client.send_message(destination=client.channel_get(channelid), content="You need 4 people to start the game!")

async def startRound(game1, client):
  if player1.score < game1.max_score or player2.score < game1.max_score or player3.score < game1.max_score or player4.score < game1.max_score:
    await choose_dealer(game1)
    await send_bcard(client, game1)
  else:
    score = ["","","",""]
    score[0] = player1.score
    score[1] = player2.score
    score[2] = player3.score
    score[3] = player4.score
    winner = max(score)
    if winner == player1.score:
      print("player1 won")
    elif winner == player2.score:
      print("player2 won")
    elif winner == player3.score:
      print("player3 won")
    elif winner == player4.score:
      print("player4 won")
    await endgame(game1, client)

async def endgame(game1, client):
  await client.remove_roles(player1.owner, discord.utils.get(player1.owner.server.roles, name="game1"))
  await client.remove_roles(player2.owner, discord.utils.get(player2.owner.server.roles, name="game1"))
  await client.remove_roles(player3.owner, discord.utils.get(player3.owner.server.roles, name="game1"))
  await client.remove_roles(player4.owner, discord.utils.get(player4.owner.server.roles, name="game1"))
  await client.purge_from(channel=client.channel_get(channelid), limit=1000)

async def send_bcard(client, game1):
  global usedcards_b
  if len(usedcards_b) != 16:
    card = "Deck/B" + str(randint(1,16)) + ".png"
    if card not in usedcards_b:
      await client.send_file(destination=client.get_channel(channelid), fp=card, content=str(game1.dealer.name)+" is the card czar!")
      usedcards_b.append(card)
  else:
    usedcards_b = []
    send_bcard(client)

async def playcard1(message, client, game1, card):
  cards_played.append(card)
  if len(cards_played) == 4:
    client.send_message(destination=client.get_channel(channelid), content="All White cards have been chosen.")
    for i in range(0,3):
      client.send_file(destination=client.get_channel(channelid), fp=cards_played[i], content="card"+str(i))

async def choose_dealer(game1):
  dealer = randint(1,4)

  if dealer == 1:
    player1.is_dealer = True
    game1.dealer = player1.owner
  elif dealer == 2:
    player2.is_dealer = True
    game1.dealer = player2.owner
  elif dealer == 3:
    player3.is_dealer = True
    game1.dealer = player3.owner
  elif dealer == 4:
    player4.is_dealer = True
    game1.dealer = player4.owner

async def choose_card1(message, client, game1, card):
  print("yeehaw cowboy")

#Class for each player's hand
class hand:
  owner = ""#who's hand this is
  cards = []#What cards they have
  score = 0
  is_dealer = False

  def __init__(self):
    while len(self.cards) < 7:
      card = "Deck/W" + str(randint(1,7)) + ".png"
      if card in usedcards_w:
        self.cards.append(self.card)
        usedcards_w.append(card)

  async def send_hand(self):
    await discord.Client.send_message(destination=self.owner, content="Sending cards...")
    await discord.Client.send_typing(destination=self.owner)
    await discord.Client.purge_from(channel=self.owner, limit=20)
    for i in range(0,6):
      await discord.Client.send_file(destination=self.owner, fp=self.cards[i], content="Card "+str(i))
    await discord.Client.send_message(destination=self.owner, content="Do !card [card number] to play that card!")

  def info(self):
    print(str(self.owner))
    print(str(self.cards))