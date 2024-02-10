#!/usr/bin/python3
"""
Unittests for BaseModel class
"""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class
    """

    def test_init(self):
        """
        Test initialization of BaseModel
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_str(self):
        """
        Test __str__ method of BaseModel
        """
        my_model = BaseModel()
        string = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), string)

    def test_save(self):
        """
        Test save method of BaseModel
        """
        my_model = BaseModel()
        updated_time = my_model.updated_at
        my_model.save()
        new_updated_time = my_model.updated_at
        self.assertNotEqual(updated_time, new_updated_time)

    def test_to_dict(self):
        """
        Test to_dict method of BaseModel
        """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertTrue(isinstance(my_model_dict, dict))
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertEqual(type(my_model_dict['created_at']), str)
        self.assertEqual(type(my_model_dict['updated_at']), str)
