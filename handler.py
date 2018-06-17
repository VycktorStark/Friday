#!/usr/bin/env python3
# encoding=utf8
from langs import lang
import flask, config, os, requests, json
app = flask.Flask(__name__)
BOT = config.BOT
Sys = config.Sys
request = flask.request

@app.before_first_request
def init_():
	print(lang('int', 'main', sudo='True').format(BOT['token'][:9]))

@app.before_request
def handler_():
	if request.method == 'GET':
		if request.path == "/webhook_int":
			requests.get(BOT['API'].format(token=BOT['token'],method='setWebhook'), params={"url": "{}/webhook".format(Sys['host']), 'max_connections': 1, "allowed_updates": json.dumps(["message", "edited_message", "callback_query"])})
			return (lang('started_webhook', 'main', sudo='True'),200)
	elif request.method == 'POST':
		msg = request.get_json(silent=True, force=True)
		if request.path == "/webhook":
			from TelegramBOT import callback_query_, status_service_, forward_msg_, reply_caption_, pinned_message_, msg_media_, msg_receive_, log_
			if Sys['debug_request'] == True: print(json.dumps(msg, indent=1))
			if ('message' in msg) or ('callback_query' in msg) or ('edited_message' in msg):
				if ('callback_query' in msg):
						callback_query_(msg['callback_query'])
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
								return flask.Response(status=200)
						elif ('new_chat_member' in msg_) or ('left_chat_member' in msg_) or ('group_chat_created' in msg_):
								status_service_(msg_)
						elif ('forward_from' in msg_):
								forward_msg_(msg_)
						elif ('reply_to_message' in msg_):
								reply_caption_(msg_)
						elif ('pinned_message' in msg_):
								pinned_message_(msg_)
						elif ('photo'  in msg_) or ('video'  in msg_) or ('document'  in msg_) or ('voice'  in msg_) or ('audio'  in msg_) or ('sticker'  in msg_) or ('entities'  in msg_):
								msg_media_(msg_)
						else:
								msg_receive_(msg_)

@app.errorhandler(404)
def server_error(e):
	return flask.Response(status=200)

from TelegramBOT import plugins_
if __name__ == '__main__':
	plugins_()
	app.run(debug=config.Sys['debug_main'], port=int(os.getenv('PORT', 3000)), host='0.0.0.0')
