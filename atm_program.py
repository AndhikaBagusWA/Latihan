import random
import datetime
from customer import Customer

atm = Customer(id)

#looping pemeriksaan
while True:

    id = int(input('Masukkan pin anda: '))
    trial = 0

    #looping verifikasi
    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input('Pin anda salah. Silahkan Masukkan lagi: '))
        trial += 1

        if trial == 3:
            print('Error, silahkan ambil kartu lagi dan coba lagi...')
            exit()
    while True:

        print('Selamat datang\n')
        print('1. Cek Saldo \t 2. Debet \n 3. Simpan \t 4. Ganti Pin \n 5. Keluar')

        pilih_menu = int(input('Silahkan pilih menu : '))

        if pilih_menu == 1:
            print('Saldo anda sekrang: Rp. ' + str(atm.checkBalance()) + '\n'  )
        elif pilih_menu == 2:
            nominal = float(input('Masukkan nominal saldo: '))
        elif pilih_menu == 3:
        elif pilih_menu == 4:
        elif pilih_menu == 5: