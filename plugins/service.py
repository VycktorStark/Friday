from main import utils, api, json, lang
def Function(msg, cmd, ln):
		if "botadded" in cmd[0]:
			api.sendAdmin(text=lang('alertbotadded', 'service', sudo=True).format(json.dumps(msg['chat'], indent=1), json.dumps(msg['adder'], indent=1)), parse_mode="HTML")
			return utils.msg_replace_(msg, lang('newGroup', ln))		
		elif "botremoved" in cmd[0]:
			api.sendAdmin(text=lang('alertbotremoved', 'service', sudo=True).format(json.dumps(msg['chat'], indent=1), json.dumps(msg['adder'], indent=1)), parse_mode="HTML")
						
					
plugin = {
	'patterns': [
		'^###(botadded)',
		'^###(botremoved)'
	],
	'function': Function,
	'name': "service",
	'sudo': True,
	}