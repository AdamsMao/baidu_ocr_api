# -*- coding:utf-8 -*-

import sys, urllib, urllib2, json, base64,demjson

reload(sys)
sys.setdefaultencoding('utf8')

def b64encode_image(image):
	with open(image,'rb') as f:
		return base64.b64encode(f.read())

url = 'http://apis.baidu.com/apistore/idlocr/ocr'

data = {}
data['fromdevice'] = "pc"
data['clientip'] = "10.10.10.0"
data['detecttype'] = "LocateRecognize"
data['languagetype'] = "CHN_ENG"
data['imagetype'] = "1"
#data['image'] = "/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDABMNDxEPDBMREBEWFRMXHTAfHRsbHTsqLSMwRj5KSUU+RENNV29eTVJpU0NEYYRiaXN3fX59S12Jkoh5kW96fXj/2wBDARUWFh0ZHTkfHzl4UERQeHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHj/wAARCAAfACEDAREAAhEBAxEB/8QAGAABAQEBAQAAAAAAAAAAAAAAAAQDBQb/xAAjEAACAgICAgEFAAAAAAAAAAABAgADBBESIRMxBSIyQXGB/8QAFAEBAAAAAAAAAAAAAAAAAAAAAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/APawEBAQEBAgy8i8ZTVV3UY6V1eU2XoWDDZB19S646Gz39w9fkKsW1r8Wm2yo1PYis1be0JG9H9QNYCAgc35Cl3yuVuJZl0cB41rZQa32dt2y6OuOiOxo61vsLcVblxaVyXD3hFFjL6La7I/sDWAgICAgICB/9k="
data['image'] = b64encode_image('Page2.jpg')

decoded_data = urllib.urlencode(data)
req = urllib2.Request(url, data = decoded_data)

req.add_header("Content-Type", "application/x-www-form-urlencoded")
req.add_header("apikey", "your apikey")

# If you need proxy sever to access the Internet:
#proxy = urllib2.ProxyHandler({'http':'10.48.6.1:8080'})
#opener = urllib2.build_opener(proxy)
#urllib2.install_opener(opener)
resp = urllib2.urlopen(req)
content = resp.read()

if(content):

	f = open('result.txt','w')

	dic = demjson.decode(content)
	for d in dic['retData']:
		print d['word']
		f.write(d['word']+'\n')

	f.close()



