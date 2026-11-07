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


if __name__ == "__main__":
    unittest.main()
