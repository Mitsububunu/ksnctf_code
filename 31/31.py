import subprocess
import re
import requests


kangacha_url = "http://ctfq.sweetduet.info:10080/~q31/kangacha.php"
s= requests.Session()

print("Post then get cookie")
r = s.post(kangacha_url, data = {"submit":"Gacha"})
data = s.cookies["ship"]
signature = s.cookies["signature"]

print("Prepare hashpump -> subprocess")
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
proc = subprocess.Popen(cmd.strip().split(" "), stdout=subprocess.PIPE)
print("proc.communicate()")
out, err = proc.communicate()

print("Encode url with getting cookie") 
crack_signature, crack_data = out.decode("utf-8").strip().split("\n")
crack_data = crack_data.replace("\\x","%")

print("Change cookie and re-connaction")
s.cookies.clear()
setargs = {"domain":"ctfq.sweetduet.info","path":"/~q31"}
s.cookies.set("ship",crack_data,**setargs)
s.cookies.set("signature",crack_signature,**setargs)
r = s.get(kangacha_url)

print("get from Yamato item ")
m = re.search("Yamato \[(?P<flag>.*)\]", r.text)
print(m.group("flag"))