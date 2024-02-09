#ex 1
def gtoo(grams):
    ounces = 28.3495231 * grams
    return (ounces)

grams = float(input())
print(gtoo(grams))

#ex 2
def t(num):
    c = (5/9) * (num - 32)
    return (c)

num = int(input())
print(t(num))

#ex 3
def solve(h, l):
    rabbits = (l-2*h)/2
    chickens = h - rabbits

    return f"rabbits: {int(rabbits)}, chickens: {int(chickens)}"
   
h = 35
l = 94
s = solve(h, l)
print(s)

#ex 4
from array import array
def filter_prime(a):
    b=[]
    for i in a:
        s=0
        for i in range(1, i+1):
            if i%j == 0:
                s+=1
            if s==2:
                b.append(i)
        for i in b:
            print(i)

a = array('i')
a = list(map(int, input().split()))
filter_prime(a)

#ex 5
from itertools import permutations

def permutation(s):
    all_permutations = permutations(s)

    for i in all_permutations:
        print(''.join(i))

s = str(input())

permutation(s)


#ex 6
def rev(s):
    return s[::-1]

s = input()
print(rev(s))

#ex 7
def has_33(n):
    for i in range(len(n) - 1):
        if n[i] == 3 and n[i + 1] == 3:
            return True
    return False

a = input()
n = [int(x) for x in a.split()]

result = has_33(n)
print(result)

#ex 8
def spy_game(n):
    count = 0
    for i in n:
        if i == 0 and count < 2:
            count += 1
        elif n == 7 and count == 2:
            return True
    return False

a = input()
n = [int(x) for x in a.split()]

result = spy_game(n)
print(result)


#ex 9
def v(r):
    V = float((4/3)*3.14*r*r*r)
    return(V)
    
r = int(input())
print (v(r))

#ex 10
def unique_elements(n):
    m = []
    for i in n:
        if i not in m:
            m.append(i)
    return m

a = input()
n = [int(x) for x in a.split()]

result = unique_elements(n)
print(result)


#ex 11
def palindrome(s):
    m = s[::-1]
    if m == s:
        print("Yes")
    else:
        print("No")

s = str(input())
r = palindrome(s)

#ex 12
def histogram(a, b, c):
    for i in range(1, a + 1):
        print("*", end=' ')
    print()

    for i in range(1, b + 1):
        print("*", end=' ')
    print()

    for i in range(1, c + 1):
        print("*", end=' ')

a = int(input())
b = int(input())
c = int(input())
histogram(a, b, c)

#ex 13
import random 

def guess_the_number(name):
    n = random.randint(1,20)
    attempts = 0
    while True:
        m = int(input())
        attempts += 1
        if m == n:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break
        elif m<n:
            print("Your guess is too low. Take a guess")
        elif m>n:
            print("Your guess is too big. Take a guess")



name = (input("Hello! What is your name? "))
print("Well,", name, ", I am thinking of a number between 1 and 20. Take guess")

n = guess_the_number(name)

#ex 14

from forex14 import gtoo 