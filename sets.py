# Sets bentuknya adalah kurung kurawal {}
# Sets tidak boleh ada nilai yang duplikat, jika ada maka akan menghapus salah satunya
# Sets tidak memiliki urutan, sehingga tidak bisa dipanggil secara spesifik
# ketika dipanggil dia akan menampilkan valuenya secara random

x = {'ardhi', 'yudhi', 'ardhi', 'wahyu'}
x.add('pipo')
x.remove('yudhi')

print(x)
print()

# teori matematika seperti irisan, gabungan, dll #
y = {1,2,3,4,5}
z = {4,5,6,7,8}
print(y.union(z))                   # gabungan
print(y.intersection(z))            # irisan (yang sama)
print(y.difference(z))              # perbedaan dari y
print(z.difference(y))              # perbedaan dari z
print(y.symmetric_difference(z))    # perbedaan tidak termasuk angka yang sama 