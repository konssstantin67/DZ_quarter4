import  time

class trafficlight:
    __color = [('красный', 7), ('желтый', 3), ('зеленый', 5)]
    def running(self):
        for c, t in self.__color:
            print(f'{c} включен на {t} секунд')
            time.sleep(t)

a = trafficlight()
trafficlight.running(a)