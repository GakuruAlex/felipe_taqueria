class FelipeTaqueria:
    def __init__(self):
        self.menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
        self.total = 0
    
    def get_price(self, meal: str) -> float:
        """_Get price of an item in the menu_

        Args:
            meal (str): _Meal_

        Returns:
            float: _Price of Meal_
        Example:
            >>> get_price("Tortilla Salad")
                8.00
        """
        return self.menu[meal.title()]

