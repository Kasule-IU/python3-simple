import random


#classes
class Player(object):

    def __init__(self, name, health, strength,tough):
        self.name = name
        self.health = health
        self.strength = strength
        self.tough = tough

    def __repr__(self):
        return 'Player(' + repr(self.name) + ', ' + 'health: ' + repr(self.health) + ', ' + 'strength: ' + repr(self.strength) + 'toughness: ' + repr(self.tough) + ')'


            
class Monster(object):

    def __init__(self, name, health, strength,tough):
        self.name = name
        self.health = health
        self.strength = strength
        self.tough = tough

    def __repr__(self):
        return 'Monster(' + repr(self.name) + ', ' + repr(self.health) + ', ' + repr(self.strength) +  repr(self.tough) +')'


#functions
def attack(obj1,obj2):
    if obj1.health > 0:
        obj2.health = obj2.health + obj2.tough - obj1.strength
        return obj2.health

def defend(obj1):
    obj1.health = obj1.health + 5
    return obj1.health
        
        

        






#main

inv = []

monster_lst = ['wretched spider','putrid slime','corrupted trent']
random_monster = random.choice(monster_lst)
userName = input('What is your name, noble warrior? > ')

main_player = Player(userName,9,5,0)

print('Welcome to Innistrad,',userName)
print("You're under attack!!")
print('Type "attack" to attack the monster in front of you.')
print('The monster in front of you is a', str(random_monster))
first_monster = Monster(random_monster,10,1,0)

input1 = input('> ')
while True:
    if input1.lower() == 'attack':
        print('You attack the', random_monster)
        attack(main_player,first_monster)
        if first_monster.health <= 0:
            print('Congratulations, you have slain your first enemy!')
            break
        if first_monster.health > 0:
            while first_monster.health > 0:
                attack(first_monster, main_player)
                print('The', random_monster, 'attacks you for 1 HP')
                attack(main_player,first_monster)
                print('You hit the',random_monster,'with your mighty fists')
    else:
        print('Not vaild input')
        input1 = input('> ')

print('You are ready to continue on your quest.')
print('Here in Innistrad, there are many horrors.')
print('Horrors much worse than the',random_monster,'that you just faced.')
print('Here, take this health potion.  Drink it now, you deserve it for defeating your first beast.')
print('Potion added to inventory.  Will you drink it now? Y/N')

input2 = input('> ')
while True:
    if input2.lower() == 'y':
        break
    elif input2.lower() == 'n':
        break
    else:
        print('Not a valid input')
        input2 = input('Type "Y" or "N" >')

while True:
    if input2.lower() == 'y':
        print('You drop to your knees, hearing a voice say, "Fool!"')
        print('You wake up in a room with the man from earlier staring at you, greatsword in hand.  What do you do?')
        input3 = input('pick up great scythe in the corner(input GS)/pick up large club on table(input (LC)/attack the man with your fists (input FISTS) >')

        if input3.lower() == 'gs':
            inv.append('great scythe')
            print('Great Scythe added to inventory')
            break
        
        elif input3.lower() == 'lc':
            inv.append('large club')
            print('Large Club added to inventory')
            break
        
        elif input3.lower() == 'fists':
            print("You're a true man")
            break

        else:
            print('Not a vaild input')
            input4 = input('GS/LC/FISTS > ')
    

    elif input2.lower() == 'n':
        print('You notice two weapons, a great scythe and a large club.  Do those strike your fancy?  Or do prefer to use your fists?')
        input4 = input('great scythe-> type GS / large club -> type LC / fists -> type FISTS >')

        if input4.lower() == 'gs':
            inv.append('great scythe')
            print('Great Scythe added to inventory')
            break
        
        elif input4.lower() == 'lc':
            inv.append('large club')
            print('Large Club added to inventory')
            break
        
        elif input4.lower() == 'fists':
            print("You're a true man")
            break
        else:
            print('Not a vaild input')
            input4 = input('GS/LC/FISTS > ')
        

tutorial_boss = Monster('Innistrad Tutor',50,4,0)

if 'great scythe' in inv:
    main_player.strength = 10

if 'large club' in inv:
    main_player.strength = 6
    main_player.tough = 1

if inv == []:
    main_player.tough =  2

    

print('The Innistrad tutor has challenged you.  Choose to "attack" or "defend"')

input5 = input('> ')

while True:
    if input5 == 'attack':
        print('You attack!')
        attack(main_player,tutorial_boss)
        print('Innistrad Tutor swings his greatsword at you!')
        attack(tutorial_boss,main_player)
    elif input5 == 'defend':
        print('3 HP recovered')
        defend(main_player)
        print('Innistrad Tutor swings his greatsword at you!')
        attack(tutorial_boss,main_player)
    else:
        print('Not a valid input')
    print('You have', str(main_player.health),'HP')
    print('Enemy Innistrad Tutor has ',str(tutorial_boss.health), 'HP')

    if main_player.health <= 0:
        print('GAME OVER')
        break
    elif tutorial_boss.health <= 0:
        print('You have slain the tutor of Innistrad')
        break
    else:
        input5 = input('"attack" or "defend" ?  > ')

print('Current status')
print(main_player)
print('Inventory')
print(inv)

print('Now, the REAL adventure begins!')


    
    
    









    
    
