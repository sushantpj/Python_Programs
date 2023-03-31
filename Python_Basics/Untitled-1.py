
import collections
import queue
from xml.dom.minidom import Element

"""---STACK---

stack=collections.deque()
stack.append(10)
stack.append(20)
stack.append(30)
stack.popleft()
stack.popleft()
print(stack)"""

"""
STACK=queue.LifoQueue(3)
STACK.put(10)
STACK.put(20)
STACK.put(30)

print(STACK.get())
print(STACK.get())
print(STACK.get())
print(STACK.get(timeout=1)) """


"""---QUEUE---

Q=queue.Queue(3)

Q.put(10)
Q.put(1300)
Q.put(20)
#Q.put(40,timeout=1)

print(Q.get())
print(Q.get())
print(Q.get())"""

"""Q=collections.deque()
Q.appendleft(10)
Q.appendleft(20)
Q.appendleft(30)

print(Q.pop())
print(Q.pop())
print(Q.pop())

Q=collections.deque()
Q.append(10)
Q.append(20)
Q.append(30)

print(Q.popleft())
print(Q.popleft())
print(Q.popleft())"""


"""----PriorityQueue----"""
"""

pq=queue.PriorityQueue(3)
pq.put(50)
pq.put(10)
pq.put(20)

print(pq.get())
print(pq.get())
print(pq.get())

pq=[]
pq.append((1,50))
pq.append((3,800))
pq.append((2,10))

print(pq)
pq.sort()
print(pq.pop())
print(pq.pop())"""

"""----------Linked List--------"""

"""--Singly Linked list--"""

class Node():
    def __init__(self,data):
        self.data=data
        self.ref=None

class LL:
    def __init__(self):
        self.head=None
    
    def traversal(self):
        if self.head==None:
            print("LL is empty..")
        
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    
    def add_elem_start(self,data):
        node=Node(data)
        node.ref=self.head
        self.head=node
    
    def add_elem_end(self,data):    
        n=self.head
        node=Node(data)
        if n==None:
            n=node    
        else:
            while n.ref is not None:
                n=n.ref
            n.ref=node
    
    def add_elem_before(self,data,x):
        n=self.head
        if n is None:
            print("Element not present...")
            return
        if x==n.data:
            node=Node(data)
            node.ref=n
            self.head=node
            return
       
        while n is not None:
            if n.ref==None:
                break
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref==None:
            print("Node not present")
        else:
            node=Node(data)
            node.ref=n.ref
            n.ref=node

    def add_elem_after(self,data,x):
        n=self.head
        if n==None:
            print("Element not present...")
            return
            
        while n is not None:
            if n.data==x:
                break
            n=n.ref
        if n is None:
            print("Element not present...")
        else:
            node=Node(data)
            node.ref=n.ref
            n.ref=node

    def del_elem_first(self):
            self.head=self.head.ref
            
        
    def del_elem_last(self):
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None    
        
    def del_elem_given(self,x):
            n=self.head
            if n.data==x:
                n=None
                return

            while n is not None:
                if n.ref.data==x:
                    break
                n=n.ref
            if n==None:
                print("Node not present...")
            else:
                n.ref=n.ref.ref


        
ll=LL()

ll.add_elem_start(10)

ll.add_elem_start(20)
ll.add_elem_start(30)
ll.add_elem_end(50)
ll.add_elem_end(40)
ll.add_elem_end(60)
ll.add_elem_after(55,50)
ll.add_elem_before(45,50)

ll.del_elem_first()
ll.del_elem_last()
ll.del_elem_given(50)

ll.traversal()


        