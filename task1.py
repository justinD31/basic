import random

class Player:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        if self.inventory:
            print("Inventory:")
            for item in self.inventory:
                print(item)
        else:
            print("Inventory is empty.")

class Game:
    def __init__(self):
        self.player = None
        self.game_map = {
            'start': {'description': 'You wake up in a dimly lit room.'},
            'room1': {'description': 'You enter a dusty library.'},
            'room2': {'description': 'You find yourself in a garden with a fountain.'},
            'end': {'description': 'Congratulations! You have completed the game.'}
        }

    def start(self):
        print("Welcome to the Text Adventure Game!")
        self.create_character()
        self.play()

    def create_character(self):
        name = input("Enter your name: ")
        character_class = input("Choose your class (warrior, mage, rogue): ")
        self.player = Player(name, character_class)

    def play(self):
        current_location = 'start'
        while True:
            print("\n---")
            print(self.game_map[current_location]['description'])
            command = input("What do you want to do? ").lower().strip()

            if command == 'quit':
                print("Quitting game...")
                break
            elif command == 'inventory':
                self.player.show_inventory()
            else:
                print("Invalid command. Type 'quit' to exit.")

if __name__ == "__main__":
    game = Game()
    game.start()
