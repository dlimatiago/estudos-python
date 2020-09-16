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
q = f"""
insert into cadastros (nome, endereco) values
    ('{input('Nome: ')}', '{input('Endereço: ')}');
"""
with conexao.cursor() as cursos:
    cursos.execute(f'{q}')
    conexao.commit()
