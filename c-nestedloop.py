'''
for i in range(5):
    for b in range(i):
        print("I ---", i, "B ---", b, " ")
    print()
print("---")
for i in range(5):
    for b in range(i):
        print(b, end=" ")
    print()
'''

name = ["Rayhan", "Rizky", "Akbar"]
cars = ["Mercedes", "Porsche", "Hyundai"]
quantity = [1,2,3]
for ite_name in name:
    for ite_cars in cars:
        for ite_quantity in quantity:
            print(f"{ite_name} mempunyai {ite_quantity} buah mobil {ite_cars}")