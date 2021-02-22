nama = []
umur = []
gender = []
def minta_data():
    minta_nama = str(input("Nama : "))
    minta_umur = int(input("Umur : "))
    minta_gender = str(input("Jenis kelamin (L/P): "))
    if minta_gender == 'L' or minta_gender == 'l' or minta_gender == 'Laki-laki':
        gender.append("Laki-laki")
        nama.append(minta_nama)
        umur.append(minta_umur)
    elif minta_gender == 'P' or minta_gender == 'p' or minta_gender == 'Perempuan':
        gender.append("Perempuan")
        nama.append(minta_nama)
        umur.append(minta_umur)
def unjuk_data():
    for i in range(len(nama)):
        print("Nama: ", nama[i])
        print("Umur: ", umur[i])
        print("Jenis Kelamin: ", gender[i])
        print()
while True:
    print("Menu")
    print("1. Input data")
    print("2. Lihat data")
    print()
    inputan = int(input("Pilih menu: "))
    if inputan == 1:
        minta_data()
    elif inputan == 2:
        unjuk_data()
    else:
        print("Menu tidak ditemukan")
        pass