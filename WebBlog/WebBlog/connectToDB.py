import mysql.connector
import base64

 
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
       
       

        
        
        newList = {}
        for name in name:
            newList[name[0]] = name[1]
          
 
        

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

def takeTegToPost(teg):
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                        host='localhost',
                                        port=3308, # change to the port number used by MAMP
                                        database='test')
        cursor = conn.cursor()
        cursor.execute("SELECT name,tegs FROM `blog`")
        name = cursor.fetchall()
        
        my_dict = dict(name)

        return my_dict.get(teg)
    

    except mysql.connector.Error as e:
        print("Error connecting to MySQL: ", e)

def takeTegOfPosts(teg):
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                        host='localhost',
                                        port=3308, # change to the port number used by MAMP
                                        database='test')
        cursor = conn.cursor()
        cursor.execute("SELECT name,primaryKey,tegs FROM `blog`")
        name = cursor.fetchall()
        
        
      
        
        newList = {}
        for name in name:
            allTegs = name[2].split(',')
            for tegs in allTegs:
                if(tegs.lower() == teg.lower() ):
                    newList[name[0]] = name[1]
                    print(str(name[0]) +"|"+ str(name[1])+"|" + str(name[2]))
            

        
           
        return newList
    

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



def addPost(namePost,dataPost,tegPost,imgPost):
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                        host='localhost',
                                        port=3308, # change to the port number used by MAMP
                                        database='test')
        

    
        cursor = conn.cursor()
       
        
        # encoded_image = base64.b64encode(imgPost).decode("utf-8")
        print(imgPost)
        textForInset = f"INSERT INTO `blog` (`primaryKey`, `name`, `tegs`, `data`, `img`) VALUES (NULL, '{namePost}', '{tegPost}', '{dataPost}', Null);"
        cursor.execute(textForInset)
       
       
        conn.commit()
    
    except mysql.connector.Error as e:
        print("Error connecting to MySQL: ", e)

def updatePost(namePost,dataPost,tegPost,imgPost,id):
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                        host='localhost',
                                        port=3308, # change to the port number used by MAMP
                                        database='test')
        

        print(imgPost)
        cursor = conn.cursor()
        textForInset = f"UPDATE `blog` SET `name` = '{namePost}', `tegs` = '{tegPost}', `data` = '{dataPost}' WHERE `blog`.`primaryKey` = {id};"


        cursor.execute(textForInset)
        conn.commit()
    
    except mysql.connector.Error as e:
        print("Error connecting to MySQL: ", e)



def takeImg(namePost):
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                        host='localhost',
                                        port=3308, # change to the port number used by MAMP
                                        database='test')
        

        cursor = conn.cursor()
        cursor.execute(f"SELECT name,primaryKey FROM `blog`")
        allName = cursor.fetchall()

        id = ""
        for Name in allName:
            if(Name[0] == namePost):
                id = Name[1] 
           


        cursor.execute(f"SELECT img FROM `blog` WHERE primaryKey = {id}")
        img = cursor.fetchone()[0]    


        image_base64 = base64.b64encode(img).decode('utf-8')
        
        return image_base64
       

    except mysql.connector.Error as e:
        print("Error connecting to MySQL: ", e)


def takeAllImg():
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                        host='localhost',
                                        port=3308, # change to the port number used by MAMP
                                        database='test')
        

        cursor = conn.cursor()
        cursor.execute(f"SELECT img,primaryKey FROM `blog`")
        allImg = cursor.fetchall()


        newList = {}
        for result in allImg:
            if result[0] is not None:
                image_base64 = base64.b64encode(result[0]).decode('utf-8')
                
     
                newList[result[1]] = image_base64
         
        return newList
      

    except mysql.connector.Error as e:
        print("Error connecting to MySQL: ", e)



    
