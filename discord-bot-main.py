import discord
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_mesage(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client=MyClient()
client.run('your-bot-token')
