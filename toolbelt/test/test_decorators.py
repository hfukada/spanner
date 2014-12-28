import unittest
from toolbelt.decorators import validate_args


include = True


@validate_args(int, str, list, float)
def foo(a, b, c=[0], d=None):
    pass

# improperly annotated (not all args have type specified)
@validate_args(int, str, list)
def bar(a, b, c, d=None):
    pass



class DecoratorTestCase(unittest.TestCase):

    def test_correct_args(self):
        try:
            foo(1, '2', [3], 4.)
        except Exception as e:
            self.fail('Caught unexpected exception: ' + str(e))

    def test_incorrect_args(self):
        with self.assertRaises(Exception):
            foo('1', '2', [3], 4)

    def test_keyword_args(self):
        try:
            foo(1, '2', c=[3], d=4.)
        except Exception as e:
            self.fail('Caught unexpected exception: ' + str(e))

    def test_reordered_keyword_args(self):
        try:
            foo(1, '2', d=4., c=[3])
        except Exception as e:
            self.fail('Caught unexpected exception: ' + str(e))

    def test_not_all_args_specified(self):
        with self.assertRaises(Exception):
            foo(1)

    def test_not_all_types_specified(self):
        with self.assertRaises(Exception):
            bar(1, '2', [3], 4.)

