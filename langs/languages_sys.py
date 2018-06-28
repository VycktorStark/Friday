sudo_string_lang = {
	########## bad request ##########
	'bad_request': [{
			'error': '<b>An error has occurred:</b> {}',
			"error_occurred": "<b>An error occurred with code:</b> <code>{}</code>\n{}",
			'Bad Request: Not enough rights to kick participant': 101,
			'Bad Request: USER_ADMIN_INVALID': 102,
			'Bad Request: method is available for supergroup chats only': 103,
			'Bad Request: Only creator of the group can kick administrators from the group': 104,
			'Bad Request: Need to be inviter of the user to kick it from the group': 105,
			'Bad Request: USER_NOT_PARTICIPANT': 106,
			'Bad Request: CHAT_ADMIN_REQUIRED': 107,
			'Bad Request: there is no administrators in the private chat': 108,
			'Bad Request: PEER_ID_INVALID': 110,
			'Bad Request: message is not modified': 111,
			'Bad Request: Can\'t parse message text: Can\'t find end of the entity starting at byte offset 0': 112,
			'Bad Request: group chat is migrated to a supergroup chat': 113,
			'Bad Request: Message can\'t be forwarded': 114,
			'Bad Request: message text is empty': 115,
			'Bad Request: message not found': 116,
			'Bad Request: chat not found': 117,
			'Bad Request: Message is too long': 118,
			'Bad Request: User not found': 119,
			'Bad Request: Can\'t parse reply keyboard markup JSON object': 120,
			'Bad Request: Field \\\"inline_keyboard\\\" of the InlineKeyboardMarkup should be an Array of Arrays': 121,
			'Bad Request: Can\'t parse inline keyboard button: InlineKeyboardButton should be an Object': 122,
			'Bad Request: Object expected as reply markup': 123,
			'Bad Request: QUERY_ID_INVALID': 124,
			'Bad Request: CHANNEL_PRIVATE': 125,
			'Bad Request: MESSAGE_TOO_LONG': 126,
			'Bad Request: wrong user_id specified': 127,
			'Bad Request: Too big total timeout [%d%.]+': 128,
			'Bad Request: BUTTON_DATA_INVALID': 129,
			'Bad Request: Type of file to send mismatch': 130,
			'Bad Request: MESSAGE_ID_INVALID': 131,
			'Bad Request: can\'t parse entities: Unexpected end tag at byte offset 0': 132,
			'Bad Request: Bot was blocked by the user': 403,
			'Bad Request: Too many requests: retry later': 429,
			'Bad Request: Too big total timeout': 430,
	}],
	########## tools.py ##########
	'tools':[{
		"Shell_Not":  'Nothing was done.',
	}],
	########## main.py ##########
	'main':[{
		"plugin_err":'Failed to execute: {}\nDetail: {}',
		"migrate":'\033[37m* The chat is being migrated para \033[36msupergrupo\033[37',
		"sudo_not":'Hey, you can not tell me.!',
    'int': '\033[31m  Friday was started!\n  \033[37mID: \033[31m{}\033[37m',
    'jump line':'\n___________________\n',
    'id_text': '\033[37mID: \033[31m{}\033[37m',
		'started_webhook': '<li>Ok<h1>Bot started </h1></li>',
		'nottokenFB': 'Missing check token matching',
		'OktokenFB': "Check token match - OK"
	}],
	########## service.py ##########
	"service":[{
		"alertbotadded": "#ALERT:\n<b> Bot foi added to a group:</b>\n<code>Group Information: {}\nUser Information:{}</code>",
		"alertbotremoved": "#ALERT:\n<b> Bot foi kicked to a group:</b>\n<code>Group Information: {}\nUser Information:{}</code>"
	}],
	########## viewer ##########
	'viewer':[{
		'###pinned_message': 'pinned message in chat\nDetails: {}',
		'###added':"a user has been added the group",
		"###removed":"a user has been removed the group",
		"###botadded":"the bot was added to the group",
		'###botremoved':"the bot was removed to the group",
		"###forward":"message forwarded: {}",
		"###forwardbot":"message forwarded from a bot: {}",
		"###Photo": "sent a foto.",
		"###Sticker": "sent a Sticker.",
		"###Voice": "sent a voz.",
		"###Audio": "sent a Audio.",
		"###Video": "sent a Video.",
		"###contact": "sent a contact.",
		"###gif": "sent a Gif.",
		"###pdf_file": "sent a pdf file.",
		"###app": "sent a App.",
		"###rar_file": "sent a RAR file.",
		"###zip_file": "sent a Zip file.",
		"###script_in_python": "sent a Script in python.",
		"###text_file": "sent a Script de texto simples.",
		"###script_in_shell": "sent a Script in shell.",
		"###script_in_lua": "sent a Script in lua.",
		"###script_in_HTML": "sent a Script in HTML.",
		"###script_in_JSON": "sent a Script in JSON.",
		"###script_in_JavaScrip": "sent a Script in JavaScript.",
		"###script_in_octet-stream": "sent a Script in octet-stream.",
		"###script_in_Markdown": "sent a Script in Markdown." ,
		"###script_in_yaml": "sent a Script in yaml.",
		"###file":"sent document",
		'###url':"sent a url: {}",
		'###text':"sent a message: {}",
		"###reply":"replied the following text: {}",
		'###mention': "mentioned someone\ndetails of the mention: {}",
		"###bot_command": '\033[37m sent a command:: \033[31m{}\033[37m',
		"viewer": '''\033[37m\033[36m{user} \033[37m(\033[31m{user_id}\033[37m) {text}
- Details
* Sent from a {chat_name} (ID: \033[31m{chat_id}\033[37m)
* performed t he action: \033[31m{SendType}\033[37m
'''
	}]
}