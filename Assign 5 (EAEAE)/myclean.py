import re
file = open("input.txt")
# data = file.read().split()
# print(len(data))
data_in = file.read().split()
# print(data_in)
file = open("output.txt")
data = file.read()
entry = re.findall("[f-u]{16}",data)

out_put = []
in_put = []
for i in range(len(entry)):
    if(i%2==0):
        in_put.append(entry[i])
    else:
        out_put.append(entry[i])
if(in_put==data_in):
    print(True)

file = open("clean.txt","w")
for line in out_put:
    if(line == 'ffffffffffffffff'):
        file.write('\n')
    file.write(line)
    file.write(' ')
file.close
