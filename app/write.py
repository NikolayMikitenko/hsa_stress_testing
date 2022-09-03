import psycopg2



conn = None
try:

    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(
        host="postgres",
        #host="localhost",
        port="5432",
        database="db",
        user="postgres",
        password="postgres")
		
    # create a cursor
    cur = conn.cursor()
        
	# execute a statement
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')

    # display the PostgreSQL database server version
    db_version = cur.fetchone()
    print(db_version)
       
	# close the communication with the PostgreSQL
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')







# import psycopg2

# try:
#     connection = psycopg2.connect(user="sysadmin",
#                                   password="pynative@#29",
#                                   host="127.0.0.1",
#                                   port="5432",
#                                   database="postgres_db")
#     cursor = connection.cursor()

#     postgres_insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (%s,%s,%s)"""
#     record_to_insert = (5, 'One Plus 6', 950)
#     cursor.execute(postgres_insert_query, record_to_insert)

#     connection.commit()
#     count = cursor.rowcount
#     print(count, "Record inserted successfully into mobile table")

# except (Exception, psycopg2.Error) as error:
#     print("Failed to insert record into mobile table", error)

# finally:
#     # closing database connection.
#     if connection:
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")        