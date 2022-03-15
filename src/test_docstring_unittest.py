import shape_area_docstring_placement as shape_a
import unittest
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(shape_a))
    return tests
