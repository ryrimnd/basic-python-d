nama = []
age = []
banyak_data = int(input("Banyak data yang ingin dimasukan: "))
for data in range(banyak_data):
    print("+===========================+")
    nama_cus = str(input("Nama Customer: "))
    age_cus = int(input("Umur Customer: "))
    nama.append(nama_cus)
    age.append(age_cus)
    print(nama, age)
for sebut_cus in range(len(nama)):
    print("+=================+")
    print("Data customer yang tersimpan:")
    print("Nama Customer: {}".format(nama[sebut_cus]))
    print("Umur Customer: {}".format(age[sebut_cus]))