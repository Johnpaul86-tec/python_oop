# ---------------- Assignment 1: Smartphone Example ----------------
class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def ring(self):
        print(f"{self.brand} {self.model} is ringing")


# Subclass (Inheritance + Polymorphism)
class GamingPhone(Smartphone):
    def ring(self):   # overrides base method
        print(f"{self.brand} {self.model} plays a cool gaming sound instead of ringing!")


# Create objects
my_phone = Smartphone("Samsung", "Galaxy G4")
gamer_phone = GamingPhone("Asus", "ROG Phone 8")

# Demonstration
my_phone.ring()       # Samsung Galaxy G4 is ringing
gamer_phone.ring()    # Asus ROG Phone 8 plays a cool gaming sound instead of ringing!


# ---------------- Activity 2: Vehicle Example ----------------
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print(f"{self.brand} {self.model} - the vehicle is moving...")


class Plane(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} - the plane is flying in the sky!")


class Boat(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} - the boat is sailing on the water.")


class Bicycle(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} - the bicycle is pedaling along the path.")


# Create objects
my_car = Vehicle("Ford", "Mustang")
my_plane = Plane("Kenya", "Airways")
my_boat = Boat("Titanic", "Cruise")
my_bike = Bicycle("Giant", "Escape 3")

# Demonstration
print(my_car.brand)   
my_car.move()       
my_plane.move()     
my_boat.move()      
my_bike.move()
