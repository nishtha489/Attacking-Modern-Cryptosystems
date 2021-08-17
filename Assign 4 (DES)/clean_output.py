import re
file = open("output.txt","r")
text = file.read()
# print(text)
outputs = re.findall("[f-u]{16}",text)
print(outputs)

fout = open("clean_output.txt","w")
for line in outputs:
    fout.write(line)
    fout.write("\n")
fout.close()
