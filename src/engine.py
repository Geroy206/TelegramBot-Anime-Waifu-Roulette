import random

# for debug CLI
def show_titles(titles):
    for index in range(len(titles)):
        print(f"{index}. {titles[index]}")
     
def get_random_character(t_l, g_characters_dict):
    # Select a random title from the list
    random_title = random.choice(t_l)
    
    # We get a list of characters for the selected title
    characters = g_characters_dict.get(random_title, [])
    
    # Select a random character from the list
    return "Тайтл: " + random_title + "\n" + "Персонаж: " + random.choice(characters) if characters else "Error"

def get_random_title_character(title, g_characters_dict):
    characters = g_characters_dict.get(title, [])
    
    return "Тайтл: " + title + "\n" + "Персонаж: " + random.choice(characters) if characters else "Error"