import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "root", "", "test3", charset='utf8')

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM category"

try:
   id_category = input('ID категории: ')   
   sql = "DELETE FROM category WHERE id = " + id_category
   print(sql)
   cursor.execute(sql)
   db.commit()
except Exception as e:
   print("type error: " + str(e))

# disconnect from server
db.close()
