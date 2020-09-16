from statistics import mean as med

ages = list()

while True:
    while True:
        age = int(input('Digite uma idade (-1 para): '))
        if age >= 0 or age == -1:
            break
        else:
            print('\033[1;31mValor inválido!\033[m')
    if age == -1:
        media = med(ages)
        print(f'A média de idade é {int(media)} anos.\n'
              f'Foram registradas {len(ages)} pessoas.\n'
              f'A pessoa mais velha tem {max(ages)} anos.\n'
              f'A pessoa mais nova tem {min(ages)} anos.')
        break
    ages.append(age)
