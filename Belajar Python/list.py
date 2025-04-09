menu = [item.lower() for item in ["Nasi Goreng", "Sate", "Rendang", "Gado-Gado", "Bakso"]]

def check_menu(selection):
    if selection in menu:
        print(f"{selection} tersedia.")
    else:
        print("Menu tidak tersedia.")

selected_food = input("Pilih makanan: ") 
check_menu(selected_food)