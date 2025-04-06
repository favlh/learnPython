buah = ["pisang", "apel", "semangka", "apukat"]

buah.extend(["mangga", "jeruk"])

def menu(selection):
    if selection in buah:
        print(f"{selection} tersedia")
    else:
        print(f"{selection} tidak tersedia")

def pilih_makanan():
    while True:
        buah_buahan = input("Pilih buah-buahanmu (ketik 'keluar' untuk berhenti): ")
        if buah_buahan.lower() == "keluar":
            print("Terima kasih telah menggunakan program ini.")
            break
        menu(buah_buahan)  # memanggil fungsi menu

pilih_makanan()