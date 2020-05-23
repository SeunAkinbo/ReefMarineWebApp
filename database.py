import mysql.connector


def connect_db(user, password, host, database):
    conn = mysql.connector.connect(user=user,
                                   password=password,
                                   host=host,
                                   database=database,
                                   auth_plugin='mysql_native_password')
    return conn


# Contact Table to store the hashed password
def create_password_table(db, table_name):
    try:
        conn = connect_db('root', 'password', '127.0.0.1', 'contact')
        cursor = conn.cursor()

        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {db}.{table_name}(
            id SERIAL NOT NULL,
            head_password VARCHAR(5) NOT NULL,
            tail_password VARCHAR(35) NOT NULL)""")

    except Exception as err:
        print(f'The connection returned the following error: {err}')


# Updates password table with hased password
def update_password_table(db, table_name, password_list):
    try:
        conn = connect_db('root', 'password', '127.0.0.1', db)
        cursor = conn.cursor()

        query = f"""INSERT INTO {db}.{table_name}(head_password, tail_password) VALUES(%s,%s)"""

        cursor.execute(query, password_list)
        conn.commit()

    except Exception as err:
        return f'The connection returned the following error: {err}'

    finally:
        conn.close()


# Contact Table to store the contact
def create_contact_table(db, table_name):
    try:
        conn = connect_db('root', 'password', '127.0.0.1', db)
        cursor = conn.cursor()

        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {db}.{table_name}(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    category VARCHAR(20),
                    priority VARCHAR(7),
                    copy VARCHAR(3),
                    human VARCHAR(3),
                    message VARCHAR(300) NOT NULL)""")

    except Exception as err:
        return f'The connection returned the following error: {err}'


# Updates contact table with user data
def update_contact_table(db, table_name, data):
    try:
        conn = connect_db('root', 'password', '127.0.0.1', db)
        cursor = conn.cursor()

        query = f"""INSERT INTO {db}.{table_name}(name, email, category, priority, copy, human, message)
                VALUES(%s,%s,%s,%s,%s,%s,%s)"""
        table_values = (data['name'], data['email'], data['category'], data['priority'],
                        data['copy'], data['human'], data['message'])

        cursor.execute(query, table_values)

        conn.commit()

    except Exception as err:
        return f'The connection returned the following error: {err}'

    finally:
        conn.close()


# Registration table to store the registrant
def create_reg_table(db, table_name):
    try:
        conn = connect_db('root', 'password', '127.0.0.1', 'contact')
        cursor = conn.cursor()

        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {db}.{table_name}(
                    id SERIAL PRIMARY KEY,
                    company_name VARCHAR(20) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    category VARCHAR(20) NOT NULL,
                    password VARCHAR(30) NOT NULL,
                    rc_num VARCHAR(10) NOT NULL)""")

    except Exception as err:
        return f'The connection returned the following error: {err}'


# Updates registeration table with user data
def update_reg_table(db, table_name, data):
    try:
        conn = connect_db('root', 'password', '127.0.0.1', db)
        cursor = conn.cursor()

        query = f"""INSERT INTO {db}.{table_name}(company_name, email, category, password, rc_num) VALUES(%s,%s,%s,%s,%s)"""
        table_values = (data['company_name'], data['email'],
                        data['category'], data['password'], data['rc_num'])

        cursor.execute(query, table_values)
        conn.commit()

    except Exception as err:
        return f'The connection returned the following error: {err}'

    finally:
        conn.close()
