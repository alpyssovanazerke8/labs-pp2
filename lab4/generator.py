#ex 1
def square(n):
    for i in range(n+1):
        yield i*i

n = int(input())
x = square(n)
print(*list(x))

#ex 2
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
b = even_numbers(n)
print(','.join(map(str, list(b))))

#ex 3
def threeandfour(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
m = threeandfour(n)
print(*list(m))

#ex 4
def squares(a, b):
    for i in range(a, b + 1):
        yield i*i


a = int(input())
b = int(input()) 
c = squares(a, b)
for value in c:
    print(value)

#ex 5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
s = countdown(n)
print(*list(s))

