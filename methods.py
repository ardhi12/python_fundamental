class MyClass:
    x = 0.0 
    y = 0.0

    def set_vector(self, x, y):
        self.x = x              # variable self.x tertuju pada variable x yang ada didalam class, sedangan value x itu adalah nilai yg didapat dr parameter
        self.y = y

def MyVector():
    MyVec = MyClass()
    MyVec.set_vector(5.3,3.8)

    print('X : '+ str(MyVec.x) + ', Y : '+ str(MyVec.y))

if __name__ == "__main__":
    MyVector()
