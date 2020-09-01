# AgRec

超A&G+を録画するやつ

# Features

rtmp/HLSサーバーの自動取得<sup id="note_ref-1"><a href="#note-1">[注1]</a></sup>

# Requirement

* Windows 10
* Python    3.6
* m3u8      0.6.0
* requests  2.20.0

# Installation
1. Pythonパッケージのインストール
 ```bash
 pip install m3u8
 pip install requests
 ```
2. rtmpdump.exe、ffmpeg.exeの配置

# Usage

```bash
python AgRec.py -t TIME -o OUTPUT -m MODE -mu MULTI
```
* `-t TIME`		…録画時間(秒)
* `-o OUTPUT`	…保存ファイル名
* `-m MODE`		…モード(1～3)<sup id="note_ref-1"><a href="#note-1">[注1]</a></sup>
* `-mu MULTI`	…同時録画数

# Note
1. <b><a id="note-1" href="#note_ref-1">^</a></b> HLSのアドレスは各自で調べてください
2. <b><a id="note-2" href="#note_ref-2">^</a></b> 1：RTMP 2：HLS 3：両方


# Author

* 桜餅([Twitter@jbqfm](https://twitter.com/jbqfm))

# License
 
"AgRec" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
