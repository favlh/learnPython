def jangan_kosong(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("jangan ada yang kosong!! Masukkan sesuatu")

try:
    kalimat_pertama = jangan_kosong("masukkan kalimat atau angka pertama: ")
    kalimat_kedua = jangan_kosong("masukkan kalimat atau angka kedua: ")
    
    if not kalimat_pertama or not kalimat_kedua:
        raise ValueError("jangan ada yang kosong!!")
    
    if kalimat_pertama == kalimat_kedua:
        print("kalimatnya sama")
    else:
        print("kalimatnya beda")
except ValueError as e:
    print(f"error: {e}")