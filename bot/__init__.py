#-*- coding: utf-8 -*-
import re, os , sys, time, subprocess, config, requests, json, flask, datetime
from os import listdir
from os.path import isfile, join, realpath, dirname
from PythonColorize import colors
from langs import *
__all__ = ['colors', 're', 'os', 'sys','subprocess', 'time', 'lang', 'config', 'requests', 'json', 'flask', 'datetime']
from .utils.tools import *
__all__ += utils.tools.__all__
from .methods.methods import *
__all__ += methods.methods.__all__
__all__ += ['loadplugins', 'plugins', 'plugins_name']
curPath = dirname(realpath(__file__))
def loadplugins():
	global plugins, plugins_name
	plugins = []
	plugins_name = []
	pluginFiles = [curPath + "/plugins/" + f for f in listdir(curPath + "/plugins") if re.search('^.+\.py$', f)]
	for file in pluginFiles:
		values = {}
		with open(file, encoding='utf-8') as f:
			code = compile(f.read(), file, 'exec')
			exec(code, values)
		plugin = values['plugin']
		plugins.append(plugin)
		plugins_name.append(plugin['name'])
	plugins_name.remove('Admin')
def rethink_reply(msg):
  msg['reply'] = msg['reply_to_message']
  if msg['reply']['caption']:
    msg['reply']['text'] = msg['reply']['caption']
  end
  return on_msg_receive(msg)

def service_to_message(msg):
  msg['service'] = true
  if msg['new_chat_member']:
    if str(msg['new_chat_member']['id']) == str(config.BOT['id']):
      msg['text'] = '###botadded'
    else:
      msg['text'] = '###added'
    msg['adder'] = msg['from']
    msg['added'] = msg['new_chat_member']
  elif msg['left_chat_member']:
    if str(msg['left_chat_member']['id']) == str(config.BOT['id']):
      msg['text'] = '###botremoved'
    else:
      msg['text'] = '###removed'
    msg['remover'] = msg['from']
    msg['removed'] = msg['new_chat_member']
  elif msg['group_chat_created']:
    msg['chat_created'] = true
    msg['adder'] = msg['from']
    msg['text'] = '###botadded'
  return on_msg_receive(msg)

def callback_query(msg):
  msg['text'] = '###cb: {}'.format(msg['data'])
  msg['old_text'] = msg['message']['text']
  msg['old_date'] = msg['message']['date']
  msg['date'] = os.time()
  msg['cb'] = true
  msg['cb_id'] = msg['id']
  msg['message_id'] = msg['message']['message_id']
  msg['chat'] = msg['message']['chat']
  msg['message'] = nil
  return on_msg_receive(msg)

def forward_to_msg(msg):
	if msg['text']:
		msg['text'] = '###forward: {}'.format(msg['text'])
	else:
		msg['text'] = '###forward'
	return on_msg_receive(msg)

def TypeChat(self):
  self = self.replace('supergroup', 'Super Group').replace('group', 'Group Common').replace('private', 'Chat Private')
  return self
def viewer(msg):
	Chat_title = lang('send', 'main', sudo=True).format(TypeChat(msg['chat']['type']), msg['chat']['id'])
	user = msg['from']['first_name']
	if ('last_name' in msg['from']):
		user = '{} {}'.format(user, msg['from']['last_name'])
	user = '\033[37m\033[36m{} \033[37m({})\033[37m'.format(user, lang('id_text', 'main', sudo='True').format(msg['from']['id']))
	print('{} {}{}\n\033[31m{}\033[37m'.format(user, lang('infor_msg', 'main', sudo=True), Chat_title, msg['text']))
def on_msg_receive(msg):	
	msg_from_id = msg['from']['id']
	if config.Sys['viewer_shell'] == True:
		viewer(msg)
	for aPlugin in plugins:
		for patterns in aPlugin['patterns']:
			if re.search(patterns, msg['text'], re.IGNORECASE):
				matches = re.search(patterns, msg['text'], re.IGNORECASE)
				print(lang('cmd_detected', 'main', sudo=True).format(patterns))
				if aPlugin['sudo'] == True:
					if msg_from_id in config.Sys['sudo'][0]:
						resp = aPlugin['function'](msg, msg['text'].split(), msg['from']['language_code'][:2])
					else:
						sendMessage(chat_id=msg['chat']['id'], text=lang('sudo_not', 'main', sudo=True))
				else:
					print(config.Sys['maintenance'])
					if  (msg_from_id in config.Sys['sudo'][0]) or (config.Sys['maintenance'] == False):
						try:
							resp = aPlugin['function'](msg, msg['text'].split(), msg['from']['language_code'][:2])
							if resp: 
								sendMessage(chat_id=msg['chat']['id'], text=resp, parse_mode="HTML")
						except Exception as err:
							print(lang('plugin_err', 'main', sudo='True').format(err))
				break
