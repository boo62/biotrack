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
