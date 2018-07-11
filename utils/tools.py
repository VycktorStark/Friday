#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__all__ = ['time_atual_', 'bash_', 'msg_replace_', 'TypeChat_', 'viewer_', 'log_', 'polling']
from main import sys, lang, re, subprocess, time, json, requests
def viewer_(msg):
		if ("action" in msg) and ("text" in msg):
			msg['text_action'] = lang(msg['action'], 'viewer', sudo=True).format(msg['text'])
		try:
			return msg_replace_(msg, lang('viewer', 'viewer', sudo=True)), 200
		except Exception as error: 
			return "Error in viewer shell: {}".format(error), 404
	
def TypeChat_(self):
		self = self.replace('supergroup', 'Super Group').replace('group', 'Group Common').replace('private', 'Chat Private')
		return self

def time_atual_(msg_data):
		hora_atual = time.time()
		segundos = int((hora_atual-msg_data)/60)
		return segundos
	
def bash_(self, txt):
		txt = txt.replace(self,'').replace('—','--')
		if ('git' in self):
				txt = "git {}".format(txt)
		text = txt
		try:
			resp = subprocess.check_output(text, shell=True).decode('utf8')
			if (len(resp) == 1) and resp == "\n":
				resp = resp.replace("\n","Ok")
		except Exception: resp = "Ok"
		finally: return resp

def log_(message):
		try:
			print(message)
		except UnicodeEncodeError:
				print(message.encode("ascii", "ignore").decode("ascii"))
		sys.stdout.flush()

def polling():
	from methods.methods import METHOD as api
	api.deleteWebhook()
	if 'result' in resp:
		temp = 0
		resp = api.getUpdates(offset=temp, timeout=1000+l_, allowed_updates='message')
		temp  = resp['result'][0]['update_id'] + 1
		resp = requests.post("http://localhost:3000/webhook", data=json.dumps(resp['result'][0]))
		return resp
	return False

def msg_replace_(msg, text):
		user_ = msg['from']
		chat_ = msg['chat'] 
		if ('{user_id}' in text): text = text.replace("{user_id}", str(user_['id']))
		if ('{username}' in text): text = text.replace("{username}", user_['username'])
		if ('{chat_id}' in text): text = text.replace('{chat_id}', str(chat_['id']))
		if ('{chat_name}' in text): text = text.replace("{chat_name}",TypeChat_(chat_['type']))
		if ("{user}" in text):
				nome_user = user_['first_name'].encode("ascii", "ignore").decode("ascii")
				if ('last_name' in user_): nome_user = "{} {}".format(nome_user, user_['last_name']).encode("ascii", "ignore").decode("ascii")
				text = text.replace("{user}", nome_user)
		if ('{text}' in text):
			if ("text_action" in msg and msg['text_action'] != True) or ("text" in msg): text = text.replace("{text}",  (msg['text_action']) or (msg['text']))
			else: text = text.replace("{text}", "no text in the message")
		if ('{SendType}' in text):
				if ("action" in msg): text = text.replace("{SendType}", msg["action"])
				else: text = text.replace("{SendType}", "no action in the message")
		return text