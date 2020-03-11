def bold1(fun):
    def wrapper():
        print"This is before decorator"
        fun()
        print"This is after decorator"
    return wrapper
def italic1(fun):
    def wrapper():
        return "<i>"+fun()+"</i>"
    return wrapper
    
#@bold1
def say():
   print "hello"
say=bold1(say())
say

