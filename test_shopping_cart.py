# test_shopping_cart.py
import unittest
from shopping_cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("Apple", 5)
        self.cart.add_item("Banana", 3)
        self.cart.add_item("Orange", 3)
        self.cart.add_item("Pear", 1)
        self.cart.add_item("Kiwi", 1)

        self.assertEqual(self.cart.items["Apple"], 5)
        self.assertEqual(self.cart.items["Banana"], 3)
        self.assertEqual(self.cart.items["Orange"], 3)
        self.assertEqual(self.cart.items["Pear"], 1)
        self.assertEqual(self.cart.items["Kiwi"], 1)

    def test_remove_item(self):
        self.cart.add_item("Banana", 1)
        self.cart.add_item("Kiwi", 1)
        self.cart.remove_item("Banana", 1)
        self.cart.remove_item("Kiwi", 1)
        self.assertEqual(self.cart.items.get("Banana"), None)
        self.assertEqual(self.cart.items.get("Kiwi"), None)

    def test_get_total(self):
        self.cart.add_item("Apple", 5)

        total = self.cart.get_total()
        self.assertEqual(total, 50)  # (3 * 10) + (2 * 10)

    def test_empty_cart(self):
        total = self.cart.get_total()
        self.assertEqual(total, 0)

    #def test_negative_quantity(self):
     #   with self.assertRaises(ValueError):
      #      self.cart.add_item("Cherry", 1, -1)


if __name__ == "__main__":
    unittest.main()
