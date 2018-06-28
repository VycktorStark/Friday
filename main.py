#!/usr/bin/env python3
# encoding=utf8
from langs import lang
import requests, json, time, subprocess, datetime, os, re, sys, psycopg2, flask, argparse, utils
from flask import Flask, request, Response
ru = lambda text: "\n\033[02;31m{}\n\033[00;37m".format(text)
app = Flask(ru("".join(subprocess.getoutput('figlet F. R. I. D. A. Y.'))))
app.config.from_object('settings')
config = app.config
from methods.methods import METHOD as api
def plugins_():
		curPath = os.path.dirname(os.path.realpath(__file__))
		global plugins
		plugins = []
		pluginFiles = [curPath + "/plugins/" + f for f in os.listdir(curPath + "/plugins") if re.search('^.+\.py$', f)]
		for file in pluginFiles:
			values = {}
			with open(file, encoding='utf-8') as f:
				code = compile(f.read(), file, 'exec')
				exec(code, values)
			plugins.append(values['plugin'])
def msg_receive_(msg):	
		msg_from_id = msg['from']['id']
		chat_id = msg['chat']['id']
		if config['VIEW_THE_TERMINAL'] == True: 
			resp, code = utils.viewer_(msg)
			if code == 404: api.sendAdmin(text=resp)
			utils.log_(resp)
		if utils.time_atual_(msg['date']) > int(10):
			return Response(status=200)
		else:
			if (not "text" in msg): msg['text'] = msg['action']
			for aPlugin in plugins:
					for patterns in aPlugin['patterns']:
						cmd = re.search(patterns, msg['text'], re.IGNORECASE)
						if cmd:
								if cmd.groups(): cmd = cmd.groups()
								else: cmd = cmd.group()
								if "language_code" in  msg['from']:
									config["LANG"] = msg['from']['language_code'][:2]
								if aPlugin['sudo'] == True:
									if msg_from_id in config['SUDO']: aPlugin['function'](msg, cmd, config["LANG"])
									else: api.sendMessage(chat_id=chat_id, text=lang('sudo_not', 'main', sudo=True))
								elif (msg_from_id in config['SUDO']) or (config['MAINTENACE'] == False):
										try:
												resp = aPlugin['function'](msg, cmd, config["LANG"])
										except Exception as err:
												utils.log_(api.sendAdmin(text=lang('plugin_err', 'main', sudo='True').format(msg['text'], err))['result']['text'])
										else:
												if (resp != None) and (resp != False):
													api.sendMessage(chat_id=chat_id, text=resp, parse_mode="HTML")
								break

def pinned_message_(msg):
	msg['action'] = "###pinned_message"
	msg['text'] = msg['pinned_message']['text']
	return msg_receive_(msg)

def forward_msg_(msg):
		if (msg['forward_from']["is_bot"] == True):
				msg['action'] = '###forwardbot'
		msg['action'] = '###forward'
		return msg_receive_(msg)
	
def reply_caption_(msg):
		msg['action'] = "###reply"
		msg['reply'] = msg["reply_to_message"]
		if ("caption" in msg['reply']):
			msg['text'] = msg['reply']['caption']
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
	
def status_service_(msg):
		msg['service'] = True
		if ("new_chat_member" in msg):
				if str(msg['new_chat_member']['id']) == str(config['IDBOT']):
						msg['action'] = '###botadded'
				else:
						msg['action'] = '###added'
				msg['adder'] = msg['from']
				msg['added'] = msg['new_chat_member']
		if ("left_chat_member" in msg):
				if str(msg['left_chat_member']['id']) == str(config['IDBOT']):
						msg['action'] = '###botremoved'
				else:
						msg['action'] = '###removed'
				msg['remover'] = msg['from']
				msg['removed'] = msg['left_chat_member']
		if ("group_chat_created" in msg):
				msg['chat_created'] = true
				msg['adder'] = msg['from']
				msg['action'] = '###botadded'
		return msg_receive_(msg)
	
def msg_media_(msg):
		if ('photo' in msg): msg['action'] = "###Photo"
		elif ('sticker' in msg): msg['action'] = "###Sticker"
		elif ('voice' in msg): msg['action'] = "###Voice"
		elif ('audio' in msg): msg['action'] = "###Audio"
		elif ('video' in msg): msg['action'] = "###Video"
		elif ('contact' in msg): msg['action'] = "###contact"
		elif ('document' in msg and msg['document']['mime_type']):
				document = msg['document']['mime_type']
				if (document == "video/mp4"):
						msg['action'] = "###gif"
				elif (document == "application/x-bittorrent"):
						msg['action'] = "###pdf_file"    
				elif (document == "application/vnd.android.package-archive"):
						msg['action'] = "###app"    
				elif (document == "application/x-rar"):
						msg['action'] = "###rar_file"    
				elif (document == "application/x-zip"):
						msg['action'] = "###zip_file"    
				elif (document == "text/x-python"):
						msg['action'] = "###script_in_python"    
				elif (document == "text/plain"):
						msg['action'] = "###text_file"    
				elif (document == "application/x-shellscript"):
						msg['action'] = "###script_in_shell"    
				elif (document == "text/x-lua"):
						msg['action'] = "###script_in_lua"    
				elif (document == "text/html"):
						msg['action'] = "###script_in_HTML"    
				elif (document == "application/json"):
						msg['action'] = "###script_in_JSON"    
				elif (document == "application/javascript"):
						msg['action'] = "###script_in_JavaScript"    
				elif (document == "application/octet-stream"):
						msg['action'] = "###script_in_octet-stream"    
				elif (document == "text/markdown"):
						msg['action'] = "###script_in_Markdown"    
				elif (document == "application/x-yaml"):
						msg['action'] = "###script_in_yaml."
				else: 
					msg['action'] = "###file"
		elif ('entities' in msg):
			if (msg['entities'][0]['type'] == "url"):
					msg['action'] = '###url'
			elif (msg['entities'][0]['type'] == "mention"):
					msg['action'] = '###mention'
			elif (msg['entities'][0]['type'] == "bot_command"):
					msg['action'] = '###bot_command'
					msg['text'] = msg['text'].replace("@{}".format(config['USERNAMEBOT']),'')
		return msg_receive_(msg)
import handler
