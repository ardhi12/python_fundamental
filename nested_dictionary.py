# membuat dictionary dalam dictionary (bercabang)
x = {'data1' : {'nama' : 'ardhi','umur' : '12','WNI' : 'True'},
     'data2' : {'nama' : 'yudhi','umur' : '37','WNI' : 'False'}
    }

for key, value in x.items():
    print("\nKeynya : ", key)
    for data in value:
        print(data + " - " + value[data])

print()
print(x['data2'])
print(x['data2']['nama'])