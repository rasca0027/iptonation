import MySQLdb
from django.conf import settings

SERVER = settings.MYSQL_SERVER
USERNAME = settings.MYSQL_USERNAME
PASSWORD = settings.MYSQL_PASSWORD
DB = settings.MYSQL_DB
PORT = settings.MYSQL_PORT

def tonation(ip):
    db = MySQLdb.connect(SERVER, PORT, USERNAME, PASSWORD, DB)
    #db = MySQLdb.connect('localhost', 'root', 'root', 'test')
    cursor = db.cursor()

    sql = "SELECT country FROM ip2nation WHERE ip < INET_ATON('" + ip + "') ORDER BY ip DESC LIMIT 0,1"
    cursor.execute(sql)
    try:
        country = cursor.fetchone()[0]
    except:
        country = 'error'
    
    return country
    

