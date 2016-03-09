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
def pickle_models(path_pairs):
    """Pickle test case Model objects from paths of test cases.

    Requires a list of tuples containing paths to model '.csv'
    files and '_pickle.txt' files to write to.
    """
    for paths in path_pairs:
        # Create model from paths[0] and write pickle to paths[1].
        print(paths[0])
        pickle_model(Model(paths[0]), paths[1])


def pickle_model(model, filename):
    """Pickle the Model object of a test case."""
    # Do not overwrite original '.csv' model.
    assert filename.endswith("_pickle.txt")
    with open(filename, 'w') as f:
        pickle.dump(model, f)


# Pickle some AutoComponents to use as test cases
def pickle_auto_components(components):
    for component in components:
        print(component)
        outfile = PICKLE_DIR + component.accession + "_ac_pickle.txt"
        with open(outfile, 'w') as f:
            pickle.dump(component, f)    

# Path of directory containing models and directory to contain pickled
# test cases.
# Get odd behaviour when running this as C-c C-l rather than from terminal.
# To work that way it requires changing __file__ to __name__ but then it
# does not find the correct path from the terminal. Can always use compile.
TEST_DIR = os.path.dirname(os.path.realpath(__file__))
MODEL_DIR = TEST_DIR + "/example_models/"
PICKLE_DIR = TEST_DIR + "/pickled_testcases/"

# Names of model.csv files
TEST_CASE_MODELS = [
    "one_component.csv",
    "two_components.csv",
    # You cannot use a secodary accession to retrieve a UniSave entry
    # after merging. UniSave entries before merging and the current
    # http://www.uniprot.org/ entry can be retrieved with a secondary
    # accession. TrEMBLE entries will generally parse with
    # SwissProt.read() but I have found an example where a very old
    # ribE entry raises AssertionError: Missing braces. Hopefully
    # UniProt formats are now stable and error free and will parse for
    # anyone beginning to record accessions and versions. The model
    # file containing the failing accession is commented out below.
    # "two_ribE_accessions.csv",
    "same_proteins.csv",
    "two_groups_same_protein.csv"
    ]

# Paths to test case models '.csv' files.
TEST_CASE_MODEL_PATHS = [MODEL_DIR + model for model in TEST_CASE_MODELS]
PICKLE_PATHS = [PICKLE_DIR + model.split(".csv")[0] + "_pickle.txt"
                 for model in TEST_CASE_MODELS]
MODEL_PATHS = zip(TEST_CASE_MODEL_PATHS, PICKLE_PATHS)

# ribR and ribE in B. Subtilis
TEST_CASE_AUTOCOMPONENTS = [
    AutoComponent("P94465", "79"),
    AutoComponent("P16440", "90"),
    ]

# Pickle all of the test cases.
if __name__ == "__main__":
    print ("Start pickling test cases")
    pickle_models(MODEL_PATHS)
    print ("Done")
    print ("Start pickling auto component test cases")
    pickle_auto_components(TEST_CASE_AUTOCOMPONENTS)
    print ("Done")
