tpl = ()
for i in range(0, 5):
    x = int(input("x= "))
    tpl = tpl+(x,)
print(tpl)
tpl1 = tpl*2
print(f"Скала: {tpl1}")
key = int(input("Търсено в скалата"))
if key in tpl:
    print(f"{key} е в скалата")
else:
    print(f'{key} НЕ е в скалата')
for i in range(0, len(tpl)):
    print(tpl[i])
min_el = min(tpl)
print(f"min = {min_el}")
