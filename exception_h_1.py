try:
    f=open("/Users/sarojakumar.parida/Documents/printer1.rtf","r")
except IOError as err:
        print "File not found->",err
