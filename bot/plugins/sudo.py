#!/usr/bin/python
#-*- coding: utf-8 -*-
def adminPlugin(msg, cmd, ln):
	from bot import sendAdmin, config, loadplugins
	global maintenance
	if cmd[1] == 'reboot':
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
		"^/sudo (reboot)$",
		"^/sudo (manut)$",
		"^/sudo (notmanut)$",
	],
	'function': adminPlugin,
	'name': "Admin",
	'sudo': True,
	}