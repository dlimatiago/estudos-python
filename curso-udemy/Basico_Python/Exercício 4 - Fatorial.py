num = int(input('Informe um número pra saber seu fatorial: '))
fat = 1
print(f'{num}! = ', end='')
for n in range(num, 1, -1):
    fat *= n
    print(f'{n} x ', end='')
print(f'1 = {fat}')
