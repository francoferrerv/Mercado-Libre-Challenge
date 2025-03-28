#Python 3.13.2
from getpass import getpass
from mysql.connector import connect, Error

try: 
    with connect(
        host="localhost",
        user="root",
        password=getpass("Enter password: "),
        database="challenge"
    ) as connection:
        print("Connected successfully!")


        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS challenge;")

        create_tables_queries = [
            """CREATE TABLE IF NOT EXISTS customers (
                id SMALLINT NOT NULL PRIMARY KEY,
                first_name VARCHAR(64),
                last_name VARCHAR(64)
            )""",
            """CREATE TABLE IF NOT EXISTS campaigns (
                id SMALLINT NOT NULL PRIMARY KEY,
                customer_id SMALLINT,
                name VARCHAR(64)
            )""",
            """CREATE TABLE IF NOT EXISTS events (
                dt VARCHAR(19) NOT NULL,
                campaign_id SMALLINT,
                status VARCHAR(64)
            )"""
        ]

        with connection.cursor() as cursor:
            for query in create_tables_queries:
                cursor.execute(query)
            connection.commit()
            print("Tables created successfully!")

        insert_queries = [
            """INSERT INTO customers (id, first_name, last_name) VALUES 
               (1, 'Whitney', 'Ferrero'), (2, 'Dickie', 'Romera')
            """,
            """INSERT INTO campaigns (id, customer_id, name) VALUES 
               (1, 1, 'Upton Group'), (2, 1, 'Roob, Hudson and Rippin'), 
               (3, 1, 'McCullough, Rempel and Larson'), (4, 1, 'Lang and Sons'), 
               (5, 2, 'Ruecker, Hand and Haley')
            """,
            """ INSERT INTO `challenge`.`events` (`dt`, `campaign_id`, `status`) VALUES 
                ('2021-12-02 13:52:00', 1, 'failure'),
                ('2021-12-02 08:17:48', 2, 'failure'),
                ('2021-12-02 08:18:17', 2, 'failure'),
                ('2021-12-01 11:55:32', 3, 'failure'),
                ('2021-12-01 06:53:16', 4, 'failure'),
                ('2021-12-02 04:51:09', 4, 'failure'),
                ('2021-12-01 06:34:04', 5, 'failure'),
                ('2021-12-02 03:21:18', 5, 'failure'),
                ('2021-12-01 03:18:24', 5, 'failure'),
                ('2021-12-02 15:32:37', 1, 'success'),
                ('2021-12-01 04:23:20', 1, 'success'),
                ('2021-12-02 06:53:24', 1, 'success'),
                ('2021-12-02 08:01:02', 2, 'success'),
                ('2021-12-01 15:57:19', 2, 'success'),
                ('2021-12-02 16:14:34', 3, 'success'),
                ('2021-12-02 21:56:38', 3, 'success'),
                ('2021-12-01 05:54:43', 4, 'success'),
                ('2021-12-02 17:56:45', 4, 'success'),
                ('2021-12-02 11:56:50', 4, 'success'),
                ('2021-12-02 06:08:20', 5, 'success');
            """
        ]

        with connection.cursor() as cursor:
            for query in insert_queries:
                cursor.execute(query)
            connection.commit()
            print("Data inserted successfully!")

        select_customers_failures_query = """SELECT CONCAT(cu.first_name, ' ', cu.last_name) AS customer, count(*) AS failures 
                                                FROM customers cu, campaigns ca, events ev
                                                WHERE cu.id = ca.customer_id 
                                                AND ca.id = ev.campaign_id
                                                AND ev.status = 'failure'
                                                GROUP BY customer
                                                ORDER BY failures DESC LIMIT 1 
                                            """
        with connection.cursor() as cursor:
            cursor.execute(select_customers_failures_query)
            result = cursor.fetchall()
            for row in result:
                print(row)


except Error as e:
    print(f"Error: {e}")
