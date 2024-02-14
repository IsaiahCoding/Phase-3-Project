from config import app, migrate
from models import db
from rich import print
from db_utils import get_all_burgers



def display_welcome():
  print ("[blue]Get ready to meat your cravings! [bold]Welcome to Burger Hut[/bold] – where every bite is a flipping good time![/blue]")

def display_main_menu():
  print ("\n[bold]Main Menu[/bold]\n")
  print("[bold]1. View Burgers[/bold]\n")
  print ("[bold]2. Exit Burger Hut[/bold]\n")
  
def get_main_choice():
  return input("Enter your choice")

def display_all_burgers():
  burgers = get_all_burgers()
  for burger in burgers:
    print(f"Name: {burger.name}")
    print(f"Description: {burger.description}")
    
  
  





if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
  
    display_welcome()
    while True:
      display_main_menu()
      choice = get_main_choice()
      if choice == "1":
        display_all_burgers
      elif choice == "2":
        print("Exiting Burger Hut")
        break
        
      break
    
