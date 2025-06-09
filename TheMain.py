# SPDX-FileCopyrightText: © 2025 ItzDavid And Cr33pkill
# SPDX-License-Identifier: MIT
# SPDX-License-Identifier: PSF-2.0
#
# TheMain.py
#
# Copyright (C) ItzDavid And Cr33pkill, all rights reserved.
# This code is dual-licensed under MIT License and
# Python Software Foundation License 2.0
#
# If used in whole or in part under the MIT License
# the Copyright notice must be retained.
#
# © ItzDavid And Cr33dev 2025
# This is the main file for the Syntheia bot
# imports all the libraries used in the bot
from datetime import datetime
import os
import discord
from discord import app_commands
from discord.ext import commands
import random
import time

def exit_program():
    print("  █████████  █████                  █████     █████     ███                     ")
    time.sleep(0.1)
    print(" ███░░░░░███░░███                  ░░███     ░░███     ░░░                      ")
    time.sleep(0.1)
    print("░███    ░░░  ░███████   █████ ████ ███████   ███████   ████  ████████    ███████")
    time.sleep(0.1)
    print("░░█████████  ░███░░███ ░░███ ░███ ░░░███░   ░░░███░   ░░███ ░░███░░███  ███░░███")
    time.sleep(0.1)
    print(" ░░░░░░░░███ ░███ ░███  ░███ ░███   ░███      ░███     ░███  ░███ ░███ ░███ ░███")
    time.sleep(0.1)
    print(" ███    ░███ ░███ ░███  ░███ ░███   ░███ ███  ░███ ███ ░███  ░███ ░███ ░███ ░███")
    time.sleep(0.1)
    print("░░█████████  ████ █████ ░░████████  ░░█████   ░░█████  █████ ████ █████░░███████")
    time.sleep(0.1)
    print(" ░░░░░░░░░  ░░░░ ░░░░░   ░░░░░░░░    ░░░░░     ░░░░░  ░░░░░ ░░░░ ░░░░░  ░░░░░███")
    time.sleep(0.1)
    print("                                                                        ███ ░███")
    time.sleep(0.1)
    print("                                                                       ░░██████ ")
    time.sleep(0.1)
    print("                                                                        ░░░░░░  ")
    time.sleep(0.1)
    print("")
    time.sleep(0.1)
    print("")
    time.sleep(0.1)
    print("▓█████▄  ▒█████   █     █░███▄    █ ")
    time.sleep(0.1)
    print("▒██▀ ██▌▒██▒  ██▒▓█░ █ ░█░██ ▀█   █ ")
    time.sleep(0.1)
    print("░██   █▌▒██░  ██▒▒█░ █ ░█▓██  ▀█ ██▒")
    time.sleep(0.1)
    print("░▓█▄   ▌▒██   ██░░█░ █ ░█▓██▒  ▐▌██▒")
    time.sleep(0.1)
    print("░▒████▓ ░ ████▓▒░░░██▒██▓▒██░   ▓██░")
    time.sleep(0.1)
    print(" ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒ ░ ▒░   ▒ ▒ ")
    time.sleep(0.1)
    print(" ░ ▒  ▒   ░ ▒ ▒░   ▒ ░ ░ ░ ░░   ░ ▒░")
    time.sleep(0.1)
    print(" ░ ░  ░ ░ ░ ░ ▒    ░   ░    ░   ░ ░ ")
    time.sleep(0.1)
    print("   ░        ░ ░      ░            ░ ")
    time.sleep(0.1)
    print(" ░                                  ")
    for i in range(30):
        print("")
        time.sleep(0.1)
    SystemExit()

try:
    import dotenvloader
except ModuleNotFoundError:
    print("dotenvloader.py not found!")
    current_directory = os.path.dirname(os.path.abspath(__file__))
    print(f"Download dotenvloader.py from https://github.com/Cr33pkill/Holobyte-Syntheia-Discord-Bot and place it in {current_directory}")
    print("Start the program again")
    exit_program()
try:
    from dotenvloader import dotenv_load, dotenv_find
except ImportError:
    print("ERROR: dotenvloader.py has been modified or is incompatible.")
    print("Please replace it with the original at https://github.com/Cr33pkill/Holobyte-Syntheia-Discord-Bot .")
    exit_program()

def dotenv_orders():
    dotenv_path = dotenv_find()
    var_data_list = dotenv_load(dotenv_path)
    return var_data_list

var_data_list = dotenv_orders()
TOKEN = var_data_list[0]
GUILD = var_data_list[1]
GUILD = int(GUILD)
+

CHANNEL_ID = var_data_list[2]
OWNER1 = var_data_list[3]
OWNER2 = var_data_list[4]

# Creates the bot itself 'Client' and does the startup sequence
class Client(commands.Bot):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        try:
            GFC = discord.Object(id=GUILD)
            synced = await self.tree.sync(guild=GFC)  # Syncs commands
            print(f"Synced {len(synced)} commands to guild {GFC}")
            channel = self.get_channel(CHANNEL_ID)  # Get the channel object
            if channel is not None:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                DTM = f"Python script online, current time: {current_time}"  # Combine the message and time
                CCM = f"Synced {len(synced)} commands to guild ID:{GUILD}"
                await channel.send(DTM)
                await channel.send(CCM)
            else:
                print(f"Channel with ID {CHANNEL_ID} not found.") # says the channel can not be found
        except Exception as e:
            print(f"Error during on_ready: {e}") # gives an error and shows it

# sets the intents for the bot
intents = discord.Intents.default()
intents.message_content = True

# admin check
def is_admin(interaction: discord.Interaction) -> bool:
    if interaction.user.guild_permissions.administrator:
        return True
    raise app_commands.MissingPermissions(["administrator"])

'''the command_prefix is useless as discord doesn't use
it anymore but its still needed to work for some fricking reason'''
client = Client(command_prefix="!",intents=intents)

# puts the guild id into a discord.object, needed to make commands only work in 1 server 
GFC = discord.Object(id=GUILD)

# Admin commands
@client.tree.command(name="shutdown", description="Stops the bot from running", guild=GFC)
@app_commands.check(is_admin)
async def logout(ctx: discord.Interaction):
    print("Responding with 'Logged Out'")
    await ctx.response.send_message("Logged Out",ephemeral=True)
    client.close()
    exit_program()

@client.tree.command(name="kick",description="kicks members",guild=GFC)
@app_commands.describe(member="The member to kick", reason="The reason they are being kicked")
@app_commands.check(is_admin)
async def kick(interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
    if member == interaction.user:
        await interaction.response.send_message("you cannot kick yourself", ephemeral=True)
        return
    if member.guild_permissions.administrator:
        await interaction.response.send_message("You cannot kick an administrator",ephemeral=True)

    try:
        await member.kick(reason=f"kicked by {interaction.user}: {reason}")
        await interaction.response.send_message(f"Successfully kicked {member.mention} for: {reason}")
    except discord.Forbidden:
        await interaction.response.send_message("I don't have permission to kick this user.", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"An error occurred: {e}", ephemeral=True)
        print(f"An error occured: {e}")

# these are all silly /commands
@client.tree.command(name="hello",description="Says Hello!",guild=GFC)
async def SayHello(interaction: discord.Interaction):
    print("responding with 'HEY IM Syntheia!'")
    await interaction.response.send_message("HEY IM Syntheia!")

@client.tree.command(name="random",description="Gives a random number! between 1 and 100",guild=GFC)
async def SayHello(interaction: discord.Interaction):
    ran_num = random.randint(1,100)
    print(f"responding with '{ran_num}'")
    await interaction.response.send_message(f"{ran_num}")

@client.tree.command(name="owners",description="Lists owners",guild=GFC)
async def SayHello(interaction: discord.Interaction):
    print("responding with 'My owners are ItzDavid and Cr33pkill'")
    await interaction.response.send_message("My owners are ItzDavid and Cr33pkill")

@client.tree.command(name="kanye",description="lol",guild=GFC)
async def SayHello(interaction: discord.Interaction):
    print("responding with 'Wake up Mr. West!'")
    await interaction.response.send_message("wake up Mr. West!")

@client.tree.command(name="party",description="🤨",guild=GFC)
async def SP(interaction: discord.Interaction):
    print("responding with 'There ain't no party like a Sigma party :3'")
    await interaction.response.send_message("There ain't no party like a Sigma party :3")
    
@client.tree.command(name="miku",description="IM THINKING MIKU MIKU OO-EE-OO",guild=GFC)
async def singtime(interaction: discord.Interaction):
    miku_lyrics = """OMG ITS MY FAVOURITE SONGGGG!!!
I'M THINKING MIKU, MIKU, OO-EE-OO  
I'M THINKING MIKU, MIKU, OO-EE-OO  
I'M THINKING MIKU, MIKU, OO-EE-OO  
I'M THINKING MIKU, MIKU, OO-EE-OO"""
    print(f"responding with'{miku_lyrics}'")
    await interaction.response.send_message(miku_lyrics)

@client.tree.command(name="insultme",description="Get insulted by Synthia",guild=GFC)
async def insultme(interaction: discord.Interaction):
    rareinsult = random.randint(1,1000)
    if rareinsult == 69:
        Insult = "You are silly"
    else:
        Insult_Choice = random.randint(1,10)
        if Insult_Choice == 1:
            Insult = "Frick u"
        if Insult_Choice == 2:
            Insult = " I hope both sides of the pillow are warm tonight"
        if Insult_Choice == 3:
            Insult = "You are not sigma"
        if Insult_Choice == 4:
            Insult = "You are a default person"
        if Insult_Choice == 5:
            Insult = "I hates you"
        if Insult_Choice == 6:
            Insult = "You are shaped like a leek"
        if Insult_Choice == 7:
            Insult = "You look like piccolo"
        if Insult_Choice == 8:
            Insult = "You are a silly gooner"
        if Insult_Choice == 9:
            Insult = "No Sigmas"
        if Insult_Choice == 10:
            Insult = "No la passion"
    print(f"responding with'{Insult}'")
    await interaction.response.send_message(Insult)

# This pings the latency to check the delay between the bot and the console
@client.tree.command(name="ping", description="latency check",guild=GFC)
async def ping(interaction: discord.Interaction):
    latency = round(client.latency * 1000) # gets the ping and multiplies it by 1000 so its easier to read
    LMSG = f"Pong!! Latency = {latency}ms"
    print(f"Responding with '{LMSG}'")
    await interaction.response.send_message(LMSG,ephemeral=True)

@client.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message(
            "You do not have the required permissions to use this command.",
            ephemeral=True
        )
    elif isinstance(error, app_commands.CommandNotFound):
        await interaction.response.send_message(
            "This command does not exist.", ephemeral=True
        )
    else:
        await interaction.response.send_message(
            "An unexpected error occurred. Please contact the bot administrator.",
            ephemeral=True
        )

def intro():
    for i in range(40):
        print("")
        time.sleep(0.1)
    print(" █████   ███   █████          ████                                            ")
    time.sleep(0.1)
    time.sleep(0.1)
    print("░░███   ░███  ░░███          ░░███                                            ")
    time.sleep(0.1)
    print(" ░███   ░███   ░███   ██████  ░███   ██████   ██████  █████████████    ██████ ")
    time.sleep(0.1)
    print(" ░███   ░███   ░███  ███░░███ ░███  ███░░███ ███░░███░░███░░███░░███  ███░░███")
    time.sleep(0.1)
    print(" ░░███  █████  ███  ░███████  ░███ ░███ ░░░ ░███ ░███ ░███ ░███ ░███ ░███████ ")
    time.sleep(0.1)
    print("  ░░░█████░█████░   ░███░░░   ░███ ░███  ███░███ ░███ ░███ ░███ ░███ ░███░░░  ")
    time.sleep(0.1)
    print("    ░░███ ░░███     ░░██████  █████░░██████ ░░██████  █████░███ █████░░██████ ")
    time.sleep(0.1)
    print("     ░░░   ░░░       ░░░░░░  ░░░░░  ░░░░░░   ░░░░░░  ░░░░░ ░░░ ░░░░░  ░░░░░░  ")
    for i in range(5):
        print("")
        time.sleep(0.1)
    print(" █████               ████           █████                 █████            ")
    time.sleep(0.1)
    print("░░███               ░░███          ░░███                 ░░███             ")
    time.sleep(0.1)
    print(" ░███████    ██████  ░███   ██████  ░███████  █████ ████ ███████    ██████ ")
    time.sleep(0.1)
    print(" ░███░░███  ███░░███ ░███  ███░░███ ░███░░███░░███ ░███ ░░░███░    ███░░███")
    time.sleep(0.1)
    print(" ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███   ░███    ░███████ ")
    time.sleep(0.1)
    print(" ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███ ░███   ░███ ███░███░░░  ")
    time.sleep(0.1)
    print(" ████ █████░░██████  █████░░██████  ████████  ░░███████   ░░█████ ░░██████ ")
    time.sleep(0.1)
    print("░░░░ ░░░░░  ░░░░░░  ░░░░░  ░░░░░░  ░░░░░░░░    ░░░░░███    ░░░░░   ░░░░░░  ")
    time.sleep(0.1)
    print("                                               ███ ░███                    ")
    time.sleep(0.1)
    print("                                              ░░██████                     ")
    time.sleep(0.1)
    print("                                               ░░░░░░                      ")
    for i in range(2):
        print("")
        time.sleep(0.1)
    print("  █████████                         █████    █████                ███               ")
    time.sleep(0.1)
    print(" ███░░░░░███                       ░░███    ░░███                ░░░                ")
    time.sleep(0.1)
    print("░███    ░░░  █████ ████ ████████   ███████   ░███████    ██████  ████   ██████      ")
    time.sleep(0.1)
    print("░░█████████ ░░███ ░███ ░░███░░███ ░░░███░    ░███░░███  ███░░███░░███  ░░░░░███     ")   
    time.sleep(0.1)
    print(" ░░░░░░░░███ ░███ ░███  ░███ ░███   ░███     ░███ ░███ ░███████  ░███   ███████     ")
    time.sleep(0.1)
    print(" ███    ░███ ░███ ░███  ░███ ░███   ░███ ███ ░███ ░███ ░███░░░   ░███  ███░░███     ")
    time.sleep(0.1)
    print("░░█████████  ░░███████  ████ █████  ░░█████  ████ █████░░██████  █████░░████████    ")
    time.sleep(0.1)
    print(" ░░░░░░░░░    ░░░░░███ ░░░░ ░░░░░    ░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░  ░░░░░░░░     ")
    time.sleep(0.1)
    print("              ███ ░███       Cr33pkill, ItzDavid                                    ")
    time.sleep(0.1)
    print("             ░░██████                                                               ")
    time.sleep(0.1)
    print("              ░░░░░░                                                                ")                                                       
    for i in range(30):
        print("")
        time.sleep(0.1)
intro()
client.run(TOKEN)
