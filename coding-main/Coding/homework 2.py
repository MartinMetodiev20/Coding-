list=[]
for i in range(5):
    x=int(input("Enter x: "))
    list = list + [x, ]
print(list)
y=int(input("enter a number to delete: "))
if y in list:
    list.remove(y)
print(list)

