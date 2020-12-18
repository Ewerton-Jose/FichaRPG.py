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

def mostraTudo(l = [], n = 0):
    lin(25)
    print("CARACTERISTICAS:")
    print(f"Nome = {l[n][0][0]}")
    print(f"Idade = {l[n][0][1]}")
    print(f"Raça = {l[n][0][2]}")
    print(f"Espécie = {l[n][0][3]}")
    print(f"classe = {l[n][0][4]}")
    print(f"Gênero = {l[n][0][5]}")
    lin(5)
    print(f'ATRIBUTOS:')
    print(f"Vida = {l[n][1][0]}")
    print(f"Atack = {l[n][1][1]}")
    print(f"Defesa = {l[n][1][2]}")
    print(f"Carisma = {l[n][1][3]}")
    print(f"Bõnus de atak = {l[n][1][4]}")

jogadores = []
jogador = []
dados = []
atributos = []
objetos = []

print("-" * 25)
print("Alistamento de Personagem")
while True:
    dados.append(str(input("Nome do Personagem: ")))
    dados.append(int(input("Idade: ")))
    dados.append(str(input("Raça: ")))
    dados.append(str(input("Espécie: ")))
    dados.append(str(input("classe: ")))
    dados.append(str(input("Gênero: ")))
    jogador.append(dados[:])
    dados.clear
    print("Agora vamos para os atributos do seu personagem")
    print('OBS: LD siginifica os "Lados do Dado"\nE "QD" significa "Quantos Dados"')
    atributos.append(Atributos("Vida"))
    atributos.append(Atributos("Atack"))
    atributos.append(Atributos("Defesa"))
    atributos.append(Atributos("carisma"))
    atributos.append(Atributos("bõnus de atack"))
    jogador.append(atributos[:])
    atributos.clear()
    jogadores.append(jogador[:])
    jogador.clear
    break
mostraTudo(jogadores)