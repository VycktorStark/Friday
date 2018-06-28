#!/usr/bin/python
#-*- coding: utf-8 -*-
from langs import lang
def Function(msg, cmd, ln):
	return lang('about', ln)[0]['about_msg']
plugin = {
	'patterns': [
		"^[/!#](about)$",
		"^[/!#](acerca)$",
		"^[/!#](sobre)$"
	],
	'function': Function,
	'name': "About",
	'sudo': False,
	}
