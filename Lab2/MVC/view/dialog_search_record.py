import tkinter as tk
from tkinter import ttk

class SearchRecordDialog(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Search Records")
        self.geometry("800x600")

        # Поля для ввода критериев поиска
        self.criteria_label = ttk.Label(self, text="Enter search criteria:")
        self.criteria_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.fio_label = ttk.Label(self, text="ФИО:")
        self.fio_label.grid(row=1, column=0, sticky="w", padx=10)
        self.fio_entry = ttk.Entry(self)
        self.fio_entry.grid(row=1, column=1, padx=10)

        self.sport_type_label = ttk.Label(self, text="Вид спорта:")
        self.sport_type_label.grid(row=2, column=0, sticky="w", padx=10)
        self.sport_type_entry = ttk.Entry(self)
        self.sport_type_entry.grid(row=2, column=1, padx=10)

        # Кнопка поиска
        self.search_button = ttk.Button(self, text="Search", command=self.search_records)
        self.search_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Таблица для отображения результатов
        self.results_tree = ttk.Treeview(self)
        self.results_tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.results_tree["columns"] = ("fio", "composition", "position", "titles", "sport_type", "rank")
        self.results_tree.heading("#0", text="ID")
        self.results_tree.heading("fio", text="ФИО")
        self.results_tree.heading("composition", text="Состав")
        self.results_tree.heading("position", text="Позиция")
        self.results_tree.heading("titles", text="Титулы")
        self.results_tree.heading("sport_type", text="Вид спорта")
        self.results_tree.heading("rank", text="Разряд")

        # Центрирование данных в столбцах
        self.results_tree.column("#0", anchor='center', width=50)
        self.results_tree.column("fio", anchor='center', width=150)
        self.results_tree.column("composition", anchor='center', width=100)
        self.results_tree.column("position", anchor='center', width=100)
        self.results_tree.column("titles", anchor='center', width=50)
        self.results_tree.column("sport_type", anchor='center', width=100)
        self.results_tree.column("rank", anchor='center', width=100)

    def search_records(self):
        # Получение критериев из полей ввода
        fio = self.fio_entry.get()
        sport_type = self.sport_type_entry.get()

        # Передача критериев в контроллер
        results = self.controller.search_records(fio=fio, sport_type=sport_type)

        # Очистка таблицы перед выводом новых результатов
        self.results_tree.delete(*self.results_tree.get_children())

        # Отображение результатов
        for idx, record in enumerate(results, start=1):
            self.results_tree.insert("", "end", text=idx, values=(
                record.fio, record.composition, record.position, record.titles, record.sport_type, record.rank))