from config import db

#Welcome to the Burger Hut 

#Display 5 signature burgers




class Hamburger(db.Model):
    __tablename__ = "burgers"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True)
    description = db.Column(db.String)

#Do you want to customize your burgers?
#1 - yes (Let's create)
#2 - no (let's eat!)

    

class Ingredient(db.Model):
    __tablename__ = "ingredients"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    
    
    hamburger_id = db.Column(db.Integer, db.ForeignKey("burgers.id"))
    
