"""A set of test for the Fields class."""
import os
import pickle
import unittest

from biotrack.component import Component
from biotrack.fields import Fields


class TestVeryBasicFieldsValues(unittest.TestCase):

    def setUp(self):
        self.comments = [
            "FUNCTION: Lays eggs. {ECO:0000269|PubMed:6766130}.",
            "SIMILARITY: Goose. {ECO:0000255|PROSITE-ProRule:PRU00524}.",
            ]
        self.test_dict = {
            "FUNCTION": "Lays eggs. {ECO:0000269|PubMed:6766130}.",
            "SIMILARITY": "Goose. {ECO:0000255|PROSITE-ProRule:PRU00524}.",
            }
        self.fields = Fields(self.comments)

        
    def tearDown(self):
        self.fields = None

        
    def test_basic_field_dict_values(self):
        """Test field_dict has expected values."""
        self.assertDictEqual(self.test_dict, self.fields.field_dict)


    def test_print(self):
        """Test string representation of Fields object."""
        sorted_comments = sorted(self.comments)
        self.assertEqual(str(self.fields), "\n".join(sorted_comments))
                                        


class TestRibRProteinFieldsValues(unittest.TestCase):

    def setUp(self):
        """Load a pickled AutoComponent as a test case."""
        # Test on the comments field of a SwissProt entry of a pickled
        # AutoComponent test case.
        PICKLE_DIR = (os.path.dirname(os.path.realpath(__file__))
                      + "/pickled_testcases/")
        with open(PICKLE_DIR + "P94465_ac_pickle.txt", 'r') as f:
            auto_comp = pickle.load(f)
        self.old_comments = auto_comp.old_entry.comments
        self.new_comments = auto_comp.new_entry.comments


    def tearDown(self):
        self.old_comments = None
        self.new_comments = None


    def test_fields_init(self):
        old_fields = Fields(self.old_comments)
        new_fields = Fields(self.new_comments)

        
    def test_comment_parsing(self):
        # Create a test Fields object.
        test_fields = Fields(self.old_comments)
        field_dict = test_fields.field_dict
        # A Field should have field_dict attribute. 
        self.assertIsInstance(test_fields.field_dict, dict)
        # Test that all values in field_dict are strings and that
        # there is no leading or trailing whitespace.
        for field in field_dict.keys():
            self.assertIsInstance(field_dict[field], str)
            self.assertEqual(field_dict[field], str.strip(field_dict[field]))


    def test_fields_equality(self):
        # Fields are equal if their field_sets and field_dicts are
        # equal.
        old_fields1 = Fields(self.old_comments)
        old_fields2 = Fields(self.old_comments)
        new_fields = Fields(self.new_comments)
        self.assertEqual(old_fields1, old_fields2)
        self.assertNotEqual(new_fields, old_fields1)


class TestDifferentFieldDiscovery(unittest.TestCase):

    def setUp(self):
        self.comments1 = [
            "FUNCTION: Lays eggs. {ECO:0000269|PubMed:6766130}.",
            "SIMILARITY: Goose. {ECO:0000255|PROSITE-ProRule:PRU00524}.",
            ]
        # Second comments with differect object reference.
        self.comments2 = list(self.comments1)
        self.fields1 = Fields(self.comments1)

        
    def tearDown(self):
        self.fields1 = None
        self.comments1 = None
        self.comments2 = None

        
    def test_new_field_is_discovered(self):
        # Add an extra comment taking care not to alter
        # self.comments1.
        new_field = "MISCELLANEOUS: Has feathers."
        self.comments2.append(new_field)
        # New Fields with additional comment.
        fields2 = Fields(self.comments2)
        # Test equality
        self.assertNotEqual(self.fields1, fields2)
        # Test difference returns new Field object containing
        # the new field.
        diff = fields2 - self.fields1
        self.assertEqual(diff, Fields([new_field]))



    def test_changed_field_is_discovered(self):
        # Change a field in comment2 taking care not to alter comments1.
        self.comments2[0] = "FUNCTION: Stud duck."
        # Create second Fields with altered FUNCTION.
        fields2 = Fields(self.comments2)
        # Test that values FUNCTION value has changed..
        self.assertNotEqual(self.fields1, fields2)
        self.assertNotEqual(self.fields1.field_dict["FUNCTION"],
                            fields2.field_dict["FUNCTION"])
        # Test difference returns new Field object containing
        # the altered field.
        diff = fields2 - self.fields1
        self.assertEqual(diff, Fields(["FUNCTION: Stud duck."])) 
