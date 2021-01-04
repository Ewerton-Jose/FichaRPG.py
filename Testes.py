def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        return False
    else:
        return True

def criarArquivo(nome):
    a = open(nome, 'wt+')
    a.close()
    return a

def lerArquivos(nome):
    try:
        print("------")
        a = open(nome, 'rt')
    except:
        print("erro")
    else:
        return a.read()

arq = "dadosPersonagens.TXT"
if not arquivoExiste(arq):
    criarArquivo(arq)
else:
    lerArquivos(arq)