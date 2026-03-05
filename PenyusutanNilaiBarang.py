Harga_Perolehan = float(input("Masukan harga awal barang:Rp."))
Nilai_sisa = float(input("Masukan nilai sisa:Rp."))
Masa_Manfaat = float(input("Masukan umur ekonomis (dalam tahun):"))

Penyusutan = (Harga_Perolehan - Nilai_sisa) / Masa_Manfaat
nilai_2tahun = Harga_Perolehan - (Penyusutan * 2)

print("Harga awal:Rp.", Harga_Perolehan)
print("Penyusutan per tahun:Rp.", Penyusutan)
print("Nilai barang setelah dipakai 2 tahun:Rp.", nilai_2tahun)