#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__all__ = ['time_atual_', 'bash_', 'msg_replace_', 'TypeChat_', 'viewer_', 'log_', 'polling']
from main import sys, lang, re, subprocess, time, json, requests

def viewer_(self):
		if ("action" in self) and ("text" in self):
			if (self["action"] != True): 
				self['text_action'] = lang(self['action'], 'viewer', sudo=True).format(self['text'])
		try:
			resp = msg_replace_(self, lang('viewer', 'viewer', sudo=True)), 200
		except Exception as error: 
			resp = "Error in viewer shell: {}".format(error), 404 
		return resp

def TypeChat_(self):
		self = self.replace('supergroup', 'Super Group').replace('group', 'Group Common').replace('private', 'Chat Private')
		return self

def time_atual_(self):
		self = int((time.time()-self)/60)
		return self

def bash_(self):
		try:
			resp = subprocess.check_output(self, shell=True).decode('utf8')
			if (len(resp) == 1) and resp == "\n": resp = resp.replace("\n","Ok")
		except Exception as error: resp = error
		return resp

def log_(self):
		try: print(self)
		except UnicodeEncodeError: print(self.encode("ascii", "ignore").decode("ascii"))
		except Exception as error: print(error)
		finally: sys.stdout.flush()
		return False

def polling():
	from methods.methods import METHOD as api
	api.deleteWebhook()
	resp = None
	if 'result' in resp:
		temp = 0
		resp = api.getUpdates(offset=temp, timeout=1000+l_, allowed_updates='message')
		temp  = resp['result'][0]['update_id'] + 1
		resp = requests.post("http://localhost:3000/webhook", data=json.dumps(resp['result'][0]))
	return resp

def msg_replace_(self, text):
		user_ = self['from']
		chat_ = self['chat']
		if ('{user_id}' in text): text = text.replace("{user_id}", str(user_['id']))
		if ('{username}' in text): text = text.replace("{username}", user_['username'])
		if ('{chat_id}' in text): text = text.replace('{chat_id}', str(chat_['id']))
		if ('{chat_name}' in text): text = text.replace("{chat_name}",TypeChat_(chat_['type']))
		if ("{user}" in text):
				nome_user = user_['first_name'].encode("ascii", "ignore").decode("ascii")
				if ('last_name' in user_): nome_user = "{} {}".format(nome_user, user_['last_name']).encode("ascii", "ignore").decode("ascii")
				text = text.replace("{user}", nome_user)
		if ('{text}' in text):
			if ("text" in self): text = text.replace("{text}", self['text'])
			else: text = text.replace("{text}", "no text in the message")
		if ('{SendType}' in text):
				if ("action" in self): text = text.replace("{SendType}", self["action"])
				else: text = text.replace("{SendType}", "no action in the message")
		return text