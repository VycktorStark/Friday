#!/usr/bin/python
#-*- coding: utf-8 -*-
def adminPlugin(msg, cmd, ln):
	from TelegramBOT import sendAdmin, config, loadplugins
	global maintenance
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
plugin = {
	'patterns': [
		"^/(sudo) (update)$",
		"^/(sudo) (manut)$",
		"^/(sudo) (notmanut)$",
	],
	'function': adminPlugin,
	'name': "Admin",
	'sudo': True,
	}