#Write all the files with extensions mentioned 
#Write them in a dictionary
import os

file_extn=["pdf","txt","rtf"]
new_dict={x: [] for x in file_extn}
for dirpath,dirname,file in os.walk("/Users/sarojakumar.parida/Documents/Personal/Dipti/Capgimini"):
    for fname in file:
        f_extn=fname.split(".")[-1]
        if f_extn in file_extn:
            new_dict[f_extn].append(os.path.join(dirpath,fname))

for key,val in new_dict.items():
    print("key {}\n val {} \n".format(key,val))
