import ffmpy

videos = {
	# '': '', 
	# '': ''
	}

for name, url in videos.items():
	ff = ffmpy.FFmpeg(
			inputs={url: None}, 
			outputs={'/Users/Name/Downloads/'+name+'.mp4': '-c copy'})
	ff.run()

# 需 headers 時，以下
'''
ffmpeg -protocol_whitelist "file,http,https,tcp,tls" \
-user_agent "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36" \
-headers $'Origin: https://v.jav101.com\r\nReferer: https://v.jav101.com/play/avid5b73d3cfc021d?pp=10744\r\nCookie: __cfduid=dd445ade94829a8fe46012b16ee21c3a71534695198; CloudFront-Key-Pair-Id=APKAJBW3QQCETPXK5WRQ; locale=tw; CloudFront-Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdnQuamF2MTAxLmNvbS8qIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNTM0NzA2MzMwfX19XX0_; CloudFront-Signature=M0D5rb4fooxmINffb2T7T05rWWkFpxWCpeUe3vivDrUoPIp3P2hr4cC8y-IPelvSbR7sh7Sagl4fiSKn5t509p74x3S4TooKVGMNEnITq8jfCqc-SOB9vnDlsJrPyihx22mC6ykLyrRY3KFfjni%7EdTN4YZyWdyOeB8h205TEZBBHY2NNhy8NDhn9raoT2NrJIpPkOKHbDm-hfGHJ4QozRm0lkrzHdMEtg8wF63yL%7ELwzIg2mBErfDjx7wUxMtlP7PBbC6gOdjfDuvnkO5fN3pjXy2xC2cDSJSC9BolyhgIp2gnBwdRZEjogX9nyws%7E1Jmi0zN2HGHeS%7E8m7iLyJgIw__\r\n' \
-i "https://svt.jav101.com/avid5b73d3cfc021d/avid5b73d3cfc021d.m3u8" \
-c copy "example.mp4"
'''
