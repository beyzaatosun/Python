class Calculator(object):
    
    def __init__(self,a,b):
        self.v1=a
        self.v2=b
        
    def add(self):
        return self.v1+self.v2
    
    def minus(self):
        return self.v1-self.v2
    
    def multipy(self):
        return self.v1*self.v2
    
    def division(self):
        return self.v1 / self.v2
    

v1=int(input("first value: "))
v2=int(input("second value: "))

selection=int(input("Please select operation! \nadd ->1\nminus->2\nmultipy->3\ndivision->4 \n --:"))
c1=Calculator(v1,v2)

if selection==1:
    add_result=c1.add()
    print("add: {}".format(add_result))

elif selection==2:
    minus=c1.minus()
    print("minus:{}".format(minus))
    
elif selection==3:
    multipy=c1.multipy()
    print("multipy: {}".format(multipy))
elif selection==4:
    division=c1.division()
    print("division: {}".format(division))

else:
    print("invalid value")
    


