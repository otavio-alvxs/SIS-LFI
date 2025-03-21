import pymysql

DB_HOST = '54.91.193.137'
DB_USER = 'libertas'
DB_PASSWORD = '123456'
DB_NAME = 'libertas5per'
def connect_db():
    return pymysql.connect(host=DB_HOST,
                           user=DB_USER,
                           password=DB_PASSWORD,
                           database=DB_NAME)

                           