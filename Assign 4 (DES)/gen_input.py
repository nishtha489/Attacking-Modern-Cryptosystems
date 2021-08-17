import random
import numpy as np

no_of_input = 100000

Diff = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
Bin_Inp = []
for i in range(100000):
    tmp = '{:0>64}'.format(format(i,"b"))
    tmp1 = []
    for j in range(64):
        tmp1.append(int(tmp[j]))

    Bin_Inp.append(tmp1)
    Bin_Inp.append(list(np.bitwise_xor(tmp1,Diff)))
# print(Bin_Inp)

charmap = {}
for i in range(16):
    num = '{:0>4}'.format(format(i,"b"))
    charmap[num] = chr(ord('f')+i)
# print(charmap,[i for i in range(16)])

inpstr = []
for i in range(len(Bin_Inp)):
    string = ""
    for j in range(16):
        tmp = str(Bin_Inp[i][j*4+0])+str(Bin_Inp[i][j*4+1])+str(Bin_Inp[i][j*4+2])+str(Bin_Inp[i][j*4+3])
        string = string + charmap[tmp]
    inpstr.append(string)
# print(inpstr)

file = open("inputs.txt","w")
for i in inpstr:
    file.write(i)
    file.write("\n")
file.close()