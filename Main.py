import discord

client = discord.Client()

token = open("token.txt", "r").read()


@client.event
async def on_message(message):

    # author name without the #0000
    author = str(message.author)[:str(message.author).index("#")]

    # bot doesn't reply to self
    if message.author == client.user:
        return

    # open 'messages.txt' in root folder: appending only, and encoding in utf-8
    messagesFile = open("messages.txt", "a", encoding="utf-8")

    # format message for nick
    msg = author + ":" + str(message.content) + "\n"
    print("writing " + str(message.content) + " from " + author + " to messages.txt")

    # write message and close opened file
    messagesFile.write(msg)
    messagesFile.close()

    # await client.send_message(message.channel, "give me the succ")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------------')

    # clear messages file
    open("messages.txt", "w").write("")
    print("clearing messages.txt")


client.run(token)
