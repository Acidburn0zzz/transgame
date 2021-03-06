#!/usr/bin/python
# -*- coding: utf-8 -*-

from transgame_common import *
from filelock import FileLock
from urllib import quote
import base64
import random

gameid = param('gameid')

open('gamedata/' + gameid + '.current', 'a+')

with FileLock('gamedata/' + gameid + '.current') as lock:
  f = open('gamedata/' + gameid + '.current', 'r+')
  allsuggestions = []
  #print open('gamedata/' + gameid + '.suggestions', 'r+').readlines()
  while len(allsuggestions) < 1 or allsuggestions[-1] != 'END':
    allsuggestions = open('gamedata/' + gameid + '.suggestions', 'r+').readlines()
  allsuggestions = allsuggestions[:-1]
  chosen = random.choice(allsuggestions)
  text = chosen.rpartition('|')[0]
  output = []
  output.append(text)
  output.append('END')
  f.seek(0)
  f.write('\n'.join(output))
  f.truncate()
  f.close()
