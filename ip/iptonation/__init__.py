import MySQLdb
import time

time.sleep(10)

db = MySQLdb.connect(host="mysql",port=3306,user="root",passwd="root")
cur = db.cursor()

with open('ip2nation.sql', 'r') as file:
    for line in file.readlines():
        cur.execute(line)

