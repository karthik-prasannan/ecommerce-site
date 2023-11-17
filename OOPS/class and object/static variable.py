# static : variable
# *)  a variable that defines inside a class but outside a function called static variable
# *) we cannot change the value of static variable during object creation

#syntax
# class class_name:
#     def function_name(self):
#         #body
# a=class_name
# a.function_name()

# class employee:
#     company_name='TCS'
#     def setval(self,id,name,designation,salary):
#         self.id=id
#         self.name=name
#         self.designation=designation
#         self.sal=salary
#         print('company_name= ',employee.company_name)
#         print('employee id=',name)
#         print('name= ',name)
#         print('designation= ',designation)
#         print('salary= ',salary)
#         print()
# a=employee()
# a.setval(1234,'karthik','programmer',30000)
#
# b=employee()
# b.setval(3456,'jaba','programmer',10000)

# create a class student with atleast 2 static variables and dynamic variables:name,roll number,total mark

# class student:
#     school_name='unity'
#     department='science'
#     def setval(self,name,roll_no,total_mark):
#         self.name=name
#         self.roll_no=roll_no
#         self.total_mark=total_mark
#         print('school name = ',student.school_name)
#         print('department = ',student.department)
#         print('name = ',name)
#         print('roll no = ',roll_no)
#         print('total mark = ',total_mark)
#         print()
# a=student()
# a.setval('karthik',10,'55%')
#
# b=student()
# b.setval('jaba',12,'43%')