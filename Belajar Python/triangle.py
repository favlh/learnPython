class Segitiga:
  def __init__(self, tinggi):
    self.tinggi = tinggi
  
  def buat_segitiga(self):
    for i in range(1, self.tinggi + 1):
        print(' ' * (self.tinggi - i) + '*' * (2 * i - 1))
        
tinggi = int(input("masukkan tinggi segitiga (maksimal 10): "))
if tinggi > 10:
    print("Tinggi tidak boleh lebih dari 10.")
else:
    segitiga = Segitiga(tinggi)
    segitiga.buat_segitiga()