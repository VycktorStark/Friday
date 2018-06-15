#!/usr/bin/python
#-*- coding: utf-8 -*-
from TelegramBOT import sendAdmin, config, loadplugins, bash
def adminPlugin(msg, cmd, ln):
	print(len(cmd))
	global maintenance
	if 'sudo' in cmd[0]:
			if cmd[1] == 'update':
				sendAdmin(text="Done")
				return loadplugins()

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
		sendAdmin(text=bash(cmd[0], msg['text'].replace(cmd[0],'')))
	elif 'git' in cmd[0]:
		sendAdmin(text=bash(cmd[0], msg['text'].replace(cmd[0],'')))
	
plugin = {
	'patterns': [
		"^/(sudo) (update)$",
		"^/(sudo) (manut)$",
		"^/(sudo) (notmanut)$",
		"^/(shell) (.+)$",
		"^/(git) (.+)$"
	],
	'function': adminPlugin,
	'name': "Admin",
	'sudo': True,
	}
