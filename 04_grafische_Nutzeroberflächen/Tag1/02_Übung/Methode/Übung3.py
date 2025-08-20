class Car:
    total_cars = 10

    @classmethod
    def increment_total_cars(cls):
        cls.total_cars += 1


Car.increment_total_cars()
print(Car.total_cars)
