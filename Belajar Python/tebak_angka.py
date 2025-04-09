import random

angka_rahasia = random.randint(1, 10)

while True:
    try:
        tebakan = int(input("masukkan angka yang kamu pikirkan: "))
        
        if tebakan < 1 or tebakan > 10:
            print("angka harus diantara 1 sampai 10")
            continue
    
        if tebakan < angka_rahasia:
            print("tebakan kamu terlalu kecil")
        elif tebakan > angka_rahasia:
            print("tebakan kamu terlalu besar")
        else:
            print("tebakan kamu benar")
            break
    except ValueError:
        print("masukkan sesuatu!!")  