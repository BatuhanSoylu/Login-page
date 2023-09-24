import sqlite3

data = sqlite3.connect("loginPage.db")
cursor = data.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS personals(Username TEXT,Email TEXT,Password TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS personalCodes(Username TEXT,Code TEXT)")
#data.commit()


def createrandomcode(username):
    import random
    dictionary=[0,1,2,3,4,5,6,7,8,9,"q","w","e","r","t","y","u","ı","o","p","a","s","d","f"
    "g","h","j","k","l","ş","i","z","x","c","v","b","n","m","ç","Q",
    "W","E","R","T","Y","U","I","O","P","Ğ","A","S","D","F","G","H","J","K","L","Ş","Z","X","C","V",
    "B","N","M"]
    letter=[]
    for i in range(8):
        number=random.randint(0,65)
        letter.append(dictionary[number])
    code=("{}{}{}{}{}{}{}{}").format(letter[0],letter[1],letter[2],letter[3],letter[4],letter[5],letter[6],letter[7])
    cursor.execute("INSERT INTO personalCodes(Username,Code) VALUES(?,?)",(username,code))
    data.commit()
    return code

def getdata(username):
    from Networking.tutuorial.send_email import send_email
    cursor.execute("SELECT * FROM personals WHERE Username=?", (username,))
    dataPersonal = cursor.fetchall()
    data2 = []
    for i in dataPersonal:
        for j in i:
            data2.append(j)
    #-------------create code
    import random
    dictionary=[0,1,2,3,4,5,6,7,8,9,"q","w","e","r","t","y","u","ı","o","p","a","s","d","f"
    "g","h","j","k","l","ş","i","z","x","c","v","b","n","m","ç","Q",
    "W","E","R","T","Y","U","I","O","P","Ğ","A","S","D","F","G","H","J","K","L","Ş","Z","X","C","V",
    "B","N","M"]
    letter=[]
    for i in range(8):
        number=random.randint(0,65)
        letter.append(dictionary[number])
    code=("{}{}{}{}{}{}{}{}").format(letter[0],letter[1],letter[2],letter[3],letter[4],letter[5],letter[6],letter[7])
    cursor.execute("INSERT INTO personalCodes(Username,Code) VALUES(?,?)",(username,code))
    data.commit()
    send_email(code,data2[1])


def registerf(username,email,password,password_check):
    if password==password_check:
        print(username, email, password)
        cursor.execute("INSERT INTO personals(Username,Email,Password) VALUES(?,?,?)", (username, email, password))
        data.commit()
        data.close()
    else:
        print("Password not equal.Try again...")

    data.commit()

def check_code_And_Update_Password(codeAPP,newPassword,newPasswordCheck,username):
    cursor.execute("SELECT * FROM personalCodes")
    data_check=cursor.fetchall()
    last_data=[]
    for i in data_check[-1]:
        last_data.append(i)
    codeDb=last_data[1]
    if codeAPP==codeDb:
        print("hello")
        if newPassword==newPasswordCheck:
            print(1)
            cursor.execute("UPDATE personals SET Password = ? WHERE Username = ?",(newPassword, username))
            print(2)
        else:
            print("passwords not equal.")
    else:
        print("try again.")
    data.commit()
def loginPage_check(username,password):
    cursor.execute("SELECT * FROM personals WHERE Username= ?",(username,))
    data=cursor.fetchall()
    data_perso=[]
    for i in data:
        for j in i:
            data_perso.append(j)
    print(data_perso)
    if username==data_perso[0] and password==data_perso[2]:
        r=1
    else:
        r=2
    return r



