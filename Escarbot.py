import discord
import random
import asyncio
from discord.ext import commands
from os import path
import wikipedia
import urllib
import os
import ruamel.yaml
import json
from pyfiglet import figlet_format

#add steam api
client = discord.Client()
listVIP = [
    "441006352635265025",
    "223941819153514497"
]
BlacklistWords = [
    "Borbi sucks",
    "Borbi is not cool",
    "Borbi is a Homo Sapien",
]
mutedList = [

]

mockList = [
    "418134494344642570"
]

email = input("What is your discord email? ")
password = input("What is your discord password? ")


async def mockingBob(message, mocked):
    case = 0 
    newMessage = ''
    for character in message.content:
        if character.isalpha():
            if case == 0:
                character = character.upper()
            else:
                character = character.lower()
            case = (case + 1) % 2
        newMessage += character
    msg = await client.send_message(message.channel, "```{}```".format(newMessage))
    msg = await client.send_message(message.channel, "```-{} 2k18```".format(mocked))

#start nuke code Deletes all messages the user has put
async def nuke(message):
  def __retry(message):
    cnt = 0
    while 1:
      sleep(1)
      try:
        cnt += 1
        if cnt >= 3:
          break
        client.delete_message(message)
        break
      except:
        continue

  counter = 0
  async for message in client.logs_from(message.channel, limit=500):
    if message.author == client.user:
      try:
        await client.delete_message(message)
      except:
        __retry(message)
      counter += 1
      if counter == 25:
        counter = 0
#end

#start spambot spams a word
async def spam(message, cms):
    count = 0
    while count < 1000:
        msg = await client.send_message(message.channel,"BOT: {}".format(cms))
        if message.content.startswith('!spamstop'):
            count = 1000
        count += 1  # This is the same as count = count + 1
#end


@client.event
async def on_message(message):
    check = message.content
    checkid = message.author.id
    #Help command type !help in order to get a list of commands
    if message.content.startswith('!-help'):
        if message.author.id == client.user.id or message.author.id in listVIP:
            msg = await client.send_message(message.channel, "```Owners Commands\n!nuke - Deletes all messages\n!exec - executes basic python commands\n!spam message - this spams a mess times \n!spamstop - stops the spam\n!chuck generates a random chuck norris joke\n!wiki subjects - searches wikipedia for a subject \n!cowsay message - puts your message but says it as a cow.\n!addvip - Adds VIP.\n!remvip - removes VIP\n!mute - mutes person\n!unmute - unmutes person```")

    elif check in BlacklistWords:
        await client.delete_message(message)
        await client.send_message(message.channel, "BOT: borbi forgives you for falling for anglo tricks. speak not these words again. @{}".format(message.author.name))

    elif checkid in mutedList:
        await client.delete_message(message)

    elif checkid in mockList:
        mockedAuthor = message.author.name
        await mockingBob(message, mockedAuthor)
            
    #Activates the nuke method
    elif message.content.startswith('!nuke'):
        if message.author.id == client.user.id:
            await nuke(message)

    elif message.content.startswith("!figlet"):
        if message.author.id in listVIP:
            mesg = message.content[len('!figlet'):].strip()
            mesg = figlet_format('{}'.format(mesg))
            await client.send_message(message.channel, "```{}```".format(mesg))

    #kicks a player
    elif message.content.startswith('!kick'):
        if message.author.id == client.user.id :
            name = message.content[len('!kick'):].strip()
            for member in message.server.members:
                if member.id == name or member.mention == name:
                    namemen = member.mention
                    await client.send_message(message.channel, "user {} will be kicked".format(namemen))

    #activates the spam method
    elif message.content.startswith('!spam'):
        if message.author.id == client.user.id:
            cms = message.content[len('!spam'):].strip()
            await spam(message = message,cms = cms)


    elif message.content.startswith('!clear'):
        if message.author.id == client.user.id:
            tmp = await client.send_message(message.channel, 'Clearing messages...')
            async for msg in client.logs_from(message.channel):
                await client.delete_message(msg)

    #Searches wikipedia example !wiki Operation Northwoods that would show the first 5 sentences
    elif message.content.startswith("!wiki"):
        if message.author.id == client.user.id or message.author.id == listVIP[0]:
            search = message.content[len('!wiki'):].strip()
            sent = message.content[len(search):].strip()
            msg = await client.send_message(message.channel,wikipedia.summary("{}".format(search), sentences=5))

    #Executes a python command unsafe for outside users to use
    elif message.content.startswith('!exec'):
        if message.author.id == client.user.id:
            exe = message.content[len('!exec'):].strip()
            msg = await client.send_message(message.channel,eval(exe))

    #Mutes a player by deleting their messages
    elif message.content.startswith('!nigger'):
        if checkid not in listVIP:
            await client.send_message(message.channel,"BOT: You do not have access to this command")
        else:
            muteid = message.content[len('!nigger'):].strip()
            for member in message.server.members:
                if member.id == muteid or member.mention == muteid:
                    namemen = member.mention
                    thaid = member.id
                    mutedList.append("{}".format(thaid))
                    await client.send_message(message.channel, "BOT: {} Has been caught and sold into slavery".format(namemen))


    #mock a user
    elif message.content.startswith("!mock"):
        if checkid not in listVIP:
            await client.send_message(message.channel, "BOT: No access")
        else:
            mockid = message.content[len("!mock"):].strip()
            for member in message.server.members:
                if member.id == mockid or member.mention == mockid:
                    namemen = member.mention
                    thaid = member.id
                    mockList.append("{}".format(thaid))
                    await client.send_message(message.channel, "BOT: {} Has been mocked".format(namemen))

    #unmocks a usser
    elif message.content.startswith("!unmock"):
        if checkid not in listVIP:
            await client.send_message(message.channel, "BOT: You do not have access to this command")
        else:
            unmockid = message.content[len('!unmock'):].strip()
            for member in message.server.members:
                if member.id == unmockid or member.mention == unmockid:
                    mockide = member.id
                    namemen = member.mention
                    if mockide not in mockList:
                        await client.send_message(message.channel, "BOT: This user is not mocked already")
                    else:
                        mockList.remove(mockide)
                        await client.send_message(message.channel, "BOT: {} has been freed".format(namemen))


    #Unmutes a player by removing them from the mute list
    elif message.content.startswith('!freenigger'):
        if checkid not in listVIP:
            await client.send_message(message.channel, "BOT: You do not have access to this command")
        else:
            unmuteid = message.content[len('!freenigger'):].strip()
            for member in message.server.members:
                if member.id == unmuteid or member.mention == unmuteid:
                    tid = member.id
                    namemen = member.mention
                    if tid not in mutedList:
                        await client.send_message(message.channel, "BOT: This user is not a nigger already")
                    else:
                        mutedList.remove(tid)
                        await client.send_message(message.channel, "BOT: {} has been freed".format(namemen))

    #adds a user to VIP
    elif message.content.startswith('!addvip'):
        if checkid in listVIP:
            vipid = message.content[len('!addvip'):].strip()
            #checks if the id is already a VIP
            if vipid in listVIP:
                await client.send_message(message.channel, "BOT: This user is already a VIP and you cannot add a user twice")
            else:
                listVIP.append("{}".format(vipid))
                for member in message.server.members:
                    if member.id == vipid:
                        vipmention = member.mention
                        await client.send_message(message.channel ,"BOT: {} has been made VIP and can use VIP commands".format(vipmention))
        else:
            await client.send_message(message.channel, "BOT: You do not have access to this command")

    #removes a vip
    elif message.content.startswith('!remvip'):
        if checkid in listVIP:
            vipid = message.content[len('!remvip'):].strip()
            #checks if the id is already a VIP
            if vipid not in listVIP:
                await client.send_message(message.channel, "BOT: This user is already not a VIP")
            else:
                listVIP.remove(vipid)
                for member in message.server.members:
                    if member.id == vipid:
                        vipmention = member.mention
                        await client.send_message(message.channel ,"BOT: {} has been removed from VIP".format(vipmention))
        else:
            await client.send_message(message.channel, "BOT: You do not have access to this command")

    elif message.content.startswith("!code"):
        if checkid in listVIP:
            nt = message.content[len('!code'):].strip()
            await client.delete_message(message)
            msg = await client.send_message(message.channel, "```{}```".format(nt))

    elif message.content.startswith("!lua"):
        if checkid in listVIP:
            nt = message.content[len('!lua'):].strip()
            await client.delete_message(message)
            msg = await client.send_message(message.channel, "```lua\n{}```".format(nt))
        
    elif message.content.startswith('!penis'):
        if checkid in listVIP:
            await client.delete_message(message)
            get_tagged = []
            for member in message.server.members:
                get_tagged.append(member.mention)
                chunks = [get_tagged[x:x+87] for x in range(0, len(get_tagged), 87)]
                for chunk in chunks:
                 msg = await client.send_message(message.channel," ".join(chunk))
                 await client.delete_message(msg)

    # makes a cow say something
    elif message.content.startswith("!cowsay"):
        if message.author.id == client.user.id:
            cowsay = message.content[len('!cowsay'):].strip()
            await client.delete_message(message)
            msg = await client.send_message(message.channel,
"""
```
______
< {} >
 ------
\    ^__^
  \  (oo)\____
    (__)\     )\/
        ||---w||
        ||    || Sir Loin```""".format(cowsay))
@client.event
async def on_ready():
  print('Logged in as: %s#%s' % (client.user.name, client.user.id))
#login information
if __name__ == '__main__':
    client.run(email, password)
