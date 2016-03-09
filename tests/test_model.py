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
    # it is probably better to subclass the slow test classes with the
    # fast test classes in a separate test module and change setUp.
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
            self.assertTrue(component[0][0] in component[1].old_entry.accessions)
            self.assertTrue(component[0][0] in component[1].new_entry.accessions)


class TestSameProteinDifferentAccessions(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass
    
    
    def test_retrieve_entries_of_same_protein(self):
        """Test if accessions refer to the same protein."""
       pass
    
#     def test_component_types(self):
#         """Test that Model.components have correct type and format.

#         The accession of each component should match a UniProt
#         accession and the version should convert to an integer.

#         """
#         uniprot_accession = ("[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z]"
#                              + "[0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}")
#         for component in self.model_1.components:
#             self.assertIsInstance(component, tuple)
#             self.assertIsInstance(component[0], str)
#             self.assertIsInstance(component[1], str)
#             self.assertRegexpMatches(component[0], uniprot_accession)
#             self.assertIsInstance(int(component[1]), int)


#     def test_no_white_space(self):
#         for component in self.model_1.components:
#             self.assertEqual(component[0].strip(), component[0])
#             self.assertEqual(component[1].strip(), component[1])

            
# class TestBasicTwoComponentModelEntryRetrieval(unittest.TestCase):

#     def setUp(self):
#         """Setup simple model from two component test case."""
#         pickle_dir = (os.path.dirname(os.path.realpath(__file__))
#                       + "/example_models/")
#         with open(pickle_dir + "two_components_pickle.txt") as f:
#             self.model_1 = pickle.load(f)
    
#     def tearDown(self):
#         self.model_1 = None
        
#     def test_entries_length(self):
#         self.assertEqual(len(self.model_1.old_entries), 2)


#     def test_entries_have_the_expected_accession(self):
#         old_pairs = zip(self.model_1.components, self.model_1.old_entries)
#         new_pairs = zip(self.model_1.components, self.model_1.new_entries)
#         for pair in old_pairs:
#             self.assertTrue(pair[0][0] in pair[1].accessions)
#         for pair in new_pairs:
#             self.assertTrue(pair[0][0] in pair[1].accessions)
    
#     # It is possible that entries will have merged and if so we want
#     # to report this.
#     def test_if_two_entries_are_the_same(self):
#         pass
        
#     def test_old_entry_retrieval(self):
#         pass

#     def test_new_entry_retrieval(self):
#         pass


# class TestBasicTwoComponentModelEntryCommentComparison(unittest.TestCase):

#     def setUp(self):
#         """Setup simple model from two component test case."""
#         pickle_dir = (os.path.dirname(os.path.realpath(__file__))
#                       + "/example_models/")
#         with open(pickle_dir + "two_components_pickle.txt") as f:
#             self.model_1 = pickle.load(f)

#     def tearDown(self):
#         self.model_1 = None
        
#     # def test_entry_comment_comparison(self):
#     #     self.model_1.compare_entry_comments(self.model_1.old_entries[0],
#     #                                         self.model_1.new_entries[0])
