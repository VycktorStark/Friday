#-*- coding: utf-8 -*-
__all__ = ['METHOD']
from main import config
from .requesttype import organize_argument, sendRequestTelegram
class METHOD:
			def getUpdates(offset=None, limit=None, timeout=None, allowed_updates=None):
					r = sendRequestTelegram('getUpdates', locals())
					return r.response

			def setWebhook(url, certificate=None, max_connections=None, allowed_updates=None):
					r = sendRequestTelegram('setWebhook', locals())
					return r.response

			def deleteWebhook():
					r = sendRequestTelegram('deleteWebhook')
					return 'Done'

			def getWebhookInfo():
					r = sendRequestTelegram('getWebhookInfo')
					return r.response

			def getMe():
					r = sendRequestTelegram( 'getMe')
					return r.response

			def getFile(file_id=None):
					r = sendRequestTelegram('getFile', locals())
					return r.response

			def sendMessage(chat_id=None, text=None, parse_mode=None,  disable_web_page_preview=None, disable_notification=None,  reply_to_message_id=None,  reply_markup=None, inline_keyboard=None):	
					r = sendRequestTelegram('sendMessage', locals())
					return r.response

			def sendAdmin(chat_id=None, text=None, parse_mode=None,  disable_web_page_preview=None, disable_notification=None,  reply_to_message_id=None,  reply_markup=None, inline_keyboard=None):	
					if (chat_id == None) or chat_id == 'logs':
						chat_id = config['LOGS']
					elif chat_id == 'support':
						chat_id = config['SUPPORT']
						
					r = sendRequestTelegram('sendMessage', locals())
					return r.response

			def deleteMessage(chat_id=None, message_id=None):
					r = sendRequestTelegram('deleteMessage', locals())
					return r.response

			def forwardMessage(chat_id=None, from_chat_id=None, disable_notification=None,message_id=None):
					r = sendRequestTelegram('forwardMessage', locals())
					return r.response

			def editMessageText(chat_id=None, message_id=None,  inline_message_id=None, text=None, parse_mode=None, disable_web_page_preview=None, reply_markup=None, inline_keyboard=None):
					r = sendRequestTelegram('editMessageText', locals())
					return r.response

			def editMessageCaption(chat_id=None, message_id=None, inline_message_id=None, caption=None, reply_markup=None, inline_keyboard=None):
					r = sendRequestTelegram('editMessageCaption', locals())
					return r.response

			def editMessageReplyMarkup(chat_id=None, message_id=None, inline_message_id=None, reply_markup=None, inline_keyboard=None):	
					r = sendRequestTelegram('editMessageReplyMarkup', locals())
					return r.response

			def sendPhoto(chat_id=None, photo=None, capition=None, parse_mode=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
					photo=photo
					r = sendRequestTelegram('sendPhoto', organize_argument(locals(), item=['photo']), file_=photo)
					return r.response

			def sendAudio(chat_id=None, audio=None, duration=None, disable_notification=None, reply_to_message_id=None, reply_markup=None, inline_keyboard=None):
					audio=audio
					r = sendRequestTelegram('sendAudio', organize_argument(locals(), item=['audio']), file_=audio)

			def sendVoice(chat_id=None, voice=None, duration=None, disable_notification=None, reply_to_message_id=None, reply_markup=None, inline_keyboard=None):
					voice=voice
					r = sendRequestTelegram('sendVoice', organize_argument(locals(), item=['voice']), file_=voice)

			def sendVideo(chat_id=None, video=None, duration=None, width=None, height=None, caption=None, parse_mode=None, supports_streaming=None, disable_notification=False, reply_to_message_id=None, reply_markup=None):
					video=video
					r = sendRequestTelegram('sendVideo', organize_argument(locals(), item=['video']), file_=video)
					return r.response

			def sendVideoNote(chat_id=None, video_note=None, duration=None, length=None, disable_notification=False, reply_to_message_id=None, reply_markup=None):
					video_note=video_note
					r = sendRequestTelegram('sendVideoNote', organize_argument(locals(), item=['video_note']), file_=video_note)
					return r.response

			def sendDocument(chat_id=None, document=None, caption=None, parse_mode=None, disable_notification=False, reply_to_message_id=None, reply_markup=None):
					document=document
					r = sendRequestTelegram('sendDocument', organize_argument(locals(), item=['document']), file_=document)
					return r.response

			def sendContact(chat_id, phone_number=None, first_name=None, last_name=None, disable_notification=False, reply_to_message_id=None, reply_markup=None):
					r = sendRequestTelegram('sendContact', locals())
					return r.response

			def setChatStickerSet(chat_id=None, sticker_set_name=None):
					r = sendRequestTelegram('setChatStickerSet', locals())
					return r.response

			def deleteChatStickerSet(chat_id=None):
					r = sendRequestTelegram('deleteChatStickerSet', locals())
					return r.response

			def getStickerSet(name=None):
					r = sendRequestTelegram('getStickerSet', locals())
					return r.response

			def uploadStickerFile(user_id=None, png_sticker=None):
					r = sendRequestTelegram('uploadStickerFile', locals())
					return r.response

			def createNewStickerSet(user_id=None, name=None, title=None, png_sticker=None, emojis=None, contains_masks=None, mask_position=None):
					r = sendRequestTelegram('createNewStickerSet', locals())
					return r.response

			def addStickerToSet(user_id=None, name=None, png_sticker=None, emojis=None, mask_position=None):
					r = sendRequestTelegram('addStickerToSet', locals())
					return r.response

			def setStickerPositionInSet(sticker=None, position=None):
					r = sendRequestTelegram('setStickerPositionInSet', locals())
					return r.response

			def deleteStickerFromSet(sticker=None):
					r = sendRequestTelegram('deleteStickerFromSet', locals())
					return r.response

			def sendLocation(chat_id=None, latitude=None, longitude=None, live_period=None, disable_notification=False, reply_to_message_id=None, reply_markup=None):
					r = sendRequestTelegram('sendLocation', locals())
					return r.response

			def sendVenue(chat_id=None, latitude=None, longitude=None, title=None, address=None, foursquare_id=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
					r = sendRequestTelegram('sendVenue', locals())
					return r.response

			def editMessageLiveLocation(latitude, longitude, chat_id=None, message_id=None, inline_message_id=None, reply_markup=None):
					r = sendRequestTelegram('editMessageLiveLocation', locals())
					return r.response

			def stopMessageLiveLocation(chat_id=None, message_id=None, inline_message_id=None, reply_markup=None):
					r = sendRequestTelegram('stopMessageLiveLocation', locals())
					return r.response

			def sendMediaGroup(chat_id=None, media=None, disable_notification=None, reply_to_message_id=None):
					media=media
					r = sendRequestTelegram('sendMediaGroup', organize_argument(locals(), item=['media']), file_=media)
					return r.response

				### Group

			def getChat(chat_id=None):
					r = sendRequestTelegram('getChat', locals())
					return r.response

			def leaveChat(chat_id=None):
					r = sendRequestTelegram('leaveChat', locals())
					return r.response

			def kickChatMember(chat_id=None, user_id=None, until_date=None):
					r = sendRequestTelegram('kickChatMember', locals())
					return r.response

			def unbanChatMember(chat_id=None, user_id=None):
					r = sendRequestTelegram('unbanChatMember', locals())
					return r.response

			def sendChatAction(chat_id=None, action=None):
					r = sendRequestTelegram('sendChatAction', locals())
					return r.response

			def restrictChatMember(chat_id=None, user_id=None, until_date=None, can_send_messages=None, can_send_media_messages=None, can_send_other_messages=None, can_add_web_page_previews=None):
					r = sendRequestTelegram('restrictChatMember', locals())
					return r.response

			def promoteChatMember(chat_id=None, user_id=None, can_change_info=None, can_post_messages=None, can_edit_messages=None, can_delete_messages=None, can_invite_users=None, can_restrict_members=None, can_pin_messages=None, can_promote_members=None):
					r = sendRequestTelegram('promoteChatMember', locals())
					return r.response

			def getChatAdministrators(chat_id=None):
					r = sendRequestTelegram('getChatAdministrators', locals())
					return r.response

			def getChatMembersCount(chat_id):
					r = sendRequestTelegram('getChatMembersCount', locals())
					return r.response

			def getChatMember(chat_id=None, user_id=None):
					r = sendRequestTelegram("getChatMember", locals())
					return r.response

			def setChatTitle(chat_id=None, title=None):
					r = sendRequestTelegram('setChatTitle', locals())
					return r.response

			def setChatDescription(chat_id=None, description=None):
					r = sendRequestTelegram('setChatDescription', locals())
					return r.response

			def exportChatInviteLink(chat_id=None):
					r = sendRequestTelegram('exportChatInviteLink', locals())
					return r.response

			def setChatPhoto(chat_id=None, photo=None):
					photo=photo
					r = sendRequestTelegram('setChatPhoto', organize_argument(locals(), item=['photo']), file_=photo)
					return r.response

			def deleteChatPhoto(chat_id=None):
					r = sendRequestTelegram('deleteChatPhoto', locals())
					return r.response

			def getUserProfilePhotos(user_id=None, offset=None, limit=None):
					r = sendRequestTelegram('getUserProfilePhotos', locals())
					return r.response

			def pinChatMessage(chat_id=None, message_id=None, disable_notification=False):
					r = sendRequestTelegram('pinChatMessage', locals())
					return r.response

			def unpinChatMessage(chat_id=None):
					r = sendRequestTelegram('unpinChatMessage', locals())
					return r.response

			def answerCallbackQuery(callback_query_id=None, text=None, show_alert=None,cache_time=None):	
					r = sendRequestTelegram('answercallbackquery', locals())
					return r.response

			def answerInlineQuery(inline_query_id=None, results=None, cache_time=None, is_personal=None, next_offset=None, switch_pm_text=None, switch_pm_parameter=None):
					r = sendRequestTelegram('answerInlineQuery', locals())
					return r.response