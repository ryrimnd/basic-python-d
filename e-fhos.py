import os
while True:
    print("1. Create file")
    print("2. Remove file")
    int_user = int(input("Pilih Menu: "))
    if int_user == 1:
        file = open("baca.txt", "a")
        file.write("Ini adalah isinya\n")
        file.close()
    elif int_user == 2:
        os.remove("baca.txt")
    else:
        pass