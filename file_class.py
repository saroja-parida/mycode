class file_h:
    def __init__(self,fl):
        self.__fl=fl
    def file_cat(self):
        for file_n in self.__fl:
            with open(file_n,"r") as f1:
                print(f1.readline())
obj1=file_h("decorator1.py")
obj1.file_cat()
