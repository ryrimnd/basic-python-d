'''
try:
    x = str(input("Nama Anda: "))
    print("Halo!", x)
except:
    pass
'''

try:
    x = int(input("Input angka: "))
    print("Angka anda!", x)
except ValueError:
    print("Input yang dimasukan salah")
except KeyboardInterrupt:
    print("Anda belum memasukan input")