#drawQR.py

import re
import numpy as np
import matplotlib.pyplot as plt

# 大文字・小文字を0・255に変換
fp = open('ProblemText.txt','r')
s = ""
for line in fp.readlines():
    line1 = re.sub('[a-z]','255 ',line) 
    line2 = re.sub('[A-Z]','0 ',line1)
    s+=line2
    s+="\n"

fp.close()

# 0/255 に変換したデータをファイルに出力
with open('numbers.txt','w') as f:
    f.write(s)

# numpyを使ってデータを整理・描画
data = np.loadtxt('numbers.txt') #空白区切りデータから読み込み

plt.imshow(data, cmap='gray', vmin = 0, vmax =255, interpolation='none')
plt.show()