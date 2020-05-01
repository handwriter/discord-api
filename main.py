import discord
import requests
from auth import TOKEN


class DogsAndCats(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})\n'
                f'Гтов показать случайного кота или пса')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if "собак" in message.content.lower() or "собач" in message.content.lower():
            response = requests.get("https://dog.ceo/api/breeds/image/random").json()
            while not response['status'] == 'success':
                response = requests.get("https://dog.ceo/api/breeds/image/random").json()
            await message.channel.send(response['message'])
        elif "кот" in message.content.lower():
            response = requests.get("https://api.thecatapi.com/v1/images/search").json()[0]
            await message.channel.send(response['url'])


client = DogsAndCats()
client.run(TOKEN)