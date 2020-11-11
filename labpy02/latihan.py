#muhammad Rizky abdillah

# Program cari bilangan terbesar

a, b, c = input()
if a > b:
  if b > c:
    maks = a
  else:
  if c > a:
    maks = c
  elif a > c:
    maks = b
  elif c > b:
    maks = c

print maks