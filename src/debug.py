import engine
import data

def temp_input():
    while True:
        try:
            choice = int(input("> "))
            
            return choice
        except ValueError:
            print("INPUT THE NUMBER, YOU DUMBASS!")
    
def main():
    
    while True:
        print("========== # ANIME WAIFU ROULETTE # ==========")
        print("Select mode:")
        print("1. Random character from random title")
        print("2. Random character from selected title")
        print("0. Exit")
        
        choice = temp_input()
        
        # mode selection
        if choice == 1: 
            print(engine.get_random_character(data.title_list, data.girls_characters_dict))
        elif choice == 2:
            print("Select title:")
            engine.show_titles(data.title_list)
            
            choice = temp_input()
            
            try:
                print(engine.get_random_title_character(data.title_list[choice], data.girls_characters_dict))
            except IndexError:
                print("INDEX OUT OF RANGE, YOU IDIOT!")
        elif choice == 0:
            print("Exit...")
            exit(0)