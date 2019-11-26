N = int(input("Masukan jumlah anak ayam = "))

print("Anak ayam turunlah " + str(N))
if N > 1:
    for i in range(N - 1, 0, -1):
        print("Mati satu tinggallah " + str(i))

# terminate
print("Mati satu tinggal induknya")
