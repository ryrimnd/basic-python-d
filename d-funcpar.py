def fungsisaya(name):
    print(f"Halo {name}")
fungsisaya("kamu")
print()
def fungsisaya1(name, age, gender):
    print(f"Halo {name}, kamu merupakan {gender} berumur {age} tahun")
fungsisaya1("Manda", 19, "Laki-laki")
#fungsisaya1(name="Manda", age=19, gender="Laki-laki")
print()
def fungsisaya2(name="NO INPUT", age="NO INPUT", gender="NO INPUT"):
    print(f"Halo {name}, kamu merupakan {gender} berumur {age} tahun")
fungsisaya2()
fungsisaya2("Manda", 19, "Laki-laki")