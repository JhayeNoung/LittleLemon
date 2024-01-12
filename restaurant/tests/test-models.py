from django.test import TestCase
from restaurant.models import MenuItem # Replace 'yourapp' with the actual name of your Django app

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.price, 20)
