import random
from ability import Ability
from armor import Armor

# hero.py
class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
	def __init__(self, name, starting_health=100):
		# we know the name of our hero, so we assign it here
		self.name = name
		# similarly, our starting health is passed in, just like name
		self.starting_health = starting_health
		# when a hero is created, their current health is
		# always the same as their starting health (no damage taken yet!)
		self.current_health = starting_health
		self.abilities = list()
		self.armors = list()

	def fight(self, opponent):
		# winner = random.choice([self, opponent])
		# print(f"{winner.name} wins!")
		# return winner
		if len(self.abilities) == 0 and len(opponent.abilities) == 0:
			print("Draw!")
		else: 
			while self.is_alive() and opponent.is_alive():
				self.take_damage(opponent.attack())
				opponent.take_damage(self.attack())
				if not self.is_alive() and not opponent.is_alive():
					print("It's a draw!")
				elif not self.is_alive():
					print(f"{opponent.name} has won!")
					break
				elif not opponent.is_alive():
					print(f"{self.name} has won!")
					break


	def add_ability(self, ability):
		self.abilities.append(ability)

	def add_armor(self, armor):
		self.armors.append(armor)

	def attack(self):
		total_damage = 0
		for ability in self.abilities:
			total_damage += ability.attack()
		return total_damage

	def defend(self):
		total_block = 0
		if self.current_health == 0:
			return total_block
		for armor in self.armors: 
			total_block += armor.block()
		return total_block

	def take_damage(self, damage):
		total_damage = damage - self.defend()
		if total_damage > 0:
			self.current_health -= total_damage
		print(f"{self.name} has taken damage! Current health: {self.current_health}")

	def is_alive(self):
		if self.current_health <= 0:
			return False
		else: 
			return True


if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
	# hero1 = Hero("Wonder Woman")
	# hero2 = Hero("Dumbledore")
	# hero1.fight(hero2)
	# ability = Ability("Great Debugging", 50)
	# ability2 = Ability("Smarty Pants", 90)
	# hero1.add_ability(ability)
	# hero1.add_ability(ability2)
	# print(hero1.attack())
	# armor = Armor("defence", 34)
	# armor2 = Armor("woooo", 12)
	# hero1.add_armor(armor)
	# hero1.add_armor(armor2)
	# hero1.take_damage(110)
	# print(hero1.current_health)
	# print(hero1.is_alive())

	hero1 = Hero("Wonder Woman")
	hero2 = Hero("Dumbledore")
	ability1 = Ability("Super Speed", 100)
	ability2 = Ability("Super Eyes", 30)
	ability3 = Ability("Wizard Wand", 60)
	ability4 = Ability("Wizard Beard", 20)
	hero1.add_ability(ability1)
	hero1.add_ability(ability2)
	hero2.add_ability(ability3)
	hero2.add_ability(ability4)
	hero1.fight(hero2)
