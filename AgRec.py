#-*- coding: utf-8 -*-
import re
import os
import sys
import requests
import random
import m3u8
import datetime
import argparse
import subprocess
from pathlib import Path
from time import sleep
from datetime import datetime as dt
from datetime import timedelta
from threading import (Event, Thread)



parser = argparse.ArgumentParser(description='AgRec')
parser.add_argument('-t','--time', help='録画時間(ss)',type=int)
parser.add_argument('-o', '--output', help='ファイル名')
parser.add_argument('-m', '--mode', help='録画モード[1-3](1：rtmp、2：hls、3：両方)', type=int,default=1)
parser.add_argument('-mu', '--multi', help='同時録画数(1サーバー1接続を上限)',type=int,default=1)
args = parser.parse_args()



def ngchr(str):
	dic={'\¥': '￥', '/': '／', ':': '：', '*': '＊', '?': '？', '!': '！', '¥"': '”', '<': '＜', '>': '＞','|': '｜'}
	table='\\/:*?!"<>|'	
	for ch in table:
		if ch in str:
			rm = dic.pop(ch)
			str = str.replace(ch,rm)
	return str


#サーバーチェック
def svchk(num):
	
	th = num
	rq = requests.get(listurl)
	if rq.status_code != 200:
		rtmplist = None
	else:
		src = str(rq.content).replace(r'\n',"")
		src = src.replace(r'\r',"")
		src = src.replace(r'\t',"")
		serverlist = re.findall(r'<serverinfo>(.+?)<\/serverinfo>',src)
		serverlist = [s for s in serverlist if not '<cryptography>true</cryptography>' in s]
		rtmplist = []
		errurl = []
		for server in serverlist:
			s = re.findall(r'<server>.+?(rtmp.+?)<\/server>', server)
			app = re.findall(r'<app>(.+?)<\/app>', server)
			stream = re.findall(r'<stream>(.+?)<\/stream>', server)
			url = '{}/{}/{}'.format(s[0],app[0],stream[0])
			rtmplist.append(url)
		for num in range(1,len(rtmplist)+1):
			chk = dir / 'chk@{0}.flv'.format(num)
			cmd = str(dumppath) + ' -r ' + rtmplist[num-1] + ' --live -B 1 -o ' +str(chk)
			exec('serverchk%d = subprocess.Popen(cmd,shell=True)' % (num-1))
		for num in range(1,len(rtmplist)+1):
			exec('serverchk%d.communicate()' % (num-1))
			chk_ = dir / 'chk@{0}.flv'.format(num)
			if chk.stat().st_size == 0:
				errurl.append(rtmp)
			chk_.unlink()
		for url in errurl:
			rtmplist.remove(url)
		if th:
			if th > len(rtmplist):
				th = len(rtmplist)
		else:
			th = 1
		rtmplist = random.sample(rtmplist,th)
	return rtmplist
	
def m3u8get(v_m3u8):
	v_pl = m3u8.load(v_m3u8)
	urls = []
	bands = [] 
	for n in range(len(v_pl.playlists)):
		pl = v_pl.playlists[n]
		urls.append(pl.uri)
		bands.append(pl.stream_info.bandwidth)
	pl = urls[bands.index(max(bands))]
	return pl
	
def play(_pl):
	if high:
		pl = m3u8get(high)
	else:
		pl = _pl
	print(pl)
	cmd = ('"{0}" "{1}"').format(str(ffplaypath),pl)
	subprocess.run(cmd,shell=True)
#rtmp録画
def rtmp(_t,_file,_url):
	flvs = []
	r_recs = []
	for num in range(len(_url)):
		if len(_url) != 1:
			flvs.append(_file.parent / Path(_file.stem + '@' + str(num+1) + '.flv'))
		else:
			flvs.append(_file.with_suffix('.flv'))
		r_cmd = ('"{0}" -r "{1}" --live -B {2} -o "{3}"').format(str(dumppath),_url[num],_t,str(flvs[num]))
		r_recs.append(subprocess.Popen(r_cmd,shell=True))
	for num in range(len(_url)):
		r_recs[num].communicate()
	if _file.suffix != '.flv':
		for num in range(len(_url)):
			out =str(flvs[num].with_suffix(_file.suffix))
			c_cmd = ('"{0}" -i "{1}" -y -c copy "{2}"').format(str(ffmpegpath),str(flvs[num]),out)
			conv = subprocess.run(c_cmd,shell=True)
			Path(flvs[num]).unlink()

#HLS録画
def hls(_t,_file,_m3u8):
	td = datetime.timedelta(seconds=_t)
	h_out = str(_file.parent / Path(_file.stem + '(hls)' + _file.suffix))
	h_cmd = ('"{0}" -ss 0 -i "{1}" -t {2} -y -c copy "{3}"').format(str(ffmpegpath),_m3u8,td,h_out)
	subprocess.Popen(h_cmd,shell=True)

dir = Path.cwd()
dumppath = dir / 'exe' / 'rtmpdump.exe'
ffmpegpath = dir / 'exe' / 'ffmpeg.exe'
ffplaypath = dir / 'exe' / 'ffplay.exe'
listurl='http://www.uniqueradio.jp/agplayerf/getfmsListHD.php'

#高画質版に対応する場合はここを編集
high = None
pl = 'http://ic-www.uniqueradio.jp/iphone/3G.m3u8'

fname = args.output
t = args.time
m = args.mode
mu = args.multi
code = 0
if not fname:
	code = 1
if not t:
	code += 1

if code > 1:
	play(pl)
	sys.exit()
if code == 1:
	sys.exit()
now = dt.now()
DATE = now.strftime('%Y%m%d%H%M')
DATE8 = DATE[:-4]
fname = Path(ngchr(fname) + '_[%s]' % DATE8)
rtmpurl = None
if fname.suffix == '':
	fname = Path(str(fname) + '.mp4')

fname = dir / fname
if m != 2:
	rtmpurl = svchk(mu)
	if not rtmpurl or len(rtmpurl) == 0:
		m = 2
if m != 1:
	if high:
		pl = m3u8get(high)
if pl:
	hls= Thread(target=hls,args=(t,fname,pl))
if rtmpurl:
	rtmp= Thread(target=rtmp,args=(t,fname,rtmpurl))
if m == 2:
	hls.start()
	hls.join()
elif m ==3:
	hls.start()
	rtmp.start()
	hls.join()
	rtmp.join()
else:
	rtmp.start()
	rtmp.join()
sys.exit()