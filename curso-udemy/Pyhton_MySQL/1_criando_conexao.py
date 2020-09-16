import pymysql.cursors

# Cria a conexão com o BD
conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='1234.',
    db='cursopython',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
"""# Sempre que abrir a conexão e o BD, deve-se fecha-lo, igual se faz com arquivos.
cursor = conexao.cursor()
# Query a ser passada
cursor.execute('create table pessoas(nome varchar(30), idade int, endereco varchar(100));')

# Ao invés de passar a query dentro da função, eu posso atribuir a uma variavel
apagar = 'drop table pessoas;'
cursor.execute(apagar)


cursor.close()
conexao.close()
"""

# Outra forma é usando o with, ele ajuda para não ficar abrindo e fechando o cursor toda hora
query = 'create table pessoas(nome varchar(50), idade int, cpf varchar(11));'

with conexao.cursor() as cursor:
    cursor.execute(query)

