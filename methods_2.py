# agar lebih efektif daripada methods.py maka gunakan spesial method

class MyClass:

    def __init__(self, x, y):   # __init__ adalah inisialisasi
        self.x = x              # variable self.x tertuju pada variable x yang ada didalam class, sedangan value x itu adalah nilai yg didapat dr parameter
        self.y = y

def MyVector():
    MyVec = MyClass(3.1,4.7)    
    HerVec = MyClass(8.5,9.4)    
    print('X : '+ str(MyVec.x) + ', Y : '+ str(MyVec.y))
    print('X : '+ str(HerVec.x) + ', Y : '+ str(HerVec.y))

if __name__ == "__main__":
    MyVector()
