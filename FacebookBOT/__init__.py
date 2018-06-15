import re, os , sys, config, requests, json, flask
__all__ = ['re', 'os', 'sys', 'lang', 'config', 'requests', 'json', 'flask']
from .methods import *
__all__ += .methods.methods.__all__
def FbBOT(msg):
  text = msg['messaging'][0]['message']['text'].encode('utf8')
  user_id = msg['messaging'][0]["sender"]['id']
  cmd = text.split()
  if cmd[0] == "$echo":
    sendMessage(user_id, text.replace(cmd[0],''))