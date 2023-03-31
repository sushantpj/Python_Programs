

class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None

class DLL:
    def __init__(self):
        self.head=None
    
    def ftraversal(self):
        n=self.head
        if n==None:
            print("Empty DLL...")
        else:
            while n is not None:
                print(n.data)
                n=n.nref
    
    def rtraversal(self):
        n=self.head
        if n==None:
            print("Empty DLL..")
        else:
            while n.nref is not None:
                n=n.nref   
            while n is not None:
                print(n.data)
                n=n.pref

    def add_begin(self,data):
        node=Node(data)
        n=self.head
        if n is None:
            self.head=node    #displaying wrong output when replaced self.head n as
        else:
            node.nref=self.head
            self.head.pref=node
            self.head=node

    def add_end(self,data):
        node=Node(data)
        n=self.head
        if n is None:
            n=node    
        else:
            while n.nref is not None:
                n=n.nref
            node.pref=n
            n.nref=node
    
    def add_before(self,data,x):
        node=Node(data)
        n=self.head
        if self.head is None:
            print("EMpty LL ...invalid operation")
            return
        if x==n.data:
            node.nref=self.head
            self.head.pref=node
            self.head=node
            return
        while n.nref.data!=x:
            n=n.nref
            if n.nref==None:
                print("Element not present...")
                return
        node.pref=n
        node.nref=n.nref
        n.nref.pref=node
        n.nref=node
    
    def add_after(self,data,x):
        node=Node(data)
        n=self.head
        if n.data==x:
            n.nref=node
            node.pref=n
            return
        while n.data is not x:
            n=n.nref
            if n==None:
                print("Element not present...")
                return
        node.pref=n
        node.nref=n.nref
        if n.nref!=None:
            n.nref.pref=node
        n.nref=node
    
    def del_start(self):
        self.head.nref.pref=None
        self.head=self.head.nref
    
    def del_end(self):
        n=self.head
        if n is None:
            print("Deleting from empty dll..")
            return
        while n.nref.nref is not None:
            n=n.nref
        n.nref=None

    def del_given_elem(self,x):
        n=self.head
        if x==n.data:
            self.head.nref.pref=None
            self.head=self.head.nref
            return

        while self.head.nref is not None:
            print("hy")
            if self.head.data==x:
                break
            self.head=self.head.nref
        
        if self.head.nref==None:
            if self.head.data==x:
                self.head.pref.nref==None
            else:
                print("Not present...")
        else:
            self.head.nref.pref==self.head.pref
            self.head.pref.nref==self.head.nref  


dll=DLL()
dll.add_begin(10)
dll.add_begin(20)
dll.add_begin(30)
dll.add_end(5)
dll.add_end(0)
dll.add_end(-5)
dll.add_after(15,-5)

dll.ftraversal()

dll.del_given_elem(-5)
dll.del_given_elem(5)

print("---------")
dll.rtraversal()



