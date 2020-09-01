# AgRec

超A&G+を録画するやつ

# Features

rtmp/HLSサーバーの自動取得<sup>[1](#note1)</sup>

# Requirement

* Windows 10
* Python    3.6
* m3u8      0.6.0
* requests  2.20.0

# Installation

```bash
pip install m3u8
pip install requests
```

# Usage

```bash
python demo.py -t TIME -o OUTPUT -m MODE -mu MULTI
```
* `-t TIME`		…録画時間(秒)
* `-o OUTPUT`	…保存ファイル名
* `-m MODE`		…モード(1～3)<sup>[2](#note2)</sup>
* `-mu MULTI`	…同時録画数

# Note
<small id="note1">HLSのアドレスは各自で調べてください</small></br>
<small id="note2">1：RTMP 2：HLS 3：両方</small>


# Author

* 桜餅([Twitter@jbqfm](https://twitter.com/jbqfm))

# License
 
"AgRec" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
