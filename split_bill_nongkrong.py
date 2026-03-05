jumOrang = (int(input("Masukan jumlah orang:")))
jumTagihan = (float(input("Masukan total tagihan:")))

pajak = jumTagihan*(10/100)
setPajak = jumTagihan + pajak

perOrang = setPajak/jumOrang

print("Harga setelah pajak:", setPajak)
print("Split bill:", perOrang, "per orang")
