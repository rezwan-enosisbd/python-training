class Car():
  def __init__(self, name, color, price):
    self.name = name
    self.color = color
    self.price = price

class CarPriceMixin:
  def clearance_price(self):
    return self.price * .5

class ShowRoomCar(Car, CarPriceMixin):
  pass

mycar1 = ShowRoomCar('BMW', 'red', 200)
print(mycar1.clearance_price())