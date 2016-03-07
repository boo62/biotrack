#!/usr/bin/env python
import unittest

from biotrack.model import Model



class TestSimpleModel(unittest.TestCase):

    def setUp(self):
        self.model_1 = Model("tests/example_models/two_components.csv")

    def tearDown(self):
        self.model_1 = None


    def test_component_lengths(self):
        self.assertEqual(len(self.model_1.components), 2)
        for component in self.model_1.components:
            self.assertEqual(len(component), 2)


    def test_component_types(self):
        uniprot_accession = "[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}"
        for component in self.model_1.components:
            self.assertIsInstance(component, tuple)
            self.assertIsInstance(component[0], str)
            self.assertIsInstance(component[1], str)
            self.assertRegexpMatches(component[0], uniprot_accession)
            self.assertIsInstance(int(component[1]), int)

        
            
    def test_accession_parsing_fail_when_not_accession(self):
        pass
