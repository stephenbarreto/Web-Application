from django.db import connection

def drop_all_tables():
    with connection.cursor() as cursor:
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_type = 'BASE TABLE';")
        tables = cursor.fetchall()
        
        for table in tables:
            table_name = table[0]
            cursor.execute(f"DROP TABLE {table_name} CASCADE;")
        connection.commit()

drop_all_tables()

# copie todo esse código, execute o comando `python3 manage.py shell`, cole o 
# código no shell e execute.
