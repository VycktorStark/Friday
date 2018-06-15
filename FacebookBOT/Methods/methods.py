import flask, config
def sendRequest(data=None):
  params = {"access_token": config.Sys['tokenFBBOT']}
  headers = {"Content-Type": "application/json"}
  requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=json.dumps(data))
	return flask.Response(status=200)
def sendMessage(chat_id=None, text=None):
    return sendRequest(data={"recipient": {"id": chat_id},"message": {"text": text}})
