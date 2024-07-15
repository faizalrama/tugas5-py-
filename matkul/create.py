import mysql.connector

def membuat(nim, nama, nilai):
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="matakuliah"
    )

    mycursor = mysb.cursor()

    sql = "INSERT INTO pemograman_web (nim, nama, nilai) VALUES (%s, %s, %s)"
    val = (nim, nama, nilai)
    mycursor.execute(sql, val)

    mysb.commit()

    print(mycursor.rowcount, "membuat.")

    mycursor.close()
    mysb.close()