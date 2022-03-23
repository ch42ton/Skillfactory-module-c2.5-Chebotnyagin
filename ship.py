class Ship:
    def __init__(self, length, nose, rotation, dictionary):
        self.nose = tuple([int(dictionary[nose[0]]), int(nose[1])])
        self.length = length
        self.hp = length
        self.rotation = rotation
        self.body = []
        self.alive = bool()
        self.halo = []

    def alivecheck(self):
        if self.hp == 0:
            self.alive = False

            
    def is_alive(self):
        return self.alive
                
    def get_nose(self):
        return self.nose

    def get_length(self):
        return int(self.length)

    def get_rotation(self):
        return self.rotation

    def get_hp(self):
        return self.hp

    def get_body(self):
        return self.body
    
    def get_halo(self):
        return self.halo
        
    def damage(self, coord):
        if coord in self.body:
            self.hp -= 1

    def build(self):
        self.body.append(self.get_nose())
        y = self.get_nose()[0]
        x = self.get_nose()[1]
        for i in range(self.get_length() - 1):
            if self.get_rotation() == 0:
                y += 1
                self.body.append((y, x))
            elif self.get_rotation() == 1:
                x += 1
                self.body.append((y, x))
        self.alive = True





    def make_halo(self):
        ship = self.get_body()
        if self.get_rotation() == 1:
            for i in ship:
                if i[0] > 0:
                    y = i[0] - 1
                    self.halo.append((y, i[1]))
                if i[0] < 9:
                    y = i[0] + 1
                    self.halo.append((y, i[1]))            
            if ship[0][1] > 0:
                x = ship[0][1] - 1
                self.halo.append((ship[0][0], x))
            if ship[-1][1] < 9:
                x = ship[-1][1] + 1
                self.halo.append((ship[-1][0], x))         
        else:
            for i in ship:
                if i[1] > 0:
                    x = i[1] - 1
                    self.halo.append((i[0], x))
                if i[1] < 9:
                    x = i[1] + 1
                    self.halo.append((i[0], x))    
            if ship[0][0] > 0:
                y = ship[0][0] - 1
                self.halo.append((y, ship[0][1]))
            if ship[-1][0] < 9:
                y = ship[-1][0] + 1
                self.halo.append((y, ship[-1][1]))        
        
        
        


            
              
                  
                        

















