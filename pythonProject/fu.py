# class Employee:
#     id=101
#     name='shubham'
#     city='pune'
#     def empinfo(self):
#         print(f"id:{self.id},name:{self.name},city:{self.city}")
#     def updateinfo(self,sid,name,city):
#      self.id=sid
#      self.name=name
#      self.city=city
# a=Employee()
# a.empinfo()
# id=500
# name='akash'
# city='mumbai'
# b=Employee()
# b.empinfo()
# b.updateinfo(id,name,city)
# b.empinfo()
from calc import*
class Employee:
    try:
        def personalinfo(self):
            print(f"id:{self.id},name:{self.name},city:{self.city}")

        a=True
        while (a):
            userinput=int(input("1.addition\n2.substraction\n3.multiplication\4.division"))

            a=int(input("enter a number\n"))
            b=int(input("enter second number"))
            if userinput==1:
               c=add(a,b)
               print(c)
            elif userinput==2:
               c=sub(a,b)
               print(c)
            elif userinput==3:
               c=multiplication(a,b)
               print(c)
            elif userinput==4:
               c=div(a,b)
               print(c)
            else:
               print("exit")
    except ValueError as z:
        print("errpr",z)
    except NameError as X:
        print("name",X)
    except Exception as ex:
        print("shubham",ex)







