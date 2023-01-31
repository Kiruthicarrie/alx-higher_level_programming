"""
Contains unittests for the base class methods.
"""
import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):
    """Unittest test class for Base class"""

    def test_automatically_assigned_id(self):
        """Check whether id attribute is assigned automatically"""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)

    def setUp(self):
        """Set up resources required to run the tests"""
        self.base_1 = Base(5)
        self.base_2 = Base(-5)

    def tearDown(self):
        """Tear down resources required to run the tests"""
        del self.base_1
        del self.base_2

    def test_assign_id(self):
        """Check whether id is assigned automatically if none is provided"""
        self.assertEqual(self.base_1.id, 5)

    def test_assign_negative_id(self):
        """Check whether -ve value is accepted for id attribute"""
        self.assertEqual(self.base_2.id, -5)

    def test_to_json_string_method(self):
        """Check whether to_json_string method returns expected values when
           given different inputs"""
        self.assertEqual(self.base_1.to_json_string(None), "[]")
        self.assertEqual(self.base_1.to_json_string([]), "[]")
        self.assertEqual(self.base_1.to_json_string([ {'id': 1} ]),
                         '[{"id": 1}]')

    def test_from_json_string_method(self):
        """Check whether from_json_string method returns expected values when
           given different inputs"""
        self.assertEqual(self.base_1.from_json_string(None), [])
        self.assertEqual(self.base_1.from_json_string("[]"), [])
        self.assertEqual(self.base_1.from_json_string('[{ "id": 89}]'),
                         [{'id': 89}])
