from models import db, Hamburger, Ingredient


def get_all_burgers():
    return db.session.query(Hamburger).all()