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
            print("\033[31mSó numeros inteiros\033[m")
        else:
            return y
            break

def armadura():
    x = analeseInteiro("Armadura: ")
    y = analeseInteiro("Bônus da armadura: ")
    if y > 0:
        l = f'{x} + {y} = {x + y}'
    else:
        l = f'{x}'
    return l

def analeseAtributo(x = ""):
    while True:
        try:
            y = analeseInteiro(x)
            while y > 2 or y < 0:
                y = analeseInteiro("\033[31mSó 2, 1 ou 0: \033[m")
        except:
            print("Deu algum erro")
        else:
            return y
            break

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
vestimenta = ["Alta costura", "Cerimonial", "Desgastada","Amassada", "Chamuscada", "Elegante","Anacrônica Com laços", "Encardida","Antiga", "Curta", "Esfarrapada","Bordada", "Decadente", "Excêntrica","Brega", "Deselegante", "Exótica","Extravagante", "Manchada de comida", "Perfumada","Farda", "Manchada de lama", "Prática","Fora de catálogo", "Manchada de sangue", "Rasgada de batalha","Formal", "Manchada de vinho", "Remendada","Larga", "Ornamentada", "Requintada","Luxuosa", "Padrão", "Vulgar"]
personalidade = ["Alegre", "Cabeça quente", "Esperto","Amargo", "Cauteloso", "Estoico","Ameaçador", "Contrariador","Honrado","Arrogante", "Covarde", "Inquisitivo","Astuto" ,"Dominador", "Irascível","Bravo", "Espaçoso", "Justo","Leal", "Preguiçoso", "Sem coração","Mal humorado", "Protetor", "Sereno","Nervoso", "Rude", "Sociável","Orgulhoso", "Sabichão", "Solitário","Piadista", "Sarcástico", "Suspeito","Planejador", "Selvagem", "Teimoso"]
l1 = [2,1,0]
l2 = [2,0,1]
l3 = [1,2,0]
l4 = [0,2,1]
l5 = [1,0,2]
l6 = [0,1,2]
tl = [l1, l2, l3, l4, l5, l6]
contador = 1
contaLinha = 0

print("-" * 25)
print("\033[35mAlistamento de Personagem")
print("\033[33mOBS: Caso o personagem tenha uma informação desconhecida, bote -1\033[m")
while True:
    jogadores['Nome: '] = (str(input("Nome do Personagem: ")).strip()).capitalize()
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
    jogadores['Classe '] = (str(input("Classe: "))).strip().capitalize()
    jogadores['Gênero '] = (str(input("Gênero: "))).strip().capitalize()
    lin()
    PouR = str(input("\033[33mAgora vai vim a aparência do seu personagem!\nCaso você queira personalizado digite P\nCaso você queira ir no aleatório digite R\n\033[mSua opção[P/R]: ")).upper().strip()
    lin()
    while PouR not in "PR":
        PouR = str(input("\033[31mApenas P ou R: \033[m")).strip().upper()
    time.sleep(0.2)
        
    if PouR == "R":   
        jogadores['Fala '] = random.choice(fala)
        jogadores['Aparência '] = random.choice(aparência)
        jogadores['Detalhe físico '] = random.choice(detalheFisico)
        jogadores['Origem '] = random.choice(origem)
        jogadores['Vestimenta '] = random.choice(vestimenta)
        jogadores['Personalidae '] = random.choice(personalidade)
        time.sleep(0.3)
        print("\033[32mCaracteristicas Salvas\033[m")
    else:
        for element in fala:
            print(f'{"^5":element}',end = '\     ')
            contaLinha = contaLinha + 1
            if contaLinha == 4:
                print()
                contaLinha = 0

        jogadores['Fala '] = str(input("Fala: ")).capitalize()
        jogadores['Aparência '] = str(input("Aparência: ")).capitalize()
        jogadores['Detalhe físico '] = str(input("Detalhe Físico: ")).capitalize()
        jogadores['Origem '] = str(input("Origem: ")).capitalize()
        jogadores['Vestimenta '] = str(input("Vestimenta: ")).capitalize()
        jogadores['Personalidae '] = str(input("Personalidade: ")).capitalize()
    random.shuffle(objetos)
    itens = [objetos[0],objetos[1],objetos[2],objetos[3],objetos[4],objetos[5]]
    lin()
    jogadores['Armadura: '] = armadura()
    jogadores["Objetos "] = itens
    jogadores['Saúde '] = 4
    print("\033[33mAgora vamos para os atributos do seu personagem")
    print("\033[33mRolar dado ou Personalizado?\033[m")
    ePOUR = str(input("Sua opção[P\R]: ")).strip().upper()
    while ePOUR not in "PR":
        ePOUR = str(input("\033[31mApenas P ou R: \033[m")).strip().upper()
    
    if ePOUR == 'R':
        lescolhida = random.choice(tl)
        jogadores['Força '] = f'+{lescolhida[0]}'
        jogadores['Destreza '] = f'+{lescolhida[1]}'
        jogadores['Vontade '] = f'+{lescolhida[2]}'
    else:
        print("   Forc. Des. Von.")
        for elemento in tl:
            print(f'{contador} |  +{elemento[0]}   +{elemento[1]}   +{elemento[2]}')
            contador = contador + 1
        escolhaatributo = analeseInteiro("Qual é sua opcão: ")
        while escolhaatributo > 7 or escolhaatributo <= -1:
            escolhaatributo = analeseInteiro("\033[31mEscolha um numero válido: \033[m")
        escolhaatributo = escolhaatributo - 1
        lescolhida2 = tl[escolhaatributo]
        jogadores['Força '] = lescolhida2[0]
        jogadores['Destreza '] = lescolhida2[1]
        jogadores['Vontade '] = lescolhida2[2]
    
    break
print('Carregando...')
time.sleep(2)
cabeçalho("Ficha")
for k, v in jogadores.items():
    if v == "-1" or v == '':
        print(f'{k}= \033[31mDesconhecida\033[m')          
    else:
        print(f'{k}= \033[32m{v}\033[m')
    time.sleep(0.5)
lin()
print("\033[33mOBS: recomendado tirar print da ficha\033[m")
time.sleep(120)