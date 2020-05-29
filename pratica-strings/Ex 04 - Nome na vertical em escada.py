nome = input('Digite seu nome: ').upper()
n = len(nome)
for i in range(n):
	i += 1
	print(nome[slice(i)])