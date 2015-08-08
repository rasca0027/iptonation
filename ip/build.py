import MySQLdb
import time

print 'start'

with open('ip2nation.sql', 'r') as fil:
    commands = fil.read().split(';')
    conn = MySQLdb.connect(host="mysql",port=3306,user="root",passwd="root")

    cur = conn.cursor()
    
    print 'create database test'
    cur.execute('DROP DATABASE IF EXISTS test;')
    cur.execute('CREATE DATABASE test;')
    cur.execute('use test;')

    print 'create ip2nation table'
    for command in commands:
        if not command.strip():
            continue
        cur.execute(command)

