from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

from sql_alchemy.models import Projektas

engine = create_engine('sqlite:///projektai.db')
Session = sessionmaker(bind=engine)
session = Session()

class DbManagement:
    def __init__(self):
        self.session = session

    def __repr__(self):
        def __repr__(self):
            return f'{self.id}{self.name}'

    def add_value(self, projektas: Projektas):
        self.session.add(projektas)
        self.session.commit()

    def get_value_by_id(self, id):
        return session.query(Projektas).get(id)


#
    def filter_by_category(self, category):
        value = self.session.query(Projektas).filter_by(category=category).all()
        print(value)


# crUd
    def update_value(self, id, new_category):
        value = self.session.query(Projektas).get(id)
        value.category = new_category
        session.commit()


    def delete_value(self, id):
        value = self.session.query(Projektas).get(id)
        self.session.delete(value)
        self.session.commit()
