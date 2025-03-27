from MVC.model.database import Database

class AddRecordController:
    def __init__(self, db: Database):
        self.db = db

    def add_record(self, record):
        self.db.insert_record(record)