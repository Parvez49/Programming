

# method overriding is the ability of a subclass to provide
# its own implementation for a method that is already
# defined in its superclass.
class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound_cat(self):
        print("Meow")

animal = Animal()
dog = Dog()
cat = Cat()

animal.make_sound()  # Output: "Generic animal sound"
dog.make_sound()     # Output: "Bark"
cat.make_sound()     # Output: "Meow"
