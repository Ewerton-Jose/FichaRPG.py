import random
import time

def dado(x= 1, y = 6):
    l = []
    for c in range(0,x):
        y = random.randint(1,y)
        l.append(y)
    return l

def Atributos(x = ''):
    lin(5)
    print(f'{x}')
    y = int(input("QD: "))
    z = int(input("LD: "))
    if y == 0 or z == 0:
        print(f"{x} = Sem valor")
        j = 0
    else:
        j = dado(y, z)
        print(f'{x} = {j}')
    return j
    lin(5)

def lin(x = 25):
    print('-' * x)

jogadores = {}

print("-" * 25)
print("Alistamento de Personagem")
while True:
    jogadores['Nome: '] = (str(input("Nome do Personagem: ")))
    jogadores['Idade: '] = (int(input("Idade: ")))
    jogadores['Raça: '] = (str(input("Raça: ")))
    jogadores['Espécie: '] = (str(input("Espécie: ")))
    jogadores['Classe: '] = (str(input("classe: ")))
    jogadores['Gênero: '] = (str(input("Gênero: ")))
    print("Agora vamos para os atributos do seu personagem")
    print('OBS: LD siginifica os "Lados do Dado"\nE "QD" significa "Quantos Dados"')
    jogadores['Vida: '] = (Atributos("Vida"))
    jogadores['Atack: '] = Atributos("Atack")
    jogadores['Defesa: '] = (Atributos("Defesa"))
    jogadores['Carisma: '] = Atributos("carisma")
    jogadores['Bônus de atack: '] = (Atributos("bõnus de atack"))
    break
for k, v in jogadores.items():
        print(f'{k} = {v}')