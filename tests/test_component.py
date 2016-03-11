"""A set of tests for Component and AutoComponent classes."""
import unittest
import os
import pickle

from biotrack.component import Component, AutoComponent
from biotrack.fields import Fields


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


    def test_no_white_space(self):
        self.assertEqual(self.comp1.accession.strip(),
                         self.comp1.accession)
        self.assertEqual(self.comp1.version.strip(),
                         self.comp1.version)

        
    def test_non_uniprot_accession_raises_value_error(self):
        self.assertRaises(ValueError,
                          lambda: Component("N0TAPr0T", "5"))
        self.assertRaises(ValueError,
                          lambda: Component(6, "5"))


    def test_non_integer_version_rasies_exception(self):
        self.assertRaises(ValueError,
                          lambda: Component("P94465", "v1"))
        self.assertRaises(ValueError,
                          lambda: Component("P94465", 8.9))


        
# Tests on a pickled AutoComponent test case.
class TestAutoComponent(unittest.TestCase):
    """Contains additional test for entries"""

    def setUp(self):
        """Load a pickled AutoComponent as a test case."""
        PICKLE_DIR = (os.path.dirname(os.path.realpath(__file__))
                      + "/pickled_testcases/")
        with open(PICKLE_DIR + "P94465_ac_pickle.txt", 'r') as f:
            self.auto_comp = pickle.load(f)
        # self.auto_comp = AutoComponent("P94465", "79")

        
    def tearDown(self):
        self.auto_comp = None


    def test_component_attribute_values(self):
        """Test that Components have correct values and format."""
        self.assertEqual(self.auto_comp.accession, "P94465")
        self.assertEqual(self.auto_comp.version, "79")


    def test_component_attribute_types(self):
        self.assertIsInstance(self.auto_comp.accession, str)
        self.assertIsInstance(self.auto_comp.version, str)
        self.assertIsInstance(int(self.auto_comp.version), int)


    # This may be redundant given test_component_attribute_values.
    def test_no_white_space(self):
        self.assertEqual(self.auto_comp.accession.strip(),
                         self.auto_comp.accession)
        self.assertEqual(self.auto_comp.version.strip(),
                         self.auto_comp.version)

        
    def test_non_uniprot_accession_raises_value_error(self):
        self.assertRaises(ValueError, lambda:
                          AutoComponent("N0TAPR0T", "79"))
        self.assertRaises(ValueError, lambda: AutoComponent(6, "5"))
        
    def test_non_integer_version_rasies_exception(self):
        self.assertRaises(ValueError,
                          lambda: AutoComponent("P94465", "v1"))
        self.assertRaises(ValueError,
                          lambda: AutoComponent("P94465", 8.9))

        
    def test_entries_have_the_expected_accessions(self):
        self.assertTrue(self.auto_comp.accession in
                        self.auto_comp.old_entry.accessions)
        self.assertTrue(self.auto_comp.accession in
                        self.auto_comp.new_entry.accessions)


    def test_fields_object_based_comparison(self):
        # Also need a test case where old and new are the same to test
        # that None is returned.  Compares new and old entry attibutes
        # and returns a Fields object with the difference.
        changes = self.auto_comp.compare_entry_fields()
        self.assertIsInstance(changes, Fields)
