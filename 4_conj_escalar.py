#Adiciona o input a uma lista
def f_input(lista):
    for n in range(5):
        lista.append(int(input()))

def f_ProdEscalar(a, b):
    if len(a) != len(b):
        return 0
    return sum(i[0] * i[1] for i in zip(a, b))

    
def main():

    lista_a = []
    lista_b = []

    #Entrada de Dados
    f_input(lista_a)
    f_input(lista_b)
    produto_escalar = f_ProdEscalar(lista_a, lista_b)

    #Saída de Dados
    print(lista_a)
    print(lista_b)
    print(f'({lista_a[0]} x {lista_b[0]}) + ({lista_a[1]} x {lista_b[1]}) + ({lista_a[2]} x {lista_b[2]}) +'
          f'({lista_a[3]} x {lista_b[3]}) + ({lista_a[4]} x {lista_b[4]})','=',produto_escalar)

if __name__ == '__main__':
    main()
