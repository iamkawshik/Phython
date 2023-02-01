def s(t, n):
    for v in t:
        if n == v:
            return True      
    return False
t = input("Enter your Group Data: ")
n = input("Enter your Find Data: ")
print(str(s(t,n)))
