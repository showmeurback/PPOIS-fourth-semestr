import tkinter as tk
from tkinter import ttk
from MVC.model.record import Record

class AddRecordDialog(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Add Record")
        self.geometry("400x300")

        self.fio_label = ttk.Label(self, text="ФИО:")
        self.fio_label.grid(row=0, column=0)
        self.fio_entry = ttk.Entry(self)
        self.fio_entry.grid(row=0, column=1)

        self.composition_label = ttk.Label(self, text="Состав:")
        self.composition_label.grid(row=1, column=0)
        self.composition_entry = ttk.Entry(self)
        self.composition_entry.grid(row=1, column=1)

        self.position_label = ttk.Label(self, text="Позиция:")
        self.position_label.grid(row=2, column=0)
        self.position_entry = ttk.Entry(self)
        self.position_entry.grid(row=2, column=1)

        self.titles_label = ttk.Label(self, text="Титулы:")
        self.titles_label.grid(row=3, column=0)
        self.titles_entry = ttk.Entry(self)
        self.titles_entry.grid(row=3, column=1)

        self.sport_type_label = ttk.Label(self, text="Вид спорта:")
        self.sport_type_label.grid(row=4, column=0)
        self.sport_type_entry = ttk.Entry(self)
        self.sport_type_entry.grid(row=4, column=1)

        self.rank_label = ttk.Label(self, text="Разряд:")
        self.rank_label.grid(row=5, column=0)
        self.rank_entry = ttk.Entry(self)
        self.rank_entry.grid(row=5, column=1)

        self.submit_button = ttk.Button(self, text="Submit", command=self.submit)
        self.submit_button.grid(row=6, column=0, columnspan=2)

    def submit(self):
        fio = self.fio_entry.get()
        composition = self.composition_entry.get()
        position = self.position_entry.get()
        titles = int(self.titles_entry.get())
        sport_type = self.sport_type_entry.get()
        rank = self.rank_entry.get()
        record = Record(fio, composition, position, titles, sport_type, rank)
        self.controller.add_record(record)
        self.destroy()