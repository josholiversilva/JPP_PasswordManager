import sqlite3
import pandas as pd
import sqlparse
import cryptography_functions as crypto

conn = sqlite3.connect('password_manager.sql')
c = conn.cursor()
#c.execute('''CREATE TABLE josh_passwords
#             (password text, app text, created text, updated text)''')

def check_inputs(master_user, app, password):
    # If password in database for same app, then mention it to user
    c.execute("SELECT app,password FROM {} WHERE app='{}'".format(master_user, app))
    data = c.fetchall()

    if data:
        decrypted_pass = crypto.decrypt(data[0][1])

        if password == decrypted_pass:
            return 'Equal'
        else:
            return 'Update'
    
    return

def add_row(master_user, app, password, created, updated):
    encrypted_pass = crypto.encrypt(password)
    c.execute("INSERT INTO {} VALUES ('{}','{}','{}','{}')".format(master_user,app,encrypted_pass,created,updated))
    conn.commit()
    return

def update_password(app,password,updated):
    encrypted_pass = crypto.encrypt(password)
    c.execute("UPDATE josilva SET password='{}', updated='{}' WHERE app='{}'".format(encrypted_pass,updated,app))
    return '\n---\nUpdated!!!\n---\n'

def delete_password(master_user, app, password):
    encrypted_pass = crypto.encrypt(password)
    c.execute("DELETE FROM {} WHERE app={} and password={}".format(master_user, app, password))
    conn.commit()
    return '\n---\nDeleted Password from App: {}\n---\n'.format(app)

def show_table(master_user):
    return pd.read_sql_query("SELECT * FROM {}".format(master_user), conn)

def show_password(master_user, app):
    c.execute("SELECT app,password FROM {} WHERE app='{}'".format(master_user,app))
    data = c.fetchall()

    decrypted_pass = crypto.decrypt(data[0][1])
    
    return decrypted_pass