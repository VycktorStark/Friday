#-*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join, realpath, dirname
from langs import *
import re, os , sys, time, subprocess, config, requests, json, flask, datetime
__all__ = ['re', 'os', 'sys','subprocess', 'time', 'lang', 'config', 'requests', 'json', 'flask', 'datetime']
from .utils.tools import *
__all__ += utils.tools.__all__
from .methods.methods import *
__all__ += methods.methods.__all__
__all__ += ['plugins_', 'plugins']

def plugins_():
		curPath = dirname(realpath(__file__))
		global plugins
		plugins = []
		pluginFiles = [curPath + "/plugins/" + f for f in listdir(curPath + "/plugins") if re.search('^.+\.py$', f)]
		for file in pluginFiles:
			values = {}
			with open(file, encoding='utf-8') as f:
				code = compile(f.read(), file, 'exec')
				exec(code, values)
			plugin = values['plugin']
			plugins.append(plugin)
		
def reply_caption_(msg):
		msg['reply'] = msg['reply_to_message']
		if msg['reply']['caption']:
			msg['reply']['text'] = msg['reply']['caption']
		return msg_receive_(msg)

def status_service_(msg):
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
		return msg_receive_(msg)

def callback_query_(msg):
		msg['text'] = '###cb: {}'.format(msg['data'])
		msg['old_text'] = msg['message']['text']
		msg['old_date'] = msg['message']['date']
		msg['date'] = time_atual_
		msg['cb'] = true
		msg['cb_id'] = msg['id']
		msg['message_id'] = msg['message']['message_id']
		msg['chat'] = msg['message']['chat']
		msg['message'] = None
		return msg_receive_(msg)

def forward_msg_(msg):
		if msg['text']:
				msg['text'] = '###forward: {}'.format(msg['text'])
		else:
				msg['text'] = '###forward'
		return msg_receive_(msg)


def msg_receive_(msg):	
		msg_from_id = msg['from']['id']
		chat_id = msg['chat']['id']
		if config.Sys['viewer_shell'] == True:
				viewer_(msg)
		if time_atual_(msg['date']) > 10: return flask.Response(status=200)
		for aPlugin in plugins:
				for patterns in aPlugin['patterns']:
					if re.search(patterns, msg['text'], re.IGNORECASE):
							matches = re.search(patterns, msg['text'], re.IGNORECASE)
							print(lang('cmd_detected', 'main', sudo=True).format(patterns))
							if (msg_from_id in config.Sys['sudo'][0]) or (config.Sys['maintenance'] == False):
									try:
										if aPlugin['sudo'] == True:
											if msg_from_id in config.Sys['sudo'][0]: resp = aPlugin['function'](msg, msg['text'].split(), msg['from']['language_code'][:2])
											else: sendMessage(chat_id=chat_id, text=lang('sudo_not', 'main', sudo=True))
										else:
											resp = aPlugin['function'](msg, msg['text'].split(), msg['from']['language_code'][:2])
									except Exception as err:
											print(lang('plugin_err', 'main', sudo='True').format(err))
									else:
											if resp != None and resp != False:
												sendMessage(chat_id=chat_id, text=resp, parse_mode="HTML")
							break
