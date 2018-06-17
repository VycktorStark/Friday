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
		if ("caption" in msg['reply']):
			msg['reply']['text'] = msg['reply']['caption']
		return msg_receive_(msg)

def pinned_message_(msg):
	msg['text'] = "###pinned_message"
	msg = msg['pinned_message']
	return msg_receive_(msg)

def status_service_(msg):
		msg['service'] = True
		if ("new_chat_member" in msg):
				if str(msg['new_chat_member']['id']) == str(config.BOT['id']):
						msg['text'] = '###botadded'
				else:
						msg['text'] = '###added'
				msg['adder'] = msg['from']
				msg['added'] = msg['new_chat_member']
		if ("left_chat_member" in msg):
				if str(msg['left_chat_member']['id']) == str(config.BOT['id']):
						msg['text'] = '###botremoved'
				else:
						msg['text'] = '###removed'
				msg['remover'] = msg['from']
				msg['removed'] = msg['left_chat_member']
		if ("group_chat_created" in msg):
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
		if 'text' in msg:
				msg['text'] = '###forward: {}'.format(msg['text'])
		else:
				msg['text'] = '###forward'
		return msg_receive_(msg)
	
def msg_media_(msg):
		if 'photo' in msg: msg['text'] = "###Photo"
		elif 'sticker' in msg: msg['text'] = "###Sticker"
		elif 'voice' in msg: msg['text'] = "###Voice"
		elif 'audio' in msg: msg['text'] = "###Audio"
		elif 'video' in msg: msg['text'] = "###Vídeo"
		elif 'contact' in msg: msg['text'] = "###contact"
		elif msg['entities'][0]['type'] == "url": msg['url'] = "###url"
		elif 'document' in msg and msg['document']['mime_type']:
				document = msg['document']['mime_type']
				if document == "video/mp4":
						msg['text'] = "###gif."
				elif document == "application/x-bittorrent":
						msg['text'] = "###pdf_file"    
				elif document == "application/vnd.android.package-archive":
						msg['text'] = "###app"    
				elif document == "application/x-rar":
						msg['text'] = "###rar_file"    
				elif document == "application/x-zip":
						msg['text'] = "###zip_file"    
				elif document == "text/x-python":
						msg['text'] = "###script_in_python"    
				elif document == "text/plain":
						msg['text'] = "###text file"    
				elif document == "application/x-shellscript":
						msg['text'] = "###script_in_shell"    
				elif document == "text/x-lua":
						msg['text'] = "###script_in_lua"    
				elif document == "text/html":
						msg['text'] = "###script_in_HTML"    
				elif document == "application/json":
						msg['text'] = "###script_in_JSON"    
				elif document == "application/javascript":
						msg['text'] = "###script_in_JavaScript"    
				elif document == "application/octet-stream":
						msg['text'] = "###script_in_octet-stream"    
				elif document == "text/markdown":
						msg['text'] = "###script_in_Markdown"    
				elif document == "application/x-yaml":
						msg['text'] = "###script_in_yaml."
				else: 
					msg['text'] = "file"
		elif msg['entities'][0]['type'] == "url": msg['url'] = "###url"
		return msg_receive_(msg)

def msg_receive_(msg):	
		msg_from_id = msg['from']['id']
		chat_id = msg['chat']['id']
		if config.Sys['viewer_shell'] == True: viewer_(msg)
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
											err_ = lang('plugin_err', 'main', sudo='True').format(msg['text'], err)
											sendAdmin(text=err_)
											print(err_)
									else:
											if resp != None and resp != False:
												sendMessage(chat_id=chat_id, text=resp, parse_mode="HTML")
							break
