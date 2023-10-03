from db.uzduotis import Duomenu_baze

table = {
    'table_name': 'paskaitos',
    'columns':{
    'pavadinimas' : 'text',
    'destytojas' : 'text',
    'trukme' : 'integer',
    }
}

paskaitos = [
    ('Vadyba', 'Domantas', 40),
    ('Python', 'Donatas', 80),
    ('Java', 'Tomas', 80),
]

data = {
    'old_value': 'Python',
    'new_value': 'Python programavimas',
}

delete_data = ('Tomas')


delete_data_2= {
    'paskaita': 'Java',
    'destytojas' : 'Tomas',
    'trukme': '80',
}


duomenu_baze = Duomenu_baze()
# duomenu_baze.create_table(data=table)
# duomenu_baze.insert_values_to_paskaita_table(paskaitos)
# duomenu_baze.get_data()
# duomenu_baze.update_rows(data)
# duomenu_baze.delete_rows(data=delete_data_2)
duomenu_baze.print_tabele(data)


