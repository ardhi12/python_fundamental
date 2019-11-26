# silahkan input hingga 10 angka, maka akan terlihat totalnya
sum = 0

for i in range(1, 11):  # 1 adalah nilai awal (mulai) , 11 adalah nilai akhir (akhir), jadi perulangannya sampai 10 kali.
    N = int(input())
    sum = sum + N

print("totalnya adalah : " + str(sum))