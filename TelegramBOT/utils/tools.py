#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__all__ = ['time_atual_', 'bash_', 'regex_', 'msg_replace_', 'TypeChat_', 'viewer_']
from TelegramBOT import *
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
		return text
	
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

