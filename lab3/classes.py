#ex 1
class Stringw:
    def __init__(self):
        self.sentence = ""

    def getString(self):
        self.sentence = input()

    def printString(self):
        print(self.sentence.upper())

a = Stringw()
a.getString()
a.printString()


#ex 2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        self.l = l

    def area(self):
        return self.l ** 2

m = Shape()
n = int(input())
c = Square(n)
print(c.area())

#ex 3
class Rectangle(Shape):
    def __init__(self, len, width):
        self.len = len
        self.width = width

    def area(self):
        return self.len * self.width

a = int(input())
b = int(input())
c = Rectangle(a, b)
print(c.area())

#ex 4
class point():
    def init(self, x, y):
        self.x = x
        self.y = y   
    def show(self):
        print(f'({self.x}, {self.y})')
    def move(self, nx, ny):
        self.x = nx
        self.y = ny
    def dist(self, m):
        distance =((self.x - m.x)^2 + (self.y - m.y)^2)**0.5
        return distance 

p1 = point(3, 4)
p2 = point(8, 9)
p1.show()
p1.move(4, 15)
print(p1.dist(p2))

#ex 5
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. Balance: {self.balance}")
            else:
                print("Withdrawal not allowed.")

o = input()
b = int(input()) 
account = BankAccount(o, b)

d = int(input()) 
w = int(input())
account.deposit(d)
account.withdraw(w)

#ex 6
primeNum = lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1

a = input()
n = [int(x) for x in a.split()]

prime_numbers = list(filter(primeNum, n))
print(*prime_numbers)




