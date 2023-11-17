class A:
    def setval(self,name,salary):
        self.name=name
        self._salary=salary
        print('name : ',self.name)
        print('salary : ',self._salary)
class B(A):
    def setval1(self):
        print(self.name)
        print(self._salary)
obj=B()
obj.setval('kpk',10000)
obj.setval1()
print('name : ',obj.name,'salary : ',obj._salary)

#python protected acts as same as public
