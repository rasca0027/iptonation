import MySQLdb
import time

time.sleep(10)

db = MySQLdb.connect(host="mysql",port=3306,user="root",passwd="root", db="test")
cur = db.cursor()

with open('ip2nation.sql', 'r') as fil:
    #for line in fil.readlines():
        #cur.execute(line)
    cur.execute(fil.read())
