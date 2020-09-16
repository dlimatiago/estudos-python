color = {'red': '\033[41m', 'green': '\033[42m', 'close': '\033[m'}
ncolor = {'red': '\033[31m', 'green': '\033[32m', 'close': '\033[m'}

print(f'Legenda'.center(20))
print(f'Número com resto 5:     {color["green"]}     {color["close"]}\n'
      f'Número com outro resto: {color["red"]}     {color["close"]}')
for number in range(1000, 2001):
    if number % 11 == 5:
        print(f'{ncolor["green"]}{number}{ncolor["close"]}', end=' ')
    else:
        print(f'{ncolor["red"]}{number}{ncolor["close"]}', end=' ')
print()