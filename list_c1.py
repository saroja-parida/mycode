#convert celcius to farenhit
import re
st = "print only the words that start with s in this sentence"
l=re.split(" ",st)
L=[]
for i in l:
    match=re.search(r'^s[\w]',i)
    if match:
        L.append(i)
print L        


