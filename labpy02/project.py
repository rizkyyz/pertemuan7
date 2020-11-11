#muhammad rizky abdillah
print("PROGRAM BILANGAN TERBESAR DARI 3 BUAH BILANGAN YANG DIINPUTKAN")

A= int(input("Masukan bilangan pertama : "))
B= int(input("Masukan bilangan kedua   : "))
C= int(input("Masukan bilangan ketiga  : "))
if A > B and A > C:
 print(A, "Terbesar dari 3 bilangan yang diinputkan")
elif B > A and B > C:
    print(B, "Terbesar dari 3 bilangan yang diinputkan")
else:
   print(C, "Terbesar dari 3 bilangan yang diinputkan")