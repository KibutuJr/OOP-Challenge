# pet.py
import random
import time

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting hunger level
        self.energy = 10  # Starting energy level
        self.happiness = 5  # Starting happiness level
        self.tricks = []  # List to store tricks

    def eat(self):
        # Reduces hunger by 3, ensures hunger doesn't go below 0
        self.hunger = max(0, self.hunger - 3)
        self.happiness += 1
        print(f"🍖 {self.name} is eating... Yum! 😋")

    def sleep(self):
        # Increases energy by 5, ensures energy doesn't exceed 10
        self.energy = min(10, self.energy + 5)
        print(f"🌙 {self.name} is sleeping... Zzz... 💤")

    def play(self):
        # Reduces energy by 2, increases happiness by 2, and hunger by 1
        if self.energy >= 2:
            self.energy -= 2
            self.happiness += 2
            self.hunger += 1
            actions = ["chasing a ball", "fetching a stick", "rolling around", "doing a zoomie"]
            action = random.choice(actions)
            print(f"🎉 {self.name} is playing... {action} 🏃")
        else:
            print(f"😴 {self.name} is too tired to play. Time for a nap!")

    def get_status(self):
        print(f"👑 {self.name}'s Current Status:")
        print(f"Hunger: {self.hunger} 💀")
        print(f"Energy: {self.energy} ⚡")
        print(f"Happiness: {self.happiness} 😊")
        print(f"Tricks: {', '.join(self.tricks) if self.tricks else 'None yet!'} 🎩")

    def train(self, trick):
        # Adds a new trick to the list
        self.tricks.append(trick)
        print(f"🌟 {self.name} learned a new trick: {trick}! 😎")

    def show_tricks(self):
        if self.tricks:
            print(f"🎭 {self.name}'s Tricks: {', '.join(self.tricks)}")
        else:
            print(f"🎭 {self.name} hasn't learned any tricks yet... Time to train! 🐾")

    def talk(self):
        # Pet says a random thing based on its mood
        phrases = [
            f"🗣️ {self.name}: 'I'm the king of the jungle!' 👑",
            f"🗣️ {self.name}: 'Who wants to play? Meow!' 🐱",
            f"🗣️ {self.name}: 'I’m too cute for this!' 😽"
        ]
        print(random.choice(phrases))
