import sqlite3

# •Sukurti programą, kuri:
# •Sukurtų duomenų bazę
# •Sukurtų lentelę paskaitos su stulpeliais pavadinimas, destytojas ir trukme
# •Sukurtų tris paskaitas: ('Vadyba', 'Domantas', 40), ('Python', 'Donatas', 80) ir ('Java', 'Tomas', 80)
# •Atspausdintų tik tas paskaitas, kurių trukmė didesnė už 50
# •Atnaujintų paskaitos „Python“ pavadinimą į „Python programavimas“
# •Ištrintų paskaitą, kurios dėstytojas – „Tomas“

# •Atspausdintų visas paskaitas (visą lentelę)

class Duomenu_baze:

    def __init__(self, url='nauja.db'):
        self.url = url
        self.connection = sqlite3.connect(self.url)
        self.cursor = self.connection.cursor()

    def __run_sql_query(self, sql_query):
        self.cursor.execute(sql_query)
        self.connection.commit()

    def create_table(self, data):
        table_name = data['table_name']
        sql_middle = ''
        for key, value in data['columns'].items():
            sql_middle += f'{key} {value}, '

        sql_query = f"""create table if not exists {table_name}
           ({sql_middle[:-2]});"""

        self.__run_sql_query(sql_query=sql_query)

    def insert_values_to_paskaita_table(self, data):
        for paskaitos in data:
            sql_query = f"""
            INSERT INTO paskaitos(pavadinimas, destytojas, trukme)
            VALUES ("{paskaitos[0]}", "{paskaitos[1]}", {paskaitos[2]});
            """
            self.__run_sql_query(sql_query)

    def get_data(self):
        sql_query = f'''
        SELECT * FROM paskaitos
        WHERE trukme > 50;
        '''
        result = self.cursor.execute(sql_query)
        print(result.fetchall())

    def update_rows(self, data):
        sql_query = f'''
        UPDATE paskaitos SET pavadinimas = "{data["new_value"]}"
        WHERE pavadinimas = "{data["old_value"]}" '''
        print(sql_query)
        self.__run_sql_query(sql_query)

    def delete_rows(self, data):
        sql_query = f'''
                      DELETE from paskaitos
                      WHERE destytojas = "Tomas"'''
        print(sql_query)
        self.__run_sql_query(sql_query)

    def print_tabele(self,data):
        sql_query = f'select * from paskaitos;'
        print(sql_query)
        result = self.cursor.execute(sql_query)
        print(result.fetchall())







