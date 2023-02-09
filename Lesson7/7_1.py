'''Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.'''

from time import sleep
from datetime import datetime as dt

class TrafficLight:
    
    _states = {'Красный': 7, 'Желтый': 2, 'Зеленый': 10}
    _color = ''

    def running(self):
        
        for color, sw_time in self._states.items():
            self._color = color
            start_state_time = dt.now()

            print(f"Горит '{self._color}' ")

            sleep(sw_time)

           
if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()