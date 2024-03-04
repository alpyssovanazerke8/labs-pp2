#ex 1
n = [1, 3, 5, 8, 10]
x = "*".join(str(i) for i in n)
print(eval(x))

#ex 2
s = input()
up = 0
low = 0
for i in s:
    if i.isupper():
        up += 1
    elif i.islower():
        low += 1
print("Uppercase letters: ", up)
print("Lowercase letters: ", low)

#ex 3
s = input()
if s == s[::-1]:
    print("Palindrome")
else:
    print("It is not palindrome")

#ex 4
import time

n = int(input())
milsec = int(input())
sec = milsec / 1000
time.sleep(sec)
sqrt = n**0.5
s = "Square root of {fnum} after {fsec} is {fsqrt}".format(
    fnum=n, fsec=milsec, fsqrt=sqrt
)
print(s)

#ex 5
m = (True, True, False)
n = (True, True, True)
print(all(m))
print(all(n))