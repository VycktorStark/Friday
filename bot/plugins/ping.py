def Ping(msg, cmd, ln):
	return 'pong'

plugin = {
	'patterns': [
		"^/(ping)$"
	],
	'function': Ping,
	'name': "Ping",
	'sudo': False,
	}