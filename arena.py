from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
	def __init__(self):
		'''Instantiate properties
				team_one: None
		  	team_two: None
    '''
		self.team_one = None
		self.team_two = None

	def create_ability(self):
		'''Prompt for Ability Information.
			 return Ability with values from user Input
		'''
		name = input("What is the ability name? ")
		max_damage = int(input("What is the max damage of the ability? "))

		return Ability(name, max_damage)

	def create_weapon(self):
		'''Prompt user for Weapon information
			 return Weapon with values from user Input
		'''
		name = input("What is the weapon name? ")
		max_damage = int(input("What is the max damage of the weapon?"))

		return Weapon(name, max_damage)

	def create_armor(self):
		'''Prompt user for Armor infromation
			return Armor with values from user Input
		'''
		name = input("What is the armor name? ")
		max_block = int(input("What is the max block of the weapon? "))
		return Armor(name, max_block)

	def create_hero(self):
		'''Prompt user for Hero information
			 return Hero with values from user Input
		'''
		hero_name = input("Hero's name: ")
		hero = Hero(hero_name)
		add_item = None
		while add_item != "4":
			add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
			if add_item == "1":
        # TODO add an ability to the hero
        # HINT: First create the ability, then add it to the hero
				ability = self.create_ability()
				hero.add_ability(ability)
			elif add_item == "2":
        # TODO add a weapon to the hero
        # HINT: First create the weapon, then add it to the hero
				weapon = self.create_weapon()
				hero.add_weapon(weapon)
			elif add_item == "3":
        # TODO add an armor to the hero
        # HINT: First create the armor, then add it to the hero
				armor = self.create_armor()
				hero.add_armor(armor)
		return hero


	def build_team_one(self):
		'''Prompt the user to build team_one'''
		team_name = input("What is the name of team one? ")
		self.team_one = Team(team_name)
		numOfTeamMembers = int(input(f"How many members would you like on {team_name}?\n"))
		for i in range(numOfTeamMembers):
			hero = self.create_hero()
			self.team_one.add_hero(hero)

	def build_team_two(self):
		'''Prompt the user to build team_one'''
		team_name = input("What is the name of team two? ")
		self.team_two = Team(team_name)
		numOfTeamMembers = int(input(f"How many members would you like on {team_name}?\n"))
		for i in range(numOfTeamMembers):
			hero = self.create_hero()
			self.team_two.add_hero(hero)

	def team_battle(self):
		self.team_one.attack(self.team_two)

	def show_stats(self):
		pass

	def show_stats(self):
		'''Prints team statistics to terminal.'''
		# TODO: This method should print out battle statistics
		# including each team's average kill/death ratio.
		# Required Stats:
		#     Show surviving heroes.
		#     Declare winning team
		#     Show both teams average kill/death ratio.
		# Some help on how to achieve these tasks:
		# TODO: for each team, loop through all of their heroes,
		# and use the is_alive() method to check for alive heroes,
		# printing their names and increasing the count if they're alive.
		#
		# TODO: based off of your count of alive heroes,
		# you can see which team has more alive heroes, and therefore,
		# declare which team is the winning team
		#
		# TODO for each team, calculate the total kills and deaths for each hero,
		# find the average kills and deaths by dividing the totals by the number of heroes.
		# finally, divide the average number of kills by the average number of deaths for each team

		print("\n")
		print(self.team_one.name + " statistics: ")
		self.team_one.stats()
		print("\n")
		print(self.team_two.name + " statistics: ")
		self.team_two.stats()
		print("\n")

		self.calculateKD(self.team_one)
		self.calculateKD(self.team_two)

		# Here is a way to list the heroes from Team One that survived
		team1Survivors = self.listSurvivors(self.team_one)
		team2Survivors = self.listSurvivors(self.team_two)

		if team1Survivors > team2Survivors: 
			print(f"{self.team_one.name} wins!")
		elif team2Survivors > team1Survivors: 
			print(f"{self.team_two.name} wins!")
		else:
			print("It's a tie!")


	def calculateKD(self, team): 
		team_kills = 0
		team_deaths = 0
		for hero in team.heroes:
			team_kills += hero.kills
			team_deaths += hero.deaths
		if team_deaths == 0:
			team_deaths = 1
		print(team.name + " average K/D was: " + str(team_kills/team_deaths))

	def listSurvivors(self, team):
		survivors = 0
		for hero in team.heroes:
			if hero.deaths == 0:
				survivors += 1
				print("survived from " + team.name + ": " + hero.name)
		return survivors

if __name__ == "__main__":
	playAgain = True

	while playAgain:
		arena = Arena()
		arena.build_team_one()
		arena.build_team_two()
		arena.team_battle()
		arena.show_stats()
		playerChoice = input("Play again? (y/n) ")
		if playerChoice.lower() == 'n':
			playAgain = False


