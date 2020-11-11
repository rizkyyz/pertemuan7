#Muhammad Rizky Abdillah
#variable
baris = 10
kolom = baris

#hasil inputan dari variable

for bar in range(baris):
    for col in range(kolom):
        tab = bar+col
        print("{0:>5}".format(tab), end='')
    print()
