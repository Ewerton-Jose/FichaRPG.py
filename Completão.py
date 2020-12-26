import random
import time

def dado(x= 1, y = 6):
    l = []
    for c in range(0,x):
        y = random.randint(1,y)
        l.append(y)
    return l

def Atributos(x = '',b = 0):
    lin(5)
    print(f'{x}')
    y = int(input("QD: "))
    z = int(input("LD: "))
    b = int(input("Bônus: "))
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

def cabeçalho(x=''):
    print(f"------------{x}------------")

jogadores = {}
objetos = ["Algemas", "Corda (15m)", "Formão","Armadilha de urso","Corneta" ,"Fragância de animal", "Bolas de gude", "Corrente (3m)", "Frasco de ácido", "Broca de mão", "Espelho de aço",  "Frasco de veneno", "Cabo de aço", "Espigões de Ferro", "Gancho de escalada", "Cola Estrepe", "Gazuas (3)", "Giz", "Odre", "Saco de dormir", "Graxa", "Pá", "Saco Grande", "Isqueiro", "Pé de cabra", "Serra de Arco", "Lanterna", "Óleo Rações (3)", "Tenaz", "Lima", "Rede de pesca", "Tocha", "Martelo", "Remédio (3)","Vara de 3m"]

print("-" * 25)
print("Alistamento de Personagem")
print("OBS: Caso o personagem tenha uma caracteristica desconhecida, bote -1")
while True:
    jogadores['Nome: '] = (str(input("Nome do Personagem: ")).strip())
    while True:
        try:
            idade = int(input("Idade: "))
            if idade == (-1):
                jogadores['Idade'] = "Desconhecida"
            else:
                jogadores['Idade: '] = idade
        except:
            print('\033[31mCaso o personagem tenha idade desconhecida bote -1\033[m')
        else:
            break

    jogadores['Raça '] = (str(input("Raça: "))).strip().capitalize()
    jogadores['Espécie '] = (str(input("Espécie: "))).strip().capitalize()
    jogadores['Classe '] = (str(input("Classe: "))).strip().capitalize()
    jogadores['Gênero '] = (str(input("Gênero: "))).strip().capitalize()
    print("Agora vamos para os atributos do seu personagem")
    print('OBS: LD siginifica os "Lados do Dado"\nE "QD" significa "Quantos Dados"')
    jogadores['Vida '] = (Atributos("Vida"))
    jogadores['Atack '] = Atributos("Atack")
    jogadores['Defesa '] = (Atributos("Defesa"))
    jogadores['Carisma '] = Atributos("Carisma")
    jogadores['Bônus de atack '] = (Atributos("Bônus de atack"))
    break
print('Carregando...')
time.sleep(2)
cabeçalho("Ficha")
for k, v in jogadores.items():
    if v == "-1" or v == '':
        print(f'{k} = Desconhecida')
    else:
        print(f'{k} = {v}')
    time.sleep(0.5)
lin()