class Biodata :
  def __init__ (self,full_name, nickname, gender, birth, grade, age, hobby, address, n_phone, email) :
    self.f = (full_name)
    self.n = (nickname)
    self.r = (gender)
    self.b = (birth)
    self.g = (grade)
    self.a = (age)
    self.h = (hobby)
    self.d = (address)
    self.p = (n_phone)
    self.e = (email)
    
  def bio (self) :
    print (self.f, self.n, self.r, self.b, self.g, self.a, self.h, self.d, self.p, self.e)

    
full_name = input('Full Name : ')
nickname = input('Nickname : ')
gender = input('Gender : ')
birth = input('Place Date of Birth: ')
grade = input('Grade : ')
age = input('Age : ')
hobby = input('Hobby : ')
address = input('Address : ')
n_phone = input('Number Phone : ')
email = input('E-mail : ')

bi = Biodata (full_name, nickname, gender, birth, grade, age, hobby, address, n_phone, email)
print(bi.bio())
