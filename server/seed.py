from config import app
from faker import Faker

from models import *

if __name__ == "__main__":
  with app.app_context():
    fake = Faker()
   
    
    print("Clearing out tables...")
    
    Hamburger.query.delete()
    Ingredient.query.delete()
    
    print("Seeding Burger table...")
    
    new_burger_1 = Hamburger(
      name = "Lettuce Meat Again",
      description = "A peace treaty between crispy lettuce buns, a harmony patty, and toppings that'll make your taste buds hug it out!"
    )
    
    db.session.add(new_burger_1)
    db.session.commit()
    
    new_burger_2 = Hamburger(
      name = "Wham Bam Thank You Lamb",
      description = "It's a lamb-tastic delight that'll leave you saying, Thank you, lamb! "
    )
    
    db.session.add(new_burger_2)
    db.session.commit()
    
    new_burger_3 = Hamburger(
      name = "Gouda Goddess",
      description = "A juicy beef patty crowned with creamy Gouda, nestled in a bun fit for royalty!"
    )
    
    db.session.add(new_burger_3)
    db.session.commit()
    
    new_burger_4 = Hamburger(
      name = "Rooster Rapture",
      description = "Where a crispy chicken fillet, seasoned with a top-secret blend that even Colonel Sanders would envy!"
    )
    
    db.session.add(new_burger_4)
    db.session.commit()
    
    new_burger_5 = Hamburger(
      name = "Coding Crusader",
      description = "Drowning in chaos? We've got a burger for that!"
    )
    
    db.session.add(new_burger_5)
    db.session.commit()
    
    
    
    
    print("Seeding Ingredient Table...")
    
    new_ingredient = [
      Ingredient(
        name = "Lettuce (for buns)",
        hamburger_id = new_burger_1.id
      ),
      Ingredient(
        name = "Ground Chuck Patty",
        hamburger_id = new_burger_1.id
      ),
      Ingredient(
        name = "Swiss Cheese",
        hamburger_id = new_burger_1.id
      ),
      Ingredient(
        name = "Tomato Slices",
        hamburger_id = new_burger_1.id
      ),
      Ingredient(
        name = "White Onion",
        hamburger_id = new_burger_1.id
      ),
      Ingredient(
        name = "Dill Pickles",
        hamburger_id = new_burger_1.id
      ),
      Ingredient(
        name = "Mayonnaise",
        hamburger_id = new_burger_1.id
      ),
      Ingredient(
        name = "Crisp Bacon Strips",
        hamburger_id = new_burger_1.id
      ),
     
    ]
    
    
    db.session.add_all(new_ingredient)
    db.session.commit()
    
    
    new_ingredient = [
      Ingredient(
        name = "Brioche Buns",
        hamburger_id = new_burger_2.id
      ),
      Ingredient(
        name = "Ground Lamb Patty",
        hamburger_id = new_burger_2.id
      ),
      Ingredient(
        name = "Feta Cheese",
        hamburger_id = new_burger_2.id
      ),
      Ingredient(
        name = "Lettuce",
        hamburger_id = new_burger_2.id
      ),
      Ingredient(
        name = "Red Onion",
        hamburger_id = new_burger_2.id
      ),
      Ingredient(
        name = "Tzatziki Sauce",
        hamburger_id = new_burger_2.id
      ),
     
    ]
    db.session.add_all(new_ingredient)
    db.session.commit()
    
    new_ingredient = [
      Ingredient(
        name = "Ciabatta Buns",
        hamburger_id = new_burger_3.id
      ),
      Ingredient(
        name = "Ground Beef Patty",
        hamburger_id = new_burger_3.id
      ),
      Ingredient(
        name = "Gouda Cheese",
        hamburger_id = new_burger_3.id
      ),
      Ingredient(
        name = "Spinach Leaves",
        hamburger_id = new_burger_3.id
      ),
      Ingredient(
        name = "Grape Tomato Slices",
        hamburger_id = new_burger_3.id
      ),
      Ingredient(
        name = "Truffle Aoili Sauce",
        hamburger_id = new_burger_3.id
      ),

    ]
    
    
    db.session.add_all(new_ingredient)
    db.session.commit()
    
    new_ingredient = [
      Ingredient(
        name = "Buttermilk Biscuit Buns",
        hamburger_id = new_burger_4.id
      ),
      Ingredient(
        name = "Fried Chicken Fillet",
        hamburger_id = new_burger_4.id
      ),
      Ingredient(
        name = "Pepper Jack Cheese",
        hamburger_id = new_burger_4.id
      ),
      
      Ingredient(
        name = "Spicy Pickles",
        hamburger_id = new_burger_4.id
      ),
      Ingredient(
        name = "Signature Hut Sauce",
        hamburger_id = new_burger_4.id
      ),
    ]
    db.session.add_all(new_ingredient)
    db.session.commit()
    
    new_ingredient = [
      Ingredient(
        name = "Pretzle Buns",
        hamburger_id = new_burger_5.id
      ),
      Ingredient(
        name = "5 Smash Beef Patties",
        hamburger_id = new_burger_5.id
      ),
      Ingredient(
        name = "5 Slices Cheddar Cheese",
        hamburger_id = new_burger_5.id
      ),
      Ingredient(
        name = "Sauteed Mushrooms",
        hamburger_id = new_burger_5.id
      ),
      Ingredient(
        name = "Caramelized Onions",
        hamburger_id = new_burger_5.id
      ),
      Ingredient(
        name = "Fried Onion Rings",
        hamburger_id = new_burger_5.id
      ),
      Ingredient(
        name = "BBQ Sauce",
        hamburger_id = new_burger_5.id
      ),
    ]
    db.session.add_all(new_ingredient)
    db.session.commit()
    
    for _ in range(20):
      ing = Ingredient(name = fake.word())
      db.session.add(ing)
      db.session.commit()
    
    