from ketnoidb.ketnoi_mysql import connect_mysql

def update_danhmuc(ma: int, ten: str, mota: str | None = None) -> bool:
    conn = connect_mysql()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute(
            "UPDATE danhmuc SET TenDanhMuc=%s, MoTa=%s WHERE MaDanhMuc=%s",
            (ten, mota, ma),
        )
        conn.commit()
        print(f"Update DanhMuc ID={ma}, rows={cur.rowcount}")
        return cur.rowcount > 0
    except Exception as e:
        conn.rollback()
        print("Lỗi update danhmuc:", e)
        return False
    finally:
        cur.close(); conn.close()
