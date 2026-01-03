# class TestClass:
#     test_var = "This is a test class."
    
#     def test_method(self):
#         print("self refers to the instance of the class.")
#         print(self.test_var, "accessed via self in a method.")
#         self.another_method("Calling another method from test_method.")

    
#     def another_method(self, msg):
#         print(f"Message from another_method: {msg}")

# test = TestClass()
# test.test_method()

# test2 =  TestClass()
# test2.another_method("Hello from test2 instance!")

class Mage:
    def __init__(self, health, mana):
        self.health = health
        self.mana = mana

        print("Mage instance created.")
        print(f"Health: {self.health}, Mana: {self.mana}")

    def attack(self,  target):
        target.health -= 10
        self.health += 10
       

mage1 = Mage(100, 200)
mage2 = Mage(150, 300) 
# mage1.attack(mage2)
mage2.attack(mage1)

# print(f"After attack, Mage2's health: {mage2.health}") 
# print(f"After attack, Mage1's health: {mage1.health}")

# print(f"After attack, Mage1's health: {mage1.health}") 
# print(f"After attack, Mage2's health: {mage2.health}")




# Inheritance example
class Human:
    def __init__(self, health):
        self.health = health

    def attack(self):
        print("attack from Human class")

class Warrior(Human):
    def __init__(self, health, defense):
        super().__init__(health)
        self.defense = defense

class Barbarian(Human):
    def __init__(self, health, damage):
        super().__init__(health)
        self.damage = damage

        
warrior = Warrior(100, 50)
barbarian = Barbarian(150, 70)

print(f"Warrior Health: {warrior.health}, Defense: {warrior.defense}")
print(f"Barbarian Health: {barbarian.health}, Damage: {barbarian.damage}")


# Exercise
class Entity:
    def attack(self):
        print("Entity attack method")   
        print(self.damage)

    def __repr__(self):
        return f"Monster with {self.health} hp"

class Monster(Entity):
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

monster = Monster(200, 30)
monster2 = Monster(250, 80)
print(f"Monster Health: {monster.health}, Damage: {monster.damage}")
print("Calling attack method from Monster instance:")

monster.attack()
monster2.attack()

print(monster2)




   

    
