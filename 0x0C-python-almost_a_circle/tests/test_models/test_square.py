"""
Contains the definition of the test class for the Square class.
"""
import os
import json
import unittest
from models.square import Square


class TestSquareMethods(unittest.TestCase):
    """Unittest test class for Square class"""

    def setUp(self):
        """Set up resources required to run the tests"""
        self.square_1 = Square(2)
        self.square_2 = Square(1, 2, 1, 3)
        try:
           os.remove("Square.json")
        except:
            pass

    def tearDown(self):
        """Tear down resources that had been set up to run tests"""
        del self.square_1
        del self.square_2
        try:
            os.remove("Square.json")
        except:
            pass

    def test_size_assignment(self):
        """Test assignment of width and height attributes"""
        self.assertEqual(self.square_1.size, 2)

    def test_x_y_assignment(self):
        """Test assignment of x and y attributes"""
        self.assertEqual(self.square_1.x, 0)
        self.assertEqual(self.square_1.y, 0)
        self.assertEqual(self.square_2.x, 2)
        self.assertEqual(self.square_2.y, 1)

    def test_exceptions_type_str(self):
        """Test whether TypeError is raised for str arguments"""
        args = ['h', 2, 3, 4]
        self.assertRaises(TypeError, Square, *args)
        args = [4, 'h', 2, 3]
        self.assertRaises(TypeError, Square, *args)
        args = [4, 2, 'h', 3]
        self.assertRaises(TypeError, Square, *args)

    def test_exceptions_type_float(self):
        """Test whether TypeError is raised for float arguments"""
        args = [4.2, 2, 3, 4]
        self.assertRaises(TypeError, Square, *args)
        args = [4, 4.2, 2, 3]
        self.assertRaises(TypeError, Square, *args)
        args = [4, 2, 4.2, 3]
        self.assertRaises(TypeError, Square, *args)

    def test_exceptions_type_list(self):
        """Test whether TypeError is raised for list arguments"""
        args = [[1, 2], 2, 3, 4]
        self.assertRaises(TypeError, Square, *args)
        args = [4, [1, 2], 2, 3]
        self.assertRaises(TypeError, Square, *args)
        args = [4, 2, [1, 3], 3]
        self.assertRaises(TypeError, Square, *args)

    def test_exceptions_type_set(self):
        """Test whether TypeError is raised for set arguments"""
        args = [{1, 2}, 2, 3, 4]
        self.assertRaises(TypeError, Square, *args)
        args = [4, {1, 2}, 2, 3]
        self.assertRaises(TypeError, Square, *args)
        args = [4, 2, {1, 3}, 3]
        self.assertRaises(TypeError, Square, *args)

    def test_exceptions_type_tuple(self):
        """Test whether TypeError is raised for tuple arguments"""
        args = [(1, 2), 2, 3, 4]
        self.assertRaises(TypeError, Square, *args)
        args = [4, (1, 2), 2, 3]
        self.assertRaises(TypeError, Square, *args)
        args = [4, 2, (1, 3), 3]
        self.assertRaises(TypeError, Square, *args)

    def test_exceptions_type_dict(self):
        """Test whether TypeError is raised for str arguments"""
        args = [{"one": 2}, 2, 3, 4]
        self.assertRaises(TypeError, Square, *args)
        args = [4, {"two": 2}, 2, 3]
        self.assertRaises(TypeError, Square, *args)
        args = [4, 2, {"three": 3}, 3]
        self.assertRaises(TypeError, Square, *args)

    def test_type_exception_message(self):
        """Tests whether the correct exception message is printed"""
        args = ['One', 5, 1, 3]
        self.assertRaisesRegex(TypeError, "width", Square, *args)
        args = [4, 'Two', 4, 7]
        self.assertRaisesRegex(TypeError, "x", Square, *args)
        args = [4, 5, 'Three', 7]
        self.assertRaisesRegex(TypeError, "y", Square, *args)

    def test_value_exception_message(self):
        """Tests whether the correct exception message is printed"""
        args = [-5, 5, 1, 3]
        self.assertRaisesRegex(ValueError, "width", Square, *args)
        args = [0, 5, 1, 3]
        self.assertRaisesRegex(ValueError, "width", Square, *args)
        args = [4, -4, 4, 7]
        self.assertRaisesRegex(ValueError, "x", Square, *args)
        args = [4, 5, -1, 7]
        self.assertRaisesRegex(ValueError, "y", Square, *args)

    def test_exceptions_value(self):
        """Test whether ValueError is raised for unacceptable arguments"""
        args = [0, 1, 2, 3]
        self.assertRaises(ValueError, Square, *args)
        args = [1, -4, 3, 4]
        self.assertRaises(ValueError, Square, *args)
        args = [4, 2, -5, 3]
        self.assertRaises(ValueError, Square, *args)

    def test_area(self):
        """Test the area method of the Square class"""
        self.assertEqual(self.square_1.area(), 4)

    def test_str(self):
        """Test the __str__ magic method of the Square class"""
        self.assertEqual(str(self.square_2), "[Square] (3) 2/1 - 1")

    def test_update(self):
        """Test the update method of the Square class"""
        self.square_1.update(1, 1, 1, 1)
        self.assertEqual(str(self.square_1), "[Square] (1) 1/1 - 1")

    def test_update_kwargs(self):
        """Test the update method of the Square class using *kwargs"""
        self.square_1.update(size=65, id=5)
        self.assertEqual(str(self.square_1), "[Square] (5) 0/0 - 65")
        kwargs = {"size": 5, "x": 5, "y": 8, "id": 122}
        self.square_1.update(**kwargs)
        self.assertEqual(str(self.square_1), "[Square] (122) 5/8 - 5")

    def test_update_args_kwargs(self):
        """Test the update method of the Square class with args and kwargs"""
        args = [1, 1, 1, 1]
        kwargs = {"size": 1, "x": 3, "y": 2, "id": 1}
        self.square_1.update(*args, **kwargs)
        self.assertEqual(str(self.square_1), "[Square] (1) 1/1 - 1")

    def test_to_dictionary_method(self):
        """Test the to_dictionary method of the Rectangle class"""
        sq = Square(2, 0, 0, 89)
        self.assertEqual(sq.to_dictionary(),
                         {'size': 2, 'x': 0, 'y': 0, 'id': 89})

    def test_create_method(self):
        """Test the create method of the Square class"""
        r1 = Square(1, 0, 0, 89)
        r2 = Square.create(**{'id': 89})
        self.assertEqual(str(r1), str(r2))
        r1 = Square(1, 0, 0, 89)
        r2 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(str(r1), str(r2))
        r1 = Square(1, 3, 0, 89)
        r2 = Square.create(**{'id': 89, 'size': 1, 'x': 3})
        self.assertEqual(str(r1), str(r2))
        r1 = Square(1, 3, 4, 89)
        r2 = Square.create(**{'id': 89, 'size': 1, 'x': 3, 'y': 4})
        self.assertEqual(str(r1), str(r2))

    def test_save_to_file_method_None(self):
        """Test the save_to_file method of the Square class"""
        Square.save_to_file(None)
        with open("Square.json", mode="r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data, [])

    def test_save_to_file_method_Empty(self):
        """Test the save_to_file method of the Square class"""
        Square.save_to_file([])
        with open("Square.json", mode="r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data, [])

    def test_save_to_file_method(self):
        """Test the save_to_file method of the Square class"""
        Square.save_to_file([Square(1, 3, 4, 5)])
        with open("Square.json", mode="r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data, [{"size": 1, "x": 3, "y": 4,
                                 "id": 5}])

    def test_load_from_file_method(self):
        """Test the load_from_file method of the Square class"""
        data = Square.load_from_file()
        self.assertEqual(data, [])

        Square.save_to_file([Square(1, 3, 4, 5)])
        rrr = Square.load_from_file()
        self.assertEqual(str(rrr[0]), "[Square] (5) 3/4 - 1")
