from datetime import datetime, timedelta

class FoodProduct:
    def __init__(self, id: int, name: str, price: float, category: str, production_date: datetime, expiration_date: datetime):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__category = category
        self.__production_date = production_date
        self.__expiration_date = expiration_date

    def __add__(self, other) -> float:
        if isinstance(other, (float, int)):
            return self.__price + other
        return NotImplemented

    def __sub__(self, other) -> float:
        if isinstance(other, (float, int)):
            return self.__price - other
        return NotImplemented

    def __mul__(self, other) -> float:
        if isinstance(other, (float, int)):
            return self.__price * other
        return NotImplemented

    def __eq__(self, other) -> bool:
        if isinstance(other, (float, int)):
            return self.__price == other
        elif isinstance(other, FoodProduct):
            return self.__price == other.__price
        else:
            return NotImplemented

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __gt__(self, other) -> bool:
        if isinstance(other, (float, int)):
            return self.__price > other
        elif isinstance(other, FoodProduct):
            return self.__price > other.__price
        else:
            return NotImplemented

    def __lt__(self, other) -> bool:
        if isinstance(other, (float, int)):
            return self.__price < other
        elif isinstance(other, FoodProduct):
            return self.__price < other.__price
        else:
            return NotImplemented

    def __len__(self) -> int:
        time_diff = datetime.now() - self.__production_date
        return time_diff.days

    def __hash__(self) -> int:
        return hash((self.__name, self.__price, self.__category, self.__production_date, self.__expiration_date))

    def __str__(self) -> str:
        return (f"Product name:{self.__name} price:{self.__price} category:{self.__category} "
                f"production_date:{self.__production_date} expiration_date:{self.__expiration_date}")

    def __repr__(self) -> str:
        return (f"FoodProduct('{self.__name}', {self.__price}, '{self.__category}', "
                f"{self.__production_date}, {self.__expiration_date})")

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name) -> None:
        if isinstance(new_name, str):
            if len(new_name) < 3:
                raise ValueError("Product name must be at least 3 letters long.")
            if len(set(new_name.lower())) != len(new_name):
                raise ValueError("Product name cannot contain repeated characters.")
            self.__name = new_name
        else:
            raise TypeError(f"name must be {type(self.__name)}. cannot be - {type(new_name)}")

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price) -> None:
        if isinstance(new_price, (int, float)):
            new_price = float(new_price)
            if 0.1 <= new_price <= 100:
                self.__price = new_price
            else:
                raise ValueError(f"price must be between 0.1 and 100")
        else:
            raise TypeError(f"price must be {type(self.__price)}. cannot be - {type(new_price)}")

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, new_category) -> None:
        if new_category.lower() not in {'dairy', 'fur', 'meat'}:
            raise ValueError("Category must be 'dairy', 'fur', or 'meat'.")
        self.__category = new_category

    @property
    def production_date(self) -> datetime:
        return self.__production_date

    @production_date.setter
    def production_date(self, new_value) -> None:
        if new_value >= datetime.now():
            raise ValueError("Production date must be in the past.")
        self.__production_date = new_value

    @property
    def expiration_date(self) -> datetime:
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, new_value) -> None:
        if new_value <= datetime.now() + timedelta(weeks=1):
            raise ValueError("Expiration date must be at least a week ahead.")
        self.__expiration_date = new_value

    @property
    def remaining(self) -> int:
        delta = self.__expiration_date - datetime.now()
        return max(delta.days, 0)

