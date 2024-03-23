class MyClass:
    a = 5
    print("Class initialized")

    def sayHello(self):
        print("Hello, world!")
    
myc = MyClass();
print("a: {}".format(myc.a))
print(myc.sayHello())    