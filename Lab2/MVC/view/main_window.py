import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

class MainWindow(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Sport Records Manager")
        self.geometry("800x600")

        # Меню
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Add Record", command=self.controller.show_add_dialog)
        self.file_menu.add_command(label="Search Record", command=self.controller.show_search_dialog)
        self.file_menu.add_command(label="Delete Record", command=self.controller.show_delete_dialog)
        self.file_menu.add_command(label="Tree View", command=self.controller.show_tree_view)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)

        # Панель инструментов
        self.tool_bar = ttk.Frame(self)
        self.tool_bar.pack(side=tk.TOP, fill=tk.X)

        self.add_button = ttk.Button(self.tool_bar, text="Add Record", command=self.controller.show_add_dialog)
        self.add_button.pack(side=tk.LEFT)

        self.search_button = ttk.Button(self.tool_bar, text="Search Record", command=self.controller.show_search_dialog)
        self.search_button.pack(side=tk.LEFT)

        self.delete_button = ttk.Button(self.tool_bar, text="Delete Record", command=self.controller.show_delete_dialog)
        self.delete_button.pack(side=tk.LEFT)

        self.tree_view_button = ttk.Button(self.tool_bar, text="Tree View", command=self.controller.show_tree_view)
        self.tree_view_button.pack(side=tk.LEFT)

        # Новая кнопка "Load from XML"
        self.load_xml_button = ttk.Button(self.tool_bar, text="Load from XML", command=self.controller.load_from_xml)
        self.load_xml_button.pack(side=tk.LEFT)

        # Таблица для отображения записей
        self.records_tree = ttk.Treeview(self)
        self.records_tree.pack(fill=tk.BOTH, expand=True)
        self.records_tree["columns"] = ("fio", "composition", "position", "titles", "sport_type", "rank")
        self.records_tree.heading("#0", text="ID")
        self.records_tree.heading("fio", text="ФИО")
        self.records_tree.heading("composition", text="Состав")
        self.records_tree.heading("position", text="Позиция")
        self.records_tree.heading("titles", text="Титулы")
        self.records_tree.heading("sport_type", text="Вид спорта")
        self.records_tree.heading("rank", text="Разряд")

        # Центрирование данных в столбцах
        self.records_tree.column("#0", anchor='center', width=50)
        self.records_tree.column("fio", anchor='center', width=150)
        self.records_tree.column("composition", anchor='center', width=100)
        self.records_tree.column("position", anchor='center', width=100)
        self.records_tree.column("titles", anchor='center', width=50)
        self.records_tree.column("sport_type", anchor='center', width=100)
        self.records_tree.column("rank", anchor='center', width=100)

        # Панель пагинации
        self.pagination_frame = ttk.Frame(self)
        self.pagination_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.records_per_page_label = ttk.Label(self.pagination_frame, text="Records per page:")
        self.records_per_page_label.pack(side=tk.LEFT, padx=5)

        self.records_per_page_entry = ttk.Entry(self.pagination_frame, width=5)
        self.records_per_page_entry.insert(0, "10")
        self.records_per_page_entry.pack(side=tk.LEFT, padx=5)

        self.set_records_button = ttk.Button(self.pagination_frame, text="Set", command=self.set_records_per_page)
        self.set_records_button.pack(side=tk.LEFT, padx=5)

        self.pagination_info_label = ttk.Label(self.pagination_frame, text="")
        self.pagination_info_label.pack(side=tk.LEFT, padx=10)

        self.first_page_button = ttk.Button(self.pagination_frame, text="<<", command=self.go_to_first_page)
        self.first_page_button.pack(side=tk.LEFT, padx=5)

        self.previous_page_button = ttk.Button(self.pagination_frame, text="<", command=self.go_to_previous_page)
        self.previous_page_button.pack(side=tk.LEFT, padx=5)

        self.next_page_button = ttk.Button(self.pagination_frame, text=">", command=self.go_to_next_page)
        self.next_page_button.pack(side=tk.LEFT, padx=5)

        self.last_page_button = ttk.Button(self.pagination_frame, text=">>", command=self.go_to_last_page)
        self.last_page_button.pack(side=tk.LEFT, padx=5)

    def update_records(self, records):
        self.records_tree.delete(*self.records_tree.get_children())
        for idx, record in enumerate(records, start=1):
            self.records_tree.insert("", "end", text=idx, values=(
                record.fio, record.composition, record.position, record.titles, record.sport_type, record.rank))

    def update_pagination_info(self, current_page, total_pages, total_records):
        self.pagination_info_label.config(
            text=f"Page {current_page} of {total_pages} | Total records: {total_records}"
        )

    def set_records_per_page(self):
        try:
            records_per_page = int(self.records_per_page_entry.get())
            if records_per_page > 0:
                self.controller.set_records_per_page(records_per_page)
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid number.")

    def go_to_first_page(self):
        self.controller.go_to_first_page()

    def go_to_last_page(self):
        self.controller.go_to_last_page()

    def go_to_next_page(self):
        self.controller.go_to_next_page()

    def go_to_previous_page(self):
        self.controller.go_to_previous_page()