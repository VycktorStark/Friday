#!/usr/bin/env python3
# encoding=utf8
from main import app, utils, os, subprocess, argparse, plugins_
PARSER = argparse.ArgumentParser(description='RUN COMMAND')
PARSER.add_argument('--install', '-i', help='install dependency', action="store_true")
PARSER.add_argument('--polling', '-p', help='run in polling', action="store_true")
PARSER.add_argument('--synchronize', '-s', type=str, help='synchronize repository use: 1 to synchronize and clean any changes that might give errors 2 to only synchronize')
args = PARSER.parse_args()
if args.polling:
  try:
    while True:
      utils.polling()
  except KeyboardInterrupt:
    utils.log_('\n\033[01;31mEnding polling . . .\033[00;37m')
  except Exception as error:
    utils.log_('\n\033[01;31mAn error has occurred, bot application is off or has been stopped\033[00;37m')
    
elif args.install:
    print(subprocess.call("sudo apt install tmux figlet xtitle && sudo pip3 install -r requirements.txt", shell=True))
elif args.synchronize:
  if args.synchronize == "1":
    print(subprocess.getoutput('git checkout . && git pull'))
  elif args.synchronize == "2":
    print(subprocess.getoutput('git pull'))
  else:
    print('\n\033[02;37mThis is not valid, check the valid commands by executing: "\033[01;31mpython run -h\033[02;37m"\n\033[00;37m')
else:
  app.run(port=int(os.getenv('PORT', 3000)), host='0.0.0.0')
