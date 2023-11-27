#Adiciona os itens à lista
def f_input(lista):
    for n in range(10):
        lista.append(int(input()))
        

def main():

    lista_a = []
    lista_b = []

    #Entrada de Dados
    f_input(lista_a)
    f_input(lista_b)

    lista_c = lista_a + lista_b

    #Converte a lista para dicionário, e depois de volta
    #para lista. A conversão elimina as duplicatas.
    lista_final = list(dict.fromkeys(lista_c))
    
    #Saída de Dados
    print(lista_final)

if __name__ == '__main__':
    main()
