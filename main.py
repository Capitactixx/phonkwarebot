import discord
from discord.ext import commands
import os
import traceback
from dotenv import load_dotenv

load_dotenv()

# ═══════════════════════════════════════
#  Phonkware-bot
#  Color: #E0508A
# ═══════════════════════════════════════

EMBED_COLOR = 0xE0508A

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    print("❌ ERROR: TOKEN not found in .env", flush=True)
    sys.exit(1)

print(f"✅ Token loaded ({TOKEN[:10]}...)", flush=True)
print(f"✅ Python {sys.version}", flush=True)
print(f"✅ Py-cord {discord.__version__}", flush=True)

bot = commands.Bot(
    command_prefix="!",
    intents=discord.Intents.all(),
    activity=discord.Activity(
        type=discord.ActivityType.watching,
        name="Phonkware"
    )
)

# ── Load cogs ──
COGS = [
    "cogs.verification",
    "cogs.giveaways",
    "cogs.tickets",
    "cogs.moderation",
    "cogs.automod",
    "cogs.status",
]

for cog in COGS:
    try:
        bot.load_extension(cog)
        print(f"  ✅ {cog}", flush=True)
    except Exception as e:
        print(f"  ❌ {cog}: {e}", flush=True)
        traceback.print_exc()

@bot.event
async def on_ready():
    print(f"═══════════════════════════════════", flush=True)
    print(f"  Phonkware-bot online", flush=True)
    print(f"  Logged as {bot.user}", flush=True)
    print(f"  Servers: {len(bot.guilds)}", flush=True)
    print(f"═══════════════════════════════════", flush=True)

try:
    print("🚀 Starting bot...", flush=True)
    bot.run(TOKEN)
except Exception as e:
    print(f"❌ FATAL: {e}", flush=True)
    traceback.print_exc()
