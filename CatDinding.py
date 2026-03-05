Panjang = float(input("Masukan panjang (Dalam satuan Meter):"))
Lebar = float(input("Masukan lebar (Dalam satuan Meter):"))
Tinggi = float(input("Masukan tinggi (Dalam satuan Meter):"))

Luas_tanpa_alastutup = 2 * Tinggi * (Panjang + Lebar)
Jum_Cat = Luas_tanpa_alastutup / 10

print("Luas dinding:", Luas_tanpa_alastutup, "M^2")
print("Jumlah kaleng cat yang dibutuhkan:", Jum_Cat, "Kaleng")