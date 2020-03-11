#Reading and writing binary files: here the example is for a jpeg file copy
BUFFERSIZE = 200
ifile = "/Users/sarojakumar.parida/Documents/python.JPG"
ofile = "/Users/sarojakumar.parida/Documents/python-copy.JPG"
ifile = open(ifile, 'rb')
ofile = open(ofile, 'wb')
buffer = ifile.read(BUFFERSIZE)
while(len(buffer)):
    ofile.write(buffer)
    buffer = ifile.read(BUFFERSIZE)

#working with a video file 
#seek -> set pointer in a file
#take -> get the pointer in a file

tfile = open("/Users/sarojakumar.parida/Documents/chat.txt","r")
f = tfile.readline()
print (f, end='')
fpos = tfile.tell()
print("{} postion".format(fpos))
print (f, end='')
f = tfile.readline()
print("{} postion".format(fpos))
f = tfile.readline()
print (f, end='')
print("{} postion".format(fpos))
print tfile.seek(0)
