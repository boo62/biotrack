import unittest
import os

from biotrack.component import Component


def give_an_error():
    raise ValueError

class TestEntryRetrieval(unittest.TestCase):

    def setUp(self):
        self.comp1 = Component("P94465", "79")

    def tearDown(self):
        self.comp1 = None

    def test_component_attribute_values(self):
        """Test that Components have correct values and format."""
        self.assertEqual(self.comp1.accession, "P94465")
        self.assertEqual(self.comp1.version, "79")

    def test_component_attribure_types(self):
        self.assertIsInstance(self.comp1.accession, str)
        self.assertIsInstance(self.comp1.version, str)
        self.assertIsInstance(int(self.comp1.version), int)

    def test_raising(self):
        self.assertRaises(ValueError, give_an_error)
        
    def test_non_uniprot_accession_raises_value_error(self):
        self.assertRaises(AssertionError, Component.__init__("N0RRR@TPR0T", "79"))

        
