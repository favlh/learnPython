# Belajar Elif

daftar = ["nasi goreng", "mie goreng", "sate", "soto"]

while True:
    menu = input(f"silakan pilih menu dari {', '.join(daftar)}: ")

    if menu == daftar[0]:
        print(f"anda memesan {daftar[0]}")
        break
    elif menu == daftar[1]:
        print(f"anda memesan {daftar[1]}")
        break
    elif menu == daftar[2]:
        print(f"anda memesan {daftar[2]}")
        break
    elif menu == daftar[3]:
        print(f"anda memesan {daftar[3]}")
        break
    elif menu == "semua":
        print("anda memesan semua menu")
        break
    else:
        print("silahkan pilih menu yang tersedia")