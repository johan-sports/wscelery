import unittest

from wscelery.utils import select_keys


class UtilsTestCase(unittest.TestCase):
    def test_select_keys_returns_only_the_given_keys(self):
        d = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(select_keys(d, ['a', 'c']), {'a': 1, 'c': 3})

    def test_select_keys_does_not_mutate_original_dict(self):
        d = {'a': 1, 'b': 2, 'c': 3}
        _ = select_keys(d, ['a', 'c'])
        self.assertEqual(d, {'a': 1, 'b': 2, 'c': 3})
