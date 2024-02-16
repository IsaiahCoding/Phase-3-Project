from config import app, migrate
from models import db
from rich import print
from db_utils import get_all_burgers, get_burger_by_id , get_ingredient_by_id, add_ingredient_to_burger, remove_ingredient_from_burger,create_burger



def display_welcome():
  
  print("[blue]Get ready to meat your cravings! [bold]Welcome to Burger Hut[/bold] – where every bite is a flipping good time![/blue]")
  
def display_main_menu():
  print ("\n[bold]Main Menu[/bold]\n")
  print("[bold]1. View Burgers[/bold]\n")
  print ("[bold]2. Create A New Burger[/bold]\n")
  
def get_main_choice():
  return input("Enter your choice: ")

###############Shows all burger with details##########
def display_all_burgers():
  burgers = get_all_burgers()
  for burger in burgers:
        print(f"{burger.id} | [bold][blue1]{burger.name}[/blue1][/bold]")
        print(f"[deep_sky_blue1]{burger.description}[/deep_sky_blue1]")
    
 ##########this prints option for how the user would like to continue###########   
  print(f"How would you like to proceed?")
  print(f"1. See more about a burger")
  print(f"2. Return to main menu")
  
  choice = input()
  if choice == "1":
    choose_burger_by_id()
  elif choice == "2":
    display_main_menu()
    
  
#######function displays all ingredients for burger by ID###########
def choose_burger_by_id():
  search_id = input(f"Enter burger by the ID you would like to view: ")
  burger = get_burger_by_id(search_id)
  
  print(f"{burger.id} | [bold][blue1]{burger.name}[/blue1][/bold] |{burger.description}")
  for ingredient in burger.ingredients:
    print(f"{ingredient.id} | {ingredient.name}")
    
  print(f"How would you like to proceed?")
  print(f"1. Order this burger!")
  print(f"2. Customize this burger")
  print(f"3. Back to burger menu")
  print(f"4. Leave Burger Hut")
  
  choice = input()
  if choice == "1":
    print(f"Enjoy! See you soon!")
  elif choice == "2":
    customize_burger(burger)
  elif choice == "3":
    display_all_burgers()
  elif choice == "4":
    print("Bye!")
    
  customize_burger(burger)
  
########function allows user to customize the burger they selected by delteing or adding ingredients########
def customize_burger(burger):
  print(f"1. Add ingredients")
  print(f"2. Remove ingredients")
  print(f"3. Back to burger menu")
  choice = input()
  handle_custom_choice(choice, burger)
  
def handle_custom_choice(choice, burger):
  if choice == "1":
    add_ingredient_to_burger(burger)
  elif choice == "2":
    remove_ingredient_from_burger(burger)
  elif choice == "3":
    display_all_burgers()
    
    
   


    



  
  
 


  






  

    
  
     
  


  
  
    
    
  
  
  
  
  


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
        create_burger()
        break
        
      break
    
