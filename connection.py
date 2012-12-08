import psycopg2
import sys

connection = None

try :
	connection = psycopg2.connect(database='postgres', user='test', host='localhost') 
	cur = connection.cursor()
   	cur.execute('SELECT version()')          
	ver = cur.fetchone()
	print ver
except psycopg2.DatabaseError, e:
	print "Error "+str(e)
	sys.exit(1)
finally:
	if connection:
		connection.close()