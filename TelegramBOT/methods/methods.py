#-*- coding: utf-8 -*-
__all__ = [
'sendRequest', 
'sendRequestTelegram', 
'getUpdates',
'setWebhook',
'deleteWebhook',
'getWebhookInfo',
'getMe',
'getFile',
'sendMessage',
'sendAdmin', 
'deleteMessage',
'forwardMessage', 
'editMessageText',
'editMessageCaption',
'editMessageReplyMarkup', 
'sendPhoto',
'sendAudio',
'sendVoice', 
'sendVideo',
'sendVideoNote',
'sendDocument',
'sendContact',
'sendMediaGroup',
'getStickerSet',
'createNewStickerSet',
'addStickerToSet',
'setStickerPositionInSet',
'deleteStickerFromSet',
'sendLocation',
'sendVenue',
'editMessageLiveLocation',
'stopMessageLiveLocation',
'getChat',
'leaveChat',
'kickChatMember',
'unbanChatMember',
'sendChatAction',
'getChatAdministrators',
'getChatMembersCount',
'getChatMember',
'restrictChatMember',
'promoteChatMember',
'setChatTitle',
'setChatDescription',
'exportChatInviteLink',
'setChatPhoto',
'deleteChatPhoto',
'getUserProfilePhotos',
'setChatStickerSet',
'deleteChatStickerSet',
'pinChatMessage',
'unpinChatMessage',
'answerCallbackQuery',
'answerInlineQuery']
from TelegramBOT import requests, json, config, flask, log_

def sendRequest(url, type=None, params=None, headers=None, auth=None, files=None, setime=None, post=False):
		try:
				if post==True:
							data = requests.post(url, params=params, headers=headers, auth=auth, files=files)
				else:
							data = requests.get(url, params=params, headers=headers, auth=auth, files=files)
		except Exception as error:
				print(error)
		if data.status_code == 200:
			return 200, data
		else:
				log_('Error in request! {}\n{}\n\n{}'.format(url, params, data.text))
		return 400, data

def sendRequestTelegram(methods=None, query=None, file_=None):
		global RESPOSTA
		url = config.BOT['API'].format(token=config.BOT['token'] ,method=methods)
		code, data = sendRequest(url=url, params=query, files=file_)
		if code == 200:
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

def getUpdates(offset=None, limit=None, timeout=None, allowed_updates=None):
		return sendRequestTelegram('getUpdates', locals())

def setWebhook(url, certificate=None, max_connections=None, allowed_updates=None):
		return sendRequestTelegram('setWebhook', locals())

def deleteWebhook():
		return sendRequestTelegram('deleteWebhook')

def getWebhookInfo():
		return sendRequestTelegram('getWebhookInfo')

def getMe():
		return sendRequestTelegram('getMe')
	
def getFile(file_id=None):
		return sendRequestTelegram('getFile', locals())

def sendMessage(chat_id=None, text=None, parse_mode=None,  disable_web_page_preview=None, disable_notification=None,  reply_to_message_id=None,  reply_markup=None, inline_keyboard=None):	
		return sendRequestTelegram('sendMessage', locals())
	
def sendAdmin(chat_id=None,text=None, parse_mode=None, disable_web_page_preview=None,disable_notification=None, reply_to_message_id=None, reply_markup=None, inline_keyboard=None):
	if (chat_id == None) or (chat_id == 'suporte'): 
			chat_id = config.Sys['logs'] or 438131290
	return sendRequestTelegram('sendMessage', locals())

def deleteMessage(chat_id=None, message_id=None):
		return sendRequestTelegram('deleteMessage', locals())

def forwardMessage(chat_id=None, from_chat_id=None, disable_notification=None,message_id=None):
		return sendRequestTelegram('forwardMessage', locals())

def editMessageText(chat_id=None, message_id=None,  inline_message_id=None, text=None, parse_mode=None, disable_web_page_preview=None, reply_markup=None, inline_keyboard=None):
		return sendRequestTelegram('editMessageText', locals())

def editMessageCaption(chat_id=None, message_id=None, inline_message_id=None, caption=None, reply_markup=None, inline_keyboard=None):
		return sendRequestTelegram('editMessageCaption', locals())

def editMessageReplyMarkup(chat_id=None, message_id=None, inline_message_id=None, reply_markup=None, inline_keyboard=None):	
		return sendRequestTelegram('editMessageReplyMarkup', locals())

def sendPhoto(chat_id=None, photo=None, capition=None, parse_mode=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
		photo=photo
		return sendRequestTelegram('sendPhoto', organize_argument(locals(), item=['photo']), file_=photo)

def sendAudio(chat_id=None, audio=None, duration=None, disable_notification=None, reply_to_message_id=None, reply_markup=None, inline_keyboard=None):
		audio=audio
		return sendRequestTelegram('sendAudio', organize_argument(locals(), item=['audio']), file_=audio)

def sendVoice(chat_id=None, voice=None, duration=None, disable_notification=None, reply_to_message_id=None, reply_markup=None, inline_keyboard=None):
		voice=voice
		return sendRequestTelegram('sendVoice', organize_argument(locals(), item=['voice']), file_=voice)
	
def sendVideo(chat_id=None, video=None, duration=None, width=None, height=None, caption=None, parse_mode=None, supports_streaming=None, disable_notification=False, reply_to_message_id=None, reply_markup=None):
		video=video
		return sendRequestTelegram('sendVideo', organize_argument(locals(), item=['video']), file_=video)

def sendVideoNote(chat_id=None, video_note=None, duration=None, length=None, disable_notification=False, reply_to_message_id=None, reply_markup=None):
		video_note=video_note
		return sendRequestTelegram('sendVideoNote', organize_argument(locals(), item=['video_note']), file_=video_note)
	
def sendDocument(chat_id=None, document=None, caption=None, parse_mode=None, disable_notification=False, reply_to_message_id=None, reply_markup=None):
		document=document
		return sendRequestTelegram('sendDocument', organize_argument(locals(), item=['document']), file_=document)

def sendContact(chat_id, phone_number=None, first_name=None, last_name=None, disable_notification=False, reply_to_message_id=None, reply_markup=None):
		return sendRequestTelegram('sendContact', locals())

def setChatStickerSet(chat_id=None, sticker_set_name=None):
		return sendRequestTelegram('setChatStickerSet', locals())

def deleteChatStickerSet(chat_id=None):
		return sendRequestTelegram('deleteChatStickerSet', locals())

def getStickerSet(name=None):
		return sendRequestTelegram('getStickerSet', locals())

def uploadStickerFile(user_id=None, png_sticker=None):
		return sendRequestTelegram('uploadStickerFile', locals())

def createNewStickerSet(user_id=None, name=None, title=None, png_sticker=None, emojis=None, contains_masks=None, mask_position=None):
		return sendRequestTelegram('createNewStickerSet', locals())

def addStickerToSet(user_id=None, name=None, png_sticker=None, emojis=None, mask_position=None):
		return sendRequestTelegram('addStickerToSet', locals())

def setStickerPositionInSet(sticker=None, position=None):
		return sendRequestTelegram('setStickerPositionInSet', locals())

def deleteStickerFromSet(sticker=None):
		return sendRequestTelegram('deleteStickerFromSet', locals())

def sendLocation(chat_id=None, latitude=None, longitude=None, live_period=None, disable_notification=False, reply_to_message_id=None, reply_markup=None):
		return sendRequestTelegram('sendLocation', locals())

def sendVenue(chat_id=None, latitude=None, longitude=None, title=None, address=None, foursquare_id=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
		return sendRequestTelegram('sendVenue', locals())

def editMessageLiveLocation(latitude, longitude, chat_id=None, message_id=None, inline_message_id=None, reply_markup=None):
		return sendRequestTelegram('editMessageLiveLocation', locals())

def stopMessageLiveLocation(chat_id=None, message_id=None, inline_message_id=None, reply_markup=None):
		return sendRequestTelegram('stopMessageLiveLocation', locals())
	
def sendMediaGroup(chat_id=None, media=None, disable_notification=None, reply_to_message_id=None):
		media=media
		return sendRequestTelegram('sendMediaGroup', organize_argument(locals(), item=['media']), file_=media)
	
	### Group
	
def getChat(chat_id=None):
		return sendRequestTelegram('getChat', locals())
	
def leaveChat(chat_id=None):
		return sendRequestTelegram('leaveChat', locals())
	
def kickChatMember(chat_id=None, user_id=None, until_date=None):
		return sendRequestTelegram('kickChatMember', locals())

def unbanChatMember(chat_id=None, user_id=None):
		return sendRequestTelegram('unbanChatMember', locals())
	
def sendChatAction(chat_id=None, action=None):
		return sendRequestTelegram('sendChatAction', locals())
	
def restrictChatMember(chat_id=None, user_id=None, until_date=None, can_send_messages=None, can_send_media_messages=None, can_send_other_messages=None, can_add_web_page_previews=None):
		return sendRequestTelegram('restrictChatMember', locals())

def promoteChatMember(chat_id=None, user_id=None, can_change_info=None, can_post_messages=None, can_edit_messages=None, can_delete_messages=None, can_invite_users=None, can_restrict_members=None, can_pin_messages=None, can_promote_members=None):
		return sendRequestTelegram('promoteChatMember', locals())

def getChatAdministrators(chat_id=None):
		return sendRequestTelegram('getChatAdministrators', locals())

def getChatMembersCount(chat_id):
		return sendRequestTelegram('getChatMembersCount', locals())

def getChatMember(chat_id=None, user_id=None):
		return sendRequestTelegram("getChatMember", locals())
	
def setChatTitle(chat_id=None, title=None):
		return sendRequestTelegram('setChatTitle', locals())

def setChatDescription(chat_id=None, description=None):
		return sendRequestTelegram('setChatDescription', locals())

def exportChatInviteLink(chat_id=None):
		return sendRequestTelegram('exportChatInviteLink', locals())

def setChatPhoto(chat_id=None, photo=None):
		photo=photo
		return sendRequestTelegram('setChatPhoto', organize_argument(locals(), item=['photo']), file_=photo)
	
def deleteChatPhoto(chat_id=None):
		return sendRequestTelegram('deleteChatPhoto', locals())

def getUserProfilePhotos(user_id=None, offset=None, limit=None):
		return sendRequestTelegram('getUserProfilePhotos', locals())

def pinChatMessage(chat_id=None, message_id=None, disable_notification=False):
		return sendRequestTelegram('pinChatMessage', locals())

def unpinChatMessage(chat_id=None):
		return sendRequestTelegram('unpinChatMessage', locals())

def answerCallbackQuery(callback_query_id=None, text=None, show_alert=None,cache_time=None):	
		return sendRequestTelegram('answercallbackquery', locals())

def answerInlineQuery(inline_query_id=None, results=None, cache_time=None, is_personal=None, next_offset=None, switch_pm_text=None, switch_pm_parameter=None):
		return sendRequestTelegram('answerInlineQuery', locals())
