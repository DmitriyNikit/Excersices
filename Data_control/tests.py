from unittest import TestCase
from classes import Qty, Category, ClientIsPremium, FoodPurchases


class TestQty(TestCase):

    def setUp(self):
        self.qty = Qty(check_date='2021-10-13')

    def test_checker(self):
        checker_result = self.qty.checker()
        self.assertEqual(100, checker_result)


class TestCategory(TestCase):

    def setUp(self):
        self.category = Category(check_date='2021-10-13')

    def test_checker(self):
        checker_result = self.category.checker()
        self.assertEqual(95, checker_result)


class TestClientIsPremium(TestCase):

    def setUp(self):
        self.client_is_premium = ClientIsPremium(check_date='2021-10-13')

    def test_checker(self):
        checker_result = self.client_is_premium.checker()
        self.assertEqual(True, checker_result)


class TestFoodPurchases(TestCase):

    def setUp(self):
        self.food_purchases = FoodPurchases(check_date='2021-10-13')

    def test_checker(self):
        checker_result = self.food_purchases.checker()
        self.assertEqual(True, checker_result)
