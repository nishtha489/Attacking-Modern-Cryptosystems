import random
import numpy as np

file = open("random.txt", 'w+')
bitarr = ""
for i in range(1, 100001):
  for j in range(1, 65):
    bitarr += str(random.randint(0, 1))
  file.write(bitarr)
  file.write('\n')
  bitarr = ""

file.close()

bits = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
Binary = []

file = open("random.txt", 'r+')

for i in range(1, 100001):
    inp = file.readline()
    print(inp)

    temp = []
    for j in range(0, 64):
        temp.append(int(inp[j]))

    Binary.append(temp)
    Binary.append(list(np.bitwise_xor(temp, bits)))
file.close()
file = open("input.txt", 'w+')

characters = {}
for i in range(0, 16):
    number = '{:0>4}'.format(format(i, "b"))
    characters[number] = chr(ord('f') + i)

for i in range(len(Binary)):
    charstr = ""

    for j in range(0, 16):
        temp = str(Binary[i][j * 4 + 0]) + str(Binary[i][j * 4 + 1]) + str(Binary[i][j * 4 + 2]) + str(Binary[i][j * 4 + 3])
        charstr = charstr + characters[temp]
    file.write(charstr)
    file.write("\n")

file.close()
