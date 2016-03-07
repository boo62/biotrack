#!/usr/bin/env python
import unittest
import os
import pickle

from biotrack.model import Model


class TestBasicTwoComponentModelParsing(unittest.TestCase):

    def setUp(self):
        """Setup simple model from two component test case."""
        pickle_dir = (os.path.dirname(os.path.realpath(__file__))
                      + "/example_models/")
        with open(pickle_dir + "two_components_pickle.txt") as f:
            self.model_1 = pickle.load(f)

    def tearDown(self):
        self.model_1 = None


    def test_component_lengths(self):
        """Test component lenghts.

        The correct number of components should be read from file and
        each component should have length two.

        """
        self.assertEqual(len(self.model_1.components), 2)
        for component in self.model_1.components:
            self.assertEqual(len(component), 2)


    def test_component_types(self):
        """Test that Model.components have correct type and format.

        The accession of each component should match a UniProt
        accession and the version should convert to an integer.

        """
        uniprot_accession = ("[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z]"
                             + "[0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}")
        for component in self.model_1.components:
            self.assertIsInstance(component, tuple)
            self.assertIsInstance(component[0], str)
            self.assertIsInstance(component[1], str)
            self.assertRegexpMatches(component[0], uniprot_accession)
            self.assertIsInstance(int(component[1]), int)


    def test_no_white_space(self):
        for component in self.model_1.components:
            self.assertEqual(component[0].strip(), component[0])
            self.assertEqual(component[1].strip(), component[1])

            
class TestBasicTwoComponentModelEntryRetrieval(unittest.TestCase):

    def setUp(self):
        """Setup simple model from two component test case."""
        pickle_dir = (os.path.dirname(os.path.realpath(__file__))
                      + "/example_models/")
        with open(pickle_dir + "two_components_pickle.txt") as f:
            self.model_1 = pickle.load(f)
    
    def tearDown(self):
        self.model_1 = None
        
    def test_entries_length(self):
        self.assertEqual(len(self.model_1.old_entries), 2)


    def test_entries_have_the_expected_accession(self):
        old_pairs = zip(self.model_1.components, self.model_1.old_entries)
        new_pairs = zip(self.model_1.components, self.model_1.new_entries)
        for pair in old_pairs:
            self.assertTrue(pair[0][0] in pair[1].accessions)
        for pair in new_pairs:
            self.assertTrue(pair[0][0] in pair[1].accessions)
    
    # It is possible that entries will have merged and if so we want
    # to report this.
    def test_if_two_entries_are_the_same(self):
        pass
        
    def test_old_entry_retrieval(self):
        pass

    def test_new_entry_retrieval(self):
        pass


class TestBasicTwoComponentModelEntryCommentComparison(unittest.TestCase):

    def setUp(self):
        """Setup simple model from two component test case."""
        pickle_dir = (os.path.dirname(os.path.realpath(__file__))
                      + "/example_models/")
        with open(pickle_dir + "two_components_pickle.txt") as f:
            self.model_1 = pickle.load(f)

    def tearDown(self):
        self.model_1 = None
        
    # def test_entry_comment_comparison(self):
    #     self.model_1.compare_entry_comments(self.model_1.old_entries[0],
    #                                         self.model_1.new_entries[0])
