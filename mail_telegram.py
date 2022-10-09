#!/usr/bin/python3

from sys import stdin
from requests import post
from sys import argv
from email.header import decode_header
import re

URL="https://api.telegram.org/bot>>YOUR_BOT_TOKEN_HERE<</sendMessage"
ChatID="YOUR_CHAT_ID_HERE"

sieve = argv[1]
subject=""
envfrom=""
bytes=""

pattern = re.compile(r'\=\?(UTF|utf|koi|KOI|windows)\-?(8|1251)\-?r?\?')
for line in stdin:
    result = re.search(pattern, line)
    if result:
        subject += line.strip()
    elif "envelope-from" in line:
        envfrom = line.strip()

subject = subject.split('Subject: ')[-1]
envfrom = envfrom.split('>)')[0].split(' <')[-1]

bytes, encoding = decode_header(subject)[0]
msg = sieve + envfrom + " " + bytes.decode(encoding)

def send_mess(text):
    params = {'chat_id': ChatID, 'text': text}
    response = post(URL, data=params)
    return response

send_mess(msg)
