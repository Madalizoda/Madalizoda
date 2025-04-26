import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "root", "", "test3", charset='utf8')

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM category ORDER BY id"

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      title = row[1]
      # Now print fetched result
      print("id = %s, title = %s" % (id, title))

   id_category = input('ID существующей категории: ')   
   new_title = input('Новое название: ')   
   sql = "UPDATE category SET title = '" + new_title \
         + "' WHERE id = " + id_category
   print(sql)
   cursor.execute(sql)
   db.commit()
except Exception as e:
   print("type error: " + str(e))

# disconnect from server
db.close()
   
