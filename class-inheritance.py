class Enemy:
   atk = 10
   def attack(self):
      print("Enemy attack! -" + str(self.atk))

   def special_attack(self):
      print("Enemy throws spears!")
   
class Ninja(Enemy):
   atk = 15
   def special_attack(self):
      print("Ninja throws Shuriken!")

enemy1 = Enemy()
enemy2 = Ninja()

enemy1.attack()
enemy2.attack()

enemy1.special_attack()
enemy2.special_attack()