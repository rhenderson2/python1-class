# homework assignment section 9-4
class Restaurant:
    """Modeling a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self):
        """Print statement showing how many people are served."""
        print(f"{self.restaurant_name.title()} serves {self.number_served}.")

restaurant = Restaurant("billions served", "american")
print(f"{restaurant.restaurant_name.title()} serves {restaurant.number_served}.")
restaurant.number_served = 15
print(f"{restaurant.restaurant_name.title()} serves {restaurant.number_served}.")
restaurant.number_served = 153
restaurant.set_number_served()

