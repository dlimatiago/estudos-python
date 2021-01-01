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


def data_validation(phrase, typo='int', options=None):
    while True:
        try:
            if typo == 'int':
                answer = int(input(phrase))
            elif typo == 'float':
                answer = float(input(phrase))
            elif typo == 'str':
                answer = phrase
        except ValueError:
            print('\n🚫 🚫 🚫 Tipo de dado incorreto 🚫 🚫 🚫\n')
            continue
        else:
            if options is not None:
                while True:
                    if answer in options:
                        break
                    else:
                        print('\n🚫 🚫 🚫 Opção inválida 🚫 🚫 🚫\n')
            return answer


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
                print('📝 ❌ Erro ao inserir/deletar os dados 📝 ❌')
                return None
        elif action == 'fetchall':
            return cursor.fetchall()
    except:
        print('⛔ 📶 ⛔ Erro ao se comunicar com o banco de dados. Query não executada ⛔ 📶 ⛔')


def login_singup():
    global user
    user_exists = 0
    authenticaded = superuser = False

    # Como  decision é de escopo global e só será usada para leitura, não é necessária a declaração na função
    if decision == 1:
        user, password = input('✉ Digite seu login: '), input('🔑 Digite sua senha: ')

        for users in usersfound:
            values = users.values()
            if user in values and password in values:
                if 2 in values:
                    superuser = True
                authenticaded = True
                break
            else:
                authenticaded = False
        if not authenticaded:
            print('\n🚫 🚫 🚫 Login inválido. Senha ou nome de usuários não costam no banco de dados 🚫 🚫 🚫\n')

    else:
        print('Bem-vindo ao sistema. Por favor, preencha os seus dados para se cadastrar ')
        newuser, password = input('✉ Digite seu nome para login: '), input('🔑 Digite sua senha: ')

        for users in usersfound:
            values = users.values()
            if newuser in values and password in values:
                user_exists = 1  # Usuarios podem ter mesmo nome, mas senhas diferentes

        if user_exists:
            print('🙍🙍🙍‍ Ops, usuário já cadastrado. Tente outro usuário ou senha 🙍🙍🙍')
        else:
            check = query(f'insert into cadastros(usuario, senha, nivel) values("{newuser}","{password}",{1})')
            if check is not None:
                print('\n✔ Usuário cadastrado com sucesso!\n')

    return authenticaded, superuser


def product_registration():
    product = input('📥 Informe o nome do produto: ')
    ingridients = input('📝 Informe os ingredientes que compõem o produto: ')
    group = input('🔠 Informe o grupo do produto: ')
    price = data_validation('💲 Informe o preço do produto: ', 'float')

    done = query(f'insert into produtos(nome, ingredientes, grupo, preco) '
                 f'values("{product}", "{ingridients}", "{group}", "{price}")')

    if done is not None:
        print('\n✔ Produto cadastrado com sucesso!\n')


def products_list():
    products_in_db = query('select * from produtos', 'fetchall')
    if len(products_in_db) != 0:
        print('🗄️🗄️🗄️🗄️🗄️🗄️🗄️🗄️🗄️🗄️ Produtos Cadastrados no Banco de Dados 🗄️🗄️🗄️🗄️🗄️🗄️🗄️🗄️🗄️🗄️'.center(103))
        print('-' * 103)
        print(f' Id           Nome              Grupo         Preço                    Ingredientes')
        print('----- --------------------   ----------     ---------    ----------------------------------------------')
        for i in products_in_db:
            subs = '-' if not i["ingredientes"] else i["ingredientes"]
            print(f'{i["id"]:^5} {i["nome"]:^20}    {i["grupo"]:^10}     R${i["preco"]:<5,.2f} {subs:^50}')
        print('-' * 103)
    else:
        print('📦 Nenhum produto cadastrado 📦')


def delete_product():
    idproduct = data_validation('🆔 Digite o id do produto a ser excluido: ')
    check = query(f'delete from produtos where id = {idproduct}')
    if check is not None:
        print('\n🚮 Produto deletado com sucesso!\n')


def orderslist():
    orders, choice = [], 0

    while choice != 2:
        orders.clear()  # Não acumula os pedidos
        orderlist = query('select * from pedidos;', 'fetchall')

        orders = orderlist[:]

        if len(orders) != 0:
            print('📑📑📑📑📑📑📑📑📑📑📑📑📑📑 Lista de Pedidos 📑📑📑📑📑📑📑📑📑📑📑📑📑📑'.center(101))
            print('-' * 121)
            print(f' Id           Nome               Grupo          Observações                Ingredientes                Local de Entrega')
            print('----- --------------------    -----------   -------------------    -----------------------------    ---------------------')
            for i in orders:
                subs1 = '-' if not i["ingredientes"] else i["ingredientes"]
                subs2 = '-' if not i["localEntrega"] else i["localEntrega"]
                subs3 = '-' if not i["observacoes"] else i["observacoes"]
                print(f'{i["id"]:^5} {i["nome"]:^20}    {i["grupo"]:^10}     {subs3:^15} {subs1:^40} {subs2:^18}')
            print('-' * 121)

        else:
            print('⚠️Nenhum pedido feito ⚠️')

        choice = data_validation('\n✅ Pedido entregue [1]\n🔙 Voltar [2]\n\n▶ ', options=(1, 2))
        print()

        if choice == 1:
            orderdoneId = data_validation('🆔 Informe o ID do pedido entregue: ')
            query(f'delete from pedidos where id = {orderdoneId}')
            print('\n🆗 Pedido concluído 🆗\n')


auth = False
while not auth:
    decision = data_validation('🔒 Login [1]\n📖 Novo cadastro [2]\n\n▶ ', options=(1, 2))
    usersfound = query('select * from cadastros', 'fetchall')
    auth, SuperUser = login_singup()

if auth:
    print(f'\nBem-Vindo, {user}!')

    if SuperUser:
        while True:
            newdecision = data_validation('\n🚶  Sair do sistema [1]\n'
                                          '📝 Cadastrar produto [2]\n'
                                          '📄 Listar produtos cadastrados [3]\n'
                                          '📄 Listar pedidos [4]\n\n▶ ', options=(1, 2, 3, 4))
            print()
            if newdecision == 1:
                break
            elif newdecision == 2:
                product_registration()
            elif newdecision == 3:
                products_list()
                while True:
                    alter = data_validation('\n🗑️ Sim remover algum produto [S]\n'
                                            '↩  Não para voltar [N]\n\n▶',
                                            typo='str', options=('s', 'n')).strip().lower()[:1]
                    if alter == 's':
                        delete_product()
                    else:
                        break
            elif newdecision == 4:
                orderslist()

print('Sistema Finalizado com sucesso!')
