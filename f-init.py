class contoh:
    def __init__(self, name, age):
        self.nama = name
        self.umur = age
    def salam(self):
        print("Halo! Nama saya ", self.nama)
    def bye(self):
        print("Bye!", self.nama)
orang = contoh("Manda", 19)
print(orang.nama)
print(orang.umur)
orang.salam()
orang.bye()
print()
orang1 = contoh("Rizky", 18)
print(orang1.nama)
print(orang1.umur)
orang1.salam()
orang1.bye()