import discord
from discord.ext import commands
from discord.ui import View, Button
import smtplib
from email.mime.text import MIMEText
from config import TOKEN, EMAIL, PASSWORD

intents = discord.Intents.all()
intents.messages = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# --- Mail gönderme fonksiyonu ---
def send_support_mail(username, user_id, user_email, user_message):
    subject = "Yeni Destek Talebi"
    body = f"Kullanıcı: {username} (ID: {user_id})\nE-mail: {user_email}\nMesaj: {user_message}"
    
    msg = MIMEText(body)
    msg["From"] = EMAIL
    msg["To"] = EMAIL
    msg["Subject"] = subject

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, EMAIL, msg.as_string())
        print("📩 Destek maili gönderildi.")
    except Exception as e:
        print(f"❌ Mail gönderilemedi: {e}")

# --- Komut butonları ---
komutlar = {
    "Destek (DM ile destek talebi başlatır)": "!destek",
    "İletişim (Mail ve telefon bilgilerini gösterir)": "!iletisim",
    "Hakkımızda (Firma hakkında bilgi verir)": "!hakkimizda",
    "Katalog (Excel dosyasını indirir)": "!katalog",
    "Duyurular (Yeni güncellemeleri gösterir)": "!duyurular",
    "Amaç (Firmamızın amacını gösterir)": "!amac",
    "Web Site (Resmi site ve müşteri paneli linklerini verir.)": "!website",
    "Menü (Menüyü gösterir.)": "!help"
}

class KomutView(View):
    def __init__(self):
        super().__init__(timeout=None)
        for label, custom_id in komutlar.items():
            self.add_item(Button(label=label, style=discord.ButtonStyle.primary, custom_id=custom_id))

class DownloadView(View):
    @discord.ui.button(label="İndir", style=discord.ButtonStyle.green)
    async def download_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        file = discord.File("ürünler.xlsx", filename="katalog.xlsx")
        await interaction.response.send_message("Excel dosyan hazır ⬇️", file=file, ephemeral=True)
        await interaction.channel.send(f"{interaction.user.mention} kataloğu indirdi.")

class WebsiteView(View):
    def __init__(self):
        super().__init__()
        self.add_item(Button(label="Resmi Web Sitesine Git", style=discord.ButtonStyle.link, url="https://meg-software.wegic.app"))

class CustomerPanelView(View):
    def __init__(self):
        super().__init__()
        self.add_item(Button(label="Müşteri Paneline Git", style=discord.ButtonStyle.link, url="https://customer-dashboard-2.preview.emergentagent.com/"))

# --- Destek DM flow ---
async def destek_flow(user, kanal=None):
    try:
        dm = await user.create_dm()
        await dm.send("Merhaba! Destek talebiniz için önce mail adresinizi girer misiniz?")
        def check_email(m):
            return m.author == user and isinstance(m.channel, discord.DMChannel)
        email_msg = await bot.wait_for("message", check=check_email, timeout=120)
        user_email = email_msg.content.strip()

        await dm.send("Şimdi destek mesajınızı yazabilirsiniz:")
        msg_msg = await bot.wait_for("message", check=check_email, timeout=300)
        user_message = msg_msg.content.strip()

        send_support_mail(user.name, user.id, user_email, user_message)
        await dm.send("✅ Destek talebiniz alınmıştır. Teşekkürler!")
        if kanal:
            await kanal.send(f"{user.mention} destek talebini gönderdi.")
    except Exception as e:
        print(f"Destek DM hatası: {e}")
        try:
            await user.send("❌ Bir hata oluştu. Lütfen tekrar deneyin.")
        except:
            pass

# --- On ready ---
@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yapıldı.")
    for guild in bot.guilds:
        if guild.text_channels:
            general = guild.text_channels[0]
            await general.send(
                "👋 Merhaba! Ben M.E.G. Software destek botuyum.\n"
                "Menüyü görmek için !help yazabilirsiniz veya aşağıdaki butonları kullanabilirsiniz."
            )
    try:
        await bot.tree.sync()
        print("Slash komutları senkronize edildi.")
    except Exception as e:
        print(f"Hata: {e}")

# --- Prefix komutları ---
@bot.command(name="yardim")
async def yardim_prefix(ctx):
    help_message = (
        "**📋 Kullanabileceğiniz Komutlar:**\n"
        "1️⃣ !destek\n"
        "2️⃣ !iletisim\n"
        "3️⃣ !hakkimizda\n"
        "4️⃣ !katalog\n"
        "5️⃣ !duyurular\n"
        "6️⃣ !amac\n"
        "7️⃣ !website\n"
    )
    view = KomutView()
    manuel_mesaj = "💡 Komutları manuel girmek isterseniz:\n" + "\n".join(komutlar.values())
    await ctx.send("📋 Tüm komutlar aşağıda:", view=view)
    await ctx.send(manuel_mesaj)

@bot.command(name="destek")
async def destek_prefix(ctx):
    await ctx.send("📩 Size DM üzerinden destek talebi başlatıldı.")
    await destek_flow(ctx.author, ctx.channel)

@bot.command(name="iletisim")
async def iletisim_prefix(ctx):
    await ctx.send("📧 themegsoftware@gmail.com\n📱 +90 532 236 90 39")

@bot.command(name="hakkimizda")
async def hakkimizda_prefix(ctx):
    mesaj = "ℹ️ M.E.G. SOFTWARE, yenilikçi yazılım çözümleri üreten genç ve dinamik bir ekiptir.💻 🚀 Amacımız; bireylerin ve işletmelerin hayatını kolaylaştıracak, güvenilir, modern ve kullanıcı dostu yazılımlar geliştirmektir. 🌍 Teknolojiye olan tutkumuzla her projede kaliteyi ön planda tutuyor, öğrenmeye ve gelişmeye sürekli devam ediyoruz. 📈 Geleceği kodluyor, hayalleri gerçeğe dönüştürüyoruz. ✨"
    await ctx.send(mesaj)

@bot.command(name="katalog")
async def excel(ctx):
    await ctx.send("Kataloğumuzun Excel dosyasını indirmek için butona bas:", view=DownloadView())

@bot.command(name="duyurular")
async def duyurular(ctx):
    await ctx.send("📢 Discord botumuz güncellendi! Yeni özellikler eklendi. Daha fazlası için '!yardim'")

@bot.command(name="amac")
async def amac(ctx):
    await ctx.send("🚀 Amacımız; bireylerimizin ve her türlü işletmenin hayatını kolaylaştırıp, güvenilir, modern ve kullanıcı dostu yazılımlar geliştirmektir.")

@bot.command(name="website")
async def website(ctx):
    await ctx.send("🌐 Resmi Web sitemiz: https://meg-software.wegic.app", view=WebsiteView())
    await ctx.send("🌐 Müşteri Panelimiz: https://customer-dashboard-2.preview.emergentagent.com/", view=CustomerPanelView())

# --- On message: manuel komut ve geçersiz komut ---
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    valid_commands = list(komutlar.values())

    if message.content.strip() == "!help":
        view = KomutView()
        manuel_mesaj = "💡 Komutları manuel girmek isterseniz:\n" + "\n".join(valid_commands)
        await message.channel.send("📋 Tüm komutlar aşağıda:", view=view)
        await message.channel.send(manuel_mesaj)
    
    elif message.content.startswith("!") and message.content.strip() not in valid_commands:
        view = KomutView()
        manuel_mesaj = "💡 Komutları manuel girmek isterseniz:\n" + "\n".join(valid_commands)
        await message.channel.send(
            "⚠️ Geçersiz komut, lütfen menüden bir butona tıklayın veya manuel komutları kullanın.",
            view=view
        )
        await message.channel.send(manuel_mesaj)

    await bot.process_commands(message)

# --- On interaction: buton click ---
@bot.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.type == discord.InteractionType.component:
        komut = interaction.data.get("custom_id")

        if komut == "!destek":
            await interaction.response.defer(ephemeral=True)
            await interaction.followup.send("📩 Size DM üzerinden destek talebi başlatıldı.", ephemeral=True)
            await destek_flow(interaction.user)

        elif komut == "!iletisim":
            await interaction.response.defer(ephemeral=True)
            await interaction.followup.send("📧 themegsoftware@gmail.com\n📱 +90 532 236 90 39", ephemeral=True)

        elif komut == "!hakkimizda":
            await interaction.response.defer(ephemeral=True)
            await interaction.followup.send(
                "ℹ️ M.E.G. SOFTWARE, yenilikçi yazılım çözümleri üreten genç ve dinamik bir ekiptir.💻 🚀 Amacımız; bireylerin ve işletmelerin hayatını kolaylaştıracak, güvenilir, modern ve kullanıcı dostu yazılımlar geliştirmektir. 🌍 Teknolojiye olan tutkumuzla her projede kaliteyi ön planda tutuyor, öğrenmeye ve gelişmeye sürekli devam ediyoruz. 📈 Geleceği kodluyor, hayalleri gerçeğe dönüştürüyoruz. ✨",
                ephemeral=True
            )

        elif komut == "!katalog":
            await interaction.response.defer(ephemeral=True)
            view = DownloadView()
            await interaction.followup.send("Kataloğumuzun Excel dosyasını indirmek için butona bas:", view=view, ephemeral=True)

        elif komut == "!duyurular":
            await interaction.response.defer(ephemeral=True)
            await interaction.followup.send("📢 Discord botumuz güncellendi! Yeni özellikler eklendi. Daha fazlası için '!yardim'", ephemeral=True)

        elif komut == "!amac":
            await interaction.response.defer(ephemeral=True)
            await interaction.followup.send("🚀 Amacımız; bireylerimizin ve her türlü işletmenin hayatını kolaylaştırıp, güvenilir, modern ve kullanıcı dostu yazılımlar geliştirmektir.", ephemeral=True)

        elif komut == "!website":
            await interaction.response.defer(ephemeral=True)
            await interaction.followup.send(
                "🌐 Resmi Web sitemiz: https://meg-software.netlify.app\n🌐 Müşteri Panelimiz: https://customer-dashboard-2.preview.emergentagent.com/",
                ephemeral=True
            )

bot.run(TOKEN)
