dict={}
while True:
    key=input("key:")
    if key == "exit":
        break
    val=int(input("10:"))
    dict[key]=val
print(dict)
x=input("value")
if x in dict:
    print(f"{x} in dict")
else:
    print(f"{x} is not in dict")
y=input("20:")
z=int(input("30:"))
if y in dict:
    dict[y]=z
    print(dict)
else:
    print(f"{y} is not in the dict")
y=input("Input key in element for deletion")
if y in dict:
    del dict[y]
    print(dict)
else:
    print(f"Index{y} is not in the dict")
print("keys in the dict are")
keys=dict.keys()
print(keys)
print("Values in the dict are")
vals=dict.values()
print(vals)
print("Sorted dict")
lst=list(dict.keys())
lst.sort()
for key in lst:
    print(key,"",dict[key])
    