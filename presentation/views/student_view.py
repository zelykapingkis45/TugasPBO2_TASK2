import tkinter as tk
from tkinter import ttk, messagebox


class StudentView(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sistem Informasi Mahasiswa - Clean Architecture MVC")
        self.geometry("750x450")

        self.controller = None
        self._build_ui()

    def set_controller(self, controller):
        self.controller = controller

    def _build_ui(self):
        # Form Frame
        form_frame = ttk.LabelFrame(
            self,
            text=" Form Data Mahasiswa ",
            padding=10
        )
        form_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(form_frame, text="NIM:").grid(
            row=0, column=0, sticky="w", pady=2
        )

        self.ent_nim = ttk.Entry(form_frame, width=25)
        self.ent_nim.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(form_frame, text="Nama:").grid(
            row=0, column=2, sticky="w", pady=2
        )

        self.ent_nama = ttk.Entry(form_frame, width=30)
        self.ent_nama.grid(row=0, column=3, padx=5, pady=2)

        ttk.Label(form_frame, text="Prodi:").grid(
            row=1, column=0, sticky="w", pady=2
        )

        self.ent_prodi = ttk.Entry(form_frame, width=25)
        self.ent_prodi.grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(form_frame, text="Angkatan:").grid(
            row=1, column=2, sticky="w", pady=2
        )

        self.ent_angkatan = ttk.Entry(form_frame, width=15)
        self.ent_angkatan.grid(
            row=1, column=3, sticky="w", padx=5, pady=2
        )

        # Button Frame
        btn_frame = ttk.Frame(self, padding=5)
        btn_frame.pack(fill="x", padx=10)

        ttk.Button(
            btn_frame,
            text="Tambah",
            command=lambda: self.controller.add_student()
        ).pack(side="left", padx=5)

        ttk.Button(
            btn_frame,
            text="Update",
            command=lambda: self.controller.update_student()
        ).pack(side="left", padx=5)

        ttk.Button(
            btn_frame,
            text="Hapus",
            command=lambda: self.controller.delete_student()
        ).pack(side="left", padx=5)

        ttk.Button(
            btn_frame,
            text="Reset",
            command=self.clear_inputs
        ).pack(side="left", padx=5)

        # Table Frame
        table_frame = ttk.Frame(self, padding=10)
        table_frame.pack(fill="both", expand=True)

        columns = ("nim", "nama", "prodi", "angkatan")

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        self.tree.heading("nim", text="NIM")
        self.tree.heading("nama", text="Nama Mahasiswa")
        self.tree.heading("prodi", text="Program Studi")
        self.tree.heading("angkatan", text="Angkatan")

        self.tree.column("nim", width=120)
        self.tree.column("nama", width=250)
        self.tree.column("prodi", width=200)
        self.tree.column("angkatan", width=80, anchor="center")

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.tree.bind("<<TreeviewSelect>>", self._on_row_select)

    def _on_row_select(self, event):
        selected = self.tree.focus()

        if selected:
            values = self.tree.item(selected, "values")

            if values:
                self.set_inputs(
                    values[0],
                    values[1],
                    values[2],
                    values[3]
                )

    def get_inputs(self):
        return (
            self.ent_nim.get().strip(),
            self.ent_nama.get().strip(),
            self.ent_prodi.get().strip(),
            self.ent_angkatan.get().strip()
        )

    def set_inputs(self, nim, nama, prodi, angkatan):
        self.ent_nim.delete(0, tk.END)
        self.ent_nim.insert(0, nim)

        self.ent_nama.delete(0, tk.END)
        self.ent_nama.insert(0, nama)

        self.ent_prodi.delete(0, tk.END)
        self.ent_prodi.insert(0, prodi)

        self.ent_angkatan.delete(0, tk.END)
        self.ent_angkatan.insert(0, angkatan)

    def clear_inputs(self):
        self.set_inputs("", "", "", "")

    def display_students(self, students):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for mhs in students:
            self.tree.insert(
                "",
                tk.END,
                values=(
                    mhs.nim,
                    mhs.nama,
                    mhs.prodi,
                    mhs.angkatan
                )
            )

    def show_info(self, title, message):
        messagebox.showinfo(title, message)

    def show_error(self, title, message):
        messagebox.showerror(title, message)