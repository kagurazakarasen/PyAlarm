# -*- coding: utf-8 -*-
#!/usr/bin/env python3  
# 日本語コメント版。ちなみに↑のpythonの起動用の表記はその上のutf8指定と同居できない模様。（なので今のこれは意味がない）

import signal
import time
import math
import datetime

import scrollphathd

import subprocess

TIMEVIEWON = False # 毎分表示している時刻の表示をするかどうか（夜通し光るのはうるさそう）Falseならば表示しない

#scrollphathd.rotate(degrees=180) # 向きを変えたい時はここで角度を設定

alm_time_file = "/home/pi/alm_time.txt"

# ファイルからターゲットタイム読み込み
with open(alm_time_file) as f: 
    s = f.read()
    print("Target Time > "+ s.rstrip()) 

now = datetime.datetime.now()    # 現在の時刻を取得 

nowTimeString=str(now.hour).zfill(2)+str(now.minute).zfill(2)   # 時間＋分を０を頭につけた2桁で文字列化

if( s.rstrip() == nowTimeString):   # ターゲットタイムとあっているか判定　rstrip()は、\n をカットする chomp
    print("It's NOW!!")
    subprocess.Popen("aplay hotoke.wav", shell=True)    # オーディオファイル再生
    scrollphathd.write_string("Good Morning!! "+nowTimeString+"   ", brightness=0.5)

    # オートスクロールGoodMorning!!
    i=0
    while True:
        i=i+1
        # Show the buffer
        scrollphathd.show()
        # Scroll the buffer content
        scrollphathd.scroll()
        # Wait for 0.1s
        time.sleep(0.1)
        if i>108: break #大体このぐらいのカウントで一週
    scrollphathd.clear()

    # プラズマ表示（サンプルより）
    i = 0
    while True:
        i += 2
        s = math.sin(i / 50.0) * 2.0 + 6.0

        for x in range(0, 17):
            for y in range(0, 7):
                v = 0.3 + (0.3 * math.sin((x * s) + i / 4.0) * math.cos((y * s) + i / 4.0))

                scrollphathd.pixel(x, y, v)

        time.sleep(0.01)
        scrollphathd.show()
        if i>620: break # これもこのぐらいでブレイク

    # ガンマ（明るさ）の変更ループ
    DELAY = 0.0001
    i = 0
    while True:
        i=i+1
        for x in range(255):
            scrollphathd.fill(x/255.0, 0, 0, 17, 7)
            scrollphathd.show()
            time.sleep(DELAY)
        for x in reversed(range(255)):
            scrollphathd.fill(x/255.0, 0, 0, 17, 7)
            scrollphathd.show()
            time.sleep(DELAY)
        if i>2: break   # 2回回して終了

else:
    print("Wrong!!")
    if TIMEVIEWON:  # Trueなら毎分の時刻表示を行う
        scrollphathd.write_string( " " + nowTimeString +" ", brightness=0.1)    # 時刻表示用
        i=0
        while True:
            i=i+1
            scrollphathd.show()
            scrollphathd.scroll()
            time.sleep(0.1)
            if i>80: break

        scrollphathd.clear()

