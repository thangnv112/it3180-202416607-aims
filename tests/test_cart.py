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


if __name__ == "__main__":
    unittest.main()
