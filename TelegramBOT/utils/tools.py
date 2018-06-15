#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__all__ = ['time_atual', 'bash', 'regex', 'msg_replace']
from TelegramBOT import *
def msg_replace(msg, text):
	user_ = msg['from']
	chat_ = msg['chat'] 
	if "{user}" in text:
		nome_user = user_['first_name']
		if 'last_name' in user_: 
			nome_user = "{} {}".format(nome_user, user_['last_name'])
		text = text.replace("{user}", nome_user)
	if '{user_id}' in text:
		text = text.replace("{user_id}", user_['id'])
	if '{chat_id}' in text:
		text = text.replace('{chat_id}', chat_['id'])
	if '{chat_name}' in text:
		if chat_['type'] == "private": 
			texto = "Meu privado"
		else: 
			texto = chat_['title']
		text = text.replace('{chat_name}', texto)
	return text
def regex(pattern=None, string=None):
	capt = re.match(pattern, string)
	if bool(capt):
		return capt
	return None

def time_atual(msg_data):
  hora_atual = time.time()
  segundos = int((hora_atual-msg_data)/60)
	
  return segundos
def bash(self, cmd):
  if 'git' in self:
    cmd = "git " + cmd
  comando = re.sub(self, "", cmd)
  comando = re.sub('—', '--', comando)
  shell = subprocess.check_output(comando, shell=True)
  if len(shell) == 0:
    shell = lang('Shell_Not', 'tools',sudo='True')
  return shell.decode('utf8')

