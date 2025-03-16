class person(object):
    def __init__(self, name, idnumber):
           self.name = name 
           self.idnumber = idnumber
    def display(self):
          print(self.name)
          print(self.idnumber)
class Employeer(person):
    def __init__(self, name, idnumber, salary, post):
         
         self.salary = salary
         self.post = post
         person.__init__(self, name, idnumber)
a=Employeer('Angel', 202222, 122222, "Intern")      
a.display()           