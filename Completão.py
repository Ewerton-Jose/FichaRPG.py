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
    y = analeseInteiro("\033[34mQD: ")
    z = analeseInteiro("LD: \033[m")
    if y == 0 or z == 0:
        print(f"{x} = \033[31mSem valor\033[m")
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
vestimenta = ["Alta costura", "Cerimonial", "Desgastada","Amassada", "Chamuscada", "Elegante","Anacrônica Com laços", "Encardida","Antiga", "Curta", "Esfarrapada","Bordada", "Decadente", "Excêntrica","Brega", "Deselegante", "Exótica","Extravagante", "Manchada de comida", "Perfumada","Farda", "Manchada de lama", "Prática","Fora de catálogo", "Manchada de sangue", "Rasgada de batalha","Formal", "Manchada de vinho", "Remendada","Larga", "Ornamentada", "Requintada","Luxuosa", "Padrão", "Vulgar"]
personalidade = ["Alegre", "Cabeça quente", "Esperto","Amargo", "Cauteloso", "Estoico","Ameaçador", "Contrariador","Honrado","Arrogante", "Covarde", "Inquisitivo","Astuto" ,"Dominador", "Irascível","Bravo", "Espaçoso", "Justo","Leal", "Preguiçoso", "Sem coração","Mal humorado", "Protetor", "Sereno","Nervoso", "Rude", "Sociável","Orgulhoso", "Sabichão", "Solitário","Piadista", "Sarcástico", "Suspeito","Planejador", "Selvagem", "Teimoso"]

print("-" * 25)
print("\033[35mAlistamento de Personagem")
print("\033[33mOBS: Caso o personagem tenha uma informação desconhecida, bote -1\033[m")
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
    lin()
    PouR = str(input("\033[33mAgora vai vim a aparência do seu personagem!\nCaso você queira personalizado digite P\nCaso você queira ir no aleatório digite R\n\033[mSua opção[S/R]: "))[0].upper().strip()
    lin()
    time.sleep(0.5)
    while PouR not in "PR":
        PouR = str(input("\033[31mApenas P ou R: \033[m")).strip().upper()
        
    if PouR == "R":   
        jogadores['Fala '] = random.choice(fala)
        jogadores['Aparência '] = random.choice(aparência)
        jogadores['Detalhe físico '] = random.choice(detalheFisico)
        jogadores['Origem '] = random.choice(origem)
        jogadores['Vestimenta '] = random.choice(vestimenta)
        jogadores['Personalidae '] = random.choice(personalidade)
        print("\033[33mRandomizado\033[m")
    else:
        jogadores['Fala '] = str(input("Fala: "))
        jogadores['Aparência '] = str(input("Apar~encia: "))
        jogadores['Detalhe físico '] = str(input("Detalhe Físico: "))
        jogadores['Origem '] = str(input("Origem: "))
        jogadores['Vestimenta '] = str(input("Vestimenta: "))
        jogadores['Personalidae '] = str(input("Personalidade: "))
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
    elif v == 0:
        print(f'{k}= \033[33m{v}\033[m')
    else:
        print(f'{k}= \033[32m{v}\033[m')
    time.sleep(0.5)
lin()
time.sleep(120)