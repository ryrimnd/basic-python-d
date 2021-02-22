'''
a = ["Fadzar", "Rudy"]
a[0] = "John Doe"
print(a)

b = ("Faris", "Haris")
print(b)
'''

dictio = {
    "Name" : "Manda",
    "Age" : 18,
    "Gender" : "Male"
}
'''
print(dictio)
print(dictio["Name"])
print(dictio["Age"])
print(dictio["Gender"])

dictio["Nama"] = "Akbar"
print(dictio["Nama"])
'''
for i in dictio:
    print(i)
    print(dictio[i])
print("+==============+")
for i in dictio:
    print(i, dictio[i])
print()
for i, b in dictio.items():
    print(i, b)