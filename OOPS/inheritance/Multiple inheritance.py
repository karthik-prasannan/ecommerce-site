# Multiple inheritance :


# class A:
#     def fun1(self):
#         print('class A')
# class B:
#     def fun2(self):
#         print('class B')
# class C(A,B):
#     def fun3(self):
#         print('class C')
# obj1=C()
# obj1.fun1()
# obj1.fun2()
# obj1.fun3()

# father(fname,address)
# mother(mname)
# son(sname)
# create 2 son object

# class father:
#     def fun1(self,fname,address):
#         self.fname=fname
#         self.address=address
#         print('father name : ',self.fname)
#         print('Address : ',self.address)
# class mother:
#     def fun2(self,mname):
#         self.mname=mname
#         print('Mother name : ',self.mname)
# class son(father,mother):
#     def fun3(self,sname):
#         self.sname=sname
#         print('son name : ',sname)
#         print()
# c1=son()
# c1.fun1('AB','WXYZ')
# c1.fun2('BC')
# c1.fun3('CD')
#
# c2=son()
# c2.fun1('XY','ZYXW')
# c2.fun2('YZ')
# c2.fun3('XZ')

# class father:
#     def __init__(self,fname):
#         self.fname=fname
# class mother:
#     def __init__(self,mname):
#         self.mname=mname
# class son(father,mother):
#     def __init__(self,fname,mname,sname):
#         father.__init__(self,fname)
#         mother.__init__(self,mname)
#         self.sname=sname
#         print('fathername : ',self.fname)
#         print('mother name : ',self.mname)
#         print('son name : ',self.sname)
#         print()
# c=son('jaba','jaba1','jaba2')
# c1=son('baja','baja1','baja2')

# company=company name, location
# team leader=team leader name , department
# worker=emp_name,designation,salary
#
# class company:
#     def __init__(self,company_name,location):
#         self.company_name=company_name
#         self.location=location
# class team_leader:
#     def __init__(self,team_leader_name,departent):
#         self.team_leader_name=team_leader_name
#         self.department=departent
# class worker(company,team_leader):
#     def __init__(self,company_name,location,team_leader_name,department,emp_name,designation,salary):
#         company.__init__(self,company_name,location)
#         team_leader.__init__(self,team_leader_name,department)
#         self.emp_name=emp_name
#         self.designation=designation
#         self.salary=salary
#         print('company name : ',company_name)
#         print('location : ',location)
#         print('team leader name : ',team_leader_name)
#         print('department : ',department)
#         print('employee name : ',emp_name)
#         print('designation : ',designation)
#         print('salary : ',salary)
# c=worker('TCS','ERNAKULAM','JABA','PROGRAMMER','JABALI','DEVELOPER',1000000)








