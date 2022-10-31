# Tugas Besar Pengkom kelompok 5
# Alghoza Hamdani 16522207
# Muhammad Rafly 19622137
# Aththariq Lisan Qur'an Daulah Sentono 19622037
# Muhammad Ali Ibrahim Al Hariri 16522067

import datetime
from data import data

now = datetime.datetime.now()
jamnow = int(now.strftime("%H"))

lanjut = True
bank = data.bank
menu = data.menu
mobil = data.mobil
menu_makan = data.menu_makan
menu_minum = data.menu_minum
stasiun = data.stasiun
saldonow = data.saldo

while lanjut:
    print(f"Saldo gopay Anda adalah: {saldonow}\n")

    print("Silahkan pilih menu gojek di bawah ini")
    for i in range(len(menu)):
        if i != len(menu) - 1:
            print(menu[i], ";", end=" ")
        else:
            print(menu[i])
    menu_pil = str(input("Pilih menu: "))
    print()
    tarif = 0

    if menu_pil == "Top Up":
        print("Pilih bank untuk request saldo")
        for i in range(len(bank)):
            if i != len(bank) - 1:
                print(bank[i], ";", end=" ")
            else:
                print(bank[i])
        bank_pil = str(input("Pilih bank: "))
        saldo = int(input("Masukkan nominal saldo yang ingin Anda tambahkan: "))
        print(f"Saldo gopay Anda telah ditambahkan sebanyak Rp{saldo} dari bank {bank_pil}.")
        saldonow = saldonow + saldo
        print(f"Saldo gopay Anda adalah: {saldonow}")
        print()

    elif menu_pil == "GoRide":
        titik_jemput = str(input("Masukkan titik jemput Anda: "))
        titik_antar = str(input("Masukkan titik antar Anda: "))

        if 7 <= jamnow < 9:
            tarif += 15000
        elif 9 <= jamnow < 12:
            tarif += 9000
        elif 12 <= jamnow < 15:
            tarif += 11000
        elif 15 <= jamnow < 18:
            tarif += 18000
        elif 18 <= jamnow < 20:
            tarif += 15000
        elif (20 <= jamnow < 24) or (0 <= jamnow < 7):
            tarif += 16000

        print(f"Tarif Anda adalah: {tarif}")
        print()

        if saldonow >= tarif:
            print(f"Titik jemput Anda adalah {titik_antar} dan titik antar Anda adalah {titik_jemput} dengan tarif "
                  f"Rp{tarif}.")
            konfirmasi = str(input("Konfirmasi pesanan Anda: "))  # Iya/Tidak

            if konfirmasi == "Iya":
                print()
                print("Driver sedang menuju tempat Anda.")
                print("Kembali ke menu utama.")
                saldonow -= tarif
        else:
            print("Saldo Gopay Anda tidak cukup.")
            print("Kembali ke menu utama.")

        print()

    elif menu_pil == "GoCar":
        titik_jemput = str(input("Masukkan titik jemput Anda: "))
        titik_antar = str(input("Masukkan titik antar Anda: "))

        print()
        print("Tipe mobil")
        for i in range(len(mobil)):
            if i != len(mobil) - 1:
                print(list(mobil.keys())[i], ";", end=" ")
            else:
                print(list(mobil.keys())[i])

        while True:
            try:
                tipe_mobil = str(input("Pilih tipe mobil: "))
                tarif += mobil[tipe_mobil]
                break
            except KeyError:
                print("Pilih tipe mobil yang valid.")

        if 7 <= jamnow < 9:
            tarif += 17000
        elif 9 <= jamnow < 12:
            tarif += 11000
        elif 12 <= jamnow < 15:
            tarif += 13000
        elif 15 <= jamnow < 18:
            tarif += 20000
        elif 18 <= jamnow < 20:
            tarif += 17000
        elif (20 <= jamnow < 24) or (0 <= jamnow < 7):
            tarif += 18000

        print(f"Tarif Anda adalah: {tarif}")
        print()

        if saldonow >= tarif:
            print(f"Titik jemput Anda adalah {titik_antar} dan titik antar Anda adalah {titik_jemput} dengan tarif "
                  f"Rp{tarif}.")
            konfirmasi = str(input("Konfirmasi pesanan Anda: "))  # Iya/Tidak

            if konfirmasi == "Iya":
                print()
                print("Driver sedang menuju tempat Anda.")
                print("Kembali ke menu utama.")
                saldonow -= tarif
        else:
            print("Saldo Gopay Anda tidak cukup.")
            print("Kembali ke menu utama.")

        print()

    elif menu_pil == "GoSend":
        barang = str(input("Barang yang ingin dikirim adalah: "))

        while True:
            size_barang = str(input("Ukuran barang: "))  # Kecil/Sedang/Besar
            if size_barang == "Kecil":
                tarif += 1000
                break
            elif size_barang == "Sedang":
                tarif += 2000
                break
            elif size_barang == "Besar":
                tarif += 3000
                break
            else:
                print("Pilih ukurang barang yang valid.")

        print()
        titik_jemput = str(input("Masukkan titik jemput Anda: "))
        titik_antar = str(input("Masukkan titik antar Anda: "))

        if 7 <= jamnow < 9:
            tarif += 15000
        elif 9 <= jamnow < 12:
            tarif += 9000
        elif 12 <= jamnow < 15:
            tarif += 11000
        elif 15 <= jamnow < 18:
            tarif += 18000
        elif 18 <= jamnow < 20:
            tarif += 15000
        elif (20 <= jamnow < 24) or (0 <= jamnow < 7):
            tarif += 16000

        print(f"Tarif Anda adalah: {tarif}")

        if saldonow >= tarif:
            print(f"Titik jemput Anda adalah {titik_antar} dan titik antar Anda adalah {titik_jemput} dengan tarif "
                  f"Rp{tarif}.")
            konfirmasi = str(input("Konfirmasi pesanan Anda: "))  # Iya/Tidak

            if konfirmasi == "Iya":
                print()
                print("Driver sedang menuju tempat Anda.")
                print("Kembali ke menu utama.")
                saldonow -= tarif
        else:
            print("Saldo Gopay Anda tidak cukup.")
            print("Kembali ke menu utama.")

        print()

    elif menu_pil == "GoFood":
        print("Menu Makanan")
        for i in range(len(menu_makan)):
            if i != len(menu_makan) - 1:
                print(list(menu_makan.keys())[i], ";", end=" ")
            else:
                print(list(menu_makan.keys())[i])
        print("Menu Minuman")
        for i in range(len(menu_minum)):
            if i != len(menu_minum) - 1:
                print(list(menu_minum.keys())[i], ";", end=" ")
            else:
                print(list(menu_minum.keys())[i])
        print()

        while True:
            try:
                makanan = input("Pilih menu makanan: ")
                tarif += menu_makan[makanan]
                break
            except KeyError:
                print("Pilih makanan yang valid.")
        print()

        while True:
            try:
                minuman = input("Pilih menu minuman: ")
                tarif += menu_minum[minuman]
                break
            except KeyError:
                print("Pilih minuman yang valid.")
        print()

        titik_antar = str(input("Masukkan titik antar Anda: "))
        if 7 <= jamnow < 9:
            tarif += 15000
        elif 9 <= jamnow < 12:
            tarif += 9000
        elif 12 <= jamnow < 15:
            tarif += 11000
        elif 15 <= jamnow < 18:
            tarif += 18000
        elif 18 <= jamnow < 20:
            tarif += 15000
        elif (20 <= jamnow < 24) or (0 <= jamnow < 7):
            tarif += 16000
        print(f"Tarif Anda adalah: {tarif}")
        print()

        if saldonow >= tarif:
            print(f"Makanan Anda adalah {makanan} dan minuman Anda adalah {minuman} akan diantar ke tempat Anda di "
                  f"{titik_antar} dengan tarif {tarif}")
            konfirmasi = str(input("Konfirmasi pesanan Anda: "))  # Iya/Tidak
            if konfirmasi == "Iya":
                print()
                print("Driver sedang menuju tempat Anda.")
                print("Kembali ke menu utama.")
                saldonow = saldonow - tarif
        else:
            print("Saldo Gopay Anda tidak cukup.")
            print("Kembali ke menu utama.")

        print()

    elif menu_pil == "GoTransit":
        print("Pilih Stasiun")
        for i in range(len(stasiun)):
            if i != len(stasiun) - 1:
                print(stasiun[i], ";", end=" ")
            else:
                print(stasiun[i])

        stasiun_i = str(input("Pilih Stasiun Keberangkatan: "))
        stasiun_f = str(input("Pilih Stasiun Tujuan: "))
        if (stasiun_i == "Stasiun Manggarai") or (stasiun_f == "Stasiun Manggarai"):
            tarif = 5000
        else:
            tarif = 10000

        print("Tarif Anda adalah:", tarif)
        if saldonow >= tarif:
            print("Stasiun keberangkatan Anda adalah", stasiun_i, "dan Stasiun tujuan Anda adalah", stasiun_f,
                  "dengan harga tiket", tarif)
            konfirmasi = str(input("Konfirmasi pesanan Anda:"))  # Iya/Tidak
            if konfirmasi == "Iya":
                print("Silahkan simpan tiket Anda")
                print("Kembali ke menu utama")
                saldonow = saldonow - tarif
        else:
            print("Saldo Gopay Anda tidak cukup")
            print("Kembali ke menu utama")

    else:
        print("Pilihan menu tidak valid.")

    cek = str(input("Apakah Anda masih ingin melanjutkan?\n"))  # Iya/Tidak
    if cek == "Tidak":
        lanjut = False

data.saldo = saldonow
data.save()

print("Program Selesai")
