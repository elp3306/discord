import discord
import asyncio
import random
from random import *



client = discord.Client()



@client.event
async def on_ready():
     print(client.user.id)
     print('ready')
     game = discord.Game("걍있음")
     await client.change_presence(status=discord.Status.online, activity=game)
@client.event
async def on_message(message):
     if message.content.startswith('칠칠이취향'):
         i = randint(1, 15)

         await message.channel.send(file=discord.File('야짤 '+str(i)+'.jpg'))
     if message.content.startswith('남짤1'):
         await message.channel.send(file=discord.File('남자1.jpg'))
     if message.content.startswith('남짤2'):
         await message.channel.send(file=discord.File('남자2.jpg'))
     if message.content.startswith('남짤3'):
         await message.channel.send(file=discord.File('남자3.jpg'))
     if message.content.startswith('남짤4'):
         await message.channel.send(file=discord.File('남자4.jpg'))
     if message.content.startswith('칠칠님?'):
         await message.channel.send('안녕하십니까 탑게이 목욕탕총괄 박칠칠입니다 다름이아니라 탑게이 이용료를 납부하지않으시셔서 답변을드립니다 이용하신 5랄 서비스 60000원 바텀플레이 80000원 sm 플레이 70000만원으로 총 이용료는 21000원입니다. 납부 해주시길 바랍니다 ')
client.run("NzQ3MTM4NTc2NzAxMTk0MjUw.X0KhBQ.grD5lTT7ob50GYPQU_ru91GFQu4")
