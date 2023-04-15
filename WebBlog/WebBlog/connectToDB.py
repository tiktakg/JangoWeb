import mysql.connector

 
def checkAdmin(login, password):
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                        host='localhost',
                                        port=3308, # change to the port number used by MAMP
                                        database='test')
        cursor = conn.cursor()
       
        cursor.execute("SELECT * FROM `loginData`")
        data = cursor.fetchall()
        if(data[0] ==(login, password)):
            conn.close()
            return True

    except mysql.connector.Error as e:
        print("Error connecting to MySQL: ", e)

def takeAllPost():
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                        host='localhost',
                                        port=3308, # change to the port number used by MAMP
                                        database='test')
        cursor = conn.cursor()
       
        cursor.execute("SELECT name FROM `blog`")
        name = cursor.fetchall()

       
        name= ' '.join(map(str, name))

        for ch in ['(',')','\'',',']:
            name = name.replace(ch,'')
        
        name = name.split()
        print(name)
        return name
       

    except mysql.connector.Error as e:
        print("Error connecting to MySQL: ", e)

def takeTextOfPost(namePost):
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                        host='localhost',
                                        port=3308, # change to the port number used by MAMP
                                        database='test')
        cursor = conn.cursor()
       
        cursor.execute("SELECT name,data FROM `blog`")
        text = cursor.fetchall()

        for txt in text:
            if(txt[0]==namePost):
                return txt[1]

 

    except mysql.connector.Error as e:
        print("Error connecting to MySQL: ", e)

def takeTegOfPost(namePost):
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                        host='localhost',
                                        port=3308, # change to the port number used by MAMP
                                        database='test')
        cursor = conn.cursor()
       
        cursor.execute("SELECT name,tegs FROM `blog`")
        
        name= ' '.join(map(str, name))

        for ch in ['(',')','\'',',']:
            name = name.replace(ch,'')
        
        name = name.split()
        print(name)

 

    except mysql.connector.Error as e:
        print("Error connecting to MySQL: ", e)


def deltePost(namePost):
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                        host='localhost',
                                        port=3308, # change to the port number used by MAMP
                                        database='test')
        cursor = conn.cursor()
       
        cursor.execute("DELETE FROM `blog` WHERE `primaryKey` = "+ str(namePost))
        conn.commit()
    
    except mysql.connector.Error as e:
        print("Error connecting to MySQL: ", e)



# `


    

