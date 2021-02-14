teori = input("Nilai ujian teori: ")
praktek = input("Nilai ujian praktek: ")
nteori = float(teori)
npraktek = float(praktek)

if nteori >= 70 and npraktek >= 70:
    print("Selamat, anda lulus!")
elif nteori <= 70 and npraktek >= 70:
    print("Anda harus mengulang ujian teori")
elif npraktek <= 70 and nteori >= 70:
    print("Anda harus mengulang ujian praktek")
else:
    print("Anda harus mengulang ujian teori dan praktek")



