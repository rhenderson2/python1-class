# homework assignment section 9-1
class Restaurant:
    """Modeling a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Simulate making a restaurant."""
        print(f"{self.restaurant_name.title()} is a new restaurant"
              f" that serves {self.cuisine_type.title()} food.")

    def open_restaurant(self):
        """Simulate opening a restaurant."""
        print(f"{self.restaurant_name.title()} is now open.")

my_restaurant = Restaurant("blah blah blah", "mexican")
print({my_restaurant.restaurant_name})
print({my_restaurant.cuisine_type})
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()