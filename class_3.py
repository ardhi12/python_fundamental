# Setiap method harus memiliki parameter SELF
# yang artinya method tersebut dimiliki dan terdaftar ke class tersebut 
# untuk membedakan dari method atau fungsi yang ada di luar class.

# def <nama_method>(parameter), mirip seperti function namun, pada class funtion disebut dengan METHOD/METODE

# https://www.codepolitan.com/membuat-class-di-python-589528b4d558d

class Product:
    __vendor_message = "Ini adalah rahasia"  # dua underscore (__) didepan maksudnya adalah variable private
    name = ""
    price = ""
    size = ""
    unit = ""

    def __init__(self, name):               # parameter yg diinput cukup namenya saja
        print ("Ini adalah constructor")
        self.name = name
        self.unit = "ml"
        self.size = 250

    def get_vendor_message(self):
        print (self.__vendor_message)

    def set_price(self, price):
        self.price = price

p = Product("Ultora Milek")
p.set_price(5500)

print ("%s dengan ukuran %s %s harganya Rp. %d" % (p.name, p.size, p.unit, p.price))
# print p.__vendor_message

p.get_vendor_message()

p1 = Product("Indomilek")
p1.set_price(5000)

print ("%s dengan ukuran %s %s harganya Rp. %d" % (p.name, p.size, p.unit, p.price))

print (p == p)
print (p1 == p1)
print (p == p1)