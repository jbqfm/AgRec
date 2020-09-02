# AgRec

超A&G+を録画するやつ

# Features

* rtmp/HLSサーバーの自動取得
* 超A&G+高画質版の再生/録画

# Requirement

* Windows 10
* Python    3.6
* m3u8      0.6.0
* requests  2.20.0

# Installation
1. Pythonパッケージのインストール
   ```
   pip install m3u8
   pip install requests
   ```
2. [rtmpdump.exe](http://rtmpdump.mplayerhq.hu/download/)、[ffmpeg.exe・ffplay.exe](https://ffmpeg.zeranoe.com/builds/)をAgRec\\exeに配置

3. AgRec.pyの編集(高画質版利用時のみ)

   [ここ](https://github.com/jbqfm/AgRec/blob/8af3e77d857fb41e3d6eb67dce950ca0bcf9589c/AgRec.py#L136)以下2行を下記のように編集
   ```
   high = '<高画質版を含むVariantなM3U8アドレス>'
   pl = None
   ```
   ※[m3u8アドレスは各自調べてください。](https://jbqfm.blogspot.com/2020/09/a-hls.html)
# Usage

```
python AgRec.py -t TIME -o OUTPUT -m MODE -mu MULTI
```
* `-t TIME`		…録画時間(秒)
* `-o OUTPUT`	…保存ファイル名
* `-m MODE`		…モード(1～3；初期値：1)<sup id="note_ref-1"><a href="#note-1">[注1]</a></sup>
* `-mu MULTI`	…同時録画数(初期値：1)

`TIME`・`OUTPUT`ともに省略すると放送中の番組をffplayにて視聴できます。
どちらか片方のみ省略すると動作しません
# Note
1. <b><a id="note-1" href="#note_ref-1">^</a></b> 1：RTMP 2：HLS 3：両方


# Author

* 桜餅([Twitter@jbqfm](https://twitter.com/jbqfm))

# License
 
"AgRec" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
