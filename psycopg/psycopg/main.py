import psycopg
from psycopg.rows import dict_row

# Connect to an existing database
with psycopg.connect("dbname=db_name user=postgres password=postgres host=localhost port=5432") as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        # Execute a command: this creates a new table
        cur.execute("""
                    CREATE TABLE project_members (
                        id serial PRIMARY KEY,
                        project_id integer NOT NULL,
                        user_id integer NOT NULL,
                    );
                    """)

        cur.execute("""
            SELECT * FROM project_members;
            """)
        # to return a list of all records in tuple format
        # res = cur.fetchall()

        # to return a list of records in JSON format
        # res = cur.fetchmany_as_json(size=2)

        # to return a single record in JSON format
        res = cur.fetchone_as_json()
        print(res)

        conn.commit()