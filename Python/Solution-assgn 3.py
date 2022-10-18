# OOps
#1
from logging import raiseExceptions
from smtplib import SMTPServerDisconnected


class Vehicle:
    color = 'White'
    def __init__(self,name,mileage,speed):
        self.name = name
        self.speed = speed
        self.mileage = mileage

    def __str__(self) -> str:
        return f"Color: {self.color}, Vehicle name: {self.name}, Speed: {self.speed}, Mileage: {self.mileage}"


obj = Vehicle('School Volvo',12,180)
# print(obj)

# 2

# function name and property name and varible name should match and use protected as well.
class Class:
    def __init__(self):
        self.name = ""

    #getter func
    @property
    def name(self):
        return self._name
    
    #setter
    @name.setter
    def name(self,a):
        if (a == ''):
            raise ValueError('Please enter the valid name.')
        self._name = a

# obj = Class()
# obj.name = ''
# 3
class A:
    def __init__(self,a) -> None:
        print("I am in constructor of Class A.")
        self.a = a

    def func(self):
        print("I am in func of Class A.")
        return self.a

class B(A):
    def __init__(self,a,b) -> None:
        print("I am in Constructor of Class B.")
        super().__init__(a)
        self.b = b

    def func(self):
        print("I am in func of Class B.")
        super().func()
        return self.b

# obj = B(3,4)
# print(obj.func())

#4
class Demo:
    def __init__(self,a) -> None:
        self.a = a
        print("I am in constructor")

    def __del__(self):
        print("I am in destructor")

# print("Program Start")
# obj = Demo(4)
# print(obj.a)
# print("Program End")


# 5
class Modified:
    def __init__(self,func) -> None:
        self.func = func
    
    def __call__(self, *args, **kwds):
        print("before func")
        self.func(*args, **kwds)
        print("After func")

@Modified
def reverse(ls):
    print("processing started....")
    print("Reverse: ",ls[::-1])
    print("processing ended....")

# reverse([1,2,3])


#6
class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()


#7
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

#8
class Node(object):
	def __init__(self, d):
		self.next_node = None
		self.data = d

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0
	# Add d to tail of list
	def add(self, d):
		new_node = Node(d)
		if self.tail:
			self.tail.next_node = new_node
			self.tail = new_node
		else:
			self.head = new_node
			self.tail = new_node
		self.size += 1
	# Add d at location index in list
	def add_at(self, d, index):
		new_node = Node(d)
		previous_node = None
		current_node = self.head
		i = 0
		while i < index and current_node.next_node:
			previous_node = current_node
			current_node = current_node.next_node
			i += 1
		if i == index:
			previous_node.next_node = new_node
			new_node.next_node = current_node
			return True
		else:
			# List not long enough
			return False
	# Remove d; return True if successful, false otherwise
	def remove(self, d):
		previous_node = None
		current_node = self.head
		while current_node:
			if current_node.data == d:
				if previous_node:
					previous_node.next_node = current_node.next_node
				else:
					self.head = current_node.next_node
				self.size -= 1
				return True
			previous_node = current_node
			current_node = current_node.next_node
		return False
	# Return True if d is in list, false otherwise
	def find(self, d):
		current_node = self.head
		while current_node:
			if current_node.data == d:
				return True
			current_node = current_node.next_node
		return False

#9

# Object defining represent memory allocation necessary for storing the actual data of variables defined in class. 
# Each time when you create an object of class the copy of each data variables defined in that class is created.
# In simple language we can state that each object of a class has its own copy of data members defined in that class. 

# Working

# 1. A block of memory is allocated on the heap. The size of memory allocated is decided by the attributes and methods available in that class.
# 2. After the memory block is allocated, the special method __init__() is called internally. Initial data is stored into the variables through this method.
# 3. The location of the allocated memory address of the instance is returned to the object.
# 4. The memory location is passed to self. self store the memory location of object.

#10
class Product:
    def __init__(self):
        print("Instance Created")
  
    def __call__(self, a, b):
        print(a * b)
  
# Instance created
# ans = Product()
  
# ans(10, 20)

#Exception

#1
class CustomError(Exception):
    pass

def dividebyzero(n,div):
    if div == 0:
        raise CustomError("Divide by Zero Error.")

    return n/div

def dividebyzero(n,div):
    try:
        return n/div
    except Exception as e:
        print(e)

# print(dividebyzero(3,6))

# 2
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")



