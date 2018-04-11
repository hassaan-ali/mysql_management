
#!/usr/bin/python
import os.path
import MySQLdb
import time
from datetime import timedelta, date
yesterday = date.today() - timedelta(1)
timestr = yesterday.strftime("%Y-%m-%d")
fname="agritv_"+ timestr+".sql.gz"
#print (fname)
if (os.path.isfile(fname)):
	# Open database connection
	db = MySQLdb.connect("localhost","root","root123","agritv" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# execute SQL query using execute() method.
	cursor.execute("SELECT VERSION()")


	# disconnect from server
	db.close()
else:
	print ("no scene")
	exit(1)

