# class Car:
#     wheels=4
#     def __init__(self):
#         self.mil=10
#         self.com="BMW"
# c1=Car()
#
# c1.mil=15
# print(c1.com,c1.mil,c1.wheels)
# class Students:
#     school="credence"
#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
# s=Students(50,25,30)

# class Computer:
#     def __init__(self):
#         self.name="shubham"
#         self.age=26
#         self.age=25
#     def compare(self,other):
#         if self.age==other.age:
#            return True
#         else:
#            return False
# c1=Computer()
# c1.age=30
# c1.name="nikhil"
#
# c2=Computer()
# if c1.compare(c2):
#     print("they are same")
# else:
#     print("they are not same")
#
#
# print(c2.age)
# print(c1.age)
class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
     print("config is",self.cpu,self.ram)
c1=Computer('i5',16)
c1.config()











class Song(object):

 def __init__(self, lyrics):
   self.lyrics = lyrics

 def sing_me_a_song(self):
  for line in self.lyrics:
   print(line)

happy_bday = Song(["Happy birthday to you",
 "I don't want to get sued",
 "So I'll stop right there"])
bulls_on_parade = Song(["They rally around tha family",
 "With pockets full of shells"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

