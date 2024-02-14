from config import app, migrate
from models import db
from rich import print
from db_utils import get_all_burgers, get_burger_by_id



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
        print(f"{burger.id} | [bold][blue1]{burger.name}[/blue1][/bold]")
        print(f"[deep_sky_blue1]{burger.description}[/deep_sky_blue1]")
    
    
  print(f"How would you like to proceed?")
  print(f"1. See more about a burger")
  print(f"2. Return to main menu")
  choice = input()
  if choice == "1":
    choose_burger_by_id()
  else:
    return
    
    
def choose_burger_by_id():
  search_id = input(f"Enter burger by the ID you would like to view")
  burger = get_burger_by_id(search_id)
  print(
    f"{burger.id} | [bold][blue1]{burger.name}[/blue1][/bold] | {burger.description}")
    
    
  
  





if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
  
    display_welcome()
    while True:
      display_main_menu()
      choice = get_main_choice()
      if choice == "1":
        display_all_burgers()
      elif choice == "2":
        print("Exiting Burger Hut, see you soon!")
        break
        
      break
    
