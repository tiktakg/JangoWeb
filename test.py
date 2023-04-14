import mysql.connector



 
try:
    conn = mysql.connector.connect(user='root', password='root',
                                    host='localhost',
                                    port=3308, # change to the port number used by MAMP
                                    database='test')
    cursor = conn.cursor()
    select_all_row = "SELECT * FROM `loginData`"
    cursor.execute(select_all_row)

    data2 = cursor.fetchall()
    print(data2)
  
    conn.close()
except mysql.connector.Error as e:
    print("Error connecting to MySQL: ", e)


