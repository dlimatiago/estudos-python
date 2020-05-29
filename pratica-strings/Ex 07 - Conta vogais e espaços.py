frase = input('Digite uma frase qualquer: ').lower()
espaço = frase.count(' ')
a = frase.count('a')
â = frase.count('â')
ã = frase.count('ã')
á = frase.count('á')
à = frase.count('à')
e = frase.count('e')
é = frase.count('é')
ê = frase.count('ê')
i = frase.count('i')
í = frase.count('í')
o = frase.count('o')
ô = frase.count('ô')
ó = frase.count('ó')
u = frase.count('u')
ú = frase.count('ú')

AS = a + â + ã + á + à
ES = e + é + ê
IS = i + í
OS = o + ô + ó
US = u + ú
vogais = AS + ES + IS + OS + US
print('Nessa frase contém {} espaços e tem um total de {} vogais. Sendo elas {} vezes o A,'
      ' {} vezes o E, {} vezes o I, {} vezes o O e {} vezes o U.'.format(espaço, vogais, AS, ES, IS, OS, US))