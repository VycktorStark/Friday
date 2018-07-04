import requests, json
def Function(msg, matches, peer):
	req = requests.get('http://api.icndb.com/jokes/random').json()
	return req['value']['joke']

plugin = {
	'patterns': [
		"^[/!#](joke)$"
	],
	'function': Function,
	'name': "joke",
	'sudo': False,
	}