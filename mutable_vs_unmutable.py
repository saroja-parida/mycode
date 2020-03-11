"""
Mutable vs unmutable explained
"""
#Mutable 

class mutable_c:
    def __init__(self):
        print("The object is initiated")
    @classmethod
    def mutableF(self):
        print("mutable objects are like list,dictionary,integer.. etc")
        l1=['s','a','r','o','j']
        my_dict={'a':12,'b':20,'c':25}
        print("before change of the list and dictionary")
        print "=="*50
        print ("{} id of the list ".format(id(l1)))
        print l1
        print ("{} id of the dict".format(id(my_dict)))
        print my_dict
        l1[2]=60
        my_dict['d']=60
        print("after change  of the list and dictionary")
        print "=="*50
        print ("{} id of the list ".format(id(l1)))
        print l1
        print ("{} id of the dict".format(id(my_dict)))
        print my_dict
    def imutableF(self):
        print("immutable objects are like string,tuple,int. etc")
        mystr="saroj"
        my_tuple=(12,20,25)
        print("before change of the string and tuple")
        print "=="*25
        print ("{} id of the str ".format(id(mystr)))
        print mystr
        print ("{} id of the my_tuple".format(id(my_tuple)))
        print my_tuple
        mystr="change_saroj"
        my_tuple=(1,3,4)
        print("after change  of the list and dictionary")
        print "=="*50
        print ("{} id of the str".format(id(mystr)))
        print mystr
        print ("{} id of the my tuple".format(id(my_tuple)))
        print my_tuple
    def append_to_list(self,mystr,*a_list):
        newl=self.a_list.append(self.mystr)
        return newl
obj=mutable_c()
print mutable_c.mutableF()
print obj.imutableF()

print obj.append_to_list("saroj")
print obj.append_to_list("sagar")




