import tkinter as tk
from tkinter import ttk, messagebox

class DeleteRecordDialog(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Delete Records")
        self.geometry("400x300")

        # Поля для ввода критериев удаления
        self.criteria_label = ttk.Label(self, text="Enter delete criteria:")
        self.criteria_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.fio_label = ttk.Label(self, text="ФИО:")
        self.fio_label.grid(row=1, column=0, sticky="w", padx=10)
        self.fio_entry = ttk.Entry(self)
        self.fio_entry.grid(row=1, column=1, padx=10)

        self.sport_type_label = ttk.Label(self, text="Вид спорта:")
        self.sport_type_label.grid(row=2, column=0, sticky="w", padx=10)
        self.sport_type_entry = ttk.Entry(self)
        self.sport_type_entry.grid(row=2, column=1, padx=10)

        # Кнопка удаления
        self.delete_button = ttk.Button(self, text="Delete", command=self.delete_records)
        self.delete_button.grid(row=3, column=0, columnspan=2, pady=10)

    def delete_records(self):
        # Получение критериев из полей ввода
        fio = self.fio_entry.get()
        sport_type = self.sport_type_entry.get()

        # Вызов метода контроллера для удаления записей
        deleted_count = self.controller.delete_records(fio=fio, sport_type=sport_type)

        # Вывод сообщения пользователю
        if deleted_count > 0:
            messagebox.showinfo("Success", f"Deleted {deleted_count} records.")
        else:
            messagebox.showinfo("Info", "No records found matching the criteria.")