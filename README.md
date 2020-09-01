# AgRec

超A&G+を録画するやつ

# Features

rtmp/HLSサーバーの自動取得[^1]

# Requirement

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
* `-m MODE`		…モード(1～3)^2
* `-mu MULTI`	…同時録画数

# Note
[^1]: HLSのサーバーについては各自調べてください。



# Author

* 桜餅([Twitter@jbqfm](https://twitter.com/jbqfm))

# License
 
"AgRec" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
