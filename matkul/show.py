import mysql.connector

def lihat():
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="matakuliah"
    )

    mycursor = mysb.cursor(buffered=True)

    sql = "SELECT * FROM pemograman_web"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    mycursor.close()
    mysb.close()

    # print(myresult)

    for value in myresult:
        print(value)