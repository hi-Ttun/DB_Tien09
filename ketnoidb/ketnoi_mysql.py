import mysql.connector as mc

def connect_mysql():
    try:
        conn = mc.connect(
            host="localhost",
            user="root",
            password="Tun13@vn",
            database="qlthuocankhang"
        )
        if conn.is_connected():
            print("Kết nối MySQL thành công!")
            return conn
    except mc.Error as e:
        print("Lỗi khi kết nối MySQL:", e)
        return None
