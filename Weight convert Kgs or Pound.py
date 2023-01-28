we = int(input("Weight: "))
b = input("(K)g or (L)bs: ")
if b.upper() == "K":
    c = we / 0.45
    print("Weight in Pound: " + str(c))
else :
    c = we * 0.45
    print("Weight in Kgs: " + str(c))