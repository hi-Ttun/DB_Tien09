import tkinter as tk
from tkinter import ttk, messagebox
from ketnoidb.ketnoi_mysql import connect_mysql

APP_TITLE = "Quản lý Danh Mục"

class DanhMucApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry("800x500")
        self.minsize(760, 480)

        # ====== Khung nhập liệu ======
        frm_form = ttk.LabelFrame(self, text="Thông tin danh mục", padding=10)
        frm_form.pack(fill="x", padx=10, pady=(10, 5))

        ttk.Label(frm_form, text="Mã danh mục:").grid(row=0, column=0, sticky="w", padx=(0, 8), pady=4)
        self.var_id = tk.StringVar()
        ent_id = ttk.Entry(frm_form, textvariable=self.var_id, state="readonly", width=12)
        ent_id.grid(row=0, column=1, sticky="w", pady=4)

        ttk.Label(frm_form, text="Tên danh mục:").grid(row=0, column=2, sticky="w", padx=(16, 8), pady=4)
        self.var_ten = tk.StringVar()
        ent_ten = ttk.Entry(frm_form, textvariable=self.var_ten, width=40)
        ent_ten.grid(row=0, column=3, sticky="w", pady=4)

        ttk.Label(frm_form, text="Mô tả:").grid(row=1, column=0, sticky="nw", padx=(0, 8), pady=4)
        self.txt_mota = tk.Text(frm_form, height=3, width=60)
        self.txt_mota.grid(row=1, column=1, columnspan=3, sticky="we", pady=4)

        frm_form.grid_columnconfigure(3, weight=1)

        # ====== Nút tác vụ ======
        frm_btns = ttk.Frame(self)
        frm_btns.pack(fill="x", padx=10, pady=5)

        self.btn_add = ttk.Button(frm_btns, text="➕ Thêm mới", command=self.add_record)
        self.btn_add.pack(side="left", padx=(0, 6))

        self.btn_update = ttk.Button(frm_btns, text="✏️ Sửa", command=self.update_record)
        self.btn_update.pack(side="left", padx=6)

        self.btn_delete = ttk.Button(frm_btns, text="🗑️ Xóa", command=self.delete_record)
        self.btn_delete.pack(side="left", padx=6)

        self.btn_clear = ttk.Button(frm_btns, text="🧹 Xóa form", command=self.clear_form)
        self.btn_clear.pack(side="left", padx=6)

        self.btn_refresh = ttk.Button(frm_btns, text="🔄 Tải lại", command=self.load_data)
        self.btn_refresh.pack(side="left", padx=6)

        # ====== Bảng danh sách ======
        frm_table = ttk.Frame(self)
        frm_table.pack(fill="both", expand=True, padx=10, pady=(5, 10))

        columns = ("MaDanhMuc", "TenDanhMuc", "MoTa")
        self.tbl = ttk.Treeview(frm_table, columns=columns, show="headings", height=12)
        self.tbl.heading("MaDanhMuc", text="Mã")
        self.tbl.heading("TenDanhMuc", text="Tên danh mục")
        self.tbl.heading("MoTa", text="Mô tả")

        self.tbl.column("MaDanhMuc", width=80, anchor="center")
        self.tbl.column("TenDanhMuc", width=220, anchor="w")
        self.tbl.column("MoTa", anchor="w")

        vsb = ttk.Scrollbar(frm_table, orient="vertical", command=self.tbl.yview)
        hsb = ttk.Scrollbar(frm_table, orient="horizontal", command=self.tbl.xview)
        self.tbl.configure(yscroll=vsb.set, xscroll=hsb.set)

        self.tbl.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="we")

        frm_table.grid_rowconfigure(0, weight=1)
        frm_table.grid_columnconfigure(0, weight=1)

        self.tbl.bind("<<TreeviewSelect>>", self.on_select_row)

        # Tải dữ liệu ban đầu
        self.load_data()

    # ----------------- Helpers -----------------
    def _get_conn_cursor(self):
        conn = connect_mysql()
        if not conn:
            raise RuntimeError("Không kết nối được MySQL")
        return conn, conn.cursor()

    def clear_form(self):
        self.var_id.set("")
        self.var_ten.set("")
        self.txt_mota.delete("1.0", "end")
        self.tbl.selection_remove(self.tbl.selection())

    def on_select_row(self, _event=None):
        sel = self.tbl.selection()
        if not sel:
            return
        item = self.tbl.item(sel[0], "values")
        self.var_id.set(item[0])
        self.var_ten.set(item[1])
        self.txt_mota.delete("1.0", "end")
        self.txt_mota.insert("1.0", item[2] or "")

    # ----------------- CRUD -----------------
    def load_data(self):
        # Xóa bảng hiện tại
        for r in self.tbl.get_children():
            self.tbl.delete(r)

        try:
            conn, cur = self._get_conn_cursor()
            cur.execute("SELECT MaDanhMuc, TenDanhMuc, MoTa FROM danhmuc ORDER BY MaDanhMuc;")
            for row in cur.fetchall():
                self.tbl.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không tải được dữ liệu:\n{e}")
        finally:
            try:
                cur.close(); conn.close()
            except Exception:
                pass

    def add_record(self):
        ten = self.var_ten.get().strip()
        mota = self.txt_mota.get("1.0", "end").strip()
        if not ten:
            messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập 'Tên danh mục'.")
            return
        try:
            conn, cur = self._get_conn_cursor()
            cur.execute(
                "INSERT INTO danhmuc (TenDanhMuc, MoTa) VALUES (%s, %s)",
                (ten, mota if mota else None),
            )
            conn.commit()
            new_id = cur.lastrowid
            messagebox.showinfo("Thành công", f"Đã thêm danh mục (ID={new_id}).")
            self.clear_form()
            self.load_data()
        except Exception as e:
            if 'Duplicate' in str(e):
                messagebox.showerror("Lỗi", "Tên danh mục bị trùng.")
            else:
                messagebox.showerror("Lỗi", f"Không thêm được danh mục:\n{e}")
        finally:
            try:
                cur.close(); conn.close()
            except Exception:
                pass

    def update_record(self):
        id_str = self.var_id.get().strip()
        ten = self.var_ten.get().strip()
        mota = self.txt_mota.get("1.0", "end").strip()
        if not id_str:
            messagebox.showwarning("Thiếu dữ liệu", "Vui lòng chọn 1 dòng để sửa.")
            return
        if not ten:
            messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập 'Tên danh mục'.")
            return
        try:
            conn, cur = self._get_conn_cursor()
            cur.execute(
                "UPDATE danhmuc SET TenDanhMuc=%s, MoTa=%s WHERE MaDanhMuc=%s",
                (ten, mota if mota else None, id_str),
            )
            conn.commit()
            if cur.rowcount > 0:
                messagebox.showinfo("Thành công", "Đã cập nhật danh mục.")
            else:
                messagebox.showwarning("Không thay đổi", "Không có dòng nào được cập nhật.")
            self.load_data()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không cập nhật được danh mục:\n{e}")
        finally:
            try:
                cur.close(); conn.close()
            except Exception:
                pass

    def delete_record(self):
        id_str = self.var_id.get().strip()
        if not id_str:
            messagebox.showwarning("Thiếu dữ liệu", "Vui lòng chọn 1 dòng để xóa.")
            return
        if not messagebox.askyesno("Xác nhận", f"Xóa danh mục ID = {id_str}?"):
            return
        try:
            conn, cur = self._get_conn_cursor()
            cur.execute("DELETE FROM danhmuc WHERE MaDanhMuc=%s", (id_str,))
            conn.commit()
            if cur.rowcount > 0:
                messagebox.showinfo("Thành công", "Đã xóa danh mục.")
                self.clear_form()
                self.load_data()
            else:
                messagebox.showwarning("Không thay đổi", "Không có dòng nào bị xóa.")
        except Exception as e:
            # Nếu có ràng buộc khóa ngoại từ bảng khác vào danhmuc:
            if "foreign key" in str(e).lower():
                messagebox.showerror(
                    "Lỗi",
                    "Không thể xóa vì còn sản phẩm tham chiếu danh mục này.\n"
                    "Hãy chuyển sản phẩm sang danh mục khác hoặc xóa sản phẩm trước."
                )
            else:
                messagebox.showerror("Lỗi", f"Không xóa được danh mục:\n{e}")
        finally:
            try:
                cur.close(); conn.close()
            except Exception:
                pass

if __name__ == "__main__":
    DanhMucApp().mainloop()
