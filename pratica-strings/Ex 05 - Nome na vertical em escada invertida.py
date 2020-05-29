nome = input('Digite seu nome: ').upper()
n = len(nome)+1
for i in range(n):
	i += 1
	print(nome[slice(n-i)])