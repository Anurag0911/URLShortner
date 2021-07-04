import sqlite3

def short_url(url):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        query = "INSERT INTO URL (URL) VALUES('{}')".format(url)
        url_entry = cur.execute(query)
        conn.commit()
        a = url_entry.lastrowid
        return a

def original_url(id):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        query = "SELECT URL FROM URL WHERE ID='{}'".format(id) 
        cur.execute(query)
        a = cur.fetchall()
        org_url = a[0][0]
        return org_url
        