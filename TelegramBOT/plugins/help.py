from TelegramBOT import *
def Function(msg, cmd, ln):
	if (len(cmd) < 2):
		return lang('help', ln)[0]['list_cmd'].format(plugi())
	else:
			try:
				return "{}".format(lang(plugi(cmd_=cmd[1]), ln)[0]['usage'])
			except Exception as error:
				return msg_replace(msg, lang('Error_request', ln))
def plugi(cmd_=None):
	lista = []
	for aPlug in plugins:
		if not aPlug["sudo"]== True:
				lista.append(aPlug)
	x = '\n'
	for num,plug in enumerate(lista):
			if cmd_ != None:
				if cmd_.lower() == plug['name'].lower() or str(cmd_) ==str(num):
					x = plug['name'].lower()
			else:
				x = x+"{} {}\n".format(num,lista[num]['name'])
	return x
plugin = {
	'patterns': [
		"^[/!#](help)$",
		"^[/!#](help) (.+)$",
		"^[/!#](ayudar)$",
		"^[/!#](ayudar) (.+)$",
		"^[/!#](ajuda)$",
		"^[/!#](ajuda) (.+)$"
  ],
	'function': Function,
	'name': "Help",
	'sudo': False, 
	}
