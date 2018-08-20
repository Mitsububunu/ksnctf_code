# coding: UTF-8

"""

Not solving

"""


import hashlib
import urllib
#import urllib2

url = 'http://ksnctf.sweetduet.info:10080/~q9/flag.html'


username = "q9"
realm = "secret"
nonce = "bbKtsfbABAA=5dad3cce7a7dd2c3335c9b400a19d6ad02df299b"
uri = "/~q9/flag.html"
algorithm = "MD5"
response = ""
qop = "auth"
nc = "00000001"
cnonce = "9691c249745d94fc"
md5a1 = "c627e19450db746b739f41b64097d449"

a2 = 'GET:' + uri


def toMD5(str):
	return hashlib.md5(str).hexdigest()



def genAuthorized(nonce, response):
	authorized = 'Digest username="' + username + '", realm="' + realm + '", nonce="' + nonce + '",uri="' + uri + '", algorithm=' + algorithm + ', response="' + response + '", qop=' + qop + ', nc=' + nc + ', cnonce="' + cnonce + '"'
	return authorized



def main():
	#nonce = getNonce()
	#response = genResponse(nonce)
    #auth = genAuthorized(nonce, response)
    reqMD5 = toMD5(md5a1 + ':' + nonce + ':' + nc + ':' + cnonce + ':' + qop + ':' + toMD5(a2))
    authorized = 'Digest username="' + username + '", realm="' + realm + '", nonce="' + nonce + '",uri="' + uri + '", algorithm=' + algorithm + ', response="' + reqMD5 + '", qop=' + qop + ', nc=' + nc + ', cnonce="' + cnonce + '"'
    header = {'Authorization' : authorized}
    req = urllib.request.Request(url, None, header)
    
    #try:
    data = urllib.request.urlopen(req)
    html = data.read()
    print(html) 
    #except urllib2.HTTPError, e:
    #print(e.code) 
    #print(e.info())
		
if __name__ == '__main__':
    main()