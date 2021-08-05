class Car():
    "汽车之家"

    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("行驶里程" + str(self.odometer_reading) + '千米')


class Bmw(Car):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)


my_tesla = Bmw('宝马', '535li', '2018')
my_favor = Car('奔驰', '535li', '2018')
print(my_tesla.get_descriptive_name())
print(my_favor.get_descriptive_name())

