class Person:
    def __init__(self, full_name, driving_experience):
        self.full_name = full_name
        self.driving_experience = driving_experience


class Driver(Person):
    def __init__(self, full_name, driving_experience):
        super().__init__(full_name, driving_experience)


class Engine:
    def __init__(self, power, manufacturer):
        self.power = power
        self.manufacturer = manufacturer


class Car:
    def __init__(self, brand, car_class, weight, driver, engine):
        self.brand = brand
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def start(self):
        print("Поехали")

    def stop(self):
        print("Останавливаемся")

    def turn_left(self):
        print("Поворот налево")

    def turn_right(self):
        print("Поворот направо")

    def __str__(self):
        return f"Марка: {self.brand}, Класс: {self.car_class}, Вес: {self.weight} " \
               f"Водитель: {self.driver.full_name}, Стаж вождения: {self.driver.driving_experience}, Мотор: {self.engine.power}л.с., {self.engine.manufacturer}"


class Lorry(Car):
    def __init__(self, brand, car_class, weight, driver, engine, payload_capacity):
        super().__init__(brand, car_class, weight, driver, engine)
        self.payload_capacity = payload_capacity

    def __str__(self):
        return super().__str__() + f", Грузоподъемность: {self.payload_capacity} кг"


class SportCar(Car):
    def __init__(self, brand, car_class, weight, driver, engine, max_speed):
        super().__init__(brand, car_class, weight, driver, engine)
        self.max_speed = max_speed

    def __str__(self):
        return super().__str__() + f", Предельная скорость: {self.max_speed} км/ч"


driver1 = Driver("Иван Иванов", 5)
engine1 = Engine(200, "Toyota")
car1 = Car("Toyota Camry", "Седан", 1500, driver1, engine1)

driver2 = Driver("Анна Сидорова", 3)
engine2 = Engine(400, "Ferrari")
sport_car = SportCar("Ferrari 488", "Спорткар", 1500, driver2, engine2, 300)

driver3 = Driver("Петр Петров", 10)
engine3 = Engine(300, "Volvo")
lorry = Lorry("Volvo FH", "Грузовик", 8000, driver3, engine3, 5000)

print('Информация об автомобиле:\n' + str(car1))

car1.start()
car1.turn_left()
car1.stop()

print('Информация о грузовике:\n' + str(lorry))

lorry.start()
lorry.turn_left()
lorry.stop()

print('Информация о спорткаре:\n' + str(sport_car))

sport_car.start()
sport_car.turn_right()
sport_car.stop()


