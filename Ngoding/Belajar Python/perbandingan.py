try:
    angka_pertama: int = int(input("masukkan angka pertama: "))
    angka_kedua: int = int(input("masukkan angka kedua: "))
    
    angka_ketiga = angka_pertama - angka_kedua
    
    if angka_ketiga <= 10:
        print("nilai kurang dari 10")
    else:
        print("nilai lebih dari 10")
        
except ValueError:
    print("masukkan angka dan bukan huruf")