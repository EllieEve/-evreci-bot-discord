import discord
from discord.ext import commands
import random
import os

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
# client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık.')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command()
async def mem(ctx):
    file_list = os.listdir('C:/Users/omerg/OneDrive/Masaüstü/kodland/images/') # Dosya adlarını saklayan değişken 
    img_name = random.choice(file_list) # Liste içinden rastgele bir dosya seç
    with open(f'C:/Users/omerg/OneDrive/Masaüstü/kodland/images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)







@bot.command()
async def geri_donusum(ctx, atik_turu = None):
    if atik_turu is None:
        await ctx.send('Lütfen bir atık türü belirtin.')
    
    elif atik_turu.lower() == ("kağıt"):
        await ctx.send("Bu bir geri dönüştürülebilir kağıta atıktır.")

    elif atik_turu.lower() == ("pet şişe, poşet"):
        await ctx.send("Bu geri dönüştürülebilir bir plastik atıktır.")

    elif atik_turu.lower() == ("cam şişe, cam, ayna"):
        await ctx.send("Bu geri dönüştürülebilir bir cam atıktır.")

    elif atik_turu.lower() == ("metal şişe, teneke kutu, teneke, metal, kutu kola"):
        await ctx.send("Bu geri dönüştürülebilir bir metal atıktır.")

    else:
        await ctx.send("Bu geri dönüştürülemez bir atıktır.")



@bot.command()
async def fikir(ctx):
    fikirler = ["Arkası dolu kağıtların ön yüzünü kullanın.",
     "Pet şişelerden kuş yemliği yapın.", 
     "Atık kumaşlardan çanta ve cüzdan yapın.", "Atık kartonardan kalemlik yapın.", "Atık kıyafetleri ihtiyaç sahiplerine bağışlayın."]
    fikirlerim = random.choice (fikirler)
    await ctx.send(f"İşte fikirler {fikirlerim}")



bot.run("")
