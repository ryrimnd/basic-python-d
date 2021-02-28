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

alamatemailnya = []
listalamatemail = []
file = open("receiver_list.txt", "r")
for i in file:
    alamatemailnya.append(i)
print(alamatemailnya)
for x in alamatemailnya:
    listkatahapus = x.replace("\n","")
    listalamatemail.append(listkatahapus)
print(listalamatemail)

