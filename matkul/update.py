import mysql.connector

def update_record(nim,  nama, nilai ):
    try:
        mysb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="matakuliah"
        )

        mycursor = mysb.cursor()

        sql = "UPDATE pemograman_web SET nim = %s, nama = %s, nilai = %s WHERE nim = %s"
        val = (nim, nama, nilai, nim)
        print("Executing SQL:", sql % val)  # Debug statement
        mycursor.execute(sql, val)

        mysb.commit()

        print(mycursor.rowcount, "record(s) affected")

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        mycursor.close()
        mysb.close()
