# homework assignment section 9-6
class Restaurant:
    """Modeling a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self):
        """Print statement showing how many people are served."""
        print(f"{self.restaurant_name.title()} serves {self.number_served}.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = 'vanilla', 'chocolate', 'strawberry', 'drumstick', 'peppermint'

    def display_flavors(self):
        print(self.flavors)


my_icstand = IceCreamStand('I.C.Stand', 'desserts')
my_icstand.display_flavors()
