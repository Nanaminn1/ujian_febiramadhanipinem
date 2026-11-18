


print("--------------")
print("WARUNG MAKAN")
print("--------------")

total = 0

while True:
    print("=== MENU MAKANAN ===")
    print("1. Nasi Goreng - Rp25000")
    print("2. Mie Ayam - Rp15000")
    print("3. Ayam Geprek - Rp20000")
    print("4. Sate Ayam - Rp30000")
    print("5. Bakso - Rp18000")
    print("0. Selesai")

    pilihan = input("Silahkan dipilih menunya (contoh: 1,2,3): ")

    if pilihan == "0":
        break

    daftar_menu = pilihan.split(",")

    for menu in daftar_menu:
        menu = int(menu)

        if menu == 0:
            continue
        elif menu == 1:
            harga = 25000
            nama = "Nasi Goreng"
        elif menu == 2:
            harga = 15000
            nama = "Mie Ayam"
        elif menu == 3:
            harga = 20000
            nama = "Ayam Geprek"
        elif menu == 4:
            harga = 30000
            nama = "Sate Ayam"
        elif menu == 5:
            harga = 18000
            nama = "Bakso"
        else:
            print("Menu tidak tersedia")
            continue

        jumlah = int(input("Berapa porsinya " + nama + ": "))

        subtotal = harga * jumlah
        total += subtotal

        print("Nama makanan:", nama)
        print("Subtotal: Rp", subtotal)

print("----STRUK PEMBAYARAN----")
print("Total belanja: Rp", total)

if total > 100000:
    diskon = total * 10 / 100
else:
    diskon = 0

total_bayar = total - diskon

print("Diskon: Rp", diskon)
print("Total bayar: Rp", total_bayar)
print("Terima kasih")
