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


def login():
    pass


def signup():
    pass


auth = False
connect = connection()

while not auth:
    while True:
        decision = int(input('[1] Login\n[2] Novo cadastro\n-> '))
        if decision in (1, 2):
            break

    try:
        with connect.cursor() as cursor:
            cursor.execute('select * from cadastros')
            usersfound = cursor.fetchall()
            print(usersfound)
    except:
        print('Erro ao se comunicar com o banco de dados')
    else:
        if decision:
            login()
        else:
            signup()
