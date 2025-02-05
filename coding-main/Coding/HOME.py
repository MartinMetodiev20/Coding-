list=[]
for i in range(0,5):
    x=int(input("enter x:"))
    list=list +[x, ]
print(list)
y=int(input("Enter a number to delete:"))
if y in list:
    list.remove(y)
print(list)




        