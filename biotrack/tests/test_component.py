import unittest
import os

from biotrack.component import Component


class TestComponentAttributes(unittest.TestCase):

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

        
    def test_non_uniprot_accession_raises_value_error(self):
        # Had trouble getting this to work. Seems an odd way of doing
        # things. Second argument must be callable so can't just write
        # Component("N0TAPR0T", "79") and must give an instance of a
        # Component to __init__ so use comp1. If I raise the error in
        # component.py then the unittest raises the error and fails.
        self.assertRaises(ValueError,
                          Component.__init__(self.comp1, "N0TAPR0T", "79"))

        
    def test_non_integer_version_rasies_exception(self):
        self.assertRaises(ValueError,
                          Component.__init__(self.comp1, "P94465", "a_string"))
        self.assertRaises(ValueError,
                          Component.__init__(self.comp1, "P94465", 8.9))

