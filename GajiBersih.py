Gaji_Pokok = float(input("Masukan jumlah gaji pokok:Rp."))
Tunjangan = float(input("Masukan jumlah tunjangan:Rp."))

Potongan_bpjs = (Gaji_Pokok + Tunjangan) * (2/100)
Potongan_Pajak = (Gaji_Pokok + Tunjangan) * (5/100)
Gaji_Bersih = (Gaji_Pokok + Tunjangan) - Potongan_bpjs - Potongan_Pajak

print("Gaji kotor:Rp.", Gaji_Pokok+Tunjangan)
print("Potongan Pajak:Rp.", Potongan_Pajak)
print("Potongan BPJS:Rp.", Potongan_bpjs)
print("Gaji bersih:Rp.", Gaji_Bersih)