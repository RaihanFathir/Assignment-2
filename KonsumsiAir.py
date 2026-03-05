Jumlah_Orang = int(input("Masukan jumlah orang:"))

Air_perhari = Jumlah_Orang * 2.5
Air_perminggu = Air_perhari * 7
Jumlah_Galon = round(Air_perminggu / 19)
Harga_Galon = Jumlah_Galon * 19000

print("Jumlah orang:", Jumlah_Orang)
print("Kebutuhan air per minggu:", Air_perminggu, "Liter")
print("Total galon yang harus dibeli:", Jumlah_Galon, "Galon")
print("Uang yang harus dialokasikan:Rp.", Harga_Galon)
