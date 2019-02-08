# Video DRM

# 本地加密，专业

[天狼星][1]

# 本地加密，自制

最终要播放的。现成播放器总能save-as。用Javascript。

# 流媒体加密，专业

[保利威][2]

# 流媒体加密，自制

GET 视频文件
PLAY

GET 视频文件
有加密
读ProtectionData.clearkeys
解密
PLAY

GET 视频文件
有加密
读ProtectionData.clearkeys
有serverURL
JSONREQUEST
解密
PLAY

# 关于request
Httprequest / get, post
Jsonrequest

# About encryption
The mp4 file is encrypted using a 128-bit (1100…0011) key encrypted in hex (0000-\>aa, 32-char)

The decryption is done using the same 128-bit key encrypted in base64 (63-\>/). = padding is removed.

[Converter][3]

# 参考文件：
[各种方法总论][4]

# 解决方案（见github代码）

static/
用simpleHTTPserver送网页就行。

license-server/
说白了，flask server, 发密码。
顺便记录machid和ip。允许某些machid。
只要看不透dash.js加密，就搞不到request的k/kid，就不能盗版。
 

---- 

# DRM可破解性

Chrome/Firefox相关插件能下载，但下载的播放不了

youtube-dl、硕鼠下载器是Known Website URL-based。

Livestreamer: no-plugin

> IMO you can’t download this DRM (silverlight) protected video

IDM只能下载无关的init.mp4。

# Deploy之前请确认：

注意index.html（未obfuscate版本），source（视频文件未加密版本）不要传。

更改index.html中`flask_url`变量的值。

重新obfuscate index.html。

`index_obfuscate.html`要单独obfuscate HTML和Javascript，不能一块儿。

# 错误：




[1]:	http://www.tlxsoft.com/jiami.htm
[2]:	https://www.polyv.net/pricing/vod/
[3]:	https://cryptii.com/pipes/hex-decoder
[4]:	https://www.zhihu.com/question/24561177