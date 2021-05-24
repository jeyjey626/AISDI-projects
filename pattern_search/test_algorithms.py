import unittest
import random
from src import KMP_algorithm
from src import naive_algorithm
from src import RK_algorithm


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.random_text = ''.join(random.choices(['A', 'B'], k=random.randint(1000, 5000)))
        self.random_string = ''.join(random.choices(['A', 'B'], k=random.randint(2, 10)))

    # Functions for testing
    def empty_entries_function(self, function):
        with self.subTest():
            self.assertEqual(function.find('', 'ab'), [])
        with self.subTest():
            self.assertEqual(function.find('ab', ''), [])
        with self.subTest():
            self.assertEqual(function.find('', ''), [])

    def string_length_equal(self, function):
        with self.subTest():
            self.assertEqual(function.find('ab', 'ab'), [0])
        with self.subTest():
            self.assertEqual(function.find('ab', 'cb'), [])

    def string_length_bigger(self, function):
        self.assertEqual(function.find('abv', 'ab'), [])

    def string_not_in_text(self, function):
        self.assertEqual(function.find('ab', 'cdgasod'), [])

    # naive algorithm tests
    def test_naive_empty_entries(self):
        self.empty_entries_function(naive_algorithm)

    def test_naive_equal_length(self):
        self.string_length_equal(naive_algorithm)

    def test_naive_longer_string(self):
        self.string_length_bigger(naive_algorithm)

    def test_naive_string_not_in_text(self):
        self.string_not_in_text(naive_algorithm)

    def test_naive_algorithm(self):
        with self.subTest():
            self.assertEqual(naive_algorithm.find('AB', 'ABABCFDAB'), [0, 2, 7])
        with self.subTest():
            self.assertEqual(naive_algorithm.find('aB', 'ABaBAb'), [2])

    # KMP algorithm tests
    def test_KMP_empty_entries(self):
        self.empty_entries_function(KMP_algorithm)

    def test_KMO_equal_length(self):
        self.string_length_equal(KMP_algorithm)

    def test_KMP_longer_string(self):
        self.string_length_bigger(KMP_algorithm)

    def test_KMP_string_not_in_text(self):
        self.string_not_in_text(KMP_algorithm)

    # RK algorithm tests
    def test_RK_empty_entries(self):
        self.empty_entries_function(RK_algorithm)

    def test_RK_equal_length(self):
        self.string_length_equal(RK_algorithm)

    def test_RK_longer_string(self):
        self.string_length_bigger(RK_algorithm)

    def test_RK_string_not_in_text(self):
        self.string_not_in_text(RK_algorithm)

    # test all returning the same result
    def test_all_same_result(self):
        print(self.random_text)
        print(self.random_string)
        naive_result = naive_algorithm.find(self.random_string, self.random_text)
        with self.subTest('KMP'):
            self.assertListEqual(naive_result, KMP_algorithm.find(self.random_string, self.random_text))
        with self.subTest('Rabin'):
            self.assertListEqual(naive_result, RK_algorithm.find(self.random_string, self.random_text))


if __name__ == '__main__':
    unittest.main()
