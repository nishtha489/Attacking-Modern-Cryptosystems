
import numpy as np

tempfile = open("output.txt")
dictionary = {
 'f' : [0,0,0,0],
 'g' : [0,0,0,1],
 'h' : [0,0,1,0],
 'i' : [0,0,1,1],
 'j' : [0,1,0,0],
 'k' : [0,1,0,1],
 'l' : [0,1,1,0],
 'm' : [0,1,1,1],
 'n' : [1,0,0,0],
 'o' : [1,0,0,1],
 'p' : [1,0,1,0],
 'q' : [1,0,1,1],
 'r' : [1,1,0,0],
 's' : [1,1,0,1],
 't' : [1,1,1,0],
 'u' : [1,1,1,1]
 }

splitarr = tempfile.read().split("\n")
inputlist = []

for i in range(0, len(splitarr) - 1):
    temp = []
    for j in range(0, 16):
        temp = temp + dictionary[splitarr[i][j]]
    inputlist.append(temp)

Inverse_Final_Permutation = [57, 49, 41, 33, 25 ,17, 9, 1 , 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7, 58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8]
inputlist2 = [[inputlist[j][Inverse_Final_Permutation[i] - 1] for i in range(0, 64)] for j in range(0, len(inputlist))]

inputlistXor = [list(np.bitwise_xor(inputlist2[2 * i + 1], inputlist2[2 * i])) for i in range(0, int(len(inp) / 2))]

ExpansionBox = [32, 1, 2, 3, 4, 5, 4, 5,6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
inputlistExpand = [[inputlist2[j][ExpansionBox[i] - 1] for i in range(0, 48)] for j in range(0, len(inputlist))]

inputlistAlpha = [list(np.bitwise_xor(inputlistExpand[2 * i + 1], inputlistExpand[2 * i])) for i in range(0, int(len(inp) / 2))]

L5 = [0, 0, 0, 0, 0, 1] + [0 for z in range(0, 26)]
inputlistFiestal = [list(np.bitwise_xor(inputlistXor[i][32 : 64], L5)) for i in range(0, len(inputlistXor))]

Inverse_Permutation_Box = [9, 17, 23, 31, 13, 28, 2, 18, 24, 16, 30, 6, 26, 20, 10, 1, 8, 14, 25, 3, 4, 29, 11, 19, 32, 12, 22, 7, 5, 27, 15, 21]
outputlistAlpha = [[inputlistFiestal[j][Inverse_Permutation_Box[i] - 1] for i in range(0, 32)] for j in range(0, len(inputlistFiestal))]

file = open("a1.txt", "w")
for i in inputlistAlpha:
    string = ""
    for j in i:
        string = string + str(j)
    file.write(string)
    file.write("\n")
file.close()

file = open("a2.txt", "w")
for i in outputlistAlpha:
    string = ""
    for j in i:
        string = string + str(j)
    file.write(string)
    file.write("\n")
file.close()

file = open("a3.txt", "w")
for i in range(0, len(inputlistExpand)):
    if (i % 2) != 1:
        string = ""
        for j in inputlistExpand[i]:
            string = string + str(j)
        file.write(string)
        file.write("\n")
file.close()
