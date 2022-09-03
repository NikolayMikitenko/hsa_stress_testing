from fastapi import FastAPI
import psycopg2
import uuid
import random
import string

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/generate_user")
async def generate_user():
    query = '''INSERT INTO public.users (id, age, "name") VALUES (%s,%s,%s)'''
    data = (str(uuid.uuid4()), random.randint(0, 100), ''.join(random.choices(string.ascii_uppercase, k=30)))
    print(data)
    message = set_db_data(query, data)
    return {"message": message}

@app.get("/generate_page")
async def generate_user():
    query = '''INSERT INTO public.pages (id, "path", title) VALUES (%s,%s,%s)'''
    data = (str(uuid.uuid4()), ''.join(random.choices(string.ascii_uppercase, k=20)), ''.join(random.choices(string.ascii_uppercase, k=50)))
    message = set_db_data(query, data)
    return {"message": message}

@app.post("/generate_number")
async def generate_user():
    #query = '''INSERT INTO public.numbers (id, value) VALUES (%s,%s)'''
    #data = (, str(random.randint(0, 1000000)))
    query = f"INSERT INTO public.numbers (id, value) VALUES ('{str(uuid.uuid4())}', {random.randint(0, 1000000)})"
    message = set_db_data(query)
    return {"message": message}

def set_db_data(query, data=None):
    data = (str(uuid.uuid4()), random.randint(0, 100), ''.join(random.choices(string.ascii_uppercase, k=30)))    
    try:
        conn = psycopg2.connect(
            host="postgres",
            #host="localhost",
            port="5432",
            database="db",
            user="postgres",
            password="postgres")
        print("PostgreSQL connection is open")

        cur = conn.cursor()

        if data is not None:
            cur.execute(query, data)
        else:
            cur.execute(query)
        conn.commit()

        count = cur.rowcount
        print(f"Inserted successfully {count} rows")
        message = f"Data {data} inserted successfully"
        return message

    except (Exception, psycopg2.Error) as error:
        print(error)
        message = "Failed to insert data {data} with error: {error}"
    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")