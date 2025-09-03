import discord
from discord.ext import commands
from config import TOKEN

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    """Bot başladığında çalışacak fonksiyon."""
    print(f'{bot.user} olarak giriş yapıldı.')
    print("MEG Software Support Destek Botu hazır!")

@bot.event
async def on_message(message):
    # Botun kendi mesajlarını yoksay
    if message.author == bot.user:
        return

# --- Komutlar ---
@bot.command()
async def destek(ctx):
    await ctx.send("Destek talebiniz alınmıştır. En kısa sürede size yardımcı olacağız.")

@bot.command()
async def iletisim(ctx):
    await ctx.send("Bizimle *themegsoftware@gmail.com* adresi üzerinden iletişime geçebilir veya Whatsapp işletme hesabımız olan *+90 532 236 90 39* numarasından mesaj yazabilirsiniz.\nBunun dışında Whatsapp'ta olan *MEG Software* adlı kanalımızdan belirli dillerle kodlama komutları öğrenip yararlanabilirsiniz.")

@bot.command()
async def hakkimizda(ctx):
    await ctx.send("MEG Software Support, size özel yazılım çözümleri sunan bir teknoloji firmasıdır.")

@bot.command()
async def katalog(ctx):
    await ctx.send("Ürün kataloğumuza bu adresten ulaşabilirsiniz: ")

@bot.command()
async def duyurular(ctx):
    await ctx.send("Güncel duyurular ve haberler için bizi Whatsapp kanalımızdan takip edebilirsiniz.")

@bot.command()
async def amac(ctx):
    await ctx.send("Bu bot, M.E.G. SOFTWARE ekibi tarafından müşterilerin destek süreçlerini kolaylaştırmak için geliştirilmiştir. Her gün daha da gelişmeye devam ediyor. 🚀")

@bot.command()
async def website(ctx):
    await ctx.send("Web sitemizi ziyaret edin: https://meg-software.wegic.app/\nAyrıca müşteri panelimize ulaşmak için bu adrese gidin: https://customer-dashboard-2.preview.emergentagent.com/")
# Botu çalıştır
bot.run(TOKEN)

