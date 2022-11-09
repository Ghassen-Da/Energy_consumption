import psycopg2
from psycopg2.extras import RealDictCursor


class DB(object):
    # singleton pattern
    __state = {}
    def __init__(self):
        self.__dict__ = self.__state
        if not hasattr(self, 'conn'):
            self.conn = psycopg2.connect(
                host="localhost",
                database="enexflow",
                user="postgres",
                password="gh")
            self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
            print("Connection established.")
        else:
            print("Database already connected.")
        
    # JSON cursor to retrieve data from DB in JSON format
    def get_json_cursor(self):
        return self.conn.cursor(cursor_factory=RealDictCursor)

    @staticmethod #To not add "self" in arguments
    def execute_and_fetch(cursor, query):
        cursor.execute(query)
        res = cursor.fetchall()
        cursor.close()
        return res
            

    def get_consommation_between_dates(self, starting_date, ending_date):
        query = """SELECT * FROM consommation 
                 WHERE date>='{}'::date AND date<='{}'::date;""".format(starting_date,ending_date)
        cursor = self.get_json_cursor()
        return self.execute_and_fetch(cursor, query)
    