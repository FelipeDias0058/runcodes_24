#Adiciona os itens à lista
def f_input(lista):
    for n in range(20):
        lista.append(int(input()))

#Converte a lista em dicionário, depois converte em lista novamente.
#A conversão p/ dicionário remove os elementos duplicados.
def lista_sem_duplicatas(x):
    return list(dict.fromkeys(x))

def main():

    lista = []

    #Entrada de Dados
    f_input(lista)

    lista_unica = lista_sem_duplicatas(lista)

    #Saída de Dados
    print(lista_unica)

if __name__ == '__main__':
    main()
