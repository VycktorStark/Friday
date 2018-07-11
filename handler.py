from main import app, api, config, lang, request, Response, json, msg_receive_
@app.before_first_request
def init_(): print(lang('int', 'main', sudo='True').format(config['IDBOT']))
@app.errorhandler(404)
def server_error(e): return Response(status=200)

@app.before_request
def handler_():
	if request.method == 'GET' and request.path == "/webhook_int":
		allowed = ["message", "edited_message", "callback_query"]
		r = api.setWebhook("{}/webhook".format(request.host), max_connections=int(1), allowed_updates=json.dumps(allowed))
		resp = lang('started_webhook', 'main', sudo='True').format(r['description'])
		return Response(response=resp,status=200)
		
	elif request.method == 'POST' and request.path == "/webhook":
		msg = request.get_json(silent=True, force=True)
		if config['DEBUG_REQUEST'] == True: print(json.dumps(msg, indent=1))
		if ('message' in msg) or ('callback_query' in msg) or ('edited_message' in msg):
			if ('callback_query' in msg):
					msg['text'] = '###cb: {}'.format(msg['data'])
					msg['old_text'] = msg['message']['text']
					msg['old_date'] = msg['message']['date']
					msg['cb'] = True
					msg['cb_id'] = msg['id']
					msg['message_id'] = msg['message']['message_id']
					msg['chat'] = msg['message']['chat']
					msg['message'] = None
					return msg_receive_(msg)
			elif ('edited_message' in msg):
					msg['message'] = msg['edited_message']
					msg['edited_message'] = None
			elif ('message' in msg):
					msg = msg['message']
					msg['action'] = True
					msg['text_action'] = True
					if 'text' in msg: msg['action'] = "###text"
					if ("migrate_to_chat_id" in msg) or ('migrate_from_chat_id' in msg):
							msg['action'] = '###migrate'
							if ("migrate_from_chat_id" in msg): msg['migrate_to_chat_id'] = msg['migrate_from_chat_id']
							msg['old'] = msg['migrate_to_chat_id']
							msg['new'] = msg['chat']['id']
							return msg_receive_(msg)
					elif ('new_chat_member' in msg) or ('left_chat_member' in msg) or ('group_chat_created' in msg):
						msg['service'] = True
						if ("new_chat_member" in msg):
								if str(msg['new_chat_member']['id']) == str(config['IDBOT']):
										msg['action'] = '###botadded'
								else: 
										msg['action'] = '###added'
										msg['adder'] = msg['from']
										msg['added'] = msg['new_chat_member']
						elif ("left_chat_member" in msg):
								if str(msg['left_chat_member']['id']) == str(config['IDBOT']): 
										msg['action'] = '###botremoved'
								else: 
										msg['action'] = '###removed'
										msg['remover'] = msg['from']
										msg['removed'] = msg['left_chat_member']
						elif ("group_chat_created" in msg):
										msg['chat_created'] = True
										msg['adder'] = msg['from']
										msg['action'] = '###botadded'
						return msg_receive_(msg)
					elif ('forward_from' in msg):
						if (msg['forward_from']["is_bot"] == True): msg['action'] = '###forwardbot'
						msg['action'] = '###forward'
						return msg_receive_(msg)
					elif ('reply_to_message' in msg):
						msg['action'] = "###reply"
						msg['reply'] = msg["reply_to_message"]
						if ("caption" in msg['reply']): msg['text'] = msg['reply']['caption']
						return msg_receive_(msg)
					elif ('pinned_message' in msg):
						msg['action'] = "###pinned_message"
						msg['text'] = msg['pinned_message']['text']
						return msg_receive_(msg)
					elif ('photo'  in msg) or ('video'  in msg) or ('document'  in msg) or ('voice'  in msg) or ('audio'  in msg) or ('sticker'  in msg) or ('entities'  in msg):
						if ('photo' in msg):																							msg['action'] = "###Photo"
						elif ('sticker' in msg):																					msg['action'] = "###Sticker"
						elif ('voice' in msg):																						msg['action'] = "###Voice"
						elif ('audio' in msg):																						msg['action'] = "###Audio"
						elif ('video' in msg):																						msg['action'] = "###Video"
						elif ('contact' in msg):																					msg['action'] = "###contact"
						elif ('document' in msg and msg['document']['mime_type']):
								document = msg['document']['mime_type']
								if (document == "video/mp4"):																	msg['action'] = "###gif"
								elif (document == "application/x-bittorrent"):								msg['action'] = "###pdf_file"    
								elif (document == "application/vnd.android.package-archive"):	msg['action'] = "###app"    
								elif (document == "application/x-rar"):												msg['action'] = "###rar_file"    
								elif (document == "application/x-zip"):												msg['action'] = "###zip_file"    
								elif (document == "text/x-python"):														msg['action'] = "###script_in_python"    
								elif (document == "text/plain"):															msg['action'] = "###text_file"    
								elif (document == "application/x-shellscript"):								msg['action'] = "###script_in_shell"    
								elif (document == "text/x-lua"):															msg['action'] = "###script_in_lua"    
								elif (document == "text/html"):																msg['action'] = "###script_in_HTML"    
								elif (document == "application/json"):												msg['action'] = "###script_in_JSON"    
								elif (document == "application/javascript"):									msg['action'] = "###script_in_JavaScript"    
								elif (document == "application/octet-stream"):								msg['action'] = "###script_in_octet-stream"    
								elif (document == "text/markdown"):														msg['action'] = "###script_in_Markdown"    
								elif (document == "application/x-yaml"):											msg['action'] = "###script_in_yaml."
								else: 																												msg['action'] = "###file"
						elif ('entities' in msg):
								if (msg['entities'][0]['type'] == "url"):											msg['action'] = '###url'
								elif (msg['entities'][0]['type'] == "mention"):								msg['action'] = '###mention'
								elif (msg['entities'][0]['type'] == "bot_command"):
																																							msg['action'] = '###bot_command'
																																							msg['text'] = msg['text'].replace(
																																								"@{}".format(config['USERNAMEBOT']),'')
						return msg_receive_(msg)
					else: msg_receive_(msg)