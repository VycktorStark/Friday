sudo_string_lang = {
	########## bad request ##########
	"bad_request": [{
			'ONE_FIELD': '<b>An error has occurred:</b> {}',
			"error_occurred": "<b>An error occurred with code:</b> <code>{}</code>\n{}",
			400: 'Message can not be modified: /',
			112: 'Can not parse message text',
			113: 'Now this group has become a supergroup, Curti hein!',
			114: 'Message can not be forwarded: /',
			115: 'The text of this message is empty',
			116: 'This message was not found',
			117: 'chat does not exist',
			118: "This message is too long",
			119: 'User not found',
			120: 'Unable to parse the keyboard marking JSON object',
			123: 'Wrong request: object expected as response markup',
			124: 'The id does not exist',
			125: 'The channel is private',
			126: 'This message is too long',
			127: 'The specified id is incorrect',
			130: 'File type to send incompatible',
			131: 'Message Id is Incorrect',
			403: 'Start a conversation with me in private',
			429: 'You Exceeded the Limit of Requests - Please Wait A Little!',
			430: 'Extinguished timeout.'
	}],
	########## tools.py ##########
	'tools':[{
		"Shell_Not":  '<code>Nothing was done.</code>',
	}],
	########## main.py ##########
	'main':[{
		"plugin_err":'Failed plugin: {}',
		"migrate":'\033[37m* The chat is being migrated para \033[36msupergrupo\033[37',
		"sudo_not":'Hey, you can not tell me.!',
    'int': '\033[31m  Friday was started!\n  \033[37mID: \033[31m{}\033[37m',
    'jump line':'\n___________________\n',
    'id_text': '\033[37mID: \033[31m{}\033[37m',
    "viewer": '''\033[37m\033[36m{user} \033[37m(\033[31m{user_id}\033[37m) {SendType}
- Details
* Sent from a {chat_name} (ID: \033[31m{chat_id}\033[37m)
* Message send: \033[31m{text}\033[37m''',
		'cmd_detected':'\033[37m* cmd executed: \033[31m{}\033[37m',
		'started_webhook': '<li>Ok<h1>Bot started </h1></li>',
		'nottokenFB': 'Missing check token matching',
		'OktokenFB': "Check token match - OK"
	}],
	"service":[{
		"alertbotadded": "#ALERT:\n<b> Bot foi added to a group:</b>\n<code>Group Information: {}\nUser Information:{}</code>",
		"alertbotremoved": "#ALERT:\n<b> Bot foi kicked to a group:</b>\n<code>Group Information: {}\nUser Information:{}</code>"
	}]
}
