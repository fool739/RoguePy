import random
import json
from typing import Dict, List

CHARACTER_CLASSES = {
    "Knight" : {
        "base_stats": {
            "strength": 15,
            "defense": 12,
            "speed": 10,
            "wisdom": 6
        },
        "special_ability": "Wind Slash",
        "weapon_choice": ["Sword", "Lance"],
        "starting_inventory": ["Iron Sword", "Shield"]
    },
     "Wizard" : {
        "base_stats": {
            "strength": 8,
            "defense": 9,
            "speed": 12,
            "wisdom": 15
        },
        "special_ability": "Greater Fireball",
        "weapon_choice": ["Staff", "Wand"],
        "starting_inventory": ["Wood Staff", "Wizard's Eye"]
    },

     "Rogue" : {
        "base_stats": {
            "strength": 10,
            "defense": 11,
            "speed": 15,
            "wisdom": 9
        },
        "special_ability": "Invisibility",
        "weapon_choice": ["Dagger", "Crossbow"],
        "starting_inventory": ["Silver Dagger", "Wooden Crossbow"]
    }   

}

class Character:
    def __init__(self, name: str, character_class: str):
        self.name = name
        if character_class not in CHARACTER_CLASSES:
            raise ValueError(f"Invalid class. Choose from: {', '.join(CHARACTER_CLASSES.keys())}")
        class_data = CHARACTER_CLASSES[character_class]
        self.character_class = character_class
        self.level = 1
        self.exp = 0
        self.max_hp = 100
        self.hp = self.max_hp
        self.inventory = class_data["starting_inventory"].copy()
        self.stats = class_data["base_stats"].copy()
        self.special_ability = class_data["special_ability"]
        self.weapon_choice = class_data["weapon_choice"]

    def attack(self, enemy) -> int:
        damage = self.stats["strength"] + random.randint(1,10)
        enemy.hp -= max(0, damage - enemy.stats["defense"])
        return damage
    


class Enemy:
    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level
        self.hp = 50 + (level * 10)
        self.stats = {
            "strength": 5 + (level * 2),
            "defense": 5 + (level * 2),
            "speed": 5 + (level * 2)
        }

class Game: 
    def __init__(self):  
        self.player = None
        self.enemies = []  
        
    def load_enemies(self):
        # Enemy Sheet Basic
        return [
            Enemy("Goblin", 1),
            Enemy("Orc", 2),
            Enemy("Troll", 3)
        ]
    
    def create_character(self):
        name = input("Name yourself, dear warrior: ")
        
        while True:
            print("\nChoose your class:")
            for class_name, data in CHARACTER_CLASSES.items():
                print(f"\n{class_name}:")
                print("Base Stats:")
                for stat, value in data["base_stats"].items():
                    print(f"  {stat.capitalize()}: {value}")
                print(f"Special Ability: {data['special_ability']}")
                print(f"Weapons: {', '.join(data['weapon_choice'])}")
                print(f"Starting Items: {', '.join(data['starting_inventory'])}")
            choice = input("\nEnter your class name: ").capitalize()
            
            if choice in CHARACTER_CLASSES:
                self.player = Character(name, choice)
                print(f"\nWelcome {self.player.name} the {self.player.character_class}!")
                print("\nYour stats are:")
                for stat, value in self.player.stats.items():
                    print(f"{stat.capitalize()}: {value}")
                break
            else:
                print(f"\nInvalid class. Please choose from: {', '.join(CHARACTER_CLASSES.keys())}")
    
    def start_quest(self):
        print("\n" + "="*50)
        print("The shadows grow closer and the moon darker.")
        print("\nThe Kingdom of Valenta is on it's last legs. Dark forces gather in wait for it's fall.")
        print("\nIn the Riftbleeding Forest lays the key to victory.")
        print("\nAnd you have been chosen.")
        print("\nInvestigate the forces that lay within and find the key.")
        print("=" * 50 + "\n")

        input("Press enter to continue...")
        print("\nYou stand at the edge of Riftbleeding Forest. The trees loom")
        print("before you, their ancient branches twisting into the darkening sky.")

        while True: 
            print("\nWhat would you like to do?")
            print("1. Enter the forest cautiously")
            print("2. Look for tracks or signs of disturbance")
            print("3. Check your inventory")

            choice = input("Enter your choice brave hero!")

            if choice == "1":
                self.enter_forest()
            elif choice == "2":
                self.search_area()
            elif choice == "3":
                self.show_inventory()
            elif choice == "4":
                self.show_stats()
            else:
                print("Invalid choice. Please try again.")
    
    def enter_forest(self):
        print("\nYou step into the forest. The canopy above blocks most of the sunlight,")
        print(f"but your experience as a {self.player.character_class} serves you well.")
        if self.player.character_class == "Rogue":
            print("Your natural stealth allows you to move silently between the trees.")
        elif self.player.character_class == "Wizard":
            print("You can sense magical disturbances in the air.")
        elif self.player.character_class == "Knight":
            print("Your combat training keeps you alert for any threats.")
        # Add combat encounter
        print("\nSuddenly, you hear rustling in the bushes ahead...")
    def search_area(self):
        print("\nYou carefully examine the area around you...")
        if self.player.stats["wisdom"] > 10:
            print("Your keen senses reveal fresh tracks leading deeper into the forest.")
            print("They appear to be made by something... unnatural.")
        else:
            print("You find some disturbed vegetation, but can't determine much else.")
    
    def search_area(self):
        print("\nYou carefully examine the area around you...")
        if self.player.stats["wisdom"] > 10:
            print("Your keen senses reveal fresh tracks leading deeper into the forest.")
            print("They appear to be made by something... unnatural.")
        else:
            print("You find some disturbed vegetation, but can't determine much else.")
                  
    def show_inventory(self):
        print("\nYour inventory:")
        for item in self.player.inventory:
            print(f"- {item}")
    
    def show_stats(self):
        print(f"\n{self.player.name} the {self.player.character_class}")
        print(f"Level: {self.player.level}")
        print(f"HP: {self.player.hp}/{self.player.max_hp}")
        print("\nStats:")
        for stat, value in self.player.stats.items():
            print(f"{stat.capitalize()}: {value}")       
    
        
# Testing
if __name__ == "__main__":
    game = Game()
    game.create_character()
    game.start_quest()