from datetime import datetime, timedelta

#ex 1
n = datetime.now()
m = n - timedelta(days=5)

print("Current Date:", n)
print("Five Days Ago:", m)

#ex 2
t = datetime.now()
y = t - timedelta(days=1)
tm = t + timedelta(days=1)

print("Yesterday:", y)
print("Today:", t)
print("Tomorrow:", tm)

#ex 3
a = datetime.now()
b = a.replace(microsecond=0)

print("Datetime without Microseconds:", b)

#ex 4
d1 = datetime(2024, 2, 10, 12, 0, 0)
d2 = datetime(2024, 2, 15, 18, 30, 0)

c = (d2 - d1).total_seconds()

print(f"Difference between {d1} and {d2} in seconds: {c} seconds")
