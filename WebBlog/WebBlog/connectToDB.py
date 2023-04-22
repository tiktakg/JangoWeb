import mysql.connector



def checkAdmin(login, password):
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                       host='localhost',
                                       port=3308,  # change to the port number used by MAMP
                                       database='test')
        cursor = conn.cursor()

        cursor.execute("SELECT primaryKey,login,password,firstName FROM `loginData`")
        dataAboutAll = cursor.fetchall()

        cursor.execute("SELECT nameAdmin,isAdmin FROM `checkadmin`")
        dataAboutAdmin = cursor.fetchall()

        idUser = ""
        name =  ""
        for checkData in dataAboutAll:

            if (checkData[1] == login and checkData[2] == password):
                idUser = str(checkData[0])
                name =  str(checkData[3])
                

        for data in dataAboutAdmin:
            if (str(data[0]) == str(idUser)):
                if (str(data[1]) == "1"):
                    return 1,name
                elif (str(data[1]) == "0"):
                    return 0,name

        return -1,name

    except mysql.connector.Error as e:
        print("Error connecting to MySQL: ", e)


def takeAllPost():
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                       host='localhost',
                                       port=3308,  # change to the port number used by MAMP
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
                                       port=3308,  # change to the port number used by MAMP
                                       database='test')
        cursor = conn.cursor()

        cursor.execute("SELECT primaryKey FROM `blog`")
        primaryKey = cursor.fetchall()

        primaryKey = ' '.join(map(str, primaryKey))

        for ch in ['(', ')', '\'', ',']:
            primaryKey = primaryKey.replace(ch, '')

        primaryKey = primaryKey.split()

        return primaryKey

    except mysql.connector.Error as e:
        print("Error connecting to MySQL: ", e)


def takeTextOfPost(namePost):
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                       host='localhost',
                                       port=3308,  # change to the port number used by MAMP
                                       database='test')
        cursor = conn.cursor()

        cursor.execute("SELECT name,data FROM `blog`")
        text = cursor.fetchall()

        for txt in text:
            if (txt[0] == namePost):
                return txt[1]

        return ""

    except mysql.connector.Error as e:
        print("Error connecting to MySQL: ", e)


def takeTegToPost(teg):
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                       host='localhost',
                                       port=3308,  # change to the port number used by MAMP
                                       database='test')
        cursor = conn.cursor()
        cursor.execute("SELECT name,tegs FROM `blog`")
        name = cursor.fetchall()

        my_dict = dict(name)
        tegs = my_dict.get(teg)
        if (tegs is None):
            return ""

        return tegs

    except mysql.connector.Error as e:
        print("Error connecting to MySQL: ", e)


def takeTegOfPosts(teg):
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                       host='localhost',
                                       port=3308,  # change to the port number used by MAMP
                                       database='test')
        cursor = conn.cursor()
        cursor.execute("SELECT name,primaryKey,tegs FROM `blog`")
        name = cursor.fetchall()

        newList = {}
        for name in name:
            allTegs = name[2].split(',')
            for tegs in allTegs:
                if (tegs.lower() == teg.lower()):
                    newList[name[0]] = name[1]
                    print(str(name[0]) + "|" + str(name[1])+"|" + str(name[2]))

        return newList

    except mysql.connector.Error as e:
        print("Error connecting to MySQL: ", e)


def deltePost(namePost):
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                       host='localhost',
                                       port=3308,  # change to the port number used by MAMP
                                       database='test')
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM `blog` WHERE `primaryKey` = " + str(namePost))
        conn.commit()

    except mysql.connector.Error as e:
        print("Error connecting to MySQL: ", e)


def addPost(namePost, dataPost, tegPost, imgPost,nameAdmin):
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                       host='localhost',
                                       port=3308,  # change to the port number used by MAMP
                                       database='test')

        cursor = conn.cursor()


        with open('main/post_images/' + imgPost.name, 'wb+') as destination:
            for chunk in imgPost.chunks():
                destination.write(chunk)

        textForInset = f"INSERT INTO `blog` (`primaryKey`, `name`, `tegs`, `data`, `nameImage`, `nameAdmin`) VALUES (NULL, '{namePost}', '{tegPost}', '{dataPost}', '{imgPost}', '{nameAdmin}');"
        cursor.execute(textForInset)

        conn.commit()

    except mysql.connector.Error as e:
        print("Error connecting to MySQLM: ", e)


def updatePost(namePost, dataPost, tegPost, imgPost, id,nameAdmin):
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                       host='localhost',
                                       port=3308,  # change to the port number used by MAMP
                                       database='test')

        print(imgPost)
        cursor = conn.cursor()
        textForInset = f"UPDATE `blog` SET `name` = '{namePost}', `tegs` = '{tegPost}', `data` = '{dataPost}', `nameImage` ='{imgPost}', `nameAdmin`=  `{nameAdmin}` WHERE `blog`.`primaryKey` = {id};"

        cursor.execute(textForInset)
        conn.commit()

    except mysql.connector.Error as e:
        print("Error connecting to MySQLU: ", e)


def takeImg(namePost):
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                       host='localhost',
                                       port=3308,  # change to the port number used by MAMP
                                       database='test')

        cursor = conn.cursor()
        cursor.execute(f"SELECT name,primaryKey FROM `blog`")
        allName = cursor.fetchall()

        id = ""
        for Name in allName:
            if (Name[0] == namePost):
                id = Name[1]

       
        cursor.execute(
            f"SELECT nameImage FROM `blog` WHERE primaryKey = {id};")
        img = cursor.fetchone()[0]

        return img

    except mysql.connector.Error as e:
        print("Error connecting to MySQLTT: ", e)


def takeAllImg():
    try:
        conn = mysql.connector.connect(user='root', password='root',
                                       host='localhost',
                                       port=3308,  # change to the port number used by MAMP
                                       database='test')

        cursor = conn.cursor()
        cursor.execute(f"SELECT nameImage,primaryKey FROM `blog`")
        allImg = cursor.fetchall()

        newList = {}
        

        return newList

    except mysql.connector.Error as e:
        print("Error connecting to MySQL: ", e)


def checkData(title, data, teg):
    check = False
    for symbol in title:
        if (not symbol.isalpha() and not symbol.isdigit()):
            check = True

    return check


def clearTegs(tegs):
    import re
    newtegs = tegs.replace(" ", '')

    return re.sub(',+', ",", newtegs)
