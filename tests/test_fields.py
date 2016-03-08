import os
import pickle
import unittest

from biotrack.component import Component
from biotrack.fields import Fields


class TestVeryBasicFieldsValues(unittest.TestCase):

    def setUp(self):
        comments = [
            "FUNCTION: Lays eggs. {ECO:0000269|PubMed:6766130}.",
            "SIMILARITY: Goose. {ECO:0000255|PROSITE-ProRule:PRU00524}.",
            ]
        self.test_dict = {
            "FUNCTION": "Lays eggs. {ECO:0000269|PubMed:6766130}.",
            "SIMILARITY": "Goose. {ECO:0000255|PROSITE-ProRule:PRU00524}.",
            }
        self.fields = Fields(comments)

        
    def tearDown(self):
        self.fields = None

        
    def test_basic_field_set_values(self):
        self.assertSetEqual({"FUNCTION", "SIMILARITY"}, self.fields.field_set)

        
    def test_basic_field_dict_values(self):
        self.assertDictEqual(self.test_dict, self.fields.field_dict)


class TestRibRProteinFieldsValues(unittest.TestCase):

    def setUp(self):
        """Load a pickled AutoComponent as a test case."""
        # Test on the comments field of a UniProt entry of a pickled
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
        field_set = test_fields.field_set
        field_dict = test_fields.field_dict
        # A Field should have field_set and field_dict attributes. 
        self.assertIsInstance(test_fields.field_set, set)
        self.assertIsInstance(test_fields.field_dict, dict)
        # Test that all of the fields in set are also keys in dict.
        self.assertSetEqual(field_set, set(field_dict.keys()))
        # Test that all values in field_dict are strings and that
        # there is no leading or trailing whitespace.
        for field in field_dict.keys():
            self.assertIsInstance(field_dict[field], str)
            self.assertEqual(field_dict[field], str.strip(field_dict[field]))
