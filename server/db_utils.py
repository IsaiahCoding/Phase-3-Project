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
    
    
    db.session.commit()
    
def remove_ingredient_from_burger(burger):
    ingredient_names = [ingredient.name for ingredient in burger.ingredients]
    title = "Which ingredient would you like to remove?"
    ing_name, index = pick(ingredient_names, title)
    ingredient = db.session.query(Ingredient).filter(Ingredient.name == ing_name).first()
    ingredient.hamburger_id = None
    
    db.session.commit()
    
    
def create_burger():
    ingredient_names = [ingredient.name for ingredient in db.session.query(Ingredient).all() if not ingredient.hamburger_id]
    title = "Which ingredient would you like to add?"
    name = input(f"What do you wanna call your burger?")
    description = input(f"Describe your burger?")

    selected_ingredients = []
    while True:
        ing_name, index = pick(ingredient_names, title)
        ingredient = db.session.query(Ingredient).filter(Ingredient.name == ing_name).first()
        ingredient.hamburger_id = None
        selected_ingredients.append(ingredient)
        more_ingredients = input("Do you want to add more ingredients? (Y/N)")
        if more_ingredients.lower() != "Y":
            break

    push_pig = Hamburger(
        name=name,
        description=description,
        ingredients=selected_ingredients
    )

    db.session.add(push_pig)
    db.session.commit()
    
    
    
    