#Adiciona os itens à lista
def f_input(lista):
    for n in range(10):
        lista.append(int(input()))

def f_posi(lista, lista_p):
    for n in lista:
        if n >= 0:
            lista_p.append(n)

def f_neg(lista, lista_n):
    for n in lista:
        if n < 0:
            lista_n.append(n)


def main():
    lista = []
    lista_p = []
    lista_n = []

    #Entrada de Dados
    f_input(lista)
    f_posi(lista, lista_p)
    f_neg(lista, lista_n)

    #Saída de Dados
    print(lista)
    print(len(lista_n))
    print(sum(lista_p))

if __name__ == '__main__':
    main()
