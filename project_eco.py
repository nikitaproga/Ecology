import discord
from random import choice
from time import sleep
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

bot_info = [
    "1. analyzer - говорит, как стоит переработать мусор. Пишите вид мусора, и бот вам ответит, что с ним делать",
    "2. advice - советы"
]

trash = {
    "Пищевой мусор": "Биоотходы - природа сама переработает",
    "Пластик": "Переработка",
    "Стекло": "Переработка",
    "Металл": "Переработка",
    "Бумага": "Переработка",
    "Батарейки": "Сдача в специализированные центры",
}

advice_info = [
    "1. Сократите потребление воды, например, закрывая кран во время чистки зубов или установив прерывистый душ.",
    "2. Используйте энергоэффективные лампы и приборы для экономии электроэнергии.",
    "3. Раздельно собирайте мусор для переработки, такой как пластик, стекло, бумага и металл.",
    "4. Избегайте использования одноразовых пластиковых изделий, таких как пластиковые стаканчики и пакеты.",
    "5. Приобретайте товары с минимальной упаковкой или вообще без нее.",
    "6. Переходите на утилизацию отходов, такую как компостирование, для снижения количества отходов, отправляемых на свалку.",
    "7. Разделяйте органические отходы и используйте их для создания удобрений для вашего сада или огорода.",
    "8. Путешествуйте на общественном транспорте, если это возможно, или велосипедом или пешком, чтобы снизить выбросы углекислого газа.",
]

img_info = [
    "https://risovach.ru/upload/2014/10/mem/master-joda_62672910_orig_.jpg",
    "https://i01.fotocdn.net/s128/0a5d30ad253159d2/public_pin_l/2900441237.jpg",
    "https://travel-dom.ru/wp-content/uploads/2020/05/PAafM4.jpg",
    "https://cdn.culture.ru/images/f714e0bf-2f6b-562b-bf4c-0708dfd346e5",
    "https://cdn.fishki.net/upload/users/2019/03/04/1530878/556d10956d8e7b5890e7affd42949a08.png"
]

@bot.command()
async def info_bot(ctx):
    await ctx.send("Ваш список комманд (перед началом пишите знак $):")
    for i in bot_info:
        await ctx.send(i)
        sleep(1)
    

@bot.command()
async def analyzer(ctx, trash_choice: str):
    if trash_choice in trash:
        await ctx.send(f"Вам следует сделать следующее: {trash[trash_choice]}")
    else:
        await ctx.send("Такого мусора у нас нет")

@bot.command()
async def advice(ctx):
    await ctx.send(f"Вот ваш совет: {choice(advice_info)}")

@bot.command()
async def img(ctx):
    await ctx.send(f"Вот ваш совет: {choice(img_info)}")

bot.run("") 