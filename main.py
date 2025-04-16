# main.py
from pet import Pet
import time

if __name__ == "__main__":
    pet_name = "Simba"  # Let's name the pet Simba for this creative version!
    simba = Pet(pet_name)
    print(f"🌟 Creating your pet: {simba.name}")

    # Fun introduction to Simba's personality
    simba.talk()

    # Testing the pet actions
    simba.eat()
    time.sleep(1)
    simba.play()
    time.sleep(1)
    simba.sleep()

    # Check status
    simba.get_status()
    time.sleep(1)
    simba.train("roll over")
    simba.train("play dead")
    simba.show_tricks()
    time.sleep(1)
    simba.talk()  # Simba talks again after some playtime!
