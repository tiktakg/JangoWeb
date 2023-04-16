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
       
        cursor.execute("SELECT name,primaryKey FROM `blog`")
        name = cursor.fetchall()
       
        # print("name1")

        
        
        newList = {}
        for name in name:

            newList[name[0]] = name[1]
            newname =str(name[0]) + ":"+ str(name[1])
            # print(newname)
            
           
        # print(newList)

        # name= ' '.join(map(str, name))

       

        # for ch in ['(',')','\'',',']:
        #     name = name.replace(ch,'')
        
        # name = name.split()
        

        return newList
    
    except mysql.connector.Error as e:
        print("Error connecting to MySQL: ", e)

def takeIdOfPost():
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                        host='localhost',
                                        port=3308, # change to the port number used by MAMP
                                        database='test')
        cursor = conn.cursor()
       
        cursor.execute("SELECT primaryKey FROM `blog`")
        primaryKey = cursor.fetchall()
       
        primaryKey= ' '.join(map(str, primaryKey))

       
        for ch in ['(',')','\'',',']:
            primaryKey = primaryKey.replace(ch,'')
        
        primaryKey = primaryKey.split()
        
        return primaryKey
    
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

def takeTegOfPost(name):
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                        host='localhost',
                                        port=3308, # change to the port number used by MAMP
                                        database='test')
        cursor = conn.cursor()
        cursor.execute("SELECT name,tegs FROM `blog`")
        name = cursor.fetchall()
        
        name= ' '.join(map(str, name))

        for ch in ['(',')','\'',',']:
            name = name.replace(ch,'')
        
        
        name = name.split()
    
 

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

def takeImg(namePost):
    pass
takeTegOfPost("firstNotes")

# `


    
