from random  import randint
from Team import *

printActionDescription = True

def dprint(s):
    if printActionDescription:
        print(s)

#Constants for Mage Type        
manaCost = 20
manaRecovery = 30


class Character(object):
    def __init__(self):
        self.name = ''
        self.maxhp = 1000
        self.hp = 1000
        self.str = 0
        self.maxmana = 0
        self.mana = 0
        self.cost = 9999999999
        self.alive = True

    def act(self,myTeam,enemy):
        return

    def gotHurt(self,damage):
        if damage >= self.hp:
            self.hp = 0
            self.alive = False
            dprint(self.name + ' died!')
        else:
            self.hp -= damage
            dprint(self.name +
                   f' hurt with remaining hp {self.hp}.')

    

class Fighter(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Fighter'
        self.maxhp = 1200
        self.hp = 1200
        self.str = 100
        self.cost = 100

    def act(self,myTeam,enemy):
        target = randAlive(enemy)
        dprint(f'Hurt enemy {target} by damage {self.str}.')
        enemy[target].gotHurt(self.str)
  

class Mage(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Mage'
        self.maxmana = 50
        self.mana = 50
        self.hp = 800
        self.maxhp = 800
        self.cost = 200
        self.int = 400

    def cast(self,myTeam,enemy):
        self.mana -= manaCost
        target = randAlive(enemy)
        dprint(f'Strike enemy {target} with spell')
        enemy[target].gotHurt(self.int)
        
    def act(self,myTeam,enemy):
        if self.mana < manaCost:
            self.mana += manaRecovery
            dprint(f'Mana recover to {self.mana}.')
        else:
            self.cast(myTeam,enemy)


class Berserker(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Berserker'
        self.maxhp = 1200
        self.hp = 1200
        self.str = 100
        self.cost = 200
        self.stat = 0
        

    def act(self,myTeam,enemy):
        if self.hp < self.maxhp//2 and self.stat ==0:
            self.str = self.str*2
            self.stat = 1
            dprint("Beserk mode! Attack double!")
        target = randAlive(enemy)
        dprint(f'Hurt enemy {target} by damage {self.str}.')
        enemy[target].gotHurt(self.str)


class ArchMage(Character):
    def __init__(self):
        super().__init__()
        self.name = 'ArchMage'
        self.maxmana = 50
        self.mana = 50
        self.hp = 800
        self.maxhp = 800
        self.cost = 600
        self.int = 400

    def cast(self,myTeam,enemy):
        self.mana -= manaCost
        target = randAlive(enemy)
        dprint(f'Strike enemy {target} with spell')
        enemy[target].gotHurt(self.int)

    def KABOOM(self,myTeam,enemy):
        self.mana-=manaCost
        for i in enemy:
            i.gotHurt(self.int*2)
        dprint(f"Cast KABOOOOOOMM ! (Damage {self.int*2}) to every enemy!")
        
    def act(self,myTeam,enemy):
        c = 0
        for i in myTeam:
            if i.alive == True:
                c+=1
        if c==1:
            self.KABOOM(myTeam,enemy)
        else:
            if self.mana < manaCost:
                self.mana += manaRecovery
                dprint(f'Mana recover to {self.mana}.')
            else:
                self.cast(myTeam,enemy)

class Necromancer(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Necromancer'
        self.maxhp = 600
        self.hp = 600
        self.cost = 600
        self.maxmana = 50
        self.mana = 50
        self.int = 400


    def cast(self,myTeam,enemy):
        self.mana -= manaCost
        target = randAlive(enemy)
        dprint(f'Strike enemy {target} with spell')
        enemy[target].gotHurt(self.int)


    def healcast(self,myTeam,enemy):
        self.mana-= manaCost
        target = randDeath(myTeam)
        add_hp = myTeam[target].maxhp//2
        myTeam[target].hp+=add_hp
        myTeam[target].alive = True
        dprint(f"Reving member {target} with hp {add_hp}")

    def act(self,myTeam,enemy):

        if self.mana < manaCost:
            self.mana += manaRecovery
            dprint(f'Mana recover to {self.mana}.')

            
        elif allAlive(myTeam):
            self.cast(myTeam,enemy)
        else:
            for i in myTeam:
                if i.hp==0:
                    self.healcast(myTeam,enemy)
                    break
        
        
   
    
