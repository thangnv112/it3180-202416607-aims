import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category, search_by_title


class TestSearch(unittest.TestCase):

    def test_search_by_category(self):
        dvd1 = DigitalVideoDisc("The Lion King", "Animation", cost=19.95)
        dvd2 = DigitalVideoDisc("Star Wars", "Science Fiction", cost=24.95)
        results = search_by_category([dvd1, dvd2], "Animation")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "The Lion King")

    def test_search_by_title(self):
        dvd1 = DigitalVideoDisc("The Lion King", "Animation", cost=19.95)
        dvd2 = DigitalVideoDisc("Star Wars", "Science Fiction", cost=24.95)
        results = search_by_title([dvd1, dvd2], "Star")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Star Wars")


if __name__ == "__main__":
    unittest.main()
