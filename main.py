from ytmusicapi import YTMusic


YTMusic.setup(filepath="headers_auth.json", headers_raw = "<accept: */*
accept-encoding: gzip, deflate, br
accept-language: en-AU,en;q=0.9,pt-PT;q=0.8,pt;q=0.7,es-MX;q=0.6,es;q=0.5,en-GB;q=0.4,en-US;q=0.3
authorization: SAPISIDHASH 1662702479_ffcc6d6cdc90c9f483df852be2c6ae758a99624e
content-length: 2264
content-type: application/json
cookie: VISITOR_INFO1_LIVE=iX8a9shWhJk; HSID=AePoB4k83FS4RG_wI; SSID=A2DgCfeZOKOpzG_G6; APISID=yqlfNhRPvTmxtzWK/AvGy-IHS--QTJjM8J; SAPISID=nVlZPHQ7-7BeuvKL/ARmrkFS_rbh-203ZS; __Secure-1PAPISID=nVlZPHQ7-7BeuvKL/ARmrkFS_rbh-203ZS; __Secure-3PAPISID=nVlZPHQ7-7BeuvKL/ARmrkFS_rbh-203ZS; LOGIN_INFO=AFmmF2swRgIhAPiX3llcAM0rzswsp2-3GRnrKx1TQpife0fBN_fen5DuAiEAzMXCQ1jmXYB9AiU9_pEp3ohx4c_Kg_TTyikgms25cxg:QUQ3MjNmeUVJVWJmU2dnY1FXM2EzU0FEY3N1bTlvaTVvWE9FMHBaVldaVmhSSFFvWFFFVFZRb0NTeENwcndfck5ZYW00N2d5QU41bWZYbk9DSTFaY1Y4UWxWZllnMFRFZkZEYTk0OTJYV0p0aUxrTVVTY0RKODNQY05IWURLd2tvR2tEWmRqdHZydlU4YkEwTHRhdGNUM1FfaXVPc3N5b3NB; _gcl_au=1.1.1195558297.1655642033; YSC=NOXwicm59Rc; SID=NAhzSWTmTY6WUOKKr9UkgDZIvslEzjpMli9DY1-PECujX4bl5Hi0y_VuNQqyNHLO39z58w.; __Secure-1PSID=NAhzSWTmTY6WUOKKr9UkgDZIvslEzjpMli9DY1-PECujX4blYWTRPSNC4L5qPycC761Qdg.; __Secure-3PSID=NAhzSWTmTY6WUOKKr9UkgDZIvslEzjpMli9DY1-PECujX4blPjWduHt7nMaRj62goMJcyQ.; _ga=GA1.1.1761633474.1661732372; wide=0; PREF=f6=40000080&tz=Australia.Melbourne&f4=4000000&library_tab_browse_id=FEmusic_liked_playlists&volume=100&repeat=NONE&autoplay=true&has_user_changed_default_autoplay_mode=true&f5=30000; _ga_VCGEPY40VB=GS1.1.1662702302.12.1.1662702395.0.0.0; SIDCC=AEf-XMTV5yPE5caWdle2E6XwBKu5KU3xt9ShofnTLKqqrko0DqZqrzFP5SH2XbxiHDug4m0MXm1s; __Secure-1PSIDCC=AEf-XMQEkxSs4qu7qWxywaa_v1ry_5p38gu6i8nltkh4GZc79h9iTowVXN_KfJ1ubWkYhN4Wnww; __Secure-3PSIDCC=AEf-XMRVuvW4rRtGEBEyQcjnENbkUVXhpV9Osukm06ow3Gs7NkYQ9Q5FMKsjhtvmASkg_t9-OrU; ST-197m8dl=csn=MC43NTI0NTAxOTc5ODY2MDI3&itct=CNcBENVoGAAiEwjM-ImzgYf6AhX1heYKHUtfDuA%3D
origin: https://music.youtube.com
referer: https://music.youtube.com/search?q=mitski
sec-ch-ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"
sec-ch-ua-arch: "x86"
sec-ch-ua-bitness: "64"
sec-ch-ua-full-version: "105.0.5195.102"
sec-ch-ua-full-version-list: "Google Chrome";v="105.0.5195.102", "Not)A;Brand";v="8.0.0.0", "Chromium";v="105.0.5195.102"
sec-ch-ua-mobile: ?0
sec-ch-ua-model
sec-ch-ua-platform: "macOS"
sec-ch-ua-platform-version: "12.5.0"
sec-ch-ua-wow64: ?0
sec-fetch-dest: empty
sec-fetch-mode: same-origin
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36
x-client-data: CJO2yQEIo7bJAQjBtskBCKmdygEI2d3KAQiUocsBCPq7zAEIh73MAQjXxswBCLvJzAEI4svMAQia0swBCP7XzAEI4dnMAQiA28wBGLfNzAE=
Decoded:
message ClientVariations {
  // Active client experiment variation IDs.
  repeated int32 variation_id = [3300115, 3300131, 3300161, 3313321, 3321561, 3330196, 3350010, 3350151, 3351383, 3351739, 3352034, 3352858, 3353598, 3353825, 3353984];
  // Active client experiment variation IDs that trigger server-side behavior.
  repeated int32 trigger_variation_id = [3352247];
}
x-goog-authuser: 0
x-goog-visitor-id: CgtpWDhhOXNoV2hKayiypuuYBg%3D%3D
x-origin: https://music.youtube.com
x-youtube-client-name: 67
x-youtube-client-version: 1.20220831.01.02>")
              
