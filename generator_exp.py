"""
Generator explained
"""
import traceback
class ygen:
    def __init__(self,n):
        self.n=n
        self.i=0
    def ygen_f(self):
        while self.i < self.n:
            i=self.i
            yield i
            self.i+=1
        
try:
    obj=ygen(10)
    print (type(obj.ygen_f()))
    g=obj.ygen_f()
    print( g.next())
    print( g.next() )
    print( g.next() )
    print( g.next() )
    print( g.next() )

except:
    traceback.print_exc()

        
