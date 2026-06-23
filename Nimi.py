#Nimi bot - Feito por Felipe Carneiro
import discord
#Deixar python como global ao executar para funcionar
from settings import settings
import time
import functions #Você viu que daora

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'konbakuwa! ⸜( *ˊ ᵕ ˋ* )⸝, {client.user}')


@client.event
async def on_message(message):
    print(f"|{functions.tempo()}| {message.guild.id}, {message.channel.id} = {message.channel}, {message.author.id} = {message.author}, {message.content}")
    mens = f"|{functions.tempo()}| {message.guild.id}, {message.channel.id} = {message.channel}, {message.author.id} = {message.author}, {message.content}\n"
    functions.log(mens)
    if message.author.bot:
        return 
    
    if message.content.lower().startswith("nimi") or message.content.lower().startswith(">nimi"): 
        await message.channel.send(functions.mens(settings["saudacao"]))
        
    #-x-x-x-x-x-x-x-
    #>senha
    if message.content.startswith(">senha"):
        try:
            pass_length = int(message.content.split(" ", maxsplit=1)[1])#Olha que daora, você sabia disso?
        except (ValueError, IndexError):
            await message.channel.send(functions.mens("Por favor, digite um número válido após 'senha'."))
            return
        password = functions.senha(pass_length)
        await message.channel.send(functions.mens(f"Senha gerada: {password}"))

    #-x-x-x-x-x-x-x-
    #>hora
    if message.content.startswith(">hora"):
        current_time = functions.tempo()
        await message.channel.send(functions.mens(f"Hora atual: {current_time}"))
        if current_time >= "12:00:00" and current_time <= "18:00:00":
            await message.channel.send(functions.mens("Boa tarde!"))
        elif current_time >= "00:00:00" and current_time <= "12:00:00":
            await message.channel.send(functions.mens("Bom dia!"))
        elif current_time >= "18:00:00" and current_time <= "23:59:59":
            await message.channel.send(functions.mens("Boa noite!"))
            
    #-x-x-x-x-x-x-x-
    #>moeda
    if message.content.startswith(">moeda"):
        lado = message.content.split(" ", maxsplit=1)[1] if len(message.content.split(" ", maxsplit=1)) > 1 else None
        if lado:
            result = functions.moeda()
            await message.channel.send(functions.mens(f"Você escolheu: {lado}"))
            time.sleep(1) #Dá um suspense
            await message.channel.send(functions.mens(f"Resultado: {result}"))
            await message.channel.send(functions.mens("Parabéns, você ganhou!" if lado.lower() == result.lower() else "você perdeu!"))
        else:
            await message.channel.send(functions.mens("Estrutura correta: '>moeda <cara/coroa>'"))
    
    #-x-x-x-x-x-x-x-
    #>voz
    if message.content.startswith(">voz"):
        file = discord.File("Som/Nimi.mp3", filename="Nimi.mp3")
        await message.channel.send(file=file)

    #-x-x-x-x-x-x-x- 
    #>imagem
    if message.content.startswith(">imagem"):
        file = discord.File("Image/Smug.png", filename="Smug.png")
        await message.channel.send(file=file)

    #-x-x-x-x-x-x-x-
    #>poke
    if message.content.startswith(">poke"):
        try:
            pokemon = message.content.split(" ", maxsplit=1)[1]
            data = functions.poke(pokemon)
            if data:
                #embed é um tipo de mensagem mais bonita, com título, campos, imagens e etc
                embed = discord.Embed(title=f"{data['name'].title()} (ID: {data['id']})", color=discord.Color.red())
                embed.set_thumbnail(url=data['imagem'])
                embed.add_field(name="Tipo", value=data['type'].title(), inline=True)
                embed.add_field(name="Habilidade", value=data['ability'].title(), inline=True)
                embed.add_field(name="Altura", value=f"{data['height']} cm", inline=True)
                embed.add_field(name="Peso", value=f"{data['weight']} Kg", inline=True)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send(functions.mens("Pokémon não encontrado. Verifique o nome ou número e tente novamente."))
        
        except IndexError:
            await message.channel.send(functions.mens("Digite o nome do pokemon depois do comando: '>poke <nome/número>'"))
            return
        
client.run(settings["TOKEN"])
