from bot import *
def helpFunction(msg, cmd, ln):
	if len(cmd) < 2:
		return lang('help', ln)[0]['list_cmd'].format(plugi())
	else:
			try:
				return "{}".format(lang(plugi(cmd_=cmd[1]), ln)[0]['usage'])
			except Exception as error:
				return msg_replace(msg, lang('Error_request', ln))
def plugi(cmd_=None):
	x = '\n'
	lista = plugins_name
	for num,plug in enumerate(lista):
		if cmd_ != None:
			if cmd_.lower() == plug.lower() or str(cmd_) ==str(num):
				x = plug.lower()
		else:
			x = x+"{} {}\n".format(num,plug)
	return x
plugin = {
	'patterns': [
		"^/(help)$",
		"^/(help) (.+)$",
		"^/(ayudar)$",
		"^/(ayudar) (.+)$",
		"^/(ajuda)$",
		"^/(ajuda) (.+)$"
  ],
	'function': helpFunction,
	'name': "Help",
	'sudo': False, 
	}