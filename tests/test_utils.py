import unittest

from wscelery.utils import exclude_keys


class UtilsTestCase(unittest.TestCase):
    def test_excludes_keys_returns_everything_but_the_given_keys(self):
        d = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(exclude_keys(d, ['a', 'c']), {'b': 2})

    def test_select_keys_does_not_mutate_original_dict(self):
        d = {'a': 1, 'b': 2, 'c': 3}
        exclude_keys(d, ['a', 'c'])
        self.assertEqual(d, {'a': 1, 'b': 2, 'c': 3})
