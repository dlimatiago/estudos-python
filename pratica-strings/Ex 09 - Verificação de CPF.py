cpf = input('Informe o número do seu CPF (xxx.xxx.xxx-xx):  ')
cpf = cpf.replace('.', '')
cpf = cpf.split('-')
digitos = cpf[0]
cpf_verificado = digitos
digitos_verificadores = cpf[1]
mult = list(range(10, 1, -1))
soma_dig1 = 0  # Fazendo o controle para obter a soma da multiplicação do 1º dígito verificador
for i in range(9):
    soma_dig1 += int(digitos[i])*int(mult[i])
resto = soma_dig1 % 11
if resto < 2:
    digito_verificador1 = '0'
    novos_digitos_verificadores = digito_verificador1
    cpf_verificado += digito_verificador1
else:
    digito_verificador1 = str(11 - resto)
    novos_digitos_verificadores = digito_verificador1
    cpf_verificado += digito_verificador1
# Aqui começa o calculo do segundo dígito verificar
mult2 = list(range(11, 1, -1))
soma_dig2 = 0
for j in range(10):
    soma_dig2 += int(mult2[j])*int(cpf_verificado[j])

resto_2 = soma_dig2 % 11
if resto_2 < 2:
    digito_verificador2 = '0'
    novos_digitos_verificadores += digito_verificador2
    cpf_verificado += digito_verificador2
else:
    digito_verificador2 = str(11 - resto_2)
    novos_digitos_verificadores += digito_verificador2
    cpf_verificado += digito_verificador2

if digitos_verificadores == novos_digitos_verificadores:
    print('Este CPF possuí números válidos')
else:
    print('Esse CPF possuí números inválidos')