#-*- coding: utf-8 -*-
__all__ = ['sendTelegram', 'sendMessage','forwardMessage', 
					 'editMessageText','editMessageCaption',
					 'editMessageReplyMarkup', 'answerCallbackQuery',
					'sendAdmin', 'sendInline', 'sendVoice', 'sendAudio']
from bot import *
def sendTelegram(url=None, query=None, file_=None): #function to answer the telegram request
	RESPOSTA = None
	try:
		data = requests.get(url=url, params=query, files=file_)
	except Exception as error:
		print(error)
		return False
	if data.status_code == 200:
		RESPOSTA = 'Done'
	else:
			code_err_tr(data)
			RESPOSTA = data.json()
	return flask.Response(status=200, headers={"Content-Type": "application/json"}, response=RESPOSTA)

def organize_argument(params, item=[]): #function to correct and organize argument
    return {key: value for key,value in params.items() if key not in ['self']+item}
	
def code_err_tr(dat):
	data = dat.json()
	error_code = data['error_code']
	status_code = dat.status_code
	if status_code != 403 and status_code != 429 and status_code != 111:
		try:
			sendAdmin(text=lang("ONE_FIELD", 'bad_request', sudo=True).format(lang(status_code, 'bad_request', sudo=True)), parse_mode='HTML')
		except Exception as error:
			print(error)
	else:
		sendAdmin(text=lang("error_occurred", 'bad_request', sudo=True).format(error_code, data['description']),parse_mode='HTML')
	return False

def sendMessage(chat_id=None, text=None, parse_mode=None,  disable_web_page_preview=None, disable_notification=None,  reply_to_message_id=None,  reply_markup=None, inline_keyboard=None):	
	return sendTelegram(config.BOT['API'].format(token=config.BOT['token'],method='sendMessage'), locals())

def forwardMessage(chat_id=None, from_chat_id=None, disable_notification=None,message_id=None):
		return sendTelegram(config.BOT['API'].format(token=config.BOT['token'],method='forwardMessage'), locals())

def editMessageText(chat_id=None, message_id=None,  inline_message_id=None, text=None, parse_mode=None, disable_web_page_preview=None, reply_markup=None, inline_keyboard=None):
		return sendTelegram(config.BOT['API'].format(token=config.BOT['token'],method='editMessageText'), locals())

def editMessageCaption(chat_id=None, message_id=None, inline_message_id=None, caption=None, reply_markup=None, inline_keyboard=None):
		return sendTelegram(config.BOT['API'].format(token=config.BOT['token'],method='editMessageCaption'), locals())

def editMessageReplyMarkup(chat_id=None, message_id=None, inline_message_id=None, reply_markup=None, inline_keyboard=None):	
		return sendTelegram(config.BOT['API'].format(token=config.BOT['token'],method='editMessageReplyMarkup'), locals())

def answerCallbackQuery(callback_query_id=None, text=None, show_alert=None,cache_time=None):	
		return sendTelegram(config.BOT['API'].format(token=config.BOT['token'],method='answercallbackquery'), locals())

def sendAdmin(chat_id=None,text=None, parse_mode=None, disable_web_page_preview=None,disable_notification=None, reply_to_message_id=None, reply_markup=None, inline_keyboard=None):
     if (chat_id == None) or (chat_id == 'suporte'): chat_id = config.Sys['suporte']
     else: chat_id = config.Sys['logs']
     return sendTelegram(config.BOT['API'].format(token=config.BOT['token'],method='sendMessage'), locals())
def sendAudio(chat_id=None, audio=None, duration=None, disable_notification=None, reply_to_message_id=None, reply_markup=None, inline_keyboard=None):
		audio=audio
		return sendTelegram(config.BOT['API'].format(token=config.BOT['token'],method='sendAudio'), organize_argument(locals(), item=['audio']), file_=audio)

def sendVoice(chat_id=None, voice=None, duration=None, disable_notification=None, reply_to_message_id=None, reply_markup=None, inline_keyboard=None):
		voice=voice
		return sendTelegram(config.BOT['API'].format(token=config.BOT['token'],method='sendVoice'), organize_argument(locals(), item=['voice']), file_=voice)

def sendInline(inline_query_id=None, results=None, cache_time=None, is_personal=None, next_offset=None, switch_pm_text=None, switch_pm_parameter=None):
		return sendTelegram(config.BOT['API'].format(token=config.BOT['token'],method='answerInlineQuery'), locals())

