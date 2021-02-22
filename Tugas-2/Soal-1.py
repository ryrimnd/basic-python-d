namakontak = []
telpkontak = []

def daftarkontak():
    print("Daftar kontak:")
    for i in range(len(namakontak)):
        print("Nama: ", namakontak[i])
        #print("No Telepon: {nom:012d}".format(nom=telpkontak[i]))
        print("No Telepon: 0{nom}".format(nom=telpkontak[i]))
    print()

def tambahkontak():
    namatambah = str(input("Nama: "))
    telptambah = int(input("No Telepon: "))
    namakontak.append(namatambah)
    telpkontak.append(telptambah)
    print("Kontak berhasil ditambahkan")
    print()

print("Selamat datang!")

while True:
    print("---Menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    pilihmenu = int(input("Pilih menu: "))
    print()
    if pilihmenu == 1:
        daftarkontak()
    elif pilihmenu == 2:
        tambahkontak()
    elif pilihmenu == 3:
        print("Program selesai, sampai jumpa!")
        break
    else:
        print("Menu tidak tersedia")
        pass