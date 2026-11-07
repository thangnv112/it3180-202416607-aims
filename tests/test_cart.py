import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):

    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(20):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}", "Category", cost=10.0)))
        # Đĩa thứ 21 phải bị từ chối và trả về False
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21", "Category", cost=10.0)))

    def test_discount(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD 1", "Animation", cost=100.0))
        # 100 giam 20% phai la 80
        self.assertEqual(cart.total_cost_with_discount(20), 80.0)
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)

    def test_remove_dvd(self):
        cart = Cart()
        dvd = DigitalVideoDisc("The Lion King", "Animation", cost=19.95)
        cart.add_dvd(dvd)
        self.assertTrue(cart.remove_dvd(dvd))
        self.assertFalse(cart.remove_dvd(dvd))

    def test_sort_by_title(self):
        cart = Cart()
        dvd1 = DigitalVideoDisc("Zootopia", "Animation", cost=15.0)
        dvd2 = DigitalVideoDisc("Aladdin", "Animation", cost=20.0)
        cart.add_dvd(dvd1)
        cart.add_dvd(dvd2)
        cart.sort_by_title()
        self.assertEqual(cart.items[0].title, "Aladdin")
        self.assertEqual(cart.items[1].title, "Zootopia")

    def test_sort_by_cost(self):
        cart = Cart()
        dvd1 = DigitalVideoDisc("DVD cheap", "Category", cost=10.0)
        dvd2 = DigitalVideoDisc("DVD expensive", "Category", cost=30.0)
        cart.add_dvd(dvd1)
        cart.add_dvd(dvd2)
        cart.sort_by_cost()
        self.assertEqual(cart.items[0].cost, 30.0)
        self.assertEqual(cart.items[1].cost, 10.0)


if __name__ == "__main__":
    unittest.main()
