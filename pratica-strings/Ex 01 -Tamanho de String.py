str_1 = input('Digite uma string: ')
str_2 = input('Digite outra string: ')
t_1 = len(str_1)
t_2 = len(str_2)

print(f'String 1: {str_1}')
print(f'String 2: {str_2}')
print('Tamanho de {} é: {} catacteres'.format(str_1, t_1))
print('Tamanho de {} é: {} catacteres'.format(str_2, t_2))

if str_1 != str_2:
    print('As duas string possuem conteúdos diferentes')
if str_1 == str_2:
    print('As duas strings possuem conteúdos iguais')
if t_1 != t_2:
    print('As duas strings possuem tamanhos diferentes')
else:
    print('As duas strings possuem tamanhos iguais')

