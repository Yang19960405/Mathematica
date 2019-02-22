class AAA:
    __names="aaa"
    asd=""
    def aaa(self):
        print(self.__names)
        pass
    pass

def add(id):
    print(id.__str__()+"1");
add(1)
lx=AAA()
print(lx.aaa())
import selenium
print (selenium.__file__)