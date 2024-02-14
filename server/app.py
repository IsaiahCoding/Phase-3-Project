from config import app, migrate

from models import db
#from rich import print


def display_welcome():
  print ("Get ready to 'meat' your cravings! Welcome to Burger Hut – where every bite is a flipping good time!")





if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
  
    display_welcome()
    # remove pass and write your cli logic
