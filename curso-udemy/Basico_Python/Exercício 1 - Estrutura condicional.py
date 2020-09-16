print()
print('SVB- Sistema de Verificação de Bolsas')
print()
nome = input('Informe seu nome e sobrenome: ')
nome = nome.title()
print()
idade = int(input('Informe a sua idade: '))
print()
nota_1 = float(input('Informe quanto tirou na primeira avaliação: '))
print()
nota_2 = float(input('Informe quanto tirou na segunda avaliação: '))

nota = (nota_1 + nota_2) / 2

if nota >= 6 and idade >= 18:
    print('{a} foi aprovado com nota {b}.'.format(a=nome, b=nota))
elif idade > 18:
    print('{a} foi reprovado com nota {b}.'.format(a=nome, b=nota))
elif nota >= 6:
    print('{a} foi reprovado devido a idade.'.format(a=nome))

print('**********_FIM_**********')
