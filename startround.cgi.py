#!/usr/bin/python
# -*- coding: utf-8 -*-

from transgame_common import *
from filelock import FileLock
from urllib import quote
import base64
import time

gameid = param('gameid')

open('gamedata/' + gameid + '.starttime', 'a+')

with FileLock('gamedata/' + gameid + '.starttime') as lock:
  f = open('gamedata/' + gameid + '.starttime', 'r+')
  f.seek(0)
  unixtime = int(time.time())
  f.write(str(unixtime))
  f.truncate()
  f.close()

