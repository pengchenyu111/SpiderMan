import pymysql
from MovieSpider.settings import MYSQL_HOST, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DB, MYSQL_DB_CHARSET


def connect_mysql():
    connection = pymysql.connect(host=MYSQL_HOST,
                                 user=MYSQL_USERNAME,
                                 password=MYSQL_PASSWORD,
                                 db=MYSQL_DB,
                                 charset=MYSQL_DB_CHARSET)
    return connection


connection = connect_mysql()
cursor = connection.cursor()