i = 0 
myList = []
while True:
    i+=1
    x = input(F"x{i}=")
    if x == "exit":
        break 
    else:
        try:
            myList.append(int(x))
        except ValueError:
            print("one argument is not correct")
print(myList)

