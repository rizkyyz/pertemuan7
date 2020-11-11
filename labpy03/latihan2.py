#Muhammd Rizky Abdillah
#no ambil source code
print("---Latihan 2----")
print("menampilkan bilangan berhenti ketika bilangan 0 dan menampilkan bilangan terbesar")

max=0
while True:
    a=int(input("masukan bilangan : "))
    if max < a :
        max = a
    if a==0:
        break
print("bilangan terbesar adalah = ",max)
