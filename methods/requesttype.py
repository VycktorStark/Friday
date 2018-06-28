from main import requests, json, Response, lang, config
__all__ = ['sendRequest', 'sendRequestTelegram', 'organize_argument', 'code_err_tr']
url = config['TELEGRAM_API']
def sendRequest(url, type=None, params=None, headers=None, auth=None, files=None, setime=None, post=False):
		try:
				if post is True:
							data = requests.post(url, params=params, headers=headers, auth=auth, files=files)
				else:
							data = requests.get(url, params=params, headers=headers, auth=auth, files=files)
		except Exception as error:
				print(error)
		if data.status_code == 200:
			return (200, data)
		else:
				print('Error in request! {}\n{}\n\n{}'.format(url, params, data.text))
		return (400, data)

def sendRequestTelegram(method, query=None, file_=None, post=None):
		global RESPOSTA
		code, data = sendRequest(url=url.format(method=method), params=query, files=file_, post=post)
		if (code == 200):
				RESPOSTA = data.json()
		else:
			query['text'] = code_err_tr(data)
			query['parse_mode'] = 'HTML'
			code, data = sendRequest(url=url.format(method='sendMessage'), params=query)
			RESPOSTA = data.json()
		return Response(status=200, headers={"Content-Type": "application/json"}, response=RESPOSTA)
	
def organize_argument(params, item=[]): #function to correct and organize argument
    return {key: value for key,value in params.items() if key not in ['self']+item}
	
def code_err_tr(dat):
		data = dat.json()
		error_code = data['error_code']
		status_code = dat.status_code
		if (status_code != 403) and (status_code != 429) and (status_code != 111):
			try:
				return lang("ONE_FIELD", 'bad_request', sudo=True).format(lang(status_code, 'bad_request', sudo=True))
			except Exception as error:
				return lang("error_occurred", 'bad_request', sudo=True).format(error_code, data['description'])
		return False