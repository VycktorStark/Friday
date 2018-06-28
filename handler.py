from __init__ import app, config, lang, request, requests, Response, json, bot
@app.before_first_request
def init_():
	print(lang('int', 'main', sudo='True').format(config['IDBOT']))

@app.before_request
def handler_():
	if request.method == 'GET':
		if request.path == "/webhook_int":
			params_ = dict()
			params_['url'] = "{}/webhook".format(request.host)
			params_['max_connections'] = int(1)
			params_['allowed_updates'] =json.dumps(["message", "edited_message", "callback_query"])
			requests.get(config['TELEGRAM_API'].format(method='setWebhook'), params=params_)
			return Response(response=lang('started_webhook', 'main', sudo='True'),status=200)
		
	elif request.method == 'POST':
		msg = request.get_json(silent=True, force=True)
		if request.path == "/webhook":
			if config['DEBUG_REQUEST'] == True: print(json.dumps(msg, indent=1))
			if ('message' in msg) or ('callback_query' in msg) or ('edited_message' in msg):
				if ('callback_query' in msg):
						bot.callback_query_(msg['callback_query'])
				elif ('edited_message' in msg):
						msg['message'] = msg['edited_message']
						msg['edited_message'] = None
				elif ('message' in msg):
						msg_ = msg['message']
						msg_['action'] = True
						msg_['text_action'] = True
						if 'text' in msg_: msg_['action'] = "###text"
						if ("migrate_from_chat_id" in msg_) or ("migrate_to_chat_id" in msg_):
								old = msg['chat']['id']
								new = msg['migrate_to_chat_id']
								log_(lang("migrate", "main", sudo=True))
								return Response(status=200)
						elif ('new_chat_member' in msg_) or ('left_chat_member' in msg_) or ('group_chat_created' in msg_):
								status_service_(msg_)
						elif ('forward_from' in msg_):
								bot.forward_msg_(msg_)
						elif ('reply_to_message' in msg_):
								bot.reply_caption_(msg_)
						elif ('pinned_message' in msg_):
								bot.pinned_message_(msg_)
						elif ('photo'  in msg_) or ('video'  in msg_) or ('document'  in msg_) or ('voice'  in msg_) or ('audio'  in msg_) or ('sticker'  in msg_) or ('entities'  in msg_):
								bot.msg_media_(msg_)
						else:
								bot.msg_receive_(msg_)
								
@app.errorhandler(404)
def server_error(e):
	return Response(status=200)