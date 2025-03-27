import tkinter as tk
from tkinter import ttk

class TreeViewWindow(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Tree View of Records")
        self.geometry("800x600")

        self.tree = ttk.Treeview(self)
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.refresh_button = ttk.Button(self, text="Refresh", command=self.refresh_tree)
        self.refresh_button.pack(side=tk.BOTTOM, pady=10)

        self.refresh_tree()

    def refresh_tree(self):
        self.tree.delete(*self.tree.get_children())

        records = self.controller.get_records_for_tree()

        for idx, record in enumerate(records, start=1):
            record_id = self.tree.insert("", "end", text=f"Record {idx}")
            self.tree.insert(record_id, "end", text=f"FIO: {record.fio}")
            self.tree.insert(record_id, "end", text=f"Composition: {record.composition}")
            self.tree.insert(record_id, "end", text=f"Position: {record.position}")
            self.tree.insert(record_id, "end", text=f"Titles: {record.titles}")
            self.tree.insert(record_id, "end", text=f"Sport Type: {record.sport_type}")
            self.tree.insert(record_id, "end", text=f"Rank: {record.rank}")