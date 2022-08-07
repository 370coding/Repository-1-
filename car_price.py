class Car:
    def __init__(self,make,model,year,price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.in_stock = True
    
    def price_after_down_pmt(self,percent):
        self.price = self.price * (1 - percent)

car_1 = Car ("Nissan","370Z",2017,20000)
car_1.price_after_down_pmt(0.1)
print(car_1.price)

