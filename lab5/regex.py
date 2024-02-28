import re

file = open("row.txt", "r", encoding= "utf-8")
print(file.readlines())

#ex1
s = re.compile(r'ab*')
text = input()

matches = s.findall(text)
print(matches)

#ex2
n = input()
s = re.compile(r'a(bbb?)')

m = s.findall(n)
print(m)

#ex3
s = input()
x = re.findall("[a-z]+_", s)
print(x)

#ex4
s = input()
m = re.findall("[a-z]+[A-Z]", s)
print(m)

#ex5
s = input()
n = re.compile(r'a.*b$')

m = n.findall(s)
print(m)

#ex6
s = input()
m = re.sub("\s|[,]|[.]", ":", s)
print(m)

#ex7
s = input()

c = ''.join(word.capitalize() for word in s.split('_'))
print(c)


#ex8
s = input()
m = re.findall("[A-Z][^A-Z]*", s)
print(m)

#ex9
s = input()
m = re.sub("([A-Z])", r" \1", s)
print(m)

#ex10
s = input()
m = re.sub("([a-z])([A-Z])", r"\1_\2", s)
print(m.lower())









