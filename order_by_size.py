import psycopg2


def order_by_size():
    try:
        connection = psycopg2.connect(
            user="test",
            password="test",
            host="localhost",
            port="5432",
            database="test"
        )
        cursor = connection.cursor()

        pg_order_by_size = """ SELECT * FROM public."h3" ORDER BY "size" """

        cursor.execute(pg_order_by_size)

        h1_records = cursor.fetchall()
        print("Sorted by size")
        for row in h1_records:
            print (row[0], '- xxxxx')
            print ('price', row[1], '$')
            print ('size', row[2], 'm2\n---')

    except (Exception, psycopg2.Error) as error:
        print("Error selecting data from table h1", error)
        connection = None

    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("The PostgreSQL connection is now closed")