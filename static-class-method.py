class Car():
  car_counter = 0
  def __init__(self, name, color, price):
    self.name = name
    self.color = color
    self.price = price
    Car.car_counter += 1

  @staticmethod
  def convert_price_dollar_to_taka(price):
    return price * 116

  @classmethod
  def display_car_counter(cls):
    print(Car.car_counter)


mycar1 = Car('BMW', 'green', 100)
mycar2 = Car('Mercedes', 'green', 110)
print(Car.convert_price_dollar_to_taka(100))
Car.display_car_counter()