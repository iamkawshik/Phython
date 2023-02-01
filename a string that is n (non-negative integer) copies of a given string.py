def s(t, n):
    result= " "
    for i in range (n):
        result = result + t    
    return result
t = input()
n = int(input())
print(str(s(t, n)))