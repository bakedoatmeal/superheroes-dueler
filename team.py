import random

class Team:
	def __init__(self, name):
		self.heroes = list()
		self.name = name
	
	def add_hero(self, hero):
		self.heroes.append(hero)

	def remove_hero(self, name):
		foundHero = False
		for hero in self.heroes:
			if hero.name == name: 
				self.heroes.remove(hero)
				foundHero = True
		if not foundHero:
			return 0

	def view_all_heroes(self):
		for hero in self.heroes: 
			print(f"{hero.name}")
    

	def stats(self):
		for hero in self.heroes: 
			if hero.deaths > 0:
				kd = hero.kills / hero.deaths
			else: 
				kd = hero.kills
			print(f"{hero.name} Kill/Deaths:{kd}")

	def revive_heroes(self, health=100):
		for hero in self.heroes:
			hero.current_health = hero.starting_health

	def attack(self, other_team):
		living_heroes = list()
		living_opponents = list()

		for hero in self.heroes: 
			living_heroes.append(hero)

		for hero in other_team.heroes:
			living_opponents.append(hero)

		while len(living_heroes) > 0 and len(living_opponents) > 0:
			fighting_hero = random.choice(living_heroes)
			fighting_opponent = random.choice(living_opponents)

			if fighting_hero.fight(fighting_opponent) == 1:
				living_heroes.remove(fighting_hero)
			else:
				living_opponents.remove(fighting_opponent) 
