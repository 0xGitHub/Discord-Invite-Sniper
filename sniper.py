# Discord Invite Sniper
# Made By Syntax
# Twitter: @CockSlime
# Github: https://github.com/cannabispowered

# Tested on Python 3.6.8
# With Discord API Version 1.2.5

import discord
import requests
from colorama import *

client = discord.Client()

# Define 'on_ready' messages
@client.event
async def on_ready():
        print('Logged in as:', client.user.name+"#"+client.user.discriminator)
        print('UID:', client.user.id)
        print('Discord version:', discord.__version__)
        print('Written by Syntax')
        print('Github: https://github.com/cannabispowered')

token = "" # Enter Your Token Here

# Define sniper
@client.event
async def on_message(message):
        if message.content.find("discord.gg") != -1:
                header_payload = {
                        'Authorization' : token,
                        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
                }
                        
                r = requests.get('https://discord.com/')
                cookie_payload = {
                        '__cfduid' : r.cookies['__cfduid'],
                }
                
                discordmsg = message.content
                invitecode = discordmsg.split(".gg/")
                code = invitecode[1]
                response = requests.post(f'https://discordapp.com/api/v6/invites/{code}', headers=header_payload, cookies=cookie_payload, data={})
                responsedata = response.text
                
                if 'banned' in responsedata:
                        print(Fore.RED+f"[!] User is banned from this server! | Code: {code} | Posted In '{message.guild}'")
                elif 'Maximum' in responsedata:
                        print(Fore.YELLOW+f"[-] Maximum Number Of Servers Reached (100)! | Code: {code} | Posted In '{message.guild}'")
                elif code in responsedata:
                        print(Fore.GREEN+f"[+] Server Successfully Joined! | Code: {code} | Posted In '{message.guild}'")
                else:
                        print(Fore.RED+f"[!] Unhandled Exception! - Try manually forging the request and checking the response!")

client.run(token, bot=False)
