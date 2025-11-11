from ketnoidb.ketnoi_mysql import connect_mysql

def delete_danhmuc(ma: int) -> bool:
    conn = connect_mysql()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM danhmuc WHERE MaDanhMuc=%s", (ma,))
        conn.commit()
        print(f"🗑Xoá DanhMuc ID={ma}, rows={cur.rowcount}")
        return cur.rowcount > 0
    except Exception as e:
        conn.rollback()
        print("Lỗi delete danhmuc:", e)
        return False
    finally:
        cur.close(); conn.close()
