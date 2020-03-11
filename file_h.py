
class myclass():
  @classmethod
  def c_to_f(self,temp,filen):
    with open(filen,"a") as fd:
      if temp > -273:
        f=temp*9/5+32
        print("{} is farenhit".format(f))
        fd.write("temp is"+str(f)+"\n")
      else:
        print("{} is not valid temperature".format(temp))
    
list=[10,-20,-289,100]
for i in list:
  myclass.c_to_f(i,"test.txt")
