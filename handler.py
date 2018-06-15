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
	print(lang('int', 'main', sudo='True').format(config.BOT['id']))

@app.before_request
def handler_():
	if request.method == 'GET':
		if request.path == "/webhook_int":
			requests.get(BOT['API'].format(token=BOT['token'],method='setWebhook'),
			                  params={"url": "{}/webhook/telegram".format(Sys['host']), 'max_connections': 1,
											 "allowed_updates": json.dumps(["message", "edited_message", "callback_query"])})
			return (lang('started_webhook', 'main', sudo='True'),200)
			
	elif request.method == 'POST':
		if request.path == "/webhook/telegram":
			from TelegramBOT import on_msg_receive, forward_to_msg, callback_query, service_to_message
			msg = request.get_json(silent=True, force=True)
			if Sys['debug_request'] == True:
				print(json.dumps(msg, indent=1))
			if ('message' in msg) or ('callback_query' in msg) or ('edited_message' in msg):
				if ('callback_query' in msg):
					callback_query(msg['callback_query'])
				elif ('edited_message' in msg):
					msg['message'] = msg['edited_message']
					msg['edited_message'] = None
				elif ('message' in msg):
					if ('new_chat_member' in msg['message']) or ('left_chat_member' in msg['message']) or ('group_chat_created' in msg['message']):
						service_to_message(msg['message'])
					elif ('forward_from' in msg['message']):
						forward_to_msg(msg['message'])
					elif ('reply_to_message' in msg['message']):
						rethink_reply(msg['message'])
					else:
						on_msg_receive(msg['message'])

@app.errorhandler(404)
def server_error(e):
	return flask.Response(status=200)

from TelegramBOT import loadplugins
if __name__ == '__main__':
	loadplugins()
	app.run(debug=config.Sys['debug_main'], port=int(os.getenv('PORT', 3000)), host='0.0.0.0')
