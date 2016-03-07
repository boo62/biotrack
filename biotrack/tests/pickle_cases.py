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

from biotrack.model import Model
from biotrack.component import AutoComponent

# If I change AutoComponent substantially (adding attributes or
# changing the init) I also need to repickle the Models because these
# contian AutoComponents and I will call some of their methods in
# Model. So might as well do them all at the same time.


# Pickle all of the test case Models.
def pickle_models(model_path):
    """Pickle test case Model objects from paths of test cases.

    Requires a list of paths to model '.csv' files and writes
    '_pickle.txt' files to the same directory for each model.
    """
    for path in model_path:
        # Could use regex here.
        pickle_path = path.split(".csv")[0] + "_pickle.txt"
        # Model contains accessions and new and old UniProt entries
        # for each component in the '.csv' file.
        pickle_model(Model(path), pickle_path)


def pickle_model(model, filename):
    """Pickle the Model object of a test case."""
    # Do not overwrite original '.csv' model.
    assert filename.endswith("_pickle.txt")
    with open(filename, 'w') as f:
        pickle.dump(model, f)


# Pickle some AutoComponents to use as test cases
def pickle_auto_components(components):
    for component in components:
        outfile = MODEL_DIR + component.accession + "_ac_pickle.txt"
        with open(outfile, 'w') as f:
            pickle.dump(component, f)    

# Path of directory containing models. This is relative to this files path.
MODEL_DIR = os.path.dirname(os.path.realpath(__name__)) + "/example_models/"

# Names of model.csv files
TEST_CASE_MODELS = [
    "one_component.csv",
    "two_components.csv",
    ]

# Paths to test case models '.csv' files.
TEST_CASE_MODEL_PATHS = [MODEL_DIR + model for model in TEST_CASE_MODELS]


# ribR and ribE in B. Subtilis
TEST_CASE_AUTOCOMPONENTS = [
    AutoComponent("P94465", "79"),
    AutoComponent("P16440", "90"),
    ]

# Pickle all of the test cases.
if __name__ == "__main__":
    print ("Start pickling test cases")
    pickle_models(TEST_CASE_MODEL_PATHS)
    print ("Done")
    print ("Start pickling auto component test cases")
    pickle_auto_components(TEST_CASE_AUTOCOMPONENTS)
    print ("Done")
