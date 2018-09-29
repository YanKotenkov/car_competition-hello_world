#!/usr/bin/env python

from random import randint
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('dist', type=int, help='distance')
args = parser.parse_args()

CAR_SPECS = {
    'ferrary': {"max_speed": 340, "drag_coef": 0.324, "time_to_max": 26},
    'bugatti': {"max_speed": 407, "drag_coef": 0.39, "time_to_max": 32},
    'toyota': {"max_speed": 180, "drag_coef": 0.25, "time_to_max": 40},
    'lada': {"max_speed": 180, "drag_coef": 0.32, "time_to_max": 56},
    'sx4': {"max_speed": 180, "drag_coef": 0.33, "time_to_max": 44},
}


class Car:
    """doc"""
    def __init__(self, max_speed, drag_coef, time_to_max):
        self.max_speed = max_speed
        self.drag_coef = drag_coef
        self.time_to_max = time_to_max


class Weather:
    """doc"""
    def __init__(self, wind_speed):
        self.__wind_speed = wind_speed

    @property
    def wind_speed(self):
        return randint(0, self.__wind_speed)


class Competition:
    """doc"""
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Competition, cls).__new__(cls)
        else:
            raise Exception('Must be only once Competition instance')
        return cls.instance

    def __init__(self, distance):
        self.__distance = distance

    def start(self):
        print('Competition started', 'distance:', self.__distance)
        weather = Weather(20)
        competitors = get_competitors(CAR_SPECS)
        for competitor_name in competitors:
            competitor_time = 0
            car = competitors[competitor_name]

            for distance in range(self.__distance):
                _wind_speed = weather.wind_speed

                if competitor_time == 0:
                    _speed = 1
                else:
                    _speed = (competitor_time / car.time_to_max) * car.max_speed
                    if _speed > _wind_speed:
                        _speed -= (car.drag_coef * _wind_speed)

                competitor_time += float(1) / _speed

            print("Car <%s> result: %f" % (competitor_name, competitor_time))


def get_competitors(specs):
    cars = {}
    for name in specs:
        car_specs = specs[name]
        cars[name] = Car(car_specs['max_speed'], car_specs['drag_coef'], car_specs['time_to_max'])
    return cars

competition = Competition(args.dist)
competition.start()
