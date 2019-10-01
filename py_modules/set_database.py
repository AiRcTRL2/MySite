import mysql.connector
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


def send_to_db(query,  multi_result=False, vals=None):
    # this function opens a database query for a connection
    # build engine for database
    db_engine = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Apples123",
        database="mysite-games",
    )

    # Initiate the cursor
    cursor = db_engine.cursor()
    # row = None
    # rows = None

    try:
        if vals:
            # insert queries require vals
            cursor.execute(query, vals)
            db_engine.commit()
            print("Record inserted successfully into python_users table")
        else:
            # select queries don't require vals
            cursor.execute(query)
            if multi_result:
                rows = cursor.fetchall()
                return rows
            else:
                row = cursor.fetchone()
                return row

    except mysql.connector.Error as error:
        print(error)

    finally:
        if db_engine.is_connected():
            cursor.close()
            db_engine.close()
            print("MySQL connection is closed")
            db_engine.disconnect()