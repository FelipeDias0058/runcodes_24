#Adiciona os itenss à lista
def f_input(lista):
    for n in range(10):
        lista.append(int(input()))


def main():
    lista = []

    #Entrada de Dados
    f_input(lista)

    #Saída de Dados
    print(lista)
    print(max(lista))
    print(lista.index(max(lista)))


if __name__ == '__main__':
    main()
