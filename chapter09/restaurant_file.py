# File for Restaurant class for hw_9-10

class Restaurant:
    """Modeling a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self):
            """Print statement showing how many people are served."""
            print(f"{self.restaurant_name.title()} serves {self.number_served}.")

    def describe_restaurant(self):
        """Simulate making a restaurant."""
        print(f"{self.restaurant_name.title()} is a new restaurant"
              f" that serves {self.cuisine_type.title()} food.")

    def open_restaurant(self):
        """Simulate opening a restaurant."""
        print(f"{self.restaurant_name.title()} is now open.")

