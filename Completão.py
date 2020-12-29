import random
import time

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

def analeseInteiro(x=""):
    while True:
        try:
            y = int(input(x))
        except:
            print("\033[31mSó numeros\033[m")
        else:
            return y
            break

def Atributos(x = '',b = 0):
    lin(5)
    print(f'{x}')
    y = analeseInteiro("QD: ")
    z = analeseInteiro("LD: ")
    if y == 0 or z == 0:
        print(f"{x} = Sem valor")
        j = 0
    else:
        b = analeseInteiro("Bônus: ")
        j = dado(y, z, b)
        print(f'{x} = {j}')
    return j
    lin(5)

def lin(x = 25):
    print('-' * x)

def cabeçalho(x=''):
    print(f"------------{x}------------")

jogadores = {}
objetos = ["Algemas", "Corda (15m)", "Formão","Armadilha de urso","Corneta" ,"Fragância de animal", "Bolas de gude", "Corrente (3m)", "Frasco de ácido", "Broca de mão", "Espelho de aço",  "Frasco de veneno", "Cabo de aço", "Espigões de Ferro", "Gancho de escalada", "Cola Estrepe", "Gazuas (3)", "Giz", "Odre", "Saco de dormir", "Graxa", "Pá", "Saco Grande", "Isqueiro", "Pé de cabra", "Serra de Arco", "Lanterna", "Óleo Rações (3)", "Tenaz", "Lima", "Rede de pesca", "Tocha", "Martelo", "Remédio (3)","Vara de 3m"]
fala = ["Anedotas", "Discurso Florido", "Fala rápido","Articulador" ,"Divaga" ,"Fala sozinho","Casual demais", "Dizeres Pitorescos", "Fatos Aleatórios","Chiador", "Fala alto", "Formal","Direto" ,"Fala arrastado", "Gago","Discursar" ,"Fala pausada", "Hipnótico","Interruptor", "Narra Risadas","Lacônico" ,"Oculto", "Robótico","Linguagem de rua", "Pausas longas", "Sussurra","Monótono", "Respiração funda", "Voz Expansiva","Muda de assunto", "Rimador", "Voz grave","Murmúrios", "Rir" ,"Voz Melodiosa"]
aparência = ["Abatido", "Bonito", "Doentio","Altaneiro", "Bruto" ,"Elegante","Animado" ,"Corpulento" ,"Enrugado","Aquilino" ,"Definido" ,"Entroncado","Atlético" ,"Delicado" ,"Envelhecido","Atraente" ,"Deslumbrante" ,"Esbelto","Escultural", "Inquieto" ,"Robusto","Esguio", "Musculoso" ,"Sarado","Esquelético" ,"Peludo" ,"Sensual","Estúpido", "Rechonchudo" ,"Sólido","Grisalho" ,"Repulsivo" ,"Vigoroso","Indeciso" ,"Rígido" ,"Viril"]
detalheFisico = ["Barba grande", "Cabelo enrolado", "Cicatrizes de queimadura","Bigode", "Cabelo oleoso", "Cicatrizes de rituais","Cabeça raspada", "Cabelo trançado", "Costeletas","Cabelo cacheado" ,"Cicatrizes de ácido" ,"Dente de ouro","Cabelo comprido", "Cicatrizes de batalha", "Dente Faltando","Cabelo emaranhado" ,"Cicatrizes de flagelação", "Dreadlocks","Marca de nascença" ,"Pele bronzeada", "Sobrancelhas espessas","Marca pessoal", "Pele escura", "Sotaque exótico","Nariz quebrado", "Pele pálida", "Tatuagens", "Nove dedos", "Piercings", "Topete", "Orelha Faltando" ,"Queimadura de sol", "Um olho","Pele amarelada" ,"Sarda", "Voz rouca"]
origem = ["Agiota", "Caçador de Recompensa", "Contorcionista","Alquimista", "Carrasco", "Contrabandista","Arrombador", "Cavaleiro andante", "Coveiro","Artista de rua", "Chantagista", "Cultista","Batedor de carteiras", "Charlatão", "Cunhador","Caçador de ratos ","Cobrador Desertor","Envenenador", "Limpa-chaminés", "Profeta louco","Escravo", "Lutador de rua", "Receptador","Escravo", "remador", "Mascate", "Salteador da estrada","Escrivão", "Menor abandonado", "Seqüestrador", "Falsificador", "Mercenário", "Tatuador", "Jogador", "Príncipe mendigo", "Vidente"]
vestimenta = []
personalidade = []

print("-" * 25)
print("Alistamento de Personagem")
print("OBS: Caso o personagem tenha uma caracteristica desconhecida, bote -1")
while True:
    jogadores['Nome: '] = (str(input("Nome do Personagem: ")).strip())
    while True:
        try:
            idade = int(input("Idade: "))
            if idade == (-1):
                jogadores['Idade'] = "\033[31mDesconhecida\033[m"
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
    jogadores['Fala '] = random.choice(fala)
    jogadores['Aparência '] = random.choice(aparência)
    jogadores['Detalhe físico '] = random.choice(detalheFisico)
    jogadores["Origem "] = random.choice(origem)
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
        print(f'{k}= \033[31mDesconhecida\033[m')
    else:
        print(f'{k} = {v}')
    time.sleep(0.5)
lin()
time.sleep(120)