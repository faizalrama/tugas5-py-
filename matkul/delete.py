import mysql.connector

def delete_record(nim):
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="matakuliah"
    )

    mycursor = mysb.cursor()

    sql = "DELETE FROM pemograman_web WHERE nim = %s"
    val = (nim,)
    mycursor.execute(sql, val)

    mysb.commit()

    print(mycursor.rowcount, "record(s) deleted")

    mycursor.close()
    mysb.close()