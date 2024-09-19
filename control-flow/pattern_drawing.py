while True:
    try:
        size = int(input("Enter the size of the pattern: "))
        if size > 0:
            break
    except ValueError:
        continue
    
for i in range(size):
    for j in range(size):
        print("*", end="")
    print() 







