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
import plugins
plugins_ = plugins.plugins_
plugins_()
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
			for aPlugin in plugins.plugins:
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
import handler