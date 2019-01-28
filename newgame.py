import discord

async def newgame(message, game1, game2, game3, game4, client):
    if game1.has_owner == False:
        print("game1 is open")
        game1.has_owner = True
        game1.Channelid = client.get_channel('515717874103615508')
        game1.Players = [message.author,"",""]
        await client.send_message(destination=message.channel, content="Congrats, game1 has been claimed!")
        print("Game1 info:")
        game1.info()
        member = message.author
        role = discord.utils.get(message.author.server.roles, name="game1")
        await client.add_roles(member, role)

    elif game2.has_owner == False:
        print("game2 is open")
        game2.has_owner = True
        game2.Channelid = client.get_channel('515718089493708814')
        game2.Players = [message.author,"",""]
        await client.send_message(destination=message.channel, content="Congrats, game2 has been claimed!")
        print("Game2 info:")
        game2.info()
        member = message.author
        role = discord.utils.get(message.author.server.roles, name="game2")
        await client.add_roles(member, role)

    elif game3.has_owner == False:
        print("game3 is open")
        game3.has_owner = True
        game3.Channelid = client.get_channel('515718230170533889')
        game3.Players = [message.author,"",""]
        await client.send_message(destination=message.channel, content="Congrats, game3 has been claimed!")
        print("Game3 info:")
        game3.info()
        member = message.author
        role = discord.utils.get(message.author.server.roles, name="game3")
        await client.add_roles(member, role)

    elif game4.has_owner == False:
        print("game4 is open")
        game4.has_owner = True
        game4.Channelid = client.get_channel('515718264525946893')
        game4.Players = [message.author,"",""]
        await client.send_message(destination=message.channel, content="Congrats, game4 has been claimed!")
        print("Game4 info:")
        game4.info()
        member = message.author
        role = discord.utils.get(message.author.server.roles, name="game4")
        await client.add_roles(member, role)

    else:
        print("is full")
        await client.send_message(destination=message.channel, content="All games are full!")