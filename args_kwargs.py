# args adalah argument yang lebih dari 1. simbolnya adalah * 

def printData(*args):
    for name in args:
        print(name)

printData('ardhi', 'wahyu', 'yudhi')


# kwargs adalah keyword argument yang lebih dari 1. simbol **

def printData2(**kwargs):
    for key, value in kwargs.items():
        print(key + ' -> ' + value)
        

printData2(nama='ardhi', umur='12, jenkel='L')