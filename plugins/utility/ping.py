def Function(msg, cmd, ln):
	return 'pong'

plugin = {
	'patterns': [
		"^[/!#](ping)$"
	],
	'function': Function,
	'name': "Ping",
	'sudo': False,
	}