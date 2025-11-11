from ketnoidb.ketnoi_mysql import connect_mysql

def insert_danhmuc(ten: str, mota: str | None = None) -> int | None:
    conn = connect_mysql()
    if not conn:
        return None
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO danhmuc (TenDanhMuc, MoTa) VALUES (%s, %s)",
            (ten, mota),
        )
        conn.commit()
        print("Thêm danh mục OK, id =", cur.lastrowid)
        return cur.lastrowid
    except Exception as e:
        conn.rollback()
        print("Lỗi insert danhmuc:", e)
        return None
    finally:
        cur.close(); conn.close()
