from ketnoidb.ketnoi_mysql import connect_mysql

def get_all_danhmuc():
    conn = connect_mysql()
    if not conn: return []
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT MaDanhMuc, TenDanhMuc, MoTa FROM danhmuc ORDER BY MaDanhMuc;")
        return cur.fetchall()
    finally:
        cur.close(); conn.close()

def get_danhmuc_by_id(ma: int):
    conn = connect_mysql()
    if not conn: return None
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT MaDanhMuc, TenDanhMuc, MoTa FROM danhmuc WHERE MaDanhMuc=%s", (ma,))
        return cur.fetchone()
    finally:
        cur.close(); conn.close()
