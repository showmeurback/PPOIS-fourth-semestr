from MVC.model.database import Database

class TreeViewController:
    def __init__(self, db: Database):
        self.db = db

    def get_records_for_tree(self):
        return self.db.get_records()