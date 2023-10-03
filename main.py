from db.db_management_1 import DbManagement
from sql_alchemy.models import Projektas


projektas = Projektas(category= 'Stalas',price = 450, code= 'Light', supplier= 'DOMDOM' , quantity = 15)


db = DbManagement()
# db.add_value(projektas)
# value = db.get_value_by_id(1)
# print(value.category)

# add_value(projektas)
# get_value_by_id()
# db.filter_by_category(category = 'Stalas')
db.update_value(id = 2, new_category = 'lenta' )
# db.delete_value(id = 1)