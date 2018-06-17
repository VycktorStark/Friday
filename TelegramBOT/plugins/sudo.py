#!/usr/bin/python
#-*- coding: utf-8 -*-
from TelegramBOT import sendAdmin, config, plugins_, bash_
def Function(msg, cmd, ln):
	global maintenance
	if 'sudo' in cmd[0]:
			if cmd[1] == 'att':
				sendAdmin(text="Done")
				return plugins_()

			elif cmd[1] == 'manut':
				config.Sys['maintenance'] = True
				sendAdmin(text="Done")
				return config.Sys['maintenance']

			elif cmd[1] == 'notmanut':
				config.Sys['maintenance'] = False
				sendAdmin(text="Done")
				return config.Sys['maintenance']
	elif 'shell' in cmd[0]:
		print('aqui')
		sendAdmin(chat_id=msg['chat']['id'],text=bash_(cmd[0], msg['text'].replace(cmd[0],'')))
	elif 'git' in cmd[0]:
		sendAdmin(chat_id=msg['chat']['id'],text=bash_(cmd[0], msg['text'].replace(cmd[0],'')))
	
plugin = {
	'patterns': [
		"^[/!#](sudo) (att)$",
		"^[/!#](sudo) (manut)$",
		"^[/!#](sudo) (notmanut)$",
		"^[/!#](shell) (.+)$",
		"^[/!#](git) (.+)$"
	],
	'function': Function,
	'name': "Admin",
	'sudo': True,
	}
