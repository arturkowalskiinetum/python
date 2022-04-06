import sqlite3


class Database:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def info():
        return sqlite3.sqlite_version

    def initialize(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)

    def create(self, query, body):
        try:
            self.cursor.execute(query, (None, body))
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)

    def read(self, query, doc_id):
        try:
            if type(int(doc_id[0])) == str:
                raise ValueError
            query = self.cursor.execute(query, doc_id)
            self.connection.commit()
            return query.fetchall()
        except sqlite3.Error as e:
            return {'error': str(e)}
        except ValueError:
            return {'error': 'ID must be an integer'}

    def readall(self, query):
        try:
            query = self.cursor.execute(query)
            self.connection.commit()
            return query.fetchall()
        except sqlite3.Error as e:
            return {'error': str(e)}

    def update(self, query, doc_info):
        try:
            self.cursor.execute(query, doc_info)
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)

    def delete(self, query, doc_id):
        try:
            if type(int(doc_id[0])) == str:
                raise ValueError
            self.cursor.execute(query, doc_id)
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)
        except ValueError:
            print('ID must be an integer')

    def __del__(self):
        self.connection.close()
