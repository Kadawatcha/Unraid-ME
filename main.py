import discord
from discord.ext import commands
import os

# TOKEN = "VOTRE_TOKEN_ICI"
TOKEN = ""

intents = discord.Intents.all()


bot = commands.Bot(command_prefix='!', intents=intents)



@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}')
    print(f'ID du bot : {bot.user.id}')
    print('Le bot est prêt !')
    print('------')


@bot.command(name='unraid', help='Supprime les salons nommés "raid".')
 # ATTENTION TOUT LE MDE PEUT UTILISER CETTE COMMANDE !!
 # a rajouter pour restrindre la cmd aux admin 
# @commands.has_permissions(administrator=True)
async def unraid(ctx: commands.Context):
    """
    Parcourt tous les salons du serveur et supprime ceux qui s'appellent 'raid'.
    """

    await ctx.typing()

    guild = ctx.guild
    deleted_channels = []
    failed_channels = []
    
    # On parcourt une copie de la liste des salons, car on ne peut pas modifier une liste pendant qu'on l'itère
    for channel in list(guild.channels):

        if channel.name.lower() == 'fermeture-blvd-soda': # remplacer par le nom du salon raid 
            try:
                await channel.delete(reason=f"Commande !unraid exécutée par {ctx.author}")
                deleted_channels.append(channel.name)
            except discord.Forbidden:
                failed_channels.append(f"'{channel.name}' (Permission refusée)")
            except discord.HTTPException as e:
                failed_channels.append(f"'{channel.name}' (Erreur: {e})")
    
   
    report = f"✅ **Rapport de la commande `!unraid`**\n\n"
    report += f"🗑️ **{len(deleted_channels)} salon(s) supprimé(s) avec succès.**\n"
    if failed_channels:
        report += f"❌ **{len(failed_channels)} échec(s) lors de la suppression :**\n" + "\n".join(f"- {error}" for error in failed_channels)
    
    # On envoie le rapport en message privé pour la discrétion
    try:
        await ctx.author.send(report)
        await ctx.reply("Rapport envoyé en message privé.", delete_after=10)
    except discord.Forbidden:
        # Si l'utilisateur bloque les MPs du bot
        await ctx.reply("Je n'ai pas pu vous envoyer le rapport en message privé. Avez-vous bloqué les messages de bots ?", delete_after=20)

@bot.command(name='ping', help='Affiche la latence du bot.')
async def ping(ctx: commands.Context):

    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong ! Ma latence est de {latency}ms.')


# --- DÉMARRAGE DU BOT ---

# 5. Lancer le bot avec votre token
if TOKEN is None:
    print("Erreur : Le token du bot n'est pas trouvé.")
    print("Assurez-vous d'avoir défini la variable d'environnement DISCORD_TOKEN.")
else:
    try:
        bot.run(TOKEN)
    except discord.errors.LoginFailure:
        print("Erreur : Le token fourni est invalide.")
