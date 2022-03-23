import string
import random
import time
from ship import Ship


# константы
STRING = string.ascii_lowercase[0:10:]
COORDINATES_DICTIONARY = dict(zip([i for i in string.ascii_lowercase[0:10:]],[i for i in range(10)]))

class Field:

    def __init__(self):
#клетки с кораблями
        self.ships = set()
#координаты ореолов       
        self.halos = set()
#сетка
        self.field = [[' '] * 10 for i in range(10)]
#количество живых кораблей
        self.number = 0
#демонстрация поля        
    def show(self):  #переделать под возврат(а надо?)
        print('   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |')
        field = self.get_field()
        string = STRING
        for i in range(10):
            print(f' {string[i]} | {field[i][0]} | {field[i][1]} | {field[i][2]} | {field[i][3]} | {field[i][4]} | {field[i][5]} | {field[i][6]} | {field[i][7]} | {field[i][8]} | {field[i][9]} | \n')
      
    def get_field(self):
        return self.field
        
    def get_point(self, x):
        return self.field[x[0]][x[1]]


#приземление снаряда в поле. X - кортеж координат, y - строка        
    def boom(self, x, y):
        self.field[x[0]][x[1]] = y
        
    def get_number(self):
        return self.number

    
    def get_string(self):
        return self.string
        
    

    def get_ships(self):
        return self.ships
        
    def get_halos(self):
        return self.halos
        
#прверка данных на вводе (координаты)
    def check_coord(self, x):
        while True:
            if len(x) == 2 and x[0] in STRING and int(x[1]) in range(10):
                return x
            else:
                x = input('enter correct coordinates :') 
#проверка данных на вводе (вращение)
    def check_rotation(self, x):
        while True:
            if len(x) == 1 and 0 <= int(x) <= 1:
                return x
            else:
                x = input('enter correct rotation (0 - vertical, 1 - horisontal) :')
            

#проверка на возможность постройки корабля (принимает координаты носа, длину и вращение         
    def is_build_possible(self, nose, length, rot):
        _output = []
        _ordinatt = COORDINATES_DICTIONARY[nose[0]]
        _abciss = int(nose[1])
        for i in range(length):
            if rot == 0:
                _output.append((_ordinatt, _abciss))
                _ordinatt += 1
            elif rot == 1:
                _output.append((_ordinatt, _abciss))
                _abciss += 1
        if set(_output) & self.get_ships():
            return False 
        if set(_output) & self.get_halos():
            return False
        else:
            return True
    
    def add_to_list(self, x):
        self.ships.update(x)
        
    def add_halos(self, x):
        self.halos.update(x)

#автодобавитель корабля    
    def autoadd(self, lenght, d):
        coord0 = STRING[random.randint(0, 9)]
        coord1 = str(random.randint(0, 9))
        nose = coord0 + coord1
        rot = random.randint(0, 1)
        lim = 10 - lenght
        while True:
            if rot == 0:
                if nose[0] in STRING[0:lim] and int(nose[1]) <= 9 and self.is_build_possible(nose, lenght, rot):
                    return lenght, nose, rot, d
                else:
                    coord0 = STRING[random.randint(0, 9)]
                    coord1 = random.randint(0, 9)
                    nose = coord0 + str(coord1)
                    rot = random.randint(0, 1)
            else:
                if nose[0] in STRING and int(nose[1]) <= lim and self.is_build_possible(nose, lenght, rot):
                    return lenght, nose, rot, d
                else:
                    coord0 = STRING[random.randint(0, 9)]
                    coord1 = random.randint(0, 9)
                    nose = coord0 + str(coord1)
                    rot = random.randint(0, 1)
                    
                    
#добавитель корабля    
    def addship(self, lenght, d): 
        nose = self.check_coord(input('input coordinates of nose :'))
        rot = int(self.check_rotation(input('enter rotation (0 - vertical, 1 - horisontal) :')))
        lim = 10 - lenght
        while True:
            if rot == 0:
                if nose[0] in STRING[0:lim] and int(nose[1]) <= 9 and self.is_build_possible(nose, lenght, rot):
                    return lenght, nose, rot, d
                      
                else:
                    nose = self.check_coord(input('input correct coordinates of nose: '))
                    rot = int(self.check_rotation(input('enter rotation (0 - vertical, 1 - horisontal) :')))
            else:
                if nose[0] in STRING and int(nose[1]) <= lim and self.is_build_possible(nose, lenght, rot):
                    return lenght, nose, rot, d
                else:
                    nose = self.check_coord(input('input correct coordinates of nose: '))
                    rot = int(self.check_rotation(input('enter rotation (0 - vertical, 1 - horisontal) :')))
#рисователь корабля
    def draw_ship(self, coord):
        if self.field[coord[0]][coord[1]] == ' ':
            self.field[coord[0]][coord[1]] = 'S'
#рисователь ореола            
    def draw_halo(self, coord):
        if self.field[coord[0]][coord[1]] == ' ':
            self.field[coord[0]][coord[1]] = 'O'



#Создание флота вручную
    def makefleet(self): 
        self.show()
        print('now building 4 desks Flagman')
        self.four_desks_ship = Ship(*(self.addship(4, COORDINATES_DICTIONARY)))
        self.four_desks_ship.build()
        self.four_desks_ship.make_halo()
        self.add_to_list(self.four_desks_ship.get_body())
        self.add_halos(self.four_desks_ship.get_halo())
        for i in self.get_ships():
            self.draw_ship(i)
        self.show()
        print('now building 3 desks cruiser')
        self.three_desks_ship_0 = Ship(*(self.addship(3, COORDINATES_DICTIONARY)))
        self.three_desks_ship_0.build()
        self.three_desks_ship_0.make_halo()
        self.add_to_list(self.three_desks_ship_0.get_body())
        self.add_halos(self.three_desks_ship_0.get_halo())
        for i in self.get_ships():
            self.draw_ship(i)
        self.show()
        print('now building second 3 desks cruiser')
        self.three_desks_ship_1 = Ship(*(self.addship(3, COORDINATES_DICTIONARY)))
        self.three_desks_ship_1.build()
        self.three_desks_ship_1.make_halo()
        self.add_to_list(self.three_desks_ship_1.get_body())
        self.add_halos(self.three_desks_ship_1.get_halo())
        for i in self.get_ships():
            self.draw_ship(i)
        self.show()
        print('now building 2 desks destroyer')
        self.two_desks_ship_0 = Ship(*(self.addship(2, COORDINATES_DICTIONARY)))
        self.two_desks_ship_0.build()
        self.two_desks_ship_0.make_halo()
        self.add_to_list(self.two_desks_ship_0.get_body())
        self.add_halos(self.two_desks_ship_0.get_halo())
        for i in self.get_ships():
            self.draw_ship(i)
        self.show()
        print('now building second 2 desks destroyer')
        self.two_desks_ship_1 = Ship(*(self.addship(2, COORDINATES_DICTIONARY)))
        self.two_desks_ship_1.build()
        self.two_desks_ship_1.make_halo()
        self.add_to_list(self.two_desks_ship_1.get_body())
        self.add_halos(self.two_desks_ship_1.get_halo())
        for i in self.get_ships():
            self.draw_ship(i)
        self.show()
        print('now building third 2 desks destroyer')
        self.two_desks_ship_2 = Ship(*(self.addship(2, COORDINATES_DICTIONARY)))
        self.two_desks_ship_2.build()
        self.two_desks_ship_2.make_halo()
        self.add_to_list(self.two_desks_ship_2.get_body())
        self.add_halos(self.two_desks_ship_2.get_halo())
        for i in self.get_ships():
            self.draw_ship(i)
        self.show()
        print('now building battle boat')
        self.one_desk_ship_0 = Ship(*(self.addship(1, COORDINATES_DICTIONARY)))
        self.one_desk_ship_0.build()
        self.one_desk_ship_0.make_halo()
        self.add_to_list(self.one_desk_ship_0.get_body())
        self.add_halos(self.one_desk_ship_0.get_halo())
        for i in self.get_ships():
            self.draw_ship(i)
        self.show()
        print('now building second battle boat')
        self.one_desk_ship_1 = Ship(*(self.addship(1, COORDINATES_DICTIONARY)))
        self.one_desk_ship_1.build()
        self.one_desk_ship_1.make_halo()
        self.add_to_list(self.one_desk_ship_1.get_body())
        self.add_halos(self.one_desk_ship_1.get_halo())
        for i in self.get_ships():
            self.draw_ship(i)
        self.show()
        print('now building third battle boat')
        self.one_desk_ship_2 = Ship(*(self.addship(1, COORDINATES_DICTIONARY)))
        self.one_desk_ship_2.build()
        self.one_desk_ship_2.make_halo()
        self.add_to_list(self.one_desk_ship_2.get_body())
        self.add_halos(self.one_desk_ship_2.get_halo())
        for i in self.get_ships():
            self.draw_ship(i)
        self.show()
        print('now building last battle boat')
        self.one_desk_ship_3 = Ship(*(self.addship(1, COORDINATES_DICTIONARY)))
        self.one_desk_ship_3.build()
        self.one_desk_ship_3.make_halo()
        self.add_to_list(self.one_desk_ship_3.get_body())
        self.add_halos(self.one_desk_ship_3.get_halo())
        for i in self.get_ships():
            self.draw_ship(i)
        self.show()
        self.fleet = [self.four_desks_ship,
                      self.three_desks_ship_0,
                      self.three_desks_ship_1,
                      self.two_desks_ship_0,
                      self.two_desks_ship_1,
                      self.two_desks_ship_2,
                      self.one_desk_ship_0,
                      self.one_desk_ship_1,
                      self.one_desk_ship_2,
                      self.one_desk_ship_3
                     ]
        self.number += len(self.fleet)


#генерация флота
    def autofleet(self):
        self.four_desks_ship = Ship(*(self.autoadd(4, COORDINATES_DICTIONARY)))
        self.four_desks_ship.build()
        self.four_desks_ship.make_halo()
        self.add_to_list(self.four_desks_ship.get_body())
        self.add_halos(self.four_desks_ship.get_halo())
        self.three_desks_ship_0 = Ship(*(self.autoadd(3, COORDINATES_DICTIONARY)))
        self.three_desks_ship_0.build()
        self.three_desks_ship_0.make_halo()
        self.add_to_list(self.three_desks_ship_0.get_body())
        self.add_halos(self.three_desks_ship_0.get_halo())
        self.three_desks_ship_1 = Ship(*(self.autoadd(3, COORDINATES_DICTIONARY)))
        self.three_desks_ship_1.build()
        self.three_desks_ship_1.make_halo()
        self.add_to_list(self.three_desks_ship_1.get_body())
        self.add_halos(self.three_desks_ship_1.get_halo())
        self.two_desks_ship_0 = Ship(*(self.autoadd(2, COORDINATES_DICTIONARY)))
        self.two_desks_ship_0.build()
        self.two_desks_ship_0.make_halo()
        self.add_to_list(self.two_desks_ship_0.get_body())
        self.add_halos(self.two_desks_ship_0.get_halo())
        self.two_desks_ship_1 = Ship(*(self.autoadd(2, COORDINATES_DICTIONARY)))
        self.two_desks_ship_1.build()
        self.two_desks_ship_1.make_halo()
        self.add_to_list(self.two_desks_ship_1.get_body())
        self.add_halos(self.two_desks_ship_1.get_halo())
        self.two_desks_ship_2 = Ship(*(self.autoadd(2, COORDINATES_DICTIONARY)))
        self.two_desks_ship_2.build()
        self.two_desks_ship_2.make_halo()
        self.add_to_list(self.two_desks_ship_2.get_body())
        self.add_halos(self.two_desks_ship_2.get_halo())
        self.one_desk_ship_0 = Ship(*(self.autoadd(1, COORDINATES_DICTIONARY)))
        self.one_desk_ship_0.build()
        self.one_desk_ship_0.make_halo()
        self.add_to_list(self.one_desk_ship_0.get_body())
        self.add_halos(self.one_desk_ship_0.get_halo())
        self.one_desk_ship_1 = Ship(*(self.autoadd(1, COORDINATES_DICTIONARY)))
        self.one_desk_ship_1.build()
        self.one_desk_ship_1.make_halo()
        self.add_to_list(self.one_desk_ship_1.get_body())
        self.add_halos(self.one_desk_ship_1.get_halo())
        self.one_desk_ship_2 = Ship(*(self.autoadd(1, COORDINATES_DICTIONARY))) 
        self.one_desk_ship_2.build()
        self.one_desk_ship_2.make_halo()
        self.add_to_list(self.one_desk_ship_2.get_body())
        self.add_halos(self.one_desk_ship_2.get_halo())
        self.one_desk_ship_3 = Ship(*(self.autoadd(1, COORDINATES_DICTIONARY)))
        self.one_desk_ship_3.build()
        self.one_desk_ship_3.make_halo()
        self.add_to_list(self.one_desk_ship_3.get_body())
        self.add_halos(self.one_desk_ship_3.get_halo())
        self.fleet = [self.four_desks_ship,
                      self.three_desks_ship_0,
                      self.three_desks_ship_1,
                      self.two_desks_ship_0,
                      self.two_desks_ship_1,
                      self.two_desks_ship_2,
                      self.one_desk_ship_0,
                      self.one_desk_ship_1,
                      self.one_desk_ship_2,
                      self.one_desk_ship_3
                     ]
        self.number += len(self.fleet)
        for i in self.get_ships():
            self.draw_ship(i)



class Player:
    
    def __init__(self):
        self.field = Field()
        self.enemyfield = Field()
        self.shots = []      
        self.name = 'You'          
#заряжаем пушку       
    def gun(self): 
        shot = self.enemyfield.check_coord(input('enter coordinates to fire: '))
        while True:
            if shot not in self.shots:
                self.shots.append(shot)
                return shot
            else:
                shot = self.enemyfield.check_coord(input('you already shot this point, please, enter coordinates to fire: '))
            
                           
#создаём поле              
    def makefield(self):
        answer = input('do you want to manual make your fleet (m) or generate them (g)? :')
        while True:
            if answer == 'm':
                self.field.makefleet()
                break
            elif answer == 'g':
                self.field.autofleet()
                break
            else:
                answer = input('please enter "m" to make your fleet or "g" to generate them :')  

    def get_name(self):
        return self.name     
    
#стреляем    
    def fire(self):
        shot = self.gun()
        while True:
            if self.enemyfield.check_coord(shot):
                missle = tuple([int(COORDINATES_DICTIONARY[shot[0]]), int(shot[1])])
                return missle
            else:
                shot = self.gun()
            
#ход         
    def turn(self, enemy):
        print('humans turn')
        while True:
            hit = self.fire()
            if enemy.field.get_point(hit) == ' ':
                enemy.field.boom(hit, 'O')
                self.enemyfield.boom(hit, 'O')
                break
            elif enemy.field.get_point(hit) == 'S':
                enemy.field.boom(hit, 'X') 
                self.enemyfield.boom(hit, 'X')
                print('Hit!, shoot more!')
                for i in enemy.field.fleet:
                    i.damage(hit)
                    i.alivecheck()
                    if i.is_alive() == False:
                        enemy.field.number -= 1
                        for j in i.get_halo():
                            enemy.field.draw_halo(j)
                            self.enemyfield.draw_halo(j)
                        print('kill')
                        enemy.field.fleet.remove(i)    
            elif enemy.field.get_point(hit) == 'O':
                print('moloko! hit another one time')

                 
 

class Bot(Player):

    def __init__(self):
        self.field = Field()
        self.enemyfield = Field()
        self.shots = []
        self.name = 'Bot'
    
    def gun(self):
        coord0 = STRING[random.randint(0, 9)]
        coord1 = str(random.randint(0, 9))
        shot = coord0 + coord1
        while True:
            if shot not in self.shots:
                self.shots.append(shot)
                return shot
            else:
                coord0 = STRING[random.randint(0, 9)]
                coord1 = str(random.randint(0, 9))
                shot = coord0 + coord1         

    def makefield(self):
        self.field.autofleet()
        
    def turn(self, enemy):
        print('enemies turn')
        while True:
            hit = self.fire()
            if enemy.field.get_point(hit) == ' ':
                enemy.field.boom(hit, 'O')
                break
            elif enemy.field.get_point(hit) == 'S':
                enemy.field.boom(hit, 'X') 
                for i in enemy.field.fleet:
                    i.damage(hit)
                    i.alivecheck()
                    if i.is_alive() == False:
                        enemy.field.number -= 1
                        for j in i.get_halo():
                            enemy.field.draw_halo(j)
                        enemy.field.fleet.remove(i)

            
            

  
             
               
               
               
               
               
                             
class Greet:
    def __init__(self):
        print('welcome to Battleships game!')
        #time.sleep(3)
        print('you and bot have the fleet: one Flagman, two cruisers, three destroyers and four boats')
        #time.sleep(3)
        print('you and bot fights with gun shots looks as "LetterDidgit" string (as "f6")')
        #time.sleep(3)
        print('who alives - wins. Good luck!')

    

               
class Game:
    
    def __init__(self):
        
        print('initialization of a new game')
        self.helper = Greet()
        self.human = Player()
        self.bot = Bot()
        self.players = [self.human, self.bot]
        for i in self.players:
            i.makefield()
        self.human.field.show()
        print('it is your field')
        #time.sleep(3)
        self.human.enemyfield.show()
        print('it is blank field, shoot here!')
#        self.turns = [self.human.turn(self.bot), self.bot.turn(self.human)]

    def iface(self):
        myfield = self.human.field.get_field()
        notmy_field = self.human.enemyfield.get_field()
        print('   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |                 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |')
        for i in range(10):
            print(f' {STRING[i]} | {myfield[i][0]} | {myfield[i][1]} | {myfield[i][2]} | {myfield[i][3]} | {myfield[i][4]} | {myfield[i][5]} | {myfield[i][6]} | {myfield[i][7]} | {myfield[i][8]} | {myfield[i][9]} |               {STRING[i]} | {notmy_field[i][0]} | {notmy_field[i][1]} | {notmy_field[i][2]} | {notmy_field[i][3]} | {notmy_field[i][4]} | {notmy_field[i][5]} | {notmy_field[i][6]} | {notmy_field[i][7]} | {notmy_field[i][8]} | {notmy_field[i][9]} |\n')
                


    def action(self):
        a = self.human.field.get_number()
        b = self.bot.field.get_number()
        while a != 0 and b != 0:
            self.iface()
            self.human.turn(self.bot)
            b = self.bot.field.get_number()
            self.iface()
            self.bot.turn(self.human)
            a = self.human.field.get_number()
        if a == 0:
            print('Bot win')
        else:
            print('You win')

if __name__ == '__main__':
    do = 'y'
    while do == 'y':
        game = Game()
        game.action()
        do = input('do you want one more game? (y/n): ')
    print('goodbye')
