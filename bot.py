import discord
#import random
import os
from discord.ext import commands
import time
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def oyun(ctx):
    puan = 0
    await ctx.send('a')
    for i in range(2):
        if i == 0:
            await ctx.send('Soru 1:')
            await ctx.send('"Cam" şişeler toprakta kaç yılda çözünür?\n a)4000-4500\n b)5000-5500\n c)6000-6500')
            
            @bot.command()
            async def a(ctx):
                await ctx.send('Sence de 4000-4500 yıl yaşamak bir şişe için az değil mi?\n Fakat sen onu geri dönüştürerek "daha da çok" yaşamasını sağlayabilirsin! ')
                puan += 1
                i += 1

            @bot.command()
            async def b(ctx):
                await ctx.send('Malesef yanlış. Doğru vevap "A"ydı.\n Fakat sen onu geri dönüştürerek "daha da çok" yaşamasını sağlayabilirsin!')
                i += 1

            @bot.command()
            async def c(ctx):
                await ctx.send('Malesef yanlış. Doğru vevap "A"ydı.\n Fakat sen onu geri dönüştürerek "daha da çok" yaşamasını sağlayabilirsin!')  
                i += 1

        if i == 1:
            await ctx.send('Soru 1:')
            await ctx.send('"Pet" şişeler toprakta kaç yılda yok olur?\n d)500\n e)450\n f)700')
            
            @bot.command()
            async def d(ctx):
                await ctx.send('Malesef yanlış. Doğru vevap "B"ydi.\n Fakat sen onu geri dönüştürerek "daha da çok" yaşamasını sağlayabilirsin!')
                

            @bot.command()
            async def e(ctx, puan):
                await ctx.send('Sence de 450 yıl yaşamak bir şişe için az değil mi?\n Fakat sen onu geri dönüştürerek "daha da çok" yaşamasını sağlayabilirsin! ')
                puan += 1
                

            @bot.command()
            async def f(ctx):
                await ctx.send('Malesef yanlış. Doğru vevap "E"ydi.\n Fakat sen onu geri dönüştürerek "daha da çok" yaşamasını sağlayabilirsin!')
