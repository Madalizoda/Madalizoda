import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "root", "", "test3", charset='utf8')

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM category"

try:
   new_category = input('Новая категория: ')   
   sql = "INSERT INTO category (title) VALUES ('" + new_category + "')"
   print(sql)
   cursor.execute(sql)
   db.commit()
except Exception as e:
   print("type error: " + str(e))

# disconnect from server
db.close()
