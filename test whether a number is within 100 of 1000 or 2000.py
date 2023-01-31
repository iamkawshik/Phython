def near(n):
    return ((abs(1000-n) <= 100) or (abs(2000-n) <=100))
print(near(1000))