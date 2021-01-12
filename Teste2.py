import random

def dado(x= 1, y = 6, z = 0):
    l = []
    cont = z
    for c in range(0,x):
        y = random.randint(1,y)
        cont += y
        l.append(y)
    if z != 0:
        bônus = [f'somando com o bônus(+{z}) = {cont}']
    else:
        bônus = [f"soma = {cont}"]
    l.append(bônus)
    return l

x = dado(2,6)
print(f"--------------------------------{x}")