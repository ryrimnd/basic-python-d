'''
file = open("baca.txt","a")
ta = "Selamat siang, "
tb = "salam sejahtera"
file.write(ta)
file.write(tb)
file.close()
'''
'''
file = open("baca.txt","w")
ta = "Selamat siang, "
tb = "salam sejahtera"
file.write(ta)
file.write(tb)
file.close()
'''
'''
file = open("baca.txt", "r")
print(file.read())
#print(file.read(7))
file.close()
'''
'''
file = open("baca.txt", "r")
print(file.readlines())
#print(file.readline(7))
file.close()
'''
'''
file = open("baca.txt", "r")
for i in file:
    print(i)
'''

kata = []
listbaru = []
file = open("baca.txt", "r")
for nama in file:
    kata.append(nama)

for nama in kata:
    listkatahapus = nama.replace("\n","")
    listbaru.append(listkatahapus)
print(listbaru)

