# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 21:42:05 2026

@author: vebiola
"""

# Program Simulasi Mesin ATM Pintar (Tarik Tunai)
# Fitur : Validasi kecukupan saldo, kelipatan nominal Rp50.000, dan batas penarikan Rp2.500.000

print("Mesin ATM Pintar")
print("----------------")
saldo_rekening=int(input("Saldo Rekening : Rp"))
tarik_tunai=int(input("Tarik Tunai : Rp"))
batas_maksimal=2500000
saldo_baru=saldo_rekening-tarik_tunai
if tarik_tunai>saldo_rekening :
    print("Transaksi Gagal : Saldo Anda Tidak Mencukupi")
elif tarik_tunai % 50000 !=0:
    print("Transaksi Gagal : Nominal Harus Kelipatan Rp50.000")
elif tarik_tunai>batas_maksimal :
    print("Transaksi Gagal : Batas Penarikan Tunai Sekali Transaksi Adalah Rp2.500.000")
else : 
    print("Penarikan Berhasil")
    print("Sisa Saldo Nasabah : Rp", saldo_baru)
