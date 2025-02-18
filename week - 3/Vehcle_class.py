class Vehicle:
    def __init__(self, make, model):
        self.make = make  
        self._model = model   # Encapsulation 

    


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.__num_doors = num_doors  # Encapsulation 

    def get_num_doors(self):  # getter for private attribute
        return self.__num_doors



    def describe(self):  # Polymorphism
        return f"{self._model} has {self.__num_doors} doors."


class Bike(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def describe(self):  # polymorphism 
        return f"{self._model} is a new  bike model."


car1 = Car('Honda', 'Honda Civic', 4)
print('Manufacturer : ', car1.make)
print('Model : ', car1._model)
print(car1.describe())
bike1 = Bike('Royal Enfield', 'REG-450')
print('Manufacturer : ', bike1.make)
print('Model : ', bike1._model)
print(bike1.make, bike1.describe())
