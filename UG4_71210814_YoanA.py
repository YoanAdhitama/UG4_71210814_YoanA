#Yoan Adhitama
#71210814

import json

tt = int(input("Masukkan jumlah barang Boskuu = "))
brg = []
r = 0

for i in range(tt) :
    num = i + 1
    brgname = str(input(f"Nama Barang {num} = "))
    price = int(input(f"Harga Barang {num} = "))

    brg.append({
        "nama": brgname, "harga": price
    })
    r = r + price
    print("\n")


file = dict({
    "total" : r, "barang" : brg
})
with open("data.json", "w") as data :
    json.dump(file, data)