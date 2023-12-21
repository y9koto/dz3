import random

class Human:
    def __init__(self, name, home=None, car=None):
        self.name = name
        self.money = 200
        self.enjoyment = 100
        self.home = home
        self.car = car

    def get_home(self, home):
        if home != None:
            print("Продали будинок")
        self.home = home
        print("Придбали новий будинок")

    def get_car(self, car):
        if car != None:
            print(f"Продали авто марки {car.marka}")
        self.car = car
        print(f"Придбана автівка, марка {car.marka}")

    def work(self):
        print("Ідем працювати :(")
        money = random.randint(5, 20)
        print(f"Сьогодні заробили {money}$")
        self.money += money
        self.enjoyment -= 5
        self.home.food -= 2

    def chill(self):
        print("Відпочиваємо")
        enjoyment = random.randint(3, 8)
        print(f"Ви відпочили, і почуваєтесь на всі {enjoyment} процентів!")
        self.enjoyment += enjoyment

    def shopping(self):
        if self.car != None:
            print(f"Ідем за покупками")
        else:
            print(f"Їдемо на {self.car.marka} за покупками")

        money = random.randint(5, 20)
        print(f"я сьогодні був у магазині і витратив {money}$")
        self.money -= money
        self.home.food += random.randint(5, 10)
        self.enjoyment += random.randint(-5, 5)


    def clean_house(self):
        if self.home == None:
            print(f"ти не можешь прибратися")
        else:
            print("пішли прибиратися")
            self.home.cleanlinies_level += 1
            self.enjoyment -= 3

    def life(self):
        r = random.randint(1, 4)
        if r == 1:
            self.work()
        elif r == 2:
            self.chill()
        elif r == 3:
            self.clean_house()

        if self.money < 20:
            self.work()

        if self.enjoyment < 10:
            self.chill()

        if self.money > 500:
            self.get_car(Car("BMW X22"))
            self.money -= 500

    def is_alive(self):
        if self.money <= 0 or self.home.food <= 0:
            return False
        return True

    def info(self):
        print("===============================")
        print(f"Стан {self.name}:")
        print(f"Рівень задоволення - {self.enjoyment}")
        print(f"Залишок грошей     - {self.money}")
        print(f"Наявність їжі      - {self.home.food}")
        print(f"Порядок в кімнаті  - {self.home.cleanlinies_level}")




class Car:
    def __init__(self, marka):
        self.marka = marka
        self.passengers = []

    def add_passenger(self, *human):
        for h in human:
            self.passengers.append(h)

    def passengers_info(self):
        print(f"Авто {self.marka}, ", end='')
        if self.passengers != []:
            print(f"зараз в салоні:")
            for p in self.passengers:
                print(p.name)
        else:
            print("пасажири відсутні.")


class Home:
    def __init__(self):
        self.food = 50
        self.cleanlinies_level = 50




human = Human("Serg", car=Car("BMW X6"), home=Home())
day = 1
while(human.is_alive()):
    print()
    print(f"День {day}")
    human.life()
    human.info()
    day += 1

'''car = Car("BMW M5 F90")
car.add_passenger(human1, human2, human3)
car.passengers_info()'''