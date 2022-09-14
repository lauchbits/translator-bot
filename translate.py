import discord, os
import googletrans
from discord import Option

bot = discord.Bot()
translator = googletrans.Translator()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(f"/translate | {len(bot.guilds)} servers"))
    print(f"Logged in as {bot.user}")

@bot.slash_command(name = "translate", description = "Translates text to your language")
async def help(ctx, text: Option(str, description = "What do you want to translate?", required = True), language: Option(str, description = "What language should your text be translated to?\nTo view languages use /language", required = False)):
    await ctx.channel.trigger_typing()

    if language:
        try:
            t = translator.translate(text, dest=language)
        except:
            try:
                await ctx.respond(f"**{language} is not a supported language!**\nUse /languages to view supported languages")
            except:
                await ctx.send(f"**{language} is not a supported language!**\nUse /languages to view supported languages")
    else:
        t = translator.translate(text)

    embed = discord.Embed(title = "Translator", color = discord.Color.blurple())
    embed.add_field(name = "Original", value = f"{t.origin}", inline = False)
    embed.add_field(name = "Translated", value = f"{t.text}", inline = False)
    try:
        await ctx.respond(embed=embed)
    except:
        await ctx.send(embed=embed)

@bot.slash_command(name = "languages", description = "Shows all available languages")
async def languages(ctx):
    await ctx.channel.trigger_typing()

    page = 1
    embed = discord.Embed(title = f"{page}/5", color = discord.Color.blurple())

    for key in googletrans.LANGUAGES:
        if (len(embed.fields) % 25 == 0 and len(embed.fields) != 0):
            try:
                await ctx.respond(embed=embed)
            except:
                await ctx.send(embed=embed)
            page += 1
            embed = discord.Embed(title = f"{page}/5", color = discord.Color.blurple())
        embed.add_field(name = key, value = googletrans.LANGUAGES[key].capitalize(), inline = True)
    try:
        await ctx.respond(embed=embed)
    except:
        await ctx.send(embed=embed)

bot.run(os.environ["DISCORD_TOKEN"])
#bot.run("MTAxOTIxMDExNTEzMzQ4OTE3Mg.GOPHUc.ZKS6Sd8bc0nGv4zFIOZDEUfJ8lE-XZk2zig1oI")