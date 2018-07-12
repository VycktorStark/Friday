#!/usr/bin/python
#-*- coding: utf-8 -*-
from main import api, utils, config, plugins_, json, lang
def Function(msg, cmd, ln):
	global maintenance
	if 'sudo' in cmd[0]:
			if (cmd[1] == 'update'):
				return api.sendAdmin(chat_id=msg['chat']['id'], text=lang('updatecommand','plugin', sudo=True).format(plugins_()))

			elif (cmd[1] == 'manut'):
				config['MAINTENACE'] = True
				api.sendAdmin(chat_id=msg['chat']['id'], text="Done")
				return config['MAINTENACE']

			elif (cmd[1] == 'notmanut'):
				config['MAINTENACE'] = False
				api.sendAdmin(chat_id=msg['chat']['id'], text="Done")
				return config['MAINTENACE']

	elif ('shell' in cmd[0]) or ('git' in cmd[0]):
		text = cmd[1].replace('—','--')
		if ('git' in cmd[0]): text = "git {}".format(text)
		r = utils.bash_(text)
		if len(r) == 0: r = lang('Shell_Not', 'tools', sudo=True)
		api.sendAdmin(chat_id=msg['chat']['id'],text=r)
	elif 'debug' in cmd[0]:
				if len(cmd) ==2 and cmd[1] == "user" and "reply" in msg:
					api.sendAdmin(chat_id=msg['chat']['id'],text="<code>{}</code>".format(json.dumps(msg['reply']['from'], indent=1)), parse_mode="HTML")
				else:
					api.sendAdmin(chat_id=msg['chat']['id'],text="<code>{}</code>".format(json.dumps(msg, indent=1)), parse_mode="HTML")
	
plugin = {
	'patterns': [
		"^[/!#](sudo) (update)$",
		"^[/!#](sudo) (manut)$",
		"^[/!#](sudo) (notmanut)$",
		"^[/!#](shell) (.+)$",
		"^[/!#](git) (.+)$",
		"^[/!#](debug)$",
		"^[/!#](debug) (user)$"
	],
	'function': Function,
	'name': "Admin",
	'sudo': True,
	}