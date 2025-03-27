import sqlite3
from MVC.model.record import Record

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY,
                fio TEXT,
                composition TEXT,
                position TEXT,
                titles INTEGER,
                sport_type TEXT,
                rank TEXT
            )
        ''')
        self.conn.commit()

    def insert_record(self, record):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO records (fio, composition, position, titles, sport_type, rank)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (record.fio, record.composition, record.position, record.titles, record.sport_type, record.rank))
        self.conn.commit()

    def get_records(self, limit=None, offset=None):
        """
        Возвращает записи из базы данных с учетом лимита и смещения.
        """
        cursor = self.conn.cursor()
        query = "SELECT * FROM records"
        if limit is not None and offset is not None:
            query += f" LIMIT {limit} OFFSET {offset}"
        cursor.execute(query)
        return [Record(*row[1:]) for row in cursor.fetchall()]

    def search_records(self, criteria):
        query = "SELECT * FROM records WHERE "
        conditions = []
        params = []

        if 'fio' in criteria:
            conditions.append("fio LIKE ?")
            params.append(f"%{criteria['fio']}%")
        if 'sport_type' in criteria:
            conditions.append("sport_type LIKE ?")
            params.append(f"%{criteria['sport_type']}%")

        if not conditions:
            return []

        query += " AND ".join(conditions)
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return [Record(*row[1:]) for row in cursor.fetchall()]

    def delete_records(self, criteria):
        query = "DELETE FROM records WHERE "
        conditions = []
        params = []

        if 'fio' in criteria:
            conditions.append("fio LIKE ?")
            params.append(f"%{criteria['fio']}%")
        if 'sport_type' in criteria:
            conditions.append("sport_type LIKE ?")
            params.append(f"%{criteria['sport_type']}%")

        if not conditions:
            return 0

        query += " AND ".join(conditions)
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        return cursor.rowcount

    def clear_records(self):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM records')
        self.conn.commit()