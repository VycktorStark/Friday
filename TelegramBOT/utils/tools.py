#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__all__ = ['time_atual_', 'bash_', 'regex_', 'msg_replace_', 'TypeChat_', 'viewer_', 'log_']
from TelegramBOT import sys, lang, re, subprocess, time
def msg_replace_(msg, text):
		user_ = msg['from']
		chat_ = msg['chat'] 
		if "{user}" in text:
				nome_user = user_['first_name']
				if 'last_name' in user_: 
						nome_user = "{} {}".format(nome_user, user_['last_name'])
				text = text.replace("{user}", nome_user)
		if '{user_id}' in text:
				text = text.replace("{user_id}", str(user_['id']))
		if '{chat_id}' in text:
				text = text.replace('{chat_id}', str(chat_['id']))
		if '{chat_name}' in text:
				text = text.replace("{chat_name}",TypeChat_(chat_['type']))
		if '{text}' in text:
				text = text.replace("{text}",msg['text'])
		if '{SendType}' in text:
				text = text.replace("{SendType}", SendType(msg))
		return text
def SendType(msg):
		global texto
		if 'photo' in msg: texto = "sent a foto."
		elif 'sticker' in msg: texto = "sent a Sticker."
		elif 'voice' in msg: texto = "sent a voz."
		elif 'audio' in msg: texto = "sent a Audio."
		elif 'video' in msg: texto = "sent a Video."
		elif 'document' in msg and msg['document']['mime_type']:
				document = msg['document']['mime_type']
				if document == "video/mp4":
						texto = "sent a Gif."
				elif document == "application/x-bittorrent":
						texto = "sent a pdf file."     
				elif document == "application/vnd.android.package-archive":
						texto = "sent a App."     
				elif document == "application/x-rar":
						texto = "sent a RAR file."     
				elif document == "application/x-zip":
						texto = "sent a Zip file."     
				elif document == "text/x-python":
						texto = "sent a Script in python."     
				elif document == "text/plain":
						texto = "sent a Script de texto simples."     
				elif document == "application/x-shellscript":
						texto = "sent a Script in shell."     
				elif document == "text/x-lua":
						texto = "sent a Script in lua."     
				elif document == "text/html":
						texto = "sent a Script in HTML."     
				elif document == "application/json":
						texto = "sent a Script in JSON."     
				elif document == "application/javascript":
						texto = "sent a Script in JavaScript."     
				elif document == "application/octet-stream":
						texto = "sent a Script in octet-stream."     
				elif document == "text/markdown":
						texto = "sent a Script in Markdown."     
				elif document == "application/x-yaml":
						texto = "sent a Script in yaml."
				else: texto = "Document"
		elif 'entities' in msg:
			if msg['entities'][0]['type'] == "url":
				texto = 'sent a url'
			elif msg['entities'][0]['type'] == "bot_command":
				texto = 'sent a command'
		elif 'text' in msg:
			texto = 'sent a message'
		return texto
def viewer_(msg):
		viewer = msg_replace_(msg, lang('viewer', 'main', sudo=True))
		print(viewer)
		return False
	
def TypeChat_(self):
		self = self.replace('supergroup', 'Super Group').replace('group', 'Group Common').replace('private', 'Chat Private')
		return self

def regex_(pattern=None, string=None):
		capt = re.match(pattern, string)
		if bool(capt):
			return capt
		return None

def time_atual_(msg_data):
		hora_atual = time.time()
		segundos = int((hora_atual-msg_data)/60)
		return segundos
	
def bash_(self, cmd):
		if 'git' in self:
				cmd = "git " + cmd
		comando = re.sub(self, "", cmd)
		comando = re.sub('—', '--', comando)
		shell = subprocess.check_output(comando, shell=True)
		if len(shell) == 0:
			shell = lang('Shell_Not', 'tools',sudo='True')
		return shell.decode('utf8')

def log_(message):
    print(message)
    sys.stdout.flush()
