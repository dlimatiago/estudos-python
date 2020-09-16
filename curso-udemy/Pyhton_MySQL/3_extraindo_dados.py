import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    port=3308,
    user='root',
    password='4321.',
    db='cursopython',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
query = f"""select * from cadastros;"""

with conexao.cursor() as cursor:
    # Executando a requisição
    cursor.execute(query)
    # Pegando os dados do select
    # Retorna uma lista de dicionários contendo os registros dentro
    dados = cursor.fetchall()

for k in dados:  # k pode ser tratado como um dicionário, logo dict methods são aceitos
    print(k.values())
