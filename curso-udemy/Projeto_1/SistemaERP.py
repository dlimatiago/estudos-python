import pymysql.cursors
import pymysql as sql

conecxao = sql.connect(
    host='localhost',
    port=3308,
    user='root',
    password='4321.',
    db='erp',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
