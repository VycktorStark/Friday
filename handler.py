#!/usr/bin/env python3
# encoding=utf8
import flask, config, os, requests, json
app = flask.Flask(__name__)		
from bot import loadplugins
def init():
	#https://api.telegram.org/bot<TOKEN>/setwebhook?url=https://www.example.com/webhook/telegram&max_connections=1&allowed_updates=["message", "edited_message", "callback_query", "inline_query", "chosen_inline_result"]
	try:
		data = requests.get(config.BOT['API'].format(token=config.BOT['token'],method='setWebhook'),
			                  headers={"Content-Type": "application/json"},
			                  params={"url": "{}/webhook/telegram".format(config.Sys['host']), 'max_connections': 1,
											 "allowed_updates": json.dumps(["message", "edited_message", "callback_query", "inline_query", "chosen_inline_result"])})
		print(data)
	except Exception as error:
		print(error)
	return 'ok'
@app.before_first_request
def init_():
	from langs import lang
	from bot import sendAdmin
	print("\033[31m  {}\n  {} ".format(lang('int', 'main', sudo='True'), lang('id_text', 'main', sudo='True').format(config.BOT['id'])))
	sendAdmin(text="<b>{}</b>".format(lang('int', 'main', sudo='True')), parse_mode="HTML")
@app.before_request
def handler_():
	if flask.request.method == 'GET':
		if flask.request.path == "/webhook_int":
			init()
	if flask.request.method == 'POST':
		if flask.request.path == "/webhook/telegram":
			from bot import on_msg_receive, time_atual, forward_to_msg, callback_query, service_to_message
			msg = flask.request.get_json(silent=True, force=True)
			if config.Sys['debug_request'] == True:
				print(json.dumps(msg, indent=1))
			if time_atual(msg['message']['date']) > 10: return flask.Response(status=200)
			if ('message' in msg) or ('callback_query' in msg) or ('edited_message' in msg):
				if ('callback_query' in msg):
					callback_query(msg['callback_query'])
				elif ('new_chat_member' in msg['message']) or ('left_chat_member' in msg['message']) or ('group_chat_created' in msg['message']):
					service_to_message(msg['message'])
				elif ('edited_message' in msg):
					msg['message'] = msg['edited_message']
					msg['edited_message'] = None
				elif ('forward_from' in msg['message']):
					forward_to_msg(msg['message'])
				elif ('reply_to_message' in msg['message']):
					rethink_reply(msg['message'])
				else:
					on_msg_receive(msg['message'])

@app.errorhandler(404)
def server_error(e):
	return flask.Response(status=200)

if __name__ == '__main__':
	loadplugins()
	app.run(debug=config.Sys['debug_main'], port=int(os.getenv('PORT', 3000)), host='0.0.0.0')
