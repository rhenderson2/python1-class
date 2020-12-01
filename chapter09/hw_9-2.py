# homework assignment section 9-2
class Restaurant:
    """Modeling a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Simulate making a restaurant."""
        print(f"{self.restaurant_name.title()} is a new restaurant"
              f" that serves {self.cuisine_type.title()} food.")

    def open_restaurant(self):
        """Simulate opening a restaurant."""
        print(f"{self.restaurant_name.title()} is now open.")

french_restaurant = Restaurant("chez", "french")
french_restaurant.describe_restaurant()

print('\n')
greek_restaurant = Restaurant('yiro', 'greek')
greek_restaurant.describe_restaurant()

print('\n')
chinese_restaurant = Restaurant('pei', 'chinese')
chinese_restaurant.describe_restaurant()



