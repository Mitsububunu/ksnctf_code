
list = (70,152,195,284,475,612,791,896,810,850,737,1332,1469,1120,1470,832,1785,2196,1520,1480,1449)

tmp = 0
i = 1
for c in list:
    tmp = int(c / i)
    i += 1
    print(tmp)

#---------------------------------------------

flag = ""
idx = 1
for c in list:
    flag += chr(int(c / idx))
    idx += 1
    print(flag)

print(flag)
