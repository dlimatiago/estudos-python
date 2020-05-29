frase = input('Digite uma frase: ')
v_vir = ',' in frase
v_esp = ' ' in frase
v_hif = '-' in frase
v_pon = '.' in frase
v_exc = '!' in frase
v_int = '?' in frase
v_asp = '"' in frase
v_dpo = ':' in frase
v_á = 'á' in frase
v_à = 'à' in frase
v_â = 'â' in frase
v_ã = 'ã' in frase
v_é = 'é' in frase
v_ê = 'ê' in frase
v_í = 'í' in frase
v_ó = 'ó' in frase
v_ô = 'ô' in frase
v_õ = 'õ' in frase
v_ú = 'ú' in frase

if v_vir is True:
    frase = frase.replace(',', '')
if v_esp is True:
    frase = frase.replace(' ', '')
if v_hif is True:
    frase = frase.replace('-', '')
if v_pon is True:
    frase = frase.replace('.', '')
if v_exc is True:
    frase = frase.replace('!', '')
if v_int is True:
    frase = frase.replace('?', '')
if v_asp is True:
    frase = frase.replace('"', '')
if v_dpo is True:
    frase = frase.replace(':', '')

frase = frase.replace('á', 'a') if v_á is True else frase
frase = frase.replace('à', 'a') if v_à is True else frase
frase = frase.replace('â', 'a') if v_â is True else frase
frase = frase.replace('ã', 'a') if v_ã is True else frase
frase = frase.replace('é', 'e') if v_é is True else frase
frase = frase.replace('ê', 'e') if v_ê is True else frase
frase = frase.replace('í', 'i') if v_í is True else frase
frase = frase.replace('ó', 'o') if v_ó is True else frase
frase = frase.replace('ô', 'o') if v_ô is True else frase
frase = frase.replace('õ', 'o') if v_õ is True else frase
frase = frase.replace('ú', 'u') if v_ú is True else frase

frase = frase.upper()
frase_inv = frase[::-1]

if frase_inv == frase:
    print('Essa frase é palíndroma')
else:
    print('Essa frase não é palíndroma')
