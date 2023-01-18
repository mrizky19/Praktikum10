txt = 'Hello World'
print("txt = 'Hello World'")

print("Menghitung Jumlah Karakter menggunakan 'len(txt)'")
print(len(txt))

print("Mengambil Karakter Terakhir menggunakan 'txt[-1]'")
print(txt[-1])

print("Ambil karakter index ke-2 sampai index ke-4 (llo) menggunakan 'txt[2:5]'")
print(txt[2:5])

print("Hilangkan spasi pada text tersebut (HelloWorld) menggunakan 'txt.replace(' ', '')'")
print(txt.replace(" ", ""))

print("Ubah text menjadi huruf besar menggunakan 'txt.upper()'")
print(txt.upper())

print("Ubah text menjadi huruf kecil menggunakan 'txt.lower()'")
print(txt.lower())

print("Ganti karakter H dengan karakter J menggunakan 'txt.replace('H', 'J')'")
print(txt.replace("H", "J"))


print()
print()
print()

umur = 24
txt = 'Hello, nama saya john, dan umur saya adalah {} tahun'

print(txt.format(umur))