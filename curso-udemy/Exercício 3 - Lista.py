from statistics import mean as med
pesos, ac90 = list(), 0
for p in range(7):
    pesos.append(float(input(f'Digite o {p+1}º peso: ')))
media = med(pesos)
print('-=-' * 30)
print(f'{"Pessoas":<4}{"Peso":>8}')
for pos, item in enumerate(pesos):
    print(f'{pos+1:<4}{item:>10.1f} Kg')
    ac90 = ac90 + 1 if item > 90 else ac90 + 0
print(f'Média dos pesos: {media:.1f} kg\n'
      f'Pessoas +90 kg: {ac90}')


