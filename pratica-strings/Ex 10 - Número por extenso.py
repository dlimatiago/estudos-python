import sys
resposta = 1
while resposta == 1:
    num = input('Digíte um número inteiro de 00 a 99: ')
    numeros = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    extenso_unidade = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
    extenso_dezena = ('vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')
    especiais = ('dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
    if int(num[0]) == 0:
        for i in range(10):
            if num[1] == numeros[i]:
                numero_extenso = extenso_unidade[i]
                print('O número {} por estenso é {}.'.format(num, numero_extenso))

    if int(num[0]) >= 2:
        for j in range(2, 10):
            if num[0] == numeros[j]:
                dezena_extensa = extenso_dezena[j-2]
        for k in range(10):
            if num[1] == numeros[k]:
                unidade_extensa = extenso_unidade[k]
        print('O número {} por extenso é {} e {}.'.format(num, dezena_extensa, unidade_extensa))
    if int(num[0]) == 1:
        for p in range(10):
            if num[1] == numeros[p]:
                numero_especial = especiais[p]
        print('O número {} por extenso é {}.'.format(num, numero_especial))
    resposta = int(input('Se deseja testar outro número, digite [1], caso não, digite [0]'))