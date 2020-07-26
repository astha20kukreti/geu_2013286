import re
file = open("file.txt","r")

f = file.read()
f = re.sub("[:,.?()#$]","",f).split()

d = {}
for i in f:
    if i in d.keys():
        d[i] = d[i]+f
    else:
        d[i] = f
for k,v in d.items():
    print(k , " ",v," times" )

file.close()



