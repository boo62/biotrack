#!/usr/bin/env python
import unittest
import os

from biotrack.model import Model



class TestBasicTwoComponentModelParsing(unittest.TestCase):

    def setUp(self):
        """Setup simple model from two component test case."""
        test_dir = os.path.dirname(os.path.realpath(__file__))
        self.model_1 = Model(test_dir + "/example_models/two_components.csv")

    def tearDown(self):
        self.model_1 = None


    def test_components_length(self):
        """Test component lenghts.

        The correct number of components should be read from file and
        each component should have length two.

        """
        self.assertEqual(len(self.model_1.components), 2)



    def test_component_types(self):
        """Test that Model.components have correct type and format.

        The accession of each component should match a UniProt
        accession and the version should convert to an integer.

        """
        uniprot_accession = "[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}"
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

            
    def test_accession_parsing_fail_when_not_accession(self):
        pass


class TestBasicTwoComponentModelEntryRetrieval(unittest.TestCase):

    def setUp(self):
        """Setup simple model from two component test case."""
        test_dir = os.path.dirname(os.path.realpath(__file__))
        self.model_1 = Model(test_dir + "/example_models/two_components.csv")

    def tearDown(self):
        self.model_1 = None

    def test_entries_length(self):
        self.assertEqual(len(self.model_1.old_entries), 2)
        
    def test_old_entry_retrieval(self):
        pass

    def test_new_entry_retrieval(self):
        pass


class TestBasicTwoComponentModelEntryCommentComparison(unittest.TestCase):

    def setUp(self):
        """Setup simple model from two component test case."""
        test_dir = os.path.dirname(os.path.realpath(__file__))
        self.model_1 = Model(test_dir + "/example_models/two_components.csv")

    def tearDown(self):
        self.model_1 = None
        
    def test_entry_comment_comparison(self):
        self.model_1.compare_entry_comments(self.model_1.old_entries[0],
                                            self.model_1.new_entries[0])
