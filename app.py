print("## PROGRAM PYTHON MENGHITUNG LUAS SEGITIGA ##")
print("=============================================")
print()

def hitungpLuasSegitiga(a, t):
    return round(0.5 * a * t, 2)

alas = float(input("Inpus Alas Segitiga : "))
tinggi = float(input("Inpus Tinggi Segitiga : "))
print('Luas Segitiga =', hitungpLuasSegitiga(alas, tinggi))
print()
