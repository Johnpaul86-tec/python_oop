📱🚗 Python OOP Assignment – Smartphone & Vehicle Examples
🧠 Overview
This project demonstrates Object-Oriented Programming (OOP) principles in Python through two practical examples:

A Smartphone class with a specialized GamingPhone subclass

A Vehicle class extended by Plane, Boat, and Bicycle subclasses

Key concepts covered:

Classes & Objects

Inheritance

Polymorphism

Method Overriding

📱 Assignment 1: Smartphone Example
🔧 Classes
Smartphone: Base class with brand, model, and a ring() method.

GamingPhone: Subclass that overrides ring() to simulate a gaming-style ringtone.

🧪 Demonstration
python
my_phone = Smartphone("Samsung", "Galaxy G4")
gamer_phone = GamingPhone("Asus", "ROG Phone 8")

my_phone.ring()
# Output: Samsung Galaxy G4 is ringing

gamer_phone.ring()
# Output: Asus ROG Phone 8 plays a cool gaming sound instead of ringing!
🚗 Activity 2: Vehicle Example
🔧 Classes
Vehicle: Base class with brand, model, and a move() method.

Plane, Boat, Bicycle: Subclasses that override move() to reflect unique behaviors.

🧪 Demonstration
python
my_car = Vehicle("Ford", "Mustang")
my_plane = Plane("Kenya", "Airways")
my_boat = Boat("Titanic", "Cruise")
my_bike = Bicycle("Giant", "Escape 3")

print(my_car.brand)
my_car.move()
# Output: Ford Mustang - the vehicle is moving...

my_plane.move()
# Output: Kenya Airways - the plane is flying in the sky!

my_boat.move()
# Output: Titanic Cruise - the boat is sailing on the water.

my_bike.move()
# Output: Giant Escape 3 - the bicycle is pedaling along the path.
🧩 Learning Outcomes
Understand how inheritance allows code reuse and specialization.

Practice polymorphism by overriding methods in subclasses.

Build real-world analogies to reinforce OOP design thinking.
