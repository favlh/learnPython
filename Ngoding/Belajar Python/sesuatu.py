list = ["capung", "buaya", 'hiu']

# other_list = ["kucing", "kelinci", "ayam"]

# # menghapus sesuatu dari list
# list.pop(0)

# # tambah sesuatu ke dalam list
# list.append("babi")

# # menambahkan list lain ke dalam list yang pertama 
# list.append(other_list)

# # insert something ke dalam list
# list.insert(3, 'anjing') 

# output tanpa tanda buka dan tutup 
print(f"ini adalah daftar hewan: {', '.join(list)}")


# list lain
other_list = [1, 2, 3, 4, 5]

print(str(f"ini adalah bilangan {', '.join(map(str, other_list))}"))