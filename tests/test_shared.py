import unittest
from pyiron_dataclasses.v1.shared import convert_datacontainer_to_dictionary


class TestShared(unittest.TestCase):
    def test_convert_datacontainer_to_dictionary(self):
        with self.assertRaises(TypeError):
            convert_datacontainer_to_dictionary({"__index_1": 1})

    def test_2(self):
        with self.assertRaises(KeyError):
            convert_datacontainer_to_dictionary({"a": 1, "b": 2, "a__index_1": 0})
