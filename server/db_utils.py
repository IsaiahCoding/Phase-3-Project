from models import db, Hamburger, Ingredient
from pick import pick


def get_all_burgers():
    return db.session.query(Hamburger).all()

def get_burger_by_id(id):
    return db.session.get(Hamburger, id)

def get_all_ingredients():
    return db.session.query(Ingredient).all()

def get_ingredient_by_id(id):
    return db.session.get(Ingredient, id)

def add_ingredient_to_burger(burger):
    ingredient_names = [ingredient.name for ingredient in db.session.query(Ingredient).all() if not ingredient.hamburger_id]
    title = "Which ingredient would you like to add?"
    ing_name, index = pick(ingredient_names, title)
    ingredient = db.session.query(Ingredient).filter(Ingredient.name == ing_name).first()
    ingredient.hamburger_id = burger.id
    '''for ingredient_name in ingredient_names:
        print(f"{ingredient_name}")
    ingredient_name = input(title)
    new_ingredient = Ingredient(name = ingredient_name, hamburger_id = burger.id)'''
    
    
    db.session.commit()
    
def remove_ingredient_from_burger(burger):
    ingredient_names = [ingredient.name for ingredient in burger.ingredients]
    title = "Which ingredient would you like to remove?"
    ing_name, index = pick(ingredient_names, title)
    ingredient = db.session.query(Ingredient).filter(Ingredient.name == ing_name).first()
    ingredient.hamburger_id = None
    db.session.commit()
    
    
    