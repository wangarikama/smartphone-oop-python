# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        print(f"{self.brand} {self.model} is now ON.")

    def power_off(self):
        print(f"{self.brand} {self.model} is now OFF.")

# Derived class
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        self._brand = brand
        self._model = model
        self.__storage = storage      # private attribute
        self.__battery = battery      # private attribute
        self.__powered_on = False

    def power_on(self):
        self.__powered_on = True
        print(f"{self._brand} {self._model} powered on.")

    def power_off(self):
        self.__powered_on = False
        print(f"{self._brand} {self._model} powered off.")

    def charge(self, amount):
        return self.charge_battery(amount)


    def get_specs(self):
        return {
            "brand": self._brand,
            "model": self._model,
            "storage": self.__storage,
            "battery": self.__battery
        }

    def charge_battery(self, amount):
        if amount < 0:
            raise ValueError("Charge amount must be positive")
        self.__battery += amount
        return f"Battery charged by {amount}%. Current battery: {self.__battery}%"

    def use_storage(self, amount):
        if amount < 0:
            raise ValueError("Storage usage must be positive")
        if amount > self.__storage:
            raise ValueError("Not enough storage available")
        self.__storage -= amount
        return f"Used {amount}GB of storage. Remaining storage: {self.__storage}GB"

    def power_on(self):
        self.__powered_on = True
        print(f"{self._brand} {self._model} powered on.")

    def power_off(self):
        self.__powered_on = False
        print(f"{self._brand} {self._model} powered off.")

    def charge(self, amount):
        return self.charge_battery(amount)

# Demonstration code
phone1 = Smartphone("Samsung", "Galaxy S21", 128, 75)
phone2 = Smartphone("Apple", "iPhone 13", 256, 80)

phone1.power_on()
print(phone1.get_specs())
print(phone1.use_storage(20))
print(phone1.charge(30))
phone1.power_off()

phone2.power_on()
print(phone2.get_specs())
print(phone2.use_storage(20))
print(phone2.charge(30))
phone2.power_off()
