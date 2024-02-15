from models import db, Hamburger, Ingredient


def get_all_burgers():
    return db.session.query(Hamburger).all()

def get_burger_by_id(id):
    return db.session.get(Hamburger, id)

def get_all_ingredients():
    return db.session.query(Ingredient).all()