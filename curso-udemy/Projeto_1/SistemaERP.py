import pymysql.cursors
import pymysql as sql


def connection():
    con = sql.connect(
        host='localhost',
        port=3308,
        user='root',
        password='4321.',
        db='erp',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    return con


def query(line, action='commit'):
    connect = connection()
    try:
        with connect.cursor() as cursor:
            cursor.execute(line)
        if action == 'commit':
            try:
                connect.commit()
                return True
            except:
                print('Erro ao inserir os dados!')
                return None
        elif action == 'fetchall':
            return cursor.fetchall()
    except:
        print('Erro ao se comunicar com o banco de dados. Query não executada!')


def login_singup():
    user_exists = 0
    authenticaded = False
    superuser = False

#     Como  decision é de escopo global e só será usada para leitura, não é necessária a declaração na função
    if decision == 1:
        user, password = input('Digite seu nome: '), input('Digite sua senha: ')

        for users in usersfound:
            values = users.values()
            if user in values and password in values:
                if 2 in values:
                    superuser = True
                authenticaded = True
            else:
                authenticaded = False
        if not authenticaded:
            print('\nLogin inválido: Senha ou nome de usuários não costam no banco de dados. Repita o processo.\n')

    else:
        print('Bem-vindo ao sistema. Por favor, preencha os seus dados para se cadastrar: ')
        user, password = input('Digite seu nome: '), input('Digite sua senha: ')

        for users in usersfound:
            values = users.values()
            if user in values and password in values:
                user_exists = 1    # Usuarios podem ter mesmo nome, mas senhas diferentes

        if user_exists:
            print('Usuário já cadastrado. Tente outro usuário ou senha')
        else:
            check = query(f'insert into cadastros(usuario, senha, nivel) values("{user}","{password}",{1})')
            if check is not None:
                print('\nUsuário cadastrado com sucesso!\n')


    return authenticaded, superuser


auth = False
while not auth:
    while True:
        decision = int(input('[1] Login\n[2] Novo cadastro\n-> '))
        if decision in (1, 2):
            break
        else:
            print('\nOpção inválida! Tente novamente...\n')

    usersfound = query('select * from cadastros', 'fetchall')

    auth, SuperUser = login_singup()
