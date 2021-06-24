class Biodata :
  def __init__ (self, name, grade, age, hobby, address, n_phone,email) :
    self.n = (name)
    self.g = (grade)
    self.a = (age)
    self.h = (hobby)
    self.d = (address)
    self.p = (n_phone)
    self.e = (email)
    
  def bio (self) :
    print (self.n, self.g, self.a, self.h, self.d, self.p, self.e)
    
    
name = input('Name : ')
grade = input('Grade : ')
age = input('Age : ')
hobby = input('Hobby : ')
address = input('Address : ')
n_phone = input('Number Phone : ')
email = input('E-mail : ')

bi = Biodata(name, grade, age, hobby, address, n_phone,email)
print(bi.bio())
