#!/usr/bin/python
#-*- coding: utf-8 -*-
from langs import lang
def about(msg, cmd, ln):
	return lang('about', ln)[0]['about_msg']
plugin = {
	'patterns': [
		"^/about$",
		"^/acerca$",
		"^/sobre$"
	],
	'function': about,
	'name': "About",
	'sudo': False,
	}
