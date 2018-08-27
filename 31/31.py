import http.client,hashlib
import hlextend

def main():
    count=1
    while True:
        sha=hlextend.new("sha512")
        new=sha.extend(",9,10","7,7",count,"afb98ced71d393874b68d65781bc69b2c90a8ad3c31a06922b01e4a00c986c84d953ff84180104d8f6f899ff1dff7ff93348dd62168c437a22f6325584f478c7")
        new=new.replace("\\x80","80".decode("hex"))
        new=new.replace("\\x00","%00")
        c=0
        ele=[]
        e=""
        flag=0
        for i in new:
            if i=="\\":
                flag=2
                continue
            if flag==2:
                flag=1
                continue
            if flag==1:
                e=e+i
                c=c+1
            if c==2:
                ele.append(e)
                flag=0
                c=0
                e=""
        for k in ele:
            new=new.replace("\\x"+k,k.decode("hex"))
        conn=httplib.HTTPConnection("ctfq.sweetduet.info:10080")
        uri="/~q31/kangacha.php"
        ship="ship="+new
        signature="signature="+sha.hexdigest()
        header={"Cookie":ship+";"+signature}
        conn.request("GET",uri,None,header)
        res=conn.getresponse()
        head=res.getheaders()
        k=head[0][1]
        if k!="287":
            break
        count=count+1
        print(count)
    print(res.read())
if __name__=="__main__":
    main()