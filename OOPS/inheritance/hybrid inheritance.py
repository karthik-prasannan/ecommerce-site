# it is a combination of different types of inheritance

# class parent:
#     def fun(self):
#         print('parent class')
# class childA(parent):
#     def fun1(self):
#         print('child A')
# class chiildB(parent):
#     def fun2(self):
#         print('child B')
# class childC(childA,chiildB):
#     def fun3(self):
#         print('child C')
# obj=childC()
# obj.fun()
# obj.fun1()
# obj.fun2()
# obj.fun3()


# university(univ_name,location)
# collage(collage_name)
# course(course_name)
# student(roll:no,name)

# class university:
#     def fun(self,univ_name,location):
#         self.univ_name=univ_name
#         self.location=location
#         print('university name = ',self.univ_name)
#         print('location = ',self.location)
# class collage(university):
#     def fun1(self,collage_name):
#         self.collage_name=collage_name
#         print('collage name = ',self.collage_name)
# class course(university):
#     def fun2(self,course_name):
#         self.course_name=course_name
#         print('course name = ',self.course_name)
# class student(course,collage):
#     def fun3(self,rollno,name):
#         self.rollno=rollno
#         self.name=name
#         print('roll no = ',self.rollno)
#         print('name = ',self.name)
# obj=student()
# obj.fun('calicut university','calicut')
# obj.fun1('HM COLLAGE')
# obj.fun2('BSC PHYSICS')
# obj.fun3(10,'KARTHIK')


# hw
# using constuctor
# university(univ_name,location)
# collage(collage_name)
# course(course_name)
# student(roll:no,name)

class university:
    def __init__(self,univ_name,location):
        self.univ_name=univ_name
        self.location=location

class collage(university):
    def __init__(self,univ_name,location,collage_name):
        university.__init__(self,univ_name,location)
        self.collage_name=collage_name

class course(university):
    def __init__(self,univ_name,location,course_name):
        university.__init__(self,univ_name,location)
        self.course_name=course_name

class student(collage,course):
    def __init__(self,univ_name,location,collage_name,course_name,roll_no,name):
        collage.__init__(self,univ_name,location,collage_name)
        course.__init__(self,univ_name,location,course_name)
        self.roll_no=roll_no
        self.name=name

        print('university name : ', self.univ_name, 'location : ', self.location)
        print('collage name : ', self.collage_name)
        print('course name : ', self.course_name)
        print('roll no : ', self.roll_no, 'name : ', self.name)
obj=student('calicut univ','calicut','hm collage','bsc physics',10,'karthik')













