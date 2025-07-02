class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# List of different animal objects
animals = [Dog(), Cat(), Animal()]
#for different objects methods behave differently => Polymorphism 
# Polymorphism in action
for animal in animals:
    animal.speak()
