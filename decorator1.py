def bread(fun):
    print("Bread before fun")
    fun()
    print("Bread after fun")
def tomato(fun):
    print("tomato before fun")
    fun()
    print("tamato after fun")
#@bread
#@tomato
def sandwitch(food="yes"):
    print(food)
sandwitch=bread(sandwitch)
sandwitch
