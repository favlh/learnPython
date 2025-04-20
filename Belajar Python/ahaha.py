def ahaha():
    orang = input("Masukkan suasana hatimu: ").strip()
    if orang.isdigit():
        print("Input tidak boleh berupa angka.")
        return
    if orang == "ketawa":
        print(f"Suasana hati mu sedang {orang}")
    elif orang == "sedih":
        print(f"Suasana hati mu sedang {orang}")
    elif orang == "marah":
        print(f"Suasana hati mu sedang {orang}")
    else:
        print("Suasana hati mu tidak terdaftar")

ahaha()