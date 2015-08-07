import MySQLdb
import time

time.sleep(10)

with open('ip2nation.sql', 'r') as fil:
    data = fil.read()
    db = MySQLdb.connect(host="mysql",port=3306,user="root",passwd="root", db="test")
    cur = db.cursor()
    for line in fil.readlines():
        cur.execute(line)
    #exit(cur.execute('show tables;')
