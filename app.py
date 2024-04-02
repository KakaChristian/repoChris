print("## PROGRAM PYTHON MENGHITUNG LUAS SEGITIGA ##")
print("=============================================")
print()

def hitungpLuasSegitiga(a, t):
    return round(0.5 * a * t, 2)

alas = float(input("Inpus Alas Segitiga : "))
tinggi = float(input("Inpus Tinggi Segitiga : "))
print('Luas Segitiga =', hitungpLuasSegitiga(alas, tinggi))
print()

print("## PROGRAM PYTHON MENGHITUNG LUAS SEGITIGA ##")
print("=============================================")
print()

def hitungPersegiPanjang(p, l):
    return round(p * l,2)

panjang = float(input("Input Panjang : "))
Lebar = float(input("Input Lebar : "))
print("Luas Persegi Panjang = ", hitungpLuasSegitiga(panjang, Lebar))
