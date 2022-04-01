import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    command_list=[]
    white_list={'hello':'hello','socials':'https://t.me/sobkeno','Litcode':'https://leetcode.com/ShOotNik/','git':'https://github.com/TheBeStN1ckname','youtube':'https://www.youtube.com/watch?v=zY7yvZcZIoE&list=PLk2cp6C24PxsJRtjGXSlTry231e3bCr2m&index=86'}

    if message.content in white_list:
        await message.channel.send(white_list[message.content])
    else:
        await message.channel.send('avaliable comands :'+str(white_list.keys())[11:-2:])
     








client.run('OTU1NTcxMzk2MDE5Mzc2MTQ4.YjjnNg.wzsFShIbOTMKn--1g0mfaylcUZU')