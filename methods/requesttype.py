from main import requests, json, Response, lang, config
__all__ = ['sendRequest', 'sendRequestTelegram', 'organize_argument', 'code_err_tr']
url = config['TELEGRAM_API']
def sendRequest(url, type=None, params=None, headers=None, auth=None, files=None, setime=None, post=False):
		try:
				if post == True:
							data = requests.post(url, params=params, headers=headers, auth=auth, files=files)
				else:
							data = requests.get(url, params=params, headers=headers, auth=auth, files=files)
		except Exception as error: pass
		if data.status_code == 200:
			return (200, data)
		else:
			return (400, data)

def sendRequestTelegram(method, query=None, file_=None, post=None):
		global RESPOSTA
		status_code, data = sendRequest(url=url.format(method=method), params=query, files=file_, post=post)
		if (status_code != 200) and ('description' in data.json()):
			if (status_code == 400): status_code = getcode(data.json()['description'])
			if (status_code != 403) and (status_code != 429) and (status_code != 111) and (status_code != 132):
				query['text'] = lang("error_occurred", 'bad_request', sudo=True).format(status_code, data.json()['description'])
				query['parse_mode'] = 'HTML'
			query['chat_id'] = config['LOGS']
			code, data = sendRequest(url=url.format(method='sendMessage'), params=query)
		RESPOSTA = data.json()
		if not RESPOSTA['ok']:
			return Response(status=200)
		return Response(status=200, headers={"Content-Type": "application/json"}, response=RESPOSTA)
	
def organize_argument(params, item=[]):
    return {key: value for key,value in params.items() if key not in ['self']+item}

def getcode(error):
		from langs.languages_sys import sudo_string_lang
		try:
			r = sudo_string_lang['bad_request'][0][error]
		except Exception as error_:
			r = lang("error", 'bad_request', sudo=True).format(error_, error)
		return r
