# COMPLETE OBJECT-ORIENTED PROGRAMMING (OOP) CONCEPTS IN PYTHON
# This file demonstrates ALL major OOP concepts with practical examples

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

print("=" * 60)
print("COMPLETE OOP CONCEPTS DEMONSTRATION IN PYTHON")
print("=" * 60)

# =============================================================================
# 1. CLASSES AND OBJECTS
# =============================================================================
print("\n1. CLASSES AND OBJECTS")
print("-" * 30)

class BasicCar:
    """Basic car class demonstrating class and object creation"""
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start_engine(self):
        return f"{self.brand} {self.model} engine started!"

# Creating objects
basic_car = BasicCar("Honda", "Civic")
print(f"Object created: {basic_car.brand} {basic_car.model}")
print(basic_car.start_engine())

# =============================================================================
# 2. ENCAPSULATION (Access Modifiers)
# =============================================================================
print("\n2. ENCAPSULATION (Access Modifiers)")
print("-" * 30)

class EncapsulatedCar:
    """Demonstrates public, protected, and private attributes"""
    
    def __init__(self, brand, model, price):
        self.brand = brand              # Public
        self._model = model             # Protected (convention)
        self.__price = price            # Private (name mangling)
        self.__engine_started = False   # Private state
    
    # Public method
    def get_info(self):
        return f"{self.brand} {self._model}"
    
    # Protected method (convention)
    def _internal_diagnostic(self):
        return f"Diagnostic for {self._model}"
    
    # Private method
    def __calculate_tax(self):
        return self.__price * 0.1
    
    # Public method accessing private
    def get_total_price(self):
        return self.__price + self.__calculate_tax()
    
    # Getter (Property decorator)
    @property
    def price(self):
        return self.__price
    
    # Setter (Property decorator)
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self.__price = value
    
    # Method to demonstrate private access
    def start_engine(self):
        self.__engine_started = True
        return f"Engine started for {self.get_info()}"

encap_car = EncapsulatedCar("BMW", "X5", 50000)
print(f"Public access: {encap_car.brand}")
print(f"Protected access (works but shouldn't): {encap_car._model}")
# print(encap_car.__price)  # This would cause AttributeError
print(f"Using property: ${encap_car.price}")
print(f"Total price with tax: ${encap_car.get_total_price()}")

# Using setter
encap_car.price = 55000
print(f"Updated price: ${encap_car.price}")

# =============================================================================
# 3. INHERITANCE
# =============================================================================
print("\n3. INHERITANCE")
print("-" * 30)

# Single Inheritance
class Vehicle:
    """Parent class for all vehicles"""
    total_vehicles = 0  # Class variable (static)
    
    def __init__(self, brand, fuel_type="Gasoline"):
        self.brand = brand
        self.fuel_type = fuel_type
        self.__class__.total_vehicles += 1
    
    def start(self):
        return f"{self.brand} vehicle started with {self.fuel_type}"
    
    def stop(self):
        return f"{self.brand} vehicle stopped"
    
    @classmethod
    def get_total_vehicles(cls):
        return cls.total_vehicles
    
    @staticmethod
    def get_vehicle_types():
        return ["Car", "Motorcycle", "Truck", "Bus"]

class Car(Vehicle):
    """Car class inheriting from Vehicle"""
    
    def __init__(self, brand, model, doors=4):
        super().__init__(brand, "Gasoline")  # Call parent constructor
        self.model = model
        self.doors = doors
    
    # Method overriding
    def start(self):
        parent_start = super().start()  # Call parent method
        return f"{parent_start} - Car specific startup complete"
    
    # New method specific to Car
    def honk(self):
        return f"{self.brand} {self.model} honks: BEEP BEEP!"

# Multiple Inheritance
class Electric:
    """Mixin class for electric functionality"""
    
    def __init__(self, battery_capacity=100):
        self.battery_capacity = battery_capacity
        self.charge_level = 100
    
    def charge_battery(self, amount=10):
        self.charge_level = min(100, self.charge_level + amount)
        return f"Battery charged to {self.charge_level}%"
    
    def get_range(self):
        return self.battery_capacity * 3  # 3 miles per kWh

class HybridCar(Car, Electric):
    """Demonstrates multiple inheritance"""
    
    def __init__(self, brand, model, battery_capacity=50):
        Car.__init__(self, brand, model)
        Electric.__init__(self, battery_capacity)
        self.fuel_type = "Hybrid"
    
    def start(self):
        return f"{self.brand} {self.model} hybrid system activated"
    
    def switch_mode(self, mode="electric"):
        if mode == "electric" and self.charge_level > 10:
            return f"Switched to electric mode - Range: {self.get_range()} miles"
        else:
            return "Switched to gasoline mode"

# Demonstrating inheritance
regular_car = Car("Toyota", "Camry")
hybrid_car = HybridCar("Toyota", "Prius", 60)

print(f"Regular car: {regular_car.start()}")
print(f"Hybrid car: {hybrid_car.start()}")
print(f"Charging hybrid: {hybrid_car.charge_battery(20)}")
print(f"Mode switch: {hybrid_car.switch_mode('electric')}")
print(f"Total vehicles created: {Vehicle.get_total_vehicles()}")
print(f"Available vehicle types: {Vehicle.get_vehicle_types()}")

# =============================================================================
# 4. ABSTRACTION
# =============================================================================
print("\n4. ABSTRACTION")
print("-" * 30)

# Abstract Base Class
class AbstractVehicle(ABC):
    """Abstract base class that cannot be instantiated"""
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    @abstractmethod
    def get_max_speed(self):
        """Must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def get_fuel_efficiency(self):
        """Must be implemented by subclasses"""
        pass
    
    # Concrete method that uses abstract methods
    def get_vehicle_info(self):
        return (f"{self.brand} {self.model} - "
                f"Max Speed: {self.get_max_speed()} mph, "
                f"Fuel Efficiency: {self.get_fuel_efficiency()} mpg")

class SportsCar(AbstractVehicle):
    """Concrete implementation of AbstractVehicle"""
    
    def get_max_speed(self):
        return 200
    
    def get_fuel_efficiency(self):
        return 15
    
    def turbo_mode(self):
        return f"{self.brand} {self.model} TURBO ACTIVATED! 🔥"

# Protocols (Duck Typing)
@runtime_checkable
class Drivable(Protocol):
    """Protocol defining what makes something drivable"""
    
    def start_engine(self) -> str:
        ...
    
    def accelerate(self) -> str:
        ...
    
    def brake(self) -> str:
        ...

# Can't instantiate abstract class
# abstract_vehicle = AbstractVehicle("Test", "Car")  # Would raise TypeError

sports_car = SportsCar("Ferrari", "488")
print(f"Sports car info: {sports_car.get_vehicle_info()}")
print(f"Special feature: {sports_car.turbo_mode()}")

# =============================================================================
# 5. POLYMORPHISM
# =============================================================================
print("\n5. POLYMORPHISM")
print("-" * 30)

class Motorcycle(AbstractVehicle):
    """Another concrete implementation demonstrating polymorphism"""
    
    def get_max_speed(self):
        return 180
    
    def get_fuel_efficiency(self):
        return 45
    
    def wheelie(self):
        return f"{self.brand} {self.model} doing a wheelie! 🏍️"

class Truck(AbstractVehicle):
    """Truck implementation"""
    
    def __init__(self, brand, model, cargo_capacity):
        super().__init__(brand, model)
        self.cargo_capacity = cargo_capacity
    
    def get_max_speed(self):
        return 90
    
    def get_fuel_efficiency(self):
        return 8
    
    def load_cargo(self, weight):
        if weight <= self.cargo_capacity:
            return f"Loaded {weight} tons of cargo"
        return f"Cannot load {weight} tons - max capacity is {self.cargo_capacity} tons"

# Polymorphism in action
vehicles = [
    SportsCar("Lamborghini", "Huracan"),
    Motorcycle("Harley", "Davidson"),
    Truck("Ford", "F-150", 3)
]

print("Polymorphism demonstration:")
for vehicle in vehicles:
    print(f"- {vehicle.get_vehicle_info()}")

# Duck typing with protocols
class RCCar:
    """Remote control car that implements Drivable protocol"""
    
    def __init__(self, name):
        self.name = name
    
    def start_engine(self):
        return f"{self.name} RC car powered on!"
    
    def accelerate(self):
        return f"{self.name} speeding up!"
    
    def brake(self):
        return f"{self.name} slowing down!"

def test_driving(vehicle: Drivable):
    """Function that works with any Drivable object"""
    print(f"Testing: {vehicle.start_engine()}")
    print(f"Testing: {vehicle.accelerate()}")
    print(f"Testing: {vehicle.brake()}")

rc_car = RCCar("Lightning McQueen")
if isinstance(rc_car, Drivable):
    test_driving(rc_car)

# =============================================================================
# 6. COMPOSITION AND AGGREGATION
# =============================================================================
print("\n6. COMPOSITION AND AGGREGATION")
print("-" * 30)

# Composition (strong "has-a" relationship)
class Engine:
    """Engine class for composition example"""
    
    def __init__(self, engine_type, horsepower):
        self.engine_type = engine_type
        self.horsepower = horsepower
        self.is_running = False
    
    def start(self):
        self.is_running = True
        return f"{self.engine_type} engine ({self.horsepower}HP) started"
    
    def stop(self):
        self.is_running = False
        return f"{self.engine_type} engine stopped"

class GPS:
    """GPS class for composition example"""
    
    def __init__(self):
        self.current_location = "Unknown"
    
    def navigate_to(self, destination):
        self.current_location = destination
        return f"Navigating to {destination}"

class ModernCar:
    """Car with composition - owns Engine and GPS"""
    
    def __init__(self, brand, model, engine_type="V6", horsepower=300):
        self.brand = brand
        self.model = model
        # Composition - Car owns these objects
        self.engine = Engine(engine_type, horsepower)
        self.gps = GPS()
        self.speed = 0
    
    def start_car(self):
        engine_status = self.engine.start()
        return f"{self.brand} {self.model} started - {engine_status}"
    
    def navigate(self, destination):
        if self.engine.is_running:
            return self.gps.navigate_to(destination)
        return "Please start the car first"
    
    def accelerate(self, speed_increase):
        if self.engine.is_running:
            self.speed += speed_increase
            return f"Speed increased to {self.speed} mph"
        return "Engine not running"

# Aggregation (weak "has-a" relationship)
class Driver:
    """Driver class for aggregation example"""
    
    def __init__(self, name, license_number):
        self.name = name
        self.license_number = license_number
    
    def drive(self, car):
        return f"{self.name} is driving {car.brand} {car.model}"

class CarRental:
    """Car rental demonstrating aggregation"""
    
    def __init__(self):
        self.available_cars = []
        self.rented_cars = {}
    
    def add_car(self, car):
        self.available_cars.append(car)
    
    def rent_car(self, car, driver):
        if car in self.available_cars:
            self.available_cars.remove(car)
            self.rented_cars[driver.name] = car
            return f"Car rented: {driver.drive(car)}"
        return "Car not available"

# Demonstrating composition and aggregation
modern_car = ModernCar("Audi", "A4", "Turbo V4", 250)
print(f"Car creation: {modern_car.start_car()}")
print(f"Navigation: {modern_car.navigate('Downtown')}")
print(f"Acceleration: {modern_car.accelerate(30)}")

driver = Driver("John Doe", "DL123456")
rental = CarRental()
rental.add_car(modern_car)
print(f"Rental: {rental.rent_car(modern_car, driver)}")

# =============================================================================
# 7. SPECIAL METHODS (Magic Methods / Dunder Methods)
# =============================================================================
print("\n7. SPECIAL METHODS (Magic Methods)")
print("-" * 30)

class AdvancedCar:
    """Car class with special methods"""
    
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
    
    # String representation
    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"
    
    def __repr__(self):
        return f"AdvancedCar('{self.brand}', '{self.model}', {self.year}, {self.price})"
    
    # Comparison operators
    def __eq__(self, other):
        if isinstance(other, AdvancedCar):
            return self.price == other.price
        return False
    
    def __lt__(self, other):
        if isinstance(other, AdvancedCar):
            return self.price < other.price
        return NotImplemented
    
    def __le__(self, other):
        return self < other or self == other
    
    # Arithmetic operations
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return AdvancedCar(self.brand, self.model, self.year, self.price + other)
        return NotImplemented
    
    # Container-like behavior
    def __len__(self):
        return len(f"{self.brand} {self.model}")
    
    def __getitem__(self, key):
        attrs = [self.brand, self.model, str(self.year), str(self.price)]
        return attrs[key]
    
    # Context manager
    def __enter__(self):
        print(f"Starting {self} for a test drive")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Ending test drive of {self}")
    
    # Hash support
    def __hash__(self):
        return hash((self.brand, self.model, self.year))

# Using special methods
car1 = AdvancedCar("Mercedes", "C-Class", 2023, 45000)
car2 = AdvancedCar("BMW", "3 Series", 2023, 47000)

print(f"String representation: {car1}")
print(f"Repr: {repr(car1)}")
print(f"Comparison: car1 < car2 = {car1 < car2}")
print(f"Addition: {car1 + 5000}")
print(f"Length: {len(car1)}")
print(f"Indexing: Brand = {car1[0]}, Model = {car1[1]}")

# Context manager usage
with car1 as test_car:
    print(f"Test driving: {test_car}")

# =============================================================================
# 8. CLASS METHODS AND STATIC METHODS
# =============================================================================
print("\n8. CLASS METHODS AND STATIC METHODS")
print("-" * 30)

class CarFactory:
    """Demonstrates class and static methods"""
    
    total_cars_produced = 0
    factory_location = "Detroit"
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        CarFactory.total_cars_produced += 1
    
    @classmethod
    def create_luxury_car(cls, brand):
        """Alternative constructor for luxury cars"""
        luxury_models = {"BMW": "7 Series", "Mercedes": "S-Class", "Audi": "A8"}
        model = luxury_models.get(brand, "Luxury Model")
        return cls(brand, model)
    
    @classmethod
    def get_production_stats(cls):
        """Class method to get statistics"""
        return f"Total cars produced: {cls.total_cars_produced} at {cls.factory_location}"
    
    @staticmethod
    def calculate_carbon_footprint(miles_driven, fuel_efficiency):
        """Static method - doesn't need class or instance"""
        gallons_used = miles_driven / fuel_efficiency
        co2_pounds = gallons_used * 19.6  # pounds of CO2 per gallon
        return f"Carbon footprint: {co2_pounds:.2f} lbs of CO2"
    
    @staticmethod
    def is_eco_friendly(fuel_efficiency):
        """Static utility method"""
        return fuel_efficiency > 30

# Using class and static methods
luxury_bmw = CarFactory.create_luxury_car("BMW")
luxury_mercedes = CarFactory.create_luxury_car("Mercedes")

print(f"Luxury cars created: {luxury_bmw.brand} {luxury_bmw.model}")
print(f"Production stats: {CarFactory.get_production_stats()}")
print(f"Carbon footprint: {CarFactory.calculate_carbon_footprint(1000, 25)}")
print(f"Is 35 mpg eco-friendly? {CarFactory.is_eco_friendly(35)}")

# =============================================================================
# 9. PROPERTY DECORATORS AND DESCRIPTORS
# =============================================================================
print("\n9. PROPERTY DECORATORS AND DESCRIPTORS")
print("-" * 30)

class Temperature:
    """Descriptor for temperature validation"""
    
    def __init__(self, min_temp=-40, max_temp=120):
        self.min_temp = min_temp
        self.max_temp = max_temp
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__[self.name]
    
    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.name} must be a number")
        if not (self.min_temp <= value <= self.max_temp):
            raise ValueError(f"{self.name} must be between {self.min_temp} and {self.max_temp}")
        obj.__dict__[self.name] = value

class SmartCar:
    """Car with property decorators and descriptors"""
    
    engine_temp = Temperature(min_temp=0, max_temp=250)
    cabin_temp = Temperature(min_temp=-20, max_temp=100)
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._speed = 0
        self._fuel_level = 100
        self.engine_temp = 90
        self.cabin_temp = 72
    
    @property
    def speed(self):
        """Getter for speed"""
        return self._speed
    
    @speed.setter
    def speed(self, value):
        """Setter with validation"""
        if not isinstance(value, (int, float)):
            raise TypeError("Speed must be a number")
        if value < 0:
            raise ValueError("Speed cannot be negative")
        if value > 200:
            raise ValueError("Speed cannot exceed 200 mph")
        self._speed = value
    
    @property
    def fuel_level(self):
        return self._fuel_level
    
    @fuel_level.setter
    def fuel_level(self, value):
        if 0 <= value <= 100:
            self._fuel_level = value
        else:
            raise ValueError("Fuel level must be between 0 and 100")
    
    @property
    def is_overheating(self):
        """Computed property"""
        return self.engine_temp > 200
    
    @property
    def status(self):
        """Complex computed property"""
        status_parts = []
        if self._speed > 0:
            status_parts.append(f"Moving at {self._speed} mph")
        else:
            status_parts.append("Stopped")
        
        status_parts.append(f"Fuel: {self._fuel_level}%")
        status_parts.append(f"Engine temp: {self.engine_temp}°F")
        
        if self.is_overheating:
            status_parts.append("⚠️ OVERHEATING!")
        
        return " | ".join(status_parts)

# Using properties and descriptors
smart_car = SmartCar("Tesla", "Model 3")
smart_car.speed = 65
smart_car.fuel_level = 80
smart_car.engine_temp = 180
smart_car.cabin_temp = 70

print(f"Smart car status: {smart_car.status}")
print(f"Is overheating: {smart_car.is_overheating}")

# Try invalid values (uncomment to see errors)
# smart_car.speed = -10  # ValueError
# smart_car.engine_temp = 300  # ValueError

# =============================================================================
# 10. METACLASSES (Advanced)
# =============================================================================
print("\n10. METACLASSES (Advanced)")
print("-" * 30)

class SingletonMeta(type):
    """Metaclass that creates singleton instances"""
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class CarDatabase(metaclass=SingletonMeta):
    """Singleton database for cars"""
    
    def __init__(self):
        if not hasattr(self, 'cars'):
            self.cars = []
    
    def add_car(self, car):
        self.cars.append(car)
        return f"Added {car} to database"
    
    def get_car_count(self):
        return len(self.cars)
    
    def list_cars(self):
        return [str(car) for car in self.cars]

# Singleton demonstration
db1 = CarDatabase()
db2 = CarDatabase()

print(f"Same instance? {db1 is db2}")  # True - singleton pattern

db1.add_car(car1)
print(f"Cars in db2: {db2.get_car_count()}")  # Same instance, so 1 car

# =============================================================================
# 11. COMPARISON WITH TYPESCRIPT/JAVASCRIPT CONCEPTS
# =============================================================================
print("\n11. PYTHON vs TYPESCRIPT/JAVASCRIPT OOP")
print("-" * 30)

class PythonSupra(AbstractVehicle):
    """Python equivalent of your TypeScript Supra class"""
    
    def __init__(self):
        super().__init__("Toyota", "Supra")
        self.name = "supra"                    # public (like TypeScript public)
        self._model = "GR Supra"              # protected by convention
        self.__engine = "2JZ"                 # private (name mangling)
        self.__speed = 0                      # private
    
    # Public method
    def get_name(self):
        return self.name
    
    # Private method (by convention)
    def __get_engine(self):
        return self.__engine
    
    def get_full_info(self):
        return f"{self.brand} {self.get_name()} with engine {self.__get_engine()}"
    
    def update_status(self):
        return "The 2JZ is roaring 🔥"
    
    # Property for speed (like TypeScript getter/setter)
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter  
    def speed(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__speed = value
        else:
            raise ValueError("Speed must be a non-negative number")
    
    # Abstract method implementations
    def get_max_speed(self):
        return 155  # mph (electronically limited)
    
    def get_fuel_efficiency(self):
        return 22  # mpg

# Usage comparison
python_supra = PythonSupra()
print(f"Python Supra: {python_supra.get_full_info()}")
print(f"Status: {python_supra.update_status()}")

# Property usage (like TypeScript getter/setter)
python_supra.speed = 100
print(f"Current speed: {python_supra.speed} mph")

# Demonstrate access levels
print(f"Public access: {python_supra.name}")
print(f"Protected access (works but shouldn't): {python_supra._model}")
# print(python_supra.__engine)  # AttributeError - private
# Access private via name mangling (not recommended)
print(f"Private via name mangling: {python_supra._PythonSupra__engine}")

# =============================================================================
# SUMMARY AND COMPARISON
# =============================================================================
print("\n" + "=" * 60)
print("SUMMARY: PYTHON vs TYPESCRIPT/JAVASCRIPT OOP")
print("=" * 60)

summary = """
CONCEPTS COVERED (✅ = Demonstrated):

✅ Classes and Objects
✅ Encapsulation (public, protected, private)
✅ Inheritance (single and multiple)
✅ Abstraction (ABC, abstract methods)
✅ Polymorphism (method overriding, duck typing)
✅ Composition and Aggregation
✅ Static and Class Methods
✅ Property Decorators (getter/setter)
✅ Special Methods (magic/dunder methods)
✅ Interfaces (Protocols)
✅ Descriptors
✅ Metaclasses

KEY DIFFERENCES FROM TYPESCRIPT:

PYTHON                          | TYPESCRIPT/JAVASCRIPT
------------------------------- | -------------------------------
No true private (convention)   | true private with #field
Duck typing                     | Structural typing
Multiple inheritance            | Mixins/interfaces
@property decorator             | get/set keywords
ABC for abstracts              | abstract keyword
Protocols for interfaces       | interface keyword
Metaclasses                    | Limited metaprogramming
__dunder__ methods             | No equivalent
Dynamic typing                 | Static typing (TS)

ADVANTAGES OF PYTHON OOP:
- More flexible with duck typing
- Multiple inheritance support
- Powerful metaprogramming
- Rich special methods
- Dynamic nature allows runtime modification

ADVANTAGES OF TYPESCRIPT OOP:
- True private members
- Compile-time type checking
- Better IDE support
- Interface contracts
- Cleaner syntax for some concepts
"""

print(summary)
print("\n🎯 This file demonstrates ALL major OOP concepts!")
print("💡 Compare with your TypeScript code to see the differences!")
print("🚀 Both languages are powerful for OOP - choose based on your needs!")