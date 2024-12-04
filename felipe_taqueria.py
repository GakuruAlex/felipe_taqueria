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
        self.total_price: float = 0.00
    
    def get_price(self, meal: str)-> float:
        """_Get price of an item in the menu_

        Args:
            meal (str): _Meal_

        Returns:
            float: _Price of Meal_
        Example:
            >>> get_price("Tortilla Salad")
                8.00
        """
        return round(self.menu[meal.title()], 2)
    def calculate_total(self, price: float)-> float:
        """_Calculate the current total price of ordered meal(s)_

        Args:
            price (float): _Price of recent meal_

        Returns:
            float: _Total Price of meal(s)_
        Example:
            with total at 0
            >>> calculate_total(8.00)
                8.00
        """
        self.total_price += price
        round(self.total_price, 2)
        return round(self.total_price, 2)
    def main(self):
        while True:
            try:
                meal = input("Item: ").title()
            except EOFError:
                break
            else:
                if meal == "":
                    break
                try:
                    price = self.get_price(meal)
                except KeyError:
                    print(f"{meal} is not on the menu!")
                    return self.main()
                else:
                    total = self.calculate_total(price)
                    print(f"Total: ${round(total, 2):.2f}")

if __name__ == "__main__":
    felipe_taqueria = FelipeTaqueria()
    felipe_taqueria.main()
                    
        

