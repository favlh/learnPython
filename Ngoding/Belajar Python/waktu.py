import datetime as dt

# Cetak waktu dan tanggal saat ini
current_time = dt.datetime.now()
print("Waktu dan tanggal saat ini:", current_time)

# Cetak waktu dan tanggal saat ini dengan format yang berbeda
current_time = dt.datetime.now()
print("Waktu dan tanggal saat ini:", current_time.strftime("%Y-%m-%d %H:%M:%S")) # bedanya gada waktu detik nya