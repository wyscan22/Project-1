import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    def circumference(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return (
              f"Circle"
            f"\nRadius: {self.radius}"
            f"\nArea: {self.area()}"
            f"\nCircumference: {self.circumference()}"
        )

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * self.width + self.height

class Clock:
    def __init__(self, hour = 0, minute = 0, second = 0):
        assert type(hour) == int, "Argument <hour> must be an integer."
        assert type(minute) == int, "Argument <minute> must be an integer."
        assert type(second) == int, "Argument <second> must be an integer."

        self.hour = (hour + (minute + second // 60) // 60) % 24
        self.minute = (minute + second // 60) % 60
        self.second = second % 60

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

    def __add__(self, other):
        return Clock(self.hour + other.hour, self.minute + other.minute, self.second + other.second)

BankAccountServiceInfo = {"next_id" : 0}
class BankAccount:
    def __init__(self, name, balance):
        self.__ID = BankAccountServiceInfo["next_id"]
        self.name = name
        self.__balance = balance

        BankAccountServiceInfo["next_id"] += 1

    def get_ID(self):
        return self.__ID

    def deposit(self, amount):
        assert type(self.amount) in (int, float) and amount > 0, \
            "Argument <amount> must be a positive real number."
        self.__balance += amount

    def withdraw(self, amount):
        assert type(self.amount) in (int, float) and amount > 0, \
            "Argument <amount> must be a positive real number."
        if self.__balance < amount:
            raise ValueError("Not enough funds to withdraw.")
        else: self.__balance -= amount

    def __str__(self):
        return (
            f"Bank Account"
            f"\nID: {self.__ID}"
            f"\nName: {self.name}"
            f"\nBalance: {self.__balance}"
        )

class RectCoordinates:
    def __init__(self, x = 0, y = 0):
        assert type(x) in (int, float), "Argument <x> must be a real number."
        assert type(y) in (int, float), "Argument <y> must be a real number."

        self.x = x
        self.y = y
    def __str__(self):
        return f"({str(self.x)}, {str(self.y)})"

    def is_on_x_axis(self):
        return self.y == 0
    def is_on_y_axis(self):
        return self.x == 0
    def quadrant(self):
        quadrant_table = ((3, 2), (4, 1))
        if self.is_on_x_axis() or self.is_on_y_axis():
            return None
        return quadrant_table[int(self.x > 0)][int(self.y > 0)]

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def angle(self, unit = "rad"):
        result = math.atan2(self.y, self.x)
        if unit == "rad":
            return result
        elif unit == "deg":
            return result * 180 / math.pi

    def reference_angle(self, unit = "rad"):
        result = abs((self.angle() + math.pi / 2) % math.pi - math.pi / 2)
        if unit == "rad":
            return result
        elif unit == "deg":
            return result * 180 / math.pi