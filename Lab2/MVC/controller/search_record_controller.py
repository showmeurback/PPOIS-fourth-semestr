from MVC.model.database import Database

class SearchRecordController:
    def __init__(self, db: Database):
        self.db = db

    def search_records(self, fio=None, sport_type=None):
        criteria = {}
        if fio:
            criteria['fio'] = fio
        if sport_type:
            criteria['sport_type'] = sport_type
        return self.db.search_records(criteria)