from ketnoidb.ketnoi_mysql import connect_mysql

conn = connect_mysql()
if conn:
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    print(cur.fetchone())
    cur.close()
    conn.close()
