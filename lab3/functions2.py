movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#ex 1
def imdb(i):
    if i > 5.5:
        return True
    
for i in movies:
    print(imdb(i["imdb"])) 
   
#ex 2
def above_55(i):
    if i["imdb"] > 5.5:
        return i

for i in movies:
    print(above_55(i))

#ex 3
def categoryOfFilm(s):
    m = []
    for i in movies:
        if i["category"] == s:
            m.append(i["name"])
    return m

s = input()
print(*categoryOfFilm(s))

#ex 4
def average1(d):
    s = 0
    for i in movies:
        s += i["imdb"]
    return s/len(movies)


n = average1(movies)
print(n)

#ex 5 
def average2(a):
    b = 0
    c = 0
    for i in movies:
        if a == i["category"]:
            b += i["imdb"]
            c += 1
    return b/c

a = input()
print(average2(a))