# class A:
#     def fun1(self):
#         print('class A')
# class B(A):
#     def fun2(self):
#         print('class B')
# class C(B):
#     def fun3(self):
#         print('class C')
# obj1=C()
# obj1.fun1()
# obj1.fun2()
# obj1.fun3()

#without using constructor

#mobile(storage,color)
#samsung(ram)
#samsung galaxy(speed)

# class mobile:
#     def fun1(self,storage,color):
#         self.storage=storage
#         self.color=color
#         print('storage :',self.storage)
#         print('color : ',self.color)
# class samsung(mobile):
#     def fun2(self,ram):
#         self.ram=ram
#         print('ram : ',self.ram)
# class galaxy(samsung):
#     def fun3(self,speed):
#         self.speed=speed
#         print('speed : ',self.speed)
# obj=galaxy()
# obj.fun1('120GB','BLACK')
# obj.fun2('8GB')
# obj.fun3('120HZ')


#using constructor

#car : wheel,color
#maruthi : model
#maruthi 800 : price

# class car:
#     def __init__(self,wheel,color):
#         self.wheel=wheel
#         self.color=color
#         print('wheel : ',self.wheel)
#         print('color : ',self.color)
# class maruthi(car):
#     def __init__(self,wheel,color,model):
#         super().__init__(wheel,color)
#         self.model=model
#         print('model : ',self.model)
# class maruthi_800(maruthi):
#     def __init__(self,wheel,color,model,price):
#         super().__init__(wheel,color,model)
#         self.price=price
#         print('price : ',self.price)
# obj=maruthi_800('MRF','RED',2020,500000)





