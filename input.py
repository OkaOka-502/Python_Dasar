class Segitiga :
  
  def __init__ (self, alas, tinggi) :
    self.a = int(alas)
    self.t = int(tinggi)
    
  def luas (self) :
     result = (1/2 * self.a * self.t)
     print (result)
    
alas = input('Alas : ')
tinggi = input('Tinggi : ')

sg = Segitiga(alas, tinggi)
print (sg.luas())
