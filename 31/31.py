import subprocess
import re
import requests

# セッションを接続するための準備
kangacha_url = "http://ctfq.sweetduet.info:10080/~q31/kangacha.php"
s= requests.Session()

print("一度ポストし、クッキーの情報を得る")
r = s.post(kangacha_url, data = {"submit":"Gacha"})
data = s.cookies["ship"]
signature = s.cookies["signature"]

print("hashpump を subprocess で呼ぶための準備")
args = {}
args["data"] = data
args["signature"] = signature
args["key"] = 21
args["append"] = ",10"

cmd = "hashpump -s {signature} -k {key} -d {data} "
cmd += "-a {append}"
cmd = cmd.format(**args)

print("Popen")
#stdout=subprocess.PIPE,
proc = subprocess.Popen(cmd.strip().split(" "),  shell=True)
print("proc.communicate()")
out, err = proc.communicate()

print("得られた cookie を url エンコードにする") 
crack_signature, crack_data = out.decode("utf-8").strip().split("\n")
crack_data = crack_data.replace("\\x","%")

print("cookie を変更して再接続")
s.cookies.clear()
setargs = {"domain":"ctfq.sweetduet.info","path":"/~q31"}
s.cookies.set("ship",crack_data,**setargs)
s.cookies.set("signature",crack_signature,**setargs)
r = s.get(kangacha_url)

print("Yamato がドロップしているので、フラグ部分を抜き出す。")
m = re.search("Yamato \[(?P<flag>.*)\]", r.text)
print(m.group("flag"))