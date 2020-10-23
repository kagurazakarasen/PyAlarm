# -*- coding: utf-8 -*-
import datetime

alm_time_file = "/home/pi/alm_time.txt"

now = datetime.datetime.now() 

# アラームのターゲット時間を読む
with open(alm_time_file) as f:
    s = f.read()
    print("Target Time > "+ s.rstrip())

# 時間を００００形式の文字列にする
nowTimeString=str(now.hour).zfill(2)+str(now.minute).zfill(2)
print("   Now Time > " + nowTimeString)

if( s.rstrip() == nowTimeString):
    print("It's NOW!!")
else:
    print("Wrong!!")