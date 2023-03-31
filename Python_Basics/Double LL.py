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
        if self.head is None:
            print("..")
            self.head=node
        else:
            node.nref=self.head
            self.head.pref=node
            self.head=node

dll=DLL()
dll.add_begin(10)

dll.add_begin(20)
dll.ftraversal()
dll.rtraversal()


