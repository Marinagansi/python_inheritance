# A python program to demonstarate inheritance
#BAse and super class. note object in bracket
#(Generally , object is made ancestor of all classes).
#In python 3.x "class person" is equivalent to "class parent (object)"

class Base(object):

    #constructor
    def __init__(self,name):
        self.n=name
    def __init(self):
        self.__d=42#making instance variable constant by underscore

    #To get name
    def getname(self):
        return self.n

#Inherited or sub class (Note person in bracket)
class Child(Base):
    #constructor
    def __init__(self,name,age):
        Base.__init__(self,name)
        self.age=age

    def getage(self):
        return self.age

#Ind=herited or sub class (Note person in bracket)
class Grandchild(Child):
    #constructor
    def __init__(self,name,age,address):
        Child.__init__(self,name,age)
        self.address=address

    def getaddress(self):
        return self.address

#driver code
g=Grandchild("marina",12,78)
print(g.getage(),g.getname(),g.getaddress())

