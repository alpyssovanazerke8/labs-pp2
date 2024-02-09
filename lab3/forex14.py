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