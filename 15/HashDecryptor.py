import hashlib

deviceid = 999999910000000

for x in range(0, 89999999):
    text = str((deviceid + x))
    hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
    if hash == "356280a58d3c437a45268a0b226d8cccad7b5dd28f5d1b37abf1873cc426a8a5":
        print(text)
        break

