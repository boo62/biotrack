#!/usr/bin/env python
import unittest
import os
import pickle
import csv

from biotrack.model import Model


class TestBasicTwoComponentModelParsing(unittest.TestCase):
    
    # Pickled setUp (faster)
    def setUp(self):
        """Setup simple model from two component test case."""
        # Paths to find pickled Model and raw model file.
        test_path = os.path.dirname(os.path.realpath(__file__))
        pickle_path = (test_path + "/pickled_testcases/two_components_pickle.txt")
        model_path = (test_path + "/example_models/two_components.csv")
        # Load pickled Model test cases.
        with open(pickle_path) as f:
            self.model_1 = pickle.load(f)
        # Read values used to create test case Model from file.
        with open(model_path) as f:
            component_reader = csv.reader(f, skipinitialspace=True)
            self.component_test_tuples = [(row[0], row[1]) for row in
                                          component_reader]

    # Easier to comment and uncomment setUps as required rather than
    # adding all new tests to two separate files. Could just test the
    # initial setup in the slower test file though. Do this after I
    # have finnished edditing so heavily to test things like obtaining
    # entries from urls (when version does not exist etc.). Actually,
    # it is probably better to subclass the fast test classes with the
    # slow test classes in a separate test module and override setUp.
    # # Unpickled setUp (slower)
    # def setUp(self):
    #     model_path = (os.path.dirname(os.path.realpath(__file__)) +
    #                    "/example_models/two_components.csv")
    #     # Create a test case model.
    #     self.model_1 = Model(model_path)
    #     # Read values used to create test case Model from file.
    #     with open(model_path, 'r') as f:
    #         component_reader = csv.reader(f, skipinitialspace=True)
    #         self.component_test_tuples = [(row[0], row[1]) for row in component_reader]

            
    def tearDown(self):
        self.model_1 = None
        self.component_test_tuples = None
        

    def test_components_length(self):
        """Test length of Component object list in Model"""
        self.assertEqual(len(self.model_1.components), 2)


    def test_model_components_have_correct_entries(self):
        for component in zip(self.component_test_tuples,
                             self.model_1.components):
            # Test new and old entries exist and have accessions.
            self.assertTrue(component[1].old_entry.accessions)
            self.assertTrue(component[1].new_entry.accessions)
            # Test accessions match those read from file.
            self.assertIn(component[0][0], component[1].old_entry.accessions)
            self.assertIn(component[0][0], component[1].new_entry.accessions)

    def test_group_accessions_returns_empty_list(self):
        self.assertIsInstance(self.model_1.group_accessions(), list)
        self.assertFalse(self.model_1.group_accessions())

        
class TestSameProteinDifferentAccessions(unittest.TestCase):

    def setUp(self):
        """Instantiate a Model with equivalent accessions."""
        # Paths to find pickled Model and raw model file.
        test_path = os.path.dirname(os.path.realpath(__file__))
        pickle_path = (test_path + "/pickled_testcases/same_proteins_pickle.txt")
        model_path = (test_path + "/example_models/same_proteins.csv")
        # Load pickled Model test cases.
        with open(pickle_path) as f:
            self.model = pickle.load(f)
        # Read values used to create test case Model from file.
        with open(model_path) as f:
            component_reader = csv.reader(f, skipinitialspace=True)
            self.component_test_tuples = [(row[0], row[1]) for row in
                                          component_reader]
        

    def tearDown(self):
        self.model = None
        self.component_test_tuples = None
    

    def test_model_components_contains_same_accessions(self):
        # Test that components in the model actually contian all of
        # the alternative accessions and that the proteins are the
        # same. Testing the test case essentially.
        p53_1 = self.model.components[2]
        p53_2 = self.model.components[3]
        p53_3 = self.model.components[4]
        # Test that all new entries contain the same list of
        # accessions.
        self.assertSetEqual(set(p53_1.new_entry.accessions),
                            set(p53_2.new_entry.accessions))
        self.assertSetEqual(set(p53_1.new_entry.accessions),
                            set(p53_3.new_entry.accessions))
        # Test first accession in all new entries.
        self.assertIn(p53_1.accession, set(p53_1.new_entry.accessions))
        # Test second accession in all new entries.
        self.assertIn(p53_2.accession, set(p53_1.new_entry.accessions))
        # Test third accession in all new entries.
        self.assertIn(p53_3.accession, set(p53_1.new_entry.accessions))

        
    def test_grouping_of_components_of_same_protein(self):
        """Test discovery of accessions which refer to the same protein."""
        same = [set(self.model.components[2:5])]
        self.assertEqual(self.model.group_accessions(), same)
    
    
class TestTwoGroupsSameProtein(unittest.TestCase):

    def setUp(self):
        """Instantiate a Model with equivalent accessions."""
        # Paths to find pickled Model and raw model file.
        test_path = os.path.dirname(os.path.realpath(__file__))
        pickle_path = (test_path + "/pickled_testcases/two_groups_same_protein_pickle.txt")
        model_path = (test_path + "/example_models/two_groups_same_protein.csv")
        # Load pickled Model test cases.
        with open(pickle_path) as f:
            self.model = pickle.load(f)
        # Read values used to create test case Model from file.
        with open(model_path) as f:
            component_reader = csv.reader(f, skipinitialspace=True)
            self.component_test_tuples = [(row[0], row[1]) for row in
                                          component_reader]
        

    def tearDown(self):
        self.model = None
        self.component_test_tuples = None
    

    def test_model_components_contains_same_accessions(self):
        # Test that components in the model actually contian all of
        # the alternative accessions and that the proteins are the
        # same. Testing the test case essentially.
        # p53s
        p53_1 = self.model.components[2]
        p53_2 = self.model.components[3]
        p53_3 = self.model.components[4]
        # Test that all new entries contain the same list of
        # accessions.
        self.assertSetEqual(set(p53_1.new_entry.accessions),
                            set(p53_2.new_entry.accessions))
        self.assertSetEqual(set(p53_1.new_entry.accessions),
                            set(p53_3.new_entry.accessions))
        # Test first accession in all new entries.
        self.assertIn(p53_1.accession, set(p53_1.new_entry.accessions))
        # Test second accession in all new entries.
        self.assertIn(p53_2.accession, set(p53_1.new_entry.accessions))
        # Test third accession in all new entries.
        self.assertIn(p53_3.accession, set(p53_1.new_entry.accessions))
        # Rhodopsins      
        rhod_1 = self.model.components[5]
        rhod_2 = self.model.components[6]
        # Test that all new entries contain the same list of
        # accessions.
        self.assertSetEqual(set(rhod_1.new_entry.accessions),
                            set(rhod_2.new_entry.accessions))
        # Test first accession in all new entries.
        self.assertIn(rhod_1.accession, set(rhod_1.new_entry.accessions))
        # Test second accession in all new entries.
        self.assertIn(rhod_2.accession, set(rhod_1.new_entry.accessions))
        

    def test_grouping_of_components_of_same_protein(self):
        """Test discovery of accessions which refer to the same protein."""
        same = [set(self.model.components[2:5]), set(self.model.components[5:7])]
        self.assertEqual(self.model.group_accessions(), same)
