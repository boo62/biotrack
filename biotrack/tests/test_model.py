#!/usr/bin/env python
import unittest

from model import Model



class TestSimpleModel(unittest.TestCase):

    def setUp(self):
        model_1 = Model("example_models/model.csv")

    def tearDown(self):
        model_1 = None


    def test_component_lengths(self):
        self.assertEqual(len(model_1.components), 2)
        self.assertEqual(len(model_1.components[1]), 2)


    def test_component_types(self):
        self.assertIsInstance(model_1.components[1][1], str)
        self.assertIsInstance(int(model_1.components[1][2]), int)
        
            
    def test_accession_parsing_fail_when_not_accession(self):
        pass
