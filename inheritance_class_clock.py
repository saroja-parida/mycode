class clock(object):
    def __init__(self,sec=0,minute=0,hr=0):
        self.__sec = sec
        self.__min = minute
        self.__hr = hr

    def tick(self):
        if self.__sec == 59:
            self.__sec=0
            if self.__min == 59:
                self.__min=0
                if self.__hr==23:
                    self.__hr=0
                else:
                    self.__hr+=1
            else:
                self.__min+=1
        else:
            self.__sec=+1
    def __str__(self):
        return "%d:%d:%d"%(self.__sec,self.__min,self.__hr)

obj1 = clock()
print obj1
for i in xrange(1000):
    obj1.tick()
print obj1    
