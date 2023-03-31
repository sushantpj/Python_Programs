class a:

    a1=10

    def __init__(self):
        print("I am in A")

    def h(self):
        print("I am method of A")

class b(a):

    b1=10
    
    def __init__(self):
        # super().__init__h()
        # super().h()
        # a.__init__(self)
        # a.h(self)
        print("I am in b , Accessing a1 from a ")

ob1=a()
ob2=b()


# class a:

#     a1=10

#     def __init__(self):
#         print("I am outer class")

#     def h(self):
#         print("I am method of outer class")


#     class aa:
#         def __init__(self):
#             print("I am inner class")
        
#         def aaf(self):
#             print("I am method of inner class")

# ob=a()
# ob.aa()