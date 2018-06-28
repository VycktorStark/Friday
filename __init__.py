#!/usr/bin/env python3
# encoding=utf8

from os import listdir
from os.path import realpath, dirname
from langs import lang
import requests, json, time, subprocess, datetime, os, re, sys, psycopg2, flask, argparse
from flask import Flask, request, Response
ru = lambda text: "\n\033[02;31m{}\n\033[00;37m".format(text)
app = Flask(ru("".join(subprocess.getoutput('figlet F. R. I. D. A. Y.'))))
app.config.from_object('settings')
config = app.config
import TelegramBOT as bot
bot.plugins_()
import handler