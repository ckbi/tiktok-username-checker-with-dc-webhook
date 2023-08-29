import os
from colorama import Fore, Back, Style, init
import json
import string
from os import system, name

try:
    import requests
except:
    print(Style.BRIGHT + f'    {Fore.RED}[{Fore.WHITE}CHANGELOG{Fore.RED}]{Fore.YELLOW} Module: "Requests" is not installed! Installing..')
    os.system('pip install requests')
try:
    import random
except:
    print(Style.BRIGHT + f'    {Fore.RED}[{Fore.WHITE}CHANGELOG{Fore.RED}]{Fore.YELLOW} Module: "Random" is not installed! Installing..')
    os.system('pip install random')
try:
    from discord_webhook import DiscordEmbed, DiscordWebhook
except:
    print(Style.BRIGHT + f'    {Fore.RED}[{Fore.WHITE}CHANGELOG{Fore.RED}]{Fore.YELLOW} Module: "discord_webhook" is not installed! Installing..')
    os.system('pip install discord_webhook')
    


def tiktokchecker():
    print('')
    notinuse = 0
    taken = 0
    
    with open("util/config.json", 'r') as j:
        contents = json.loads(j.read())

        amount = contents['amount of usernames to check']
        dictwords = contents['dictwords']
        length = contents['username length']
        amount = int(amount)

    for x in range(amount):
        if dictwords == 'n':
            letters = string.ascii_letters + string.digits + "." + "_"
            username = ''.join(random.choice(letters) for i in range(length))
        if dictwords == 'y':
            f = open('util/data/dictionarywords.txt', 'r').read().splitlines()
            username = random.choice(f) 

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
        response = requests.get(f"https://tiktok.com/@{username}",headers=headers)
        if response.status_code == 200:
            print(f'    {Fore.RED}[{Fore.WHITE}Taken{Fore.RED}]{Fore.RED} {username}')
            taken = taken + 1

            f = open('util/data/Taken.txt', 'a')
            f.write(f'{username}\n')
            f.close()

        if response.status_code == 404:
            print(f'    {Fore.RED}[{Fore.WHITE}Not-In-Use{Fore.RED}]{Fore.GREEN} {username}')
            notinuse = notinuse + 1

            f = open('util/data/Not-In-Use.txt', 'a')
            f.write(f'{username}\n')
            f.close()
            
            ####################################################################################################
            #Webhook
            with open("util/config.json", 'r') as j:
                contents = json.loads(j.read())

                webhook = contents['webhook']
                togglewebhook = contents['toggle-webhook']

            if togglewebhook == "y":
                url = webhook

                data = {
                    "username" : "username checker"
                }

                data["embeds"] = [
                    {
                        "type": "rich",
                        "title": "New Possible Available Username!",
                        "description": f"Username: **{username}**",
                        "color": 0x73ff00,
                    "thumbnail": {
                        "url": "https://cdn.discordapp.com/attachments/968914394689990677/968961514071543888/tiktok_tik_tok_logo_icon_134936.png",
                        "height": 0,
                        "width": 0
                    },
                    "footer": {
                        "text": "dont be mad if it dont work",
                        "icon_url": "https://cdn.discordapp.com/attachments/968914394689990677/968961514071543888/tiktok_tik_tok_logo_icon_134936.png"
                    }
                    }
                ]

                data["components"] = [
                    {
                        "type": 1,
                        "components": [
                            {
                                "style": "5",
                                "label": "best checker",
                                "url": "https://akame2cool.ml",
                                "disabled": "false",
                                "type": 2
                            }
                        ]
                    }
                ]

                result = requests.post(url, json = data)

                try:
                    result.raise_for_status()
                except requests.exceptions.HTTPError as err:
                    print(f'    {Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}] {Fore.YELLOW} There Might Be An Error With Your Webhook! Make Sure All Settings Are Correct.')
                ###################################################################################################################################################### 
