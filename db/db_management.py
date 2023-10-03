import concurrent.futures
import sqlite3


class DB:

    def __init__(self, url='new_db'):
        self.url = url
        # self.connection = sqlite3.connect(self.url)
        # self.cursor = self.connection.cursor()

    # def __run_sql_query(self,sql_query):
    #     self.cursor.exexute(sql_suery)
    #     self.connection.commit()


    def create_table(self):
        connection = sqlite3.connect('duomenu_baze.db')
        cursor = connection.cursor()
        create_workers_table = """
        create table if not exists workers(
        Vardas text,
        Pareigos text,
        Valandos integer
        );
        """
        cursor.execute(create_workers_table)
        connection.commit()
        connection.close()

    # def create_table(self, data):
    # table_name = data['table_name']
    # sql_middle = ''
    # for key, value in data['columns'].items():
    #     sql_middle += f'{key} {value}, '
    #     sql_query = f"""create table if not exists {table_name}
    #     ({sql_middle[:-2]});"""
    #     self.__run_sql_query(sql_query=sql_query)


    def insert_values(self):
        with sqlite3.connect('duomenu_baze.db') as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO workers VALUES('Laura', 'Dizainere', '40')")
            cursor.execute("INSERT INTO workers VALUES('Mantas', 'Projektuotojas', '20')")
            cursor.execute("INSERT INTO workers VALUES('Motiejus', 'Vadybininkas', '40')")

    def delete_rows(self):
        with sqlite3.connect('duomenu_baze.db') as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE from workers WHERE vardas = 'Mantas'")


    def update_rows(self):
        with sqlite3.connect('duomenu_baze.db') as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE workers SET valandos = 35 WHERE vardas = 'Laura'")

db = DB()
# db.create_table()
db.insert_values()
db.delete_rows()
db.update_rows()