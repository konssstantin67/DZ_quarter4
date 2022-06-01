
class car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police

    def go(self):
        print(f'первый первый, я база {self.name} цвет {self.color} начала движение')

    def stop(self):
        print(f'первый первый, я база {self.name} цвет {self.color} остановился')

    def turn(self, sides):
        self.sides = sides
        print(f'первый первый, я база {self.name} цвет {self.color} свернула на {self.sides}')

    def speed_control(self):
        print(f'первый первый, я база {self.name} цвет {self.color} движется со скоростью {self.speed}')

    def this_police(self):
        print(f'это едут полицаи {self.is_police}') if self.is_police==True else print('кажись пронесло - не полицаи')


class town_car(car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def this_police(self):
        print(f'это едут полицаи {self.is_police}') if self.is_police==True else print('кажись пронесло - не полицаи')


    def speed_control(self):
        print(f'первый первый, я база {self.name} цвет {self.color} движется со скоростью {self.speed}') if self.speed <=60 \
            else print(f'первый первый, я база {self.name} цвет {self.color} движется с превышением скорости')


class sport_car(car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def speed_control(self):
        print(f'первый первый, я база {self.name} цвет {self.color} движется со скоростью {self.speed}') if self.speed <=60 \
            else print(f'первый первый, я база {self.name} цвет {self.color} движется с превышением скорости')

    def this_police(self):
        print(f'это едут полицаи {self.is_police}') if self.is_police==True else print('кажись пронесло - не полицаи')

class work_car(car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def speed_control(self):
        print(f'первый первый, я база {self.name} цвет {self.color} движется со скоростью {self.speed}') if self.speed <=40 \
            else print(f'первый первый, я база {self.name} цвет {self.color} движется с превышением скорости')

    def this_police(self):
        print(f'это едут полицаи {self.is_police}') if self.is_police==True else print('кажись пронесло - не полицаи')

class police(car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

c,t,s,w,p = car (45, 'баклажан', 'lada'), town_car (48, 'грязный', 'gazel'),sport_car (80, 'ржавый', 'VAZ 2107'), \
    work_car (39, 'синий', 'ZIL'), police (90, 'бело-синяя', 'UAZ')

# s.go(), s.speed_control(), s.turn('34 градуса в лево'), s.stop()
# t.go(), t.speed_control(), t.turn('право'), t.stop(), t.this_police()
w.go(), w.speed_control(), w.turn('район, за пивасом'), w.stop(), w.this_police()
# p.go(), p.speed_control(), p.turn('по бабам'), p.stop(), p.this_police()
