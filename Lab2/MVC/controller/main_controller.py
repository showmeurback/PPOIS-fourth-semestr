from MVC.model.database import Database
from MVC.view.main_window import MainWindow
from MVC.view.dialog_add_record import AddRecordDialog
from MVC.view.dialog_search_record import SearchRecordDialog
from MVC.view.dialog_delete_record import DeleteRecordDialog
from MVC.controller.tree_view_controller import TreeViewController
from MVC.view.tree_view import TreeViewWindow
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from MVC.model.xml_handler import XMLReader


class MainController:
    def __init__(self):
        self.db = Database("records.db")
        self.main_window = MainWindow(self)
        self.records_per_page = 10  # Количество записей на странице
        self.current_page = 1       # Текущая страница
        self.total_records = len(self.db.get_records())  # Общее количество записей
        self.total_pages = (self.total_records + self.records_per_page - 1) // self.records_per_page
        self.update_main_window()

    def update_main_window(self):
        """
        Обновляет данные в главном окне с учетом пагинации.
        """
        records = self.get_paginated_records()
        self.main_window.update_records(records)
        self.main_window.update_pagination_info(
            current_page=self.current_page,
            total_pages=self.total_pages,
            total_records=self.total_records
        )

    def get_paginated_records(self):
        """
        Возвращает записи для текущей страницы.
        """
        offset = (self.current_page - 1) * self.records_per_page
        return self.db.get_records(limit=self.records_per_page, offset=offset)

    def set_records_per_page(self, records_per_page):
        """
        Устанавливает новое количество записей на странице.
        """
        self.records_per_page = records_per_page
        self.total_pages = (self.total_records + self.records_per_page - 1) // self.records_per_page
        self.current_page = 1
        self.update_main_window()

    def go_to_first_page(self):
        """
        Переходит на первую страницу.
        """
        self.current_page = 1
        self.update_main_window()

    def go_to_last_page(self):
        """
        Переходит на последнюю страницу.
        """
        self.current_page = self.total_pages
        self.update_main_window()

    def go_to_next_page(self):
        """
        Переходит на следующую страницу.
        """
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_main_window()

    def go_to_previous_page(self):
        """
        Переходит на предыдущую страницу.
        """
        if self.current_page > 1:
            self.current_page -= 1
            self.update_main_window()

    def show_add_dialog(self):
        """
        Открывает диалог добавления записи.
        """
        AddRecordDialog(self)

    def show_search_dialog(self):
        """
        Открывает диалог поиска записей.
        """
        SearchRecordDialog(self)

    def show_delete_dialog(self):
        """
        Открывает диалог удаления записей.
        """
        DeleteRecordDialog(self)

    def show_tree_view(self):
        """
        Открывает окно древовидного представления.
        """
        tree_controller = TreeViewController(self.db)
        TreeViewWindow(tree_controller)

    def load_from_xml(self):
        """
        Загружает данные из XML-файла и обновляет таблицу.
        """
        # Открываем диалог выбора файла
        file_path = filedialog.askopenfilename(
            filetypes=[("XML files", "*.xml"), ("All files", "*.*")],
            title="Select XML File to Load"
        )
        if not file_path:
            return  # Если пользователь отменил выбор файла

        try:
            # Очистка базы данных перед загрузкой новых данных
            self.db.clear_records()

            # Загрузка данных из XML
            records = XMLReader.load_from_xml(file_path)
            for record in records:
                self.db.insert_record(record)

            # Обновление главного окна
            self.total_records = len(self.db.get_records())
            self.total_pages = (self.total_records + self.records_per_page - 1) // self.records_per_page
            self.current_page = 1
            self.update_main_window()

            # Уведомление об успешной загрузке
            tk.messagebox.showinfo("Success", "Data loaded successfully from XML.")
        except Exception as e:
            # Вывод сообщения об ошибке
            tk.messagebox.showerror("Error", f"Failed to load data from XML: {e}")