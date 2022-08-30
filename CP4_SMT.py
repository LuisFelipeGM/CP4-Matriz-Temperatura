### RM: 94615 Nome: Daniel Henrique Alcântara Oliveira Martins
### RM: 94051 Nome: Luís Felipe Garcia Menezes
### RM: 93627 Nome: Pedro Victor Saraiva de Sá

## Funções

def obter_n_cardinalidade():
    '''
    () -> lista
    Função que obtêm a cardinalidade de uma matriz (linha e coluna)
    Retorno: uma lista contendo o número de linhas e colunas obtidos
    pelo usuário
    '''
    linha = int(input("Digite quantas semanas: "))
    coluna = int(input("Digite quantos dias por semana: "))
    resultado = [linha, coluna]
    return resultado

def criar_matriz(linha, coluna):
    '''
    (int, int) -> matriz
    Recebe o número de linhas e colunas, cria uma matriz, preenche e
    retorna a matriz preenchida com as temperaturas médias no período informado
    '''
    matriz = []
    for i in range(linha):
        linha = []
        for x in range(coluna):
            valor = float(input(f"Digite o valor da temperatura da {i + 1}° semana  no {x + 1}° dia: "))
            linha.append(valor)
        print("\n")
        matriz.append(linha)
    return matriz

def temp_media(matriz):
    '''
        Recebe uma matriz com valores, faz a soma das linhas da matriz 
        e retorna uma lista com as médias semanais
    '''
    soma = 0
    aux = 0
    media_sem = []
    for i in matriz:
        for x in i:
            soma += x
            aux += 1
        media = soma / aux
        media_sem.append(f"{media:.2f}")
        soma = 0
        aux = 0
    for i in range(len(media_sem)):
        media_sem[i] = float(media_sem[i])
    return media_sem


        

def obter_menor_maior_temperatura(media_sem):
    '''
    (lista) -> int
    Recebe uma matriz preenchida com as temperaturas médias no e retorna a menor
    temperatura obtida
    '''
    menor_temp = media_sem[0]
    maior_temp = media_sem[0]
    listas = []
    for i in media_sem:
        if i > maior_temp:
            maior_temp = i
        if i < menor_temp:
            menor_temp = i
    listas = [maior_temp, menor_temp]
    return listas


def obter_lista_negativos(media_sem):
    '''
    (lista) -> lista
    Recebe matriz preenchida com as temperaturas médias no período informado
    e retorna uma lista com apenas as temperaturas negativas
    '''
    lista_neg = []
    aux = 0
    for i in media_sem:
        if i < 0:
            lista_neg.append(i)
    return lista_neg

## Função de impressão
def imprimir():
    '''
        Função principal para execução do código inteiro
    '''
    x = obter_n_cardinalidade()
    matriz = criar_matriz(x[0], x[1])
    media_sem = temp_media(matriz)
    soma = 0
    for i in range(len(media_sem)):
        print (f"A média de temperatura na semana {i + 1} foi de {media_sem[i]}")
        soma += media_sem[i]
    print("\n")
    print(f"A média total das temperaturas foi de: {soma / len(media_sem)}")
    lista = obter_menor_maior_temperatura(media_sem)
    print(f"\nA maior media de temperatura foi de: {lista[0]}")
    print(f"A menor media de temperatura foi de: {lista[1]}\n")
    vl_neg = obter_lista_negativos(media_sem)
    if len(vl_neg) == 0:
        print("Não há valores negativos...\n")
    elif len(vl_neg) != 0:
        print(f"Valores negativos: {vl_neg}\n")


## Execução do código
imprimir()