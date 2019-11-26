class MyNames:
    names = []
    ages = []

    def add(self, name, age):
        self.names.append(name)
        self.ages.append(age)

def MyFunc():
    friend = MyNames()  # panggil class

    friend.add('ardhi',12)
    friend.add('wahyu',13)
    friend.add('yudhi',14)    

    print('Names : '+ str(friend.names) )
    print('Ages : '+ str(friend.ages) )

if __name__ == "__main__":
    MyFunc()


