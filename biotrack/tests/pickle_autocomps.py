# It is slow to obtain entry data from a url every time when running
# tests. I only need to do this when I change a method which affects
# model insantiation. I can pickle some test cases and load these in
# order to test new methods which do not affect the instantiation. If
# I change the instantiation I will need to repickle the test cases.
#
# How to test the instantiation?
#
# Instantiations should be tested in a separate test file which is run
# separately from other unittests and will be much slower. I will have
# to work out how to exclude these from py.test.
#
# Alternatively instantiation could be tested after the fact using the
# results it produces in the pickled test cases.
import os
import pickle

from biotrack.component import AutoComponent

# Pickle some AutoComponents to use as test cases
def pickle_test_auto_components(compnents, filename):
    for component in components:
        outfile = MODEL_DIR + component.accession + "_ac_pickle.txt"
        with open(outfile) as f:
            pickle.dump(component, f)    

        
# Path of directory containing models and test cases. This is relative to this files path.
MODEL_DIR = os.path.dirname(os.path.realpath(__name__)) + "/example_models/"

# ribR and ribE in B. Subtilis
TEST_CASE_AUTOCOMPONENTS = [
    AutoComponent("P94465", "79"),
    AutoComponent("P16440", "90")
    ]

# Pickle all of the test cases.
if __name__ == "__main__":
    print ("Start pickling auto component test cases")
    pickle_test_auto_components(TEST_CASE_AUTOCOMPONENTS)
    print ("Done")
