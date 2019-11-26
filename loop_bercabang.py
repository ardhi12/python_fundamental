# -- While -- #
# a = 1

# while a < 5 :
#     b = 0
#     while b < a :
#         print('*', end='')  # ditambahkan end='' agar nilai yg dikeluarkan menjadi sebaris / berurutan
#         b = b + 1
#     print()         # untuk print baris kosong (enter)
#     a = a + 1



# -- For -- #

# membuat tabel perkalian
for a in range(1,5):  
    for b in range(1,5):
        c = a * b
        print(c, end='  ')
    print()