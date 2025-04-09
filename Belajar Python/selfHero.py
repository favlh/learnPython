attack = 10
defense = 7
health = 12
level = 1
name = "Demon King"

class Character:
    def __init__(self, name, attack, defense, health, level):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = health
        self.level = level

    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Health: {self.health}")
        print(f"Level: {self.level}\n")
        
    def level_up(self):
        print("Leveling up...\n")
        self.level += 1
        self.attack += 2
        self.defense += 2
        self.health += 5
        print("Level up complete!")
        print("New stats after leveling up:")
        self.display_stats()
    
    def level_up_two(self):
        print("Leveling up...\n")
        self.level += 1
        self.attack += 2
        self.defense += 2
        self.health += 5
        print("Level up complete!")
        print("New stats after leveling up:")
        self.display_stats()
        
hero = Character(name, attack, defense, health, level)
hero.display_stats()
hero.level_up()  
hero.level_up_two()