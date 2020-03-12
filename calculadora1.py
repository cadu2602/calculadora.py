nome = input('Qual o seu nome?')
print('Olá', nome, 'Escreva os valores que você deseja abaixo')
n1 = input('Primeiro valor:')
n2 = input('Segundo valor:')
opção = 0
while opção != 10:
    print('''[1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] dividir
    [6] subtrair
    [7] dobro e triplo
    [8] raiz quadrada
    [9] potência
    [10] sair do programa''')
    opção = int(input('Qual das opções acima você deseja realizar?'))
    if opção == 1:
       soma = int(n1) + int(n2)
       print('A soma entre {} + {} é {}'.format(n1, n2, soma))

       n1 = input('Primeiro valor:')
       n2 = input('Segundo valor:')
    elif opção == 2:
         produto = int(n1) * int(n2)
         print('O resultado de {} x {} é {}'.format(n1, n2, produto))

         n1 = input('Primeiro valor:')
         n2 = input('Segundo valor:')
    elif opção == 3:
        if int(n1) > int(n2):
            maior = int(n1)
        else:
            maior = int(n2)
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))

        n1 = input('Primeiro valor:')
        n2 = input('Segundo valor:')
    elif opção == 4:
        print('Coloque novos valores;')

        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    elif opção == 5:
        dividir = int(n1) / int(n2)
        print('A divisão de {} / {} é {}'.format(n1, n2, dividir))

        n1 = input('Primeiro valor:')
        n2 = input('Segundo valor:')
    elif opção == 6:
        subtrair = int(n1) - int(n2)
        print('A subtração de {} - {} é {}'.format(n1, n2, subtrair))

        n1 = input('Primeiro valor:')
        n2 = input('Segundo valor:')
    elif opção == 7:
        n1 = int(input('Primeiro valor:'))
        dobro = int(n1) * 2
        triplo = int(n1) * 3
        print('O dobro de {} é {}. O triplo de {} é {}'.format(n1, dobro, n1, triplo))

        n1 = input('Primeiro valor:')
        n2 = input('Segundo valor:')
    elif opção == 8:
        n1 = int(input('Primeiro valor:'))
        raiz = int(n1) ** (1/2)
        print('A raiz quadrada de {} é {}'.format(n1,  raiz))

        n1 = input('Primeiro valor:')
        n2 = input('Segundo valor:')
    elif opção == 9:
        pot = int(n1) ** int(n2)
        print('A potência de {} e {} é {}'.format(n1, n2, pot))

        n1 = input('Primeiro valor:')
        n2 = input('Segundo valor:')
    elif opção == 10:
        print('Encerrando....')
    else:
       print('Opção não existente. Tente outra')
