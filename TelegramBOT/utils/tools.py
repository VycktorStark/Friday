#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__all__ = ['time_atual_', 'bash_', 'regex_', 'msg_replace_', 'TypeChat_', 'viewer_', 'log_']
from TelegramBOT import sys, lang, re, subprocess, time, json
def msg_replace_(msg, text):
		user_ = msg['from']
		chat_ = msg['chat'] 
		if ("{user}" in text):
				nome_user = user_['first_name'].encode("ascii", "ignore").decode("ascii")
				if ('last_name' in user_): 
						nome_user = "{} {}".format(nome_user, user_['last_name']).encode("ascii", "ignore").decode("ascii")
				text = text.replace("{user}", nome_user)
		if ('{user_id}' in text):
				text = text.replace("{user_id}", str(user_['id']))
		if ('{username}' in text):
				text = text.replace("{username}", user_['username'])
		if ('{chat_id}' in text):
				text = text.replace('{chat_id}', str(chat_['id']))
		if ('{chat_name}' in text):
				text = text.replace("{chat_name}",TypeChat_(chat_['type']))
		if ('{text}' in text):
			if ("text" in msg) or ('reply' in msg) or ("text_action" in msg):
				text = text.replace("{text}",  msg['text_action'] or msg['text'] or msg['reply']['text'])
			else:
				text = text.replace("{text}", "no text in the message")
		if ('{SendType}' in text):
				if ("action" in msg):
					text = text.replace("{SendType}", msg["action"])
				else:
					text = text.replace("{SendType}", "no action in the message")
		return text
def viewer_(msg):
		if ("action" in msg) and ("text" in msg):
			msg['text_action'] = lang(msg['action'], 'viewer', sudo=True).format(msg['text'])
		viewer = msg_replace_(msg, lang('viewer', 'viewer', sudo=True))
		log_(viewer)
	
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
		if ('git' in self):
				cmd = "git " + cmd
		comando = re.sub(self, "", cmd)
		comando = re.sub('—', '--', comando)
		shell = subprocess.check_output(comando, shell=True).decode('utf-8')
		if (len(shell) == 0):
			shell = lang('Shell_Not', 'tools',sudo='True')
		return shell

def log_(message):
    print(message.encode("ascii", "ignore").decode("ascii"))
    sys.stdout.flush()
